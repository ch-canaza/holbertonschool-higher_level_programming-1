#!/usr/bin/python3
''' lists all states from database hbtn_0e_0_usa where name matches argv[4] '''


if __name__ == "__main__":
    from sys import argv
    import MySQLdb
    db = MySQLdb.connect(user=argv[1],
                         passwd=argv[2],
                         db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * from states WHERE name LIKE '{}' ORDER BY states.id"
                .format(argv[4]))
    state_list = cur.fetchall()
    for state in state_list:
        print(state)
    cur.close()
    db.close()
