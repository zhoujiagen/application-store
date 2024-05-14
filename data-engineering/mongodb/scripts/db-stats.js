print(`db,totalSize(MB),collections,indexes,storageSize(MB),indexSize(MB)`)
db.adminCommand("listDatabases").databases.forEach(function (d) {
   mdb = db.getSiblingDB(d.name);
   mdbStats = mdb.stats();
   print(mdbStats);
   // sharding?
   collections = mdbStats.collections || (mdbStats.raw['rs-app/mongodb-shardsvr01:27017'].collections +
     mdbStats.raw['rs-app/mongodb-shardsvr02:27017'].collections +
     mdbStats.raw['rs-app/mongodb-shardsvr02:27017'].collections)
   print(`${d.name}, ${mdbStats.totalSize / 1024 / 1024}, ${collections}, ${mdbStats.indexes}, ${mdbStats.storageSize / 1024 / 1024} , ${mdbStats.indexSize / 1024 / 1024}`);
})
