export MONGODB_USERNAME=xxx
export MONGODB_PASSWORD=xxx

mongosh mongodb://$MONGODB_USERNAME:$MONGODB_PASSWORD@localhost:27017/ --quiet db-stats.js > db-stats.csv
mongosh mongodb://$MONGODB_USERNAME:$MONGODB_PASSWORD@localhost:27017/ --quiet collection-stats.js > collection-stats.csv

python3 stats.py
