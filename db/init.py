from db.db_manager import DataBaseManager
import configparser

config = configparser.ConfigParser()
config.read('./config.ini')
db_config = config['database']

db = DataBaseManager(db_config['dbname'], db_config['user'], db_config['password'])

class CreateTable:
    def execute(self) -> None:
        db.create_table("table name", {
            'column': 'value'
        })