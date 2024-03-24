db.createCollection("test");

db.test.createIndex({name: 1}, {unique: true});

// use admin;
// DEPLOY_ENV
// db.createUser({user: "devops", pwd: "devops", roles:[{role: "readWrite", db: "devops"}]});