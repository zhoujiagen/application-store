import pandas as pd

# Get stats information on MongoDB databases and collections.
if __name__ == '__main__':
    db = pd.read_csv('db-stats.csv')
    #print(db.keys())

    db = db.sort_values(by='totalSize(MB)', axis=0, ascending=False)
    print(db)

    col = pd.read_csv('collection-stats.csv')
    #print(col.keys())

    col = col.sort_values(by='size(MB)', axis=0, ascending=False)
    print(col)
