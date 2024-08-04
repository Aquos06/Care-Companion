from utils.database.graph import Neo4Graph
from utils.hash import verify_password

def login(email:str, password: str):
    graph = Neo4Graph()
    cypher = [f"MATCH (p:Patient {{email_addr: '{email}'}}) RETURN p.password"]
    patient_password = graph.read_transaction(cypher)
    if patient_password:
        pwd = patient_password[0][0]['p.password']
        return verify_password(stored_password=pwd, provided_password=password)
    return False