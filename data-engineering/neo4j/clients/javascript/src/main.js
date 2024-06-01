// ========================================================
// Connect to the database
// ========================================================

var neo4j = require('neo4j-driver');
(async () => {
  // URI examples: 'neo4j://localhost', 'neo4j+s://xxx.databases.neo4j.io'
  const URI = 'neo4j://localhost'
  const USER = 'neo4j'
  const PASSWORD = 'neo4j+devops'
  let driver

  try {
    driver = neo4j.driver(URI, neo4j.auth.basic(USER, PASSWORD))
    const serverInfo = await driver.getServerInfo()
    console.log('Connection established')
    console.log(serverInfo)
  } catch (err) {
    console.log(`Connection error\n${err}\nCause: ${err.cause}`)
  }

  // ========================================================
  // Query the database
  // ========================================================

  // Get the name of all 42 year-olds
  const { records, summary, keys } = await driver.executeQuery(
    // 'MATCH (p:Person {age: $age}) RETURN p.name AS name',
    // { age: 42 },
    // { database: 'neo4j' }
    'MATCH (p:Person {born: $born}) RETURN p.name AS name',
    { born: 1968 },
    { database: 'neo4j' }
  )

  // Summary information
  console.log(
    `>> The query ${summary.query.text} ` +
    `returned ${records.length} records ` +
    `in ${summary.resultAvailableAfter} ms.`
  )

  // Loop through results and do something with them
  console.log('>> Results')
  for (record of records) {
    console.log(record.get('name'))
  }

  // ========================================================
  // Run your own transactions
  // ========================================================

  let session = driver.session({ database: 'neo4j' })
  try {
    const result = await session.executeRead(async tx => {
      return await tx.run(`
      MATCH (p:Person WHERE p.name STARTS WITH $filter)
      RETURN p.name AS name ORDER BY name
      `, { filter: 'Al' }
      )
    })
    console.log(
      `The query ${result.summary.query.text} returned ${result.records.length} nodes.`
    )
    for (let record of result.records) {
      console.log(`Person with name: ${record.get('name')}`)
      console.log(`Available properties for this node are: ${record.keys}\n`)
    }
  } finally {
    console.log('close session')
    await session.close()
  }

  // ========================================================
  // Close connections and sessions
  // ========================================================

  console.log('close connection')
  await driver.close()
})();
