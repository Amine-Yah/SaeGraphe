import json
import networkx as nx
import matplotlib.pyplot as plt

def json_to_networkx(json_data):
    # Créer un nouveau graphe
    G = nx.Graph()

    # Parcourir chaque film dans les données JSON
    for film in json_data:
        # Ajouter un nœud pour chaque film
        G.add_node(film["title"], year=film["year"])

        # Ajouter des nœuds pour les acteurs, les réalisateurs et les producteurs
        casts = film["casts"].split(", ")
        directors = film["directors"].split(", ")
        producers = film["producers"].split(", ")

        for actor in casts + directors + producers:
            G.add_node(actor.strip())

            # Ajouter une arête entre le film et chaque acteur, réalisateur et producteur
            G.add_edge(film["title"], actor.strip())

    nx.draw(G, with_labels=True)
    plt.show()
    return G

# Charger les données JSON depuis un fichier
with open('data.json', 'r') as file:
    data = json.load(file)

graphe = json_to_networkx(data)
# Convertir les données JSON en un graphe NetworkX
print(graphe)
# Afficher les informations sur le graphe

