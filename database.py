import sqlite3

def main():
    db=sqlite3.connect('test.db')
    db.row_factory=sqlite3.Row
    db.execute('DROP TABLE IF EXISTS test')
    db.execute('CREATE TABLE TEST(t1 text,i1 int)')
    db.execute('INSERT INTO test (t1,i1) VALUES (?,?)',('one',1))
    db.execute('INSERT INTO test (t1,i1) VALUES (?,?)',('two',2))
    db.execute('INSERT INTO test (t1,i1) VALUES (?,?)',('three',3))
    db.execute('INSERT INTO test (t1,i1) VALUES (?,?)',('four',4))
    db.execute('INSERT INTO test (t1,i1) VALUES (?,?)',('five',5))
    db.commit()

    cursor=db.execute('SELECT * FROM test ORDER BY t1 ASC')
    for row in cursor:
        # print(row)
        # print(dict(row))
        # print (tuple(row))
        print(row['t1'],row['i1'])


if __name__=="__main__":
    main()
    print("Done!")