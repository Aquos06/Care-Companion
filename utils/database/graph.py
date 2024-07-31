from neo4j import GraphDatabase
from typing import List, Dict

class Neo4Graph:
    def __init__(self, uri: str, username: str, password:str) -> None:
        self.driver = GraphDatabase.driver(uri=uri, auth=(username,password))
        
    def execute_query(self, queries: List[str]):
        with self.driver.session() as session:
            for query in queries:
                session.run(query)
    def close(self):
        if self.driver is not None:
            self.driver.close()
            
    def delete_all(self):
        self.execute_query(["MATCH (n) DETACH DELETE n"])
        
    def read_transaction(self, queries: List[str]) -> List[List[Dict[str, any]]]:
        def run_query(tx, query):
            result = tx.run(query)
            return [record.data() for record in result]

        results = []
        with self.driver.session() as session:
            for query in queries:
                result = session.execute_read(run_query, query)
                results.append(result)
        return results