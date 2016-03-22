# coding=utf-8

def rebuild_table():

    import MySQLdb

    db = MySQLdb.connect(host="localhost", user="root", passwd="iiizb104", db="project")
    db.set_character_set('utf8')

    c = db.cursor()
    c.execute("SET names utf8")

    sql_drop = "DROP TABLE IF EXISTS job;"
    sql_create = "CREATE TABLE IF NOT EXISTS job (" \
                 "jobno int not null auto_increment primary key, " \
                 "src varchar(50), " \
                 "postdate date, " \
                 "title varchar(150), " \
                 "company varchar(150), " \
                 "industry varchar(100), " \
                 "loc varchar(50), " \
                 "emptype varchar(50), " \
                 "exp decimal(3,1), " \
                 "salary decimal(10,2), " \
                 "content text(65535), " \
                 "skill json, " \
                 "skill26 json, " \
                 "url varchar(200) not null unique, " \
                 "cluster int);"

    c.execute(sql_drop)
    c.execute(sql_create)
    db.commit()

    c.close()
    db.close()
