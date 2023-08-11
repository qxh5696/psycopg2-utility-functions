import unittest
from main import connect_to_database, execute_query, fetch_data, insert_data, update_data, delete_data


class TestPsycopg2UtilityFunctions(unittest.TestCase):

    def setUp(self):
        self.connection = connect_to_database(
            database='your_test_db',
            user='your_test_user',
            password='your_test_password',
            host='localhost',
            port='5432'
        )

        # Create a temporary test_table for the tests
        self.create_test_table()

    def tearDown(self):
        # Drop the temporary test_table
        self.drop_test_table()
        self.connection.close()

    def create_test_table(self):
        query = "CREATE TABLE test_table (id serial PRIMARY KEY, name varchar, age int);"
        execute_query(self.connection, query)

    def drop_test_table(self):
        query = "DROP TABLE IF EXISTS test_table;"
        execute_query(self.connection, query)

    def test_execute_query(self):
        query = "CREATE TABLE test_table (id serial PRIMARY KEY, name varchar);"
        execute_query(self.connection, query)

        # Check if the table was created
        cursor = self.connection.cursor()
        cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'test_table')")
        result = cursor.fetchone()[0]
        cursor.close()
        self.assertTrue(result)

    def test_fetch_data(self):
        query = "SELECT name, age FROM users WHERE age > %s;"

        class User:
            def __init__(self, name, age):
                self.name = name
                self.age = age

        users = fetch_data(self.connection, query, User, values=(25,))
        self.assertIsInstance(users, list)
        self.assertTrue(all(isinstance(user, User) for user in users))

    def test_insert_data(self):
        data = {'name': 'Alice', 'age': 30}
        insert_data(self.connection, 'test_table', data)

        # Check if data was inserted
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM test_table")
        result = cursor.fetchone()[0]
        cursor.close()
        self.assertEqual(result, 1)

    def test_update_data(self):
        condition = "age > %s"
        data = {'age': 31}
        update_data(self.connection, 'test_table', condition, data)

        # Check if data was updated
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM test_table WHERE age > 31")
        result = cursor.fetchone()[0]
        cursor.close()
        self.assertEqual(result, 1)

    def test_delete_data(self):
        condition = "age < %s"
        delete_data(self.connection, 'test_table', condition)

        # Check if data was deleted
        cursor = self.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM test_table")
        result = cursor.fetchone()[0]
        cursor.close()
        self.assertEqual(result, 0)


if __name__ == '__main__':
    unittest.main()
