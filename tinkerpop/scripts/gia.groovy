// example in 'Graph Databases in Action'

//Connects the Gremlin Session to the "remote" Gremlin Server
// and runs this in a session instead of the default "sessionless" mode
:remote connect tinkerpop.server conf/remote.yaml session
//Sets Gremlin Console into "remote" mode so that each command is run on the server
:remote console

//Adds a person vertex with a name of Dave and saves it to a variable
dave = g.addV('person').property('name', 'Dave').next()
//Adds a person vertex with a name of Josh and saves it to a variable
josh = g.addV('person').property('name', 'Josh').next()
//Adds a person vertex with a name of Ted and saves it to a variable
ted = g.addV('person').property('name', 'Ted').next()
//Adds a person vertex with a name of Hank and saves it to a variable
hank = g.addV('person').property('name', 'Hank').next()

//Adds a is_friends_with edge between Dave and Ted
g.addE('is_friends_with').from(dave).to(ted).next()
//Adds a is_friends_with edge between Dave and Josh
g.addE('is_friends_with').from(dave).to(josh).next()
//Adds a is_friends_with edge between Dave and Hank
g.addE('is_friends_with').from(dave).to(hank).next()
//Adds a is_friends_with edge between Josh and Hank
g.addE('is_friends_with').from(josh).to(hank).next()
//Adds a is_friends_with edge between Ted and Josh
g.addE('is_friends_with').from(ted).to(josh).next()


//Adds a person vertex with a name of Kelly and saves it to a variable
kelly = g.addV('person').property('name', 'Kelly').next()
//Adds a person vertex with a name of Josh and saves it to a variable
jim = g.addV('person').property('name', 'Jim').next()
//Adds a person vertex with a name of Paras and saves it to a variable
paras = g.addV('person').property('name', 'Paras').next()
//Adds a person vertex with a name of Denise and saves it to a variable
denise = g.addV('person').property('name', 'Denise').next()

//Adds a is_friends_with edge between Dave and Jim
g.addE('is_friends_with').from(dave).to(jim).next()
//Adds a is_friends_with edge between Dave and Kelly
g.addE('is_friends_with').from(dave).to(kelly).next()
//Adds a is_friends_with edge between Kelly and Jim
g.addE('is_friends_with').from(kelly).to(jim).next()
//Adds a is_friends_with edge between Kelly and Denise
g.addE('is_friends_with').from(kelly).to(denise).next()
//Adds a is_friends_with edge between Jim and Denise
g.addE('is_friends_with').from(jim).to(denise).next()
//Adds a is_friends_with edge between Jim and Paras
g.addE('is_friends_with').from(jim).to(paras).next()
//Adds a is_friends_with edge between Paras and Denise
g.addE('is_friends_with').from(paras).to(denise).next()