import psycopg2
import psycopg2.extras

class DataBaseManager():

    def __init__(self, dbname: str, user: str, password=None):
        self.conn = psycopg2.connect(f'dbname={dbname} user={user} password={password}')

    def __del__(self):
        self.conn.close()

    def _execute(self, command: str, values = None):
        with self.conn:
            cursor = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
            cursor.execute(command, values or [])
            return cursor
        
    def create_table(self, table_name: str, columns: dict, extra=None) -> None:
        query = f'CREATE TABLE IF NOT EXISTS {table_name} ('
        colums_with_types = [
            f'{column_name} {data_type}'
            for column_name, data_type in columns.items()
        ]
        query += ', '.join(colums_with_types)
        if extra:
            query += f', {extra}'
        query += ')'
        self._execute(query)

    def add(self, table_name: str, data: dict, return_column=None) -> any:
        """добавление новой записи в таблицу

        Args:
            table_name (str): название таблицы
            data (dict): парамеры
        """
        placeholders = ', '.join(['%s'] * len(data))
        column_names = ', '.join(data.keys())
        column_values = tuple(data.values())

        query = f'''
            INSERT INTO {table_name}
            ({column_names})
            VALUES ({placeholders})
            '''
        if return_column:
            query += f'RETURNING {return_column};'
            return self._execute(query, column_values)
        
        query += ';'
        self._execute(query, column_values)
    
    def delete (self, table_name: str, criteria: dict) -> None:
        """удаление записи из таблицы

        Args:
            table_name (str): название таблицы
            criteria (dict): критерий
        """
        placeholders = [f'{column} = %s' for column in criteria.keys()]
        delete_criteria = ' AND '.join(placeholders)
        self._execute(
            f'''
            DELETE FROM {table_name}
            WHERE {delete_criteria};
            ''',
            tuple(criteria.values()),
        )

    def select(self, table_name: str, criteria=None, order_by=None, limit=100):
        """получить данные из таблицы

        Args:
            table_name (str): название таблицы
            criteria (_type_, optional): критерий. Defaults to None.
            order_by (_type_, optional): правила сортировки. Defaults to None.
            limit (int, optional): количество записей. Defaults to 100.

        Returns:
            _type_: _description_
        """
        criteria = criteria or {}
        
        query = f'SELECT * FROM {table_name}'

        if criteria:
            placeholders = [f'{column} = %s' for column in criteria.keys()]
            select_criteria = ' AND '.join(placeholders)
            query += f' WHERE {select_criteria}'

        if order_by:
            query += f' ORDER BY {order_by}'
        
        query += f' LIMIT {limit}'

        return self._execute(
            query,
            tuple(criteria.values())
        )
    
    def update(self, table_name: str, data: dict, criteria=None) -> None:
        """обновить запись в таблице

        Args:
            table_name (str): название таблицы
            data (dict): данные, которые надо обновить
            criteria (_type_, optional): критерий. Defaults to None.
        """
        criteria = criteria or {}

        query = f'UPDATE {table_name} SET '
        column_names = ' = %s, '.join(data.keys())
        column_names += ' = %s'
        query += column_names
        column_values = tuple(data.values())

        if criteria:
            placeholders = [f'{column} = %s' for column in criteria.keys()]
            select_criteria = ' AND '.join(placeholders)
            query += f' WHERE {select_criteria}'
            column_values += tuple(criteria.values())

        self._execute(
            query,
            column_values
        )
    