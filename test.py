# import requests
# from brave import Brave
# from bs4 import BeautifulSoup
# from utils.const import BRAVE_API_KEY

# query ="Explain me about cough"
# brave = Brave(api_key=BRAVE_API_KEY)

# data = []
# num_results=2
# search_result = brave.search(q=query,count=num_results)
# websearch = search_result.web_results
# for i in websearch:
#     response = requests.get(i['url'])
#     if response.status_code != 200:
#         raise Exception("Failed to load page")

#     soup = BeautifulSoup(response.content, 'html.parser')
#     articles = soup.find_all('p')
#     for i in articles:
#         print(i.text)

from utils.database.graph import Neo4Graph

graph = Neo4Graph()
graph.delete_all()
# query = ["""MATCH (p:Patient {full_name: 'hansen rulicio'})-[r]-(related)
# RETURN p, r, related"""]

# record = graph.read_transaction(queries=query)
# print(record)