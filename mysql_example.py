import mysql.connector
import mysql.connector.cursor
import mysql.connector.types
import socket


def db_up(hostname: str = "localhost", port: int = 3306) -> bool:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    if sock.connect_ex((hostname, port)) == 0:
        sock.close()
        return True
    else:
        sock.close()
        return False


def db_exists(cursor: mysql.connector.cursor.MySQLCursorAbstract, db_name: str) -> bool:
    cursor.execute("SHOW DATABASES")
    for db in cursor:
        if db[0] == db_name:
            return True
    return False


def main(argv=None) -> int:
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "rootsql"
    )
    mycursor = mydb.cursor()

    print(db_exists(mycursor, "sys"))
    print(db_exists(mycursor, "movie_db"))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
