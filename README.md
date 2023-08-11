# Psycopg2 Utility Functions

Your Package Name is a Python package that provides utility functions for basic PostgreSQL database operations using the psycopg2 library.

## Installation

You can install Your Package Name using pip:

```bash
pip install psycopg2-utility-functions
```

# Usage
## Connecting to the Database

To establish a connection to a PostgreSQL database:

```commandline
from psycopg2_utility_functions import connect_to_database

connection = connect_to_database(database='your_db_name', user='your_db_user', password='your_db_password', host='your_db_host', port='your_db_port')
```

## Executing Queries

To execute a SQL query on the connected database:

```commandline
from psycopg2_utility_functions import execute_query

query = "CREATE TABLE users (id serial PRIMARY KEY, name varchar, age int);"
execute_query(connection, query)
```

## Fetching Data

To fetch data from the database and create objects using a custom class:

```commandline
from psycopg2_utility_functions import fetch_data

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

query = "SELECT name, age FROM users WHERE age > %s;"
users = fetch_data(connection, query, User, values=(25,))
```

## Inserting Data

To insert a single row of data into a table:

```commandline
from psycopg2_utility_functions import insert_data

data = {'name': 'Alice', 'age': 30}
insert_data(connection, 'users', data)
```

## Updating Data

To update rows in a table based on a condition:

```commandline
from psycopg2_utility_functions import update_data

condition = "age > %s"
data = {'age': 31}
update_data(connection, 'users', condition, data)
```

## Deleting Data

To delete rows from a table based on a condition:

```commandline
from psycopg2_utility_functions import delete_data

condition = "age < %s"
delete_data(connection, 'users', condition)
```


## Contributing

Feel free to contribute to this project by opening issues or pull requests on the GitHub repository.

## License

This project is licensed under the MIT License.

