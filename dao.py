import json
import sqlite3
from sqlite3 import Error
import os.path

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
db_path = os.path.join(BASE_DIR, "database/sqlite3.db")


def create_connection():
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_path)
    except Error as e:
        print(e)
    return conn


def createAudit(audit):
    conn = create_connection()

    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' insert into audit(storage,memory,cpu,user) values(?,?,?,?)'''
    print(audit)
    data = tuple(audit.values())
    cur = conn.cursor()
    cur.execute(sql, data)
    conn.commit()
    return cur.lastrowid


def getAudits():
    conn = create_connection()
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' select user,cpu,memory,storage,createdon from audit order by createdon '''
    cur = conn.cursor()
    cur.execute(sql)
    r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return (r[0] if r else None) if False else r


def getSettings():
    conn = create_connection()
    """
    Create a new project into the projects table
    :param conn:
    :param project:
    :return: project id
    """
    sql = ''' select threshold_storage,threshold_memory,threshold_cpu,max_backups from settings '''
    cur = conn.cursor()
    cur.execute(sql)
    r = [dict((cur.description[i][0], value) for i, value in enumerate(row)) for row in cur.fetchall()]
    cur.connection.close()
    return (r[0] if r else None) if False else r


def updateSettings(settings):
    """
    update priority, begin_date, and end date of a task
    :param conn:
    :param task:
    :return: project id
    """
    conn = create_connection()

    sql = ''' update  settings set threshold_cpu=? and threshold_memory=? and threshold_storage=? and max_backups=? where id=? '''
    print(settings)
    cur = conn.cursor()
    data = tuple(settings.values())
    cur.execute(sql, data)
    conn.commit()


def criseDetection():
    conn = create_connection()
    sql = '''select * from audit a,settings s where a.cpu>s.threshold_cpu or a.memory>s.threshold_memory or a.storage>s.threshold_storage'''
    cur = conn.cursor()
    cur.execute(sql)
    return cur.fetchall()


def init():
    conn = create_connection()

    audit_table = '''create table if not exists audit(
    id integer primary key autoincrement,
    createdon datetime default current_timestamp,
    user varchar(20),
    cpu decimal,
    memory decimal,
    storage decimal)'''
    settings_table = '''create table if not exists settings(
    id integer primary key autoincrement,
    createdon datetime default current_timestamp,
    threshold_cpu integer default 5,
    threshold_memory integer default 5 ,
    threshold_storage integer default 5,
    max_backups integer default 10)'''
    settings_default = '''insert into settings(threshold_cpu) values(5);'''
    print('db init')
    cur = conn.cursor()
    cur.execute(audit_table)
    cur.execute(settings_table)
    cur.execute(settings_default)
    conn.commit()


if __name__ == '__main__':
    init()
