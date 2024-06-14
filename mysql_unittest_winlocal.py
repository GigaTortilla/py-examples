import mysql_example as sql
import mysql.connector
import unittest


class SQLTest(unittest.TestCase):

    def test_server_up(self):
        self.assertTrue(sql.db_up(), "Cannot connect to local MySQL server")
        self.assertFalse(sql.db_up("192.168.178.41"), 
                         "The server 192.168.178.41 should "
                         + "not be accessible as MySQL-DB")
    
    def test_db_exists(self):
        test_db = mysql.connector.connect(host = "localhost",
                                          user = "root",
                                          password = "rootsql")
        test_cursor = test_db.cursor()
        self.assertTrue(sql.db_exists(test_cursor, "sys"))
        self.assertTrue(sql.db_exists(test_cursor, "mysql"))
        self.assertFalse(sql.db_exists(test_cursor, "NoSQL_ftw"), 
                         "The DB \"NoSQL_ftw\" should not exist.")


if __name__ == '__main__':
    unittest.main()