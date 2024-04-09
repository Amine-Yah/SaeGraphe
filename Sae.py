import json
import networkx as nx

def json_vers_nx(chemin):
    with open(chemin, 'r') as f:
        data = json.load(f)
    
    # Création du graphe
    G = nx.Graph()
    
    # Ajout des arêtes (collaborations)
    for film in data:
        acteurs = data[film]
        for i in range(len(acteurs)):
            for j in range(i+1, len(acteurs)):
                G.add_edge(acteurs[i], acteurs[j], film=film)
    
    return G

# Chemin vers le fichier JSON contenant les données de collaborations
chemin_json = 'data.txt'

# Conversion des données JSON en graphe NetworkX
graphe_collaborations = json_vers_nx(chemin_json)