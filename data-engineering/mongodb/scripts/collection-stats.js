print(`collection,size(MB),count,nindexes,totalSize(MB),totalIndexSize(MB)`)
db.adminCommand("listDatabases").databases.filter(function (d) {
    return d.name !== 'local' && d.name !== 'config' && d.name !== 'admin'
})
    .forEach(function (d) {
        mdb = db.getSiblingDB(d.name);
        mdb.getCollectionNames().forEach(function (c) {
            s = mdb[c].stats();
            print(`${d.name}.${c}, ${s.size / 1024 / 1024}, ${s.count}, ${s.nindexes}, ${s.totalSize / 1024 / 1024}, ${s.totalIndexSize / 1024 / 1024}`);
        })
    })

