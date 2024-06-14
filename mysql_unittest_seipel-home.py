import mysql_example as sql
import mysql.connector
import unittest


class SQLTest(unittest.TestCase):

    def test_server_up(self):
        self.assertTrue(sql.db_up("seipel-home"), 
                        "Cannot connect to MySQL homeserver "
                        + "at seipel-home:3306")
    
    def test_db_exists(self):
        test_db = mysql.connector.connect(host = "seipel-home",
                                          user = "root",
                                          password = "rootsql")
        test_cursor = test_db.cursor()
        self.assertTrue(sql.db_exists(test_cursor, "sys"))
        self.assertTrue(sql.db_exists(test_cursor, "mysql"))


if __name__ == '__main__':
    unittest.main()