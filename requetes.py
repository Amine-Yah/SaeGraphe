
import json
"""
# Q1
def json_vers_nx(chemin):
# Q2
def collaborateurs_communs(G,u,v):
# Q3
def collaborateurs_proches(G,u,k):
def est_proche(G,u,v,k=1):
def distance_naive(G,u,v):
def distance(G,u,v):
# Q4
def centralite(G,u):
def centre_hollywood(G):
# Q5
def eloignement_max(G:nx.Graph):
# Bonus
def centralite_groupe(G,S):
"""

"""
def json_vers_nx(chemin):
    with open(chemin, 'r') as f:
        data = json.load(f)
    
    G = nx.Graph()
    
    for film in data:
        acteurs = data[film]
        for i in range(len(acteurs)):
            for j in range(i+1, len(acteurs)):
                G.add_edge(acteurs[i], acteurs[j], film=film)
    
    return G

chemin_json = 'data.txt'

graphe_collaborations = json_vers_nx(chemin_json)


def txt_to_json(file_path):
    data_list = []
    with open(file_path, 'r') as file:
        for line in file:
            data = json.loads(line)
            data_list.append(data)
    return data_list


file_path = "data.txt"
json_data = txt_to_json(file_path)
print(json_data)


"""
"""
def txt_to_json(file_path):
    data_list = []
    with open(file_path, 'r') as file:
        for line in file:
            data = json.loads(line)
            data_list.append(data)
    return data_list
"""

def txt_to_json(chemin, nouveau_chemin):
    try :

        fichier = open(chemin, 'r')
        nouveau_fichier = open(nouveau_chemin, 'w')
        data = {"collaborations": []}
        with fichier:
            for line in fichier:
                if line.strip():  
                    acteurs = line.strip().split(', ')
                    collaboration = {"acteurs": acteurs}
                    data["collaborations"].append(collaboration)
        with nouveau_fichier:
            json.dump(data, nouveau_fichier, indent=4, ensure_ascii=False)
    except :
        print("il y'a une erreur")


def txt_to_json(input_file, output_file):
    data = {"collaborations": []}

    with open(input_file, 'r') as f:
        for line in f:
            elements = line.strip().split(', ')
            if len(elements) == 6:
                title, casts, directors, producers, companies, year = elements
                collaboration = {
                    "title": title,
                    "casts": casts,
                    "directors": directors,
                    "producers": producers,
                    "companies": companies,
                    "year": year
                }
                data["collaborations"].append(collaboration)

    with open(output_file, 'w') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def txt_to_json(input_file, output_file):
    with open(input_file, 'r') as f:
        data = f.readlines()

    formatted_data = []
    for line in data:
        entry = json.loads(line)
        formatted_entry = {
            "title": entry.get("title", ""),
            "casts": ", ".join(entry.get("cast")),
            "directors": ", ".join(entry.get("directors", [])),
            "producers": ", ".join(entry.get("producers", [])),
            "companies": ", ".join(entry.get("companies", [])),
            "year": entry.get("year", "")
            
        }
        formatted_data.append(formatted_entry)

    with open(output_file, 'w') as f:
        json.dump(formatted_data, f, indent=4, ensure_ascii=False)

txt_to_json("data.txt", "data.json")


#Question 1
"""
def json_to_networkx(file_path):
    G = nx.Graph()
    
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            movie_data = json.loads(line)
            cast = movie_data.get('cast', [])
            for actor_list in cast:
                for i in range(len(actor_list)):
                    for j in range(i+1, len(actor_list)):
                        actor1 = actor_list[i].strip('[').strip(']').strip('[').strip(']').strip(' ').split('|')[0]
                        actor2 = actor_list[j].strip('[').strip(']').strip('[').strip(']').strip(' ').split('|')[0]
                        G.add_edge(actor1, actor2, movie=movie_data['title'])
    return G


def json_vers_nx(chemin):
    with open(chemin, 'r') as fichier:
        donnees = json.load(fichier)
    
    G = nx.Graph()
    
    for film in donnees:
        acteurs = film['acteurs']
        for i in range(len(acteurs)):
            for j in range(i+1, len(acteurs)):
                G.add_edge(acteurs[i], acteurs[j])
    
    return G

file_path = "data.txt"

graph = json_vers_nx(file_path)

print(graph)

def json_vers_nx(chemin):
    res = []
    fichier = open(nom_fichier, 'r')
    fichier.readline()
    for ligne in fichier:
        champs = ligne.split(',')
        if champs[8]==True:
            res.append((champs[0], champs[1], champs[2], int(champs[3]), int(champs[4]), champs[5], champs[6], champs[7], True))
        else:
            res.append((champs[0], champs[1], champs[2], int(champs[3]), int(champs[4]), champs[5], champs[6], champs[7], False))
    fichier.close()
    return res

"""
"""
def lire_un_fichier_txt(file_path):
    donnees = []
    with open(file_path, 'r') as fichier:
        for ligne in fichier :
            objet_from = json.leads(ligne.strip[])
            donnees.append(objet_from)
    return donnees
"""