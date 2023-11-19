from .init import db
import json

class OperationExampleOne:
    def execute(self) -> list:
        return db.select('table', {'param': 'param value'}).fetchone()
    
class OperationExampleList:
    def execute(self) -> list:
        hosts = db.select('table', {'param': 'param value'}).fetchall()
        res = [dict(host) for host in hosts]
        return res