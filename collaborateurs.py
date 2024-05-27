#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code diffusé aux étudiants de BUT1 dans le cadre de la SAE 2.02: Exploration algorithmique d'un problème.

IUT d'Orleans BUT1 Informatique 2021-2022 
"""

import networkx as nx
import json
import matplotlib.pyplot as plt

def json_vers_nx(nom_fic):
    listes = []
    fic = open(nom_fic,"r",encoding='utf-8')
    for ligne in fic:
        l = json.loads(ligne)
        listes.append(l["cast"])
    res = nx.Graph()
    for ligne in listes:
        for acteur1 in ligne:
            if acteur1 not in res.nodes:
                res.add_node(acteur1)
                for acteur2 in ligne:
                    if acteur2 in res.nodes and acteur1 != acteur2:
                        res.add_edge(acteur1,acteur2)
    print(res)
    nx.draw(res,with_labels=False, node_size=3)
    plt.show() 
    return res


fichier = "data_100.txt"

G = json_vers_nx(fichier)
print(G)

def collaborateurs_communs(G,acteur1,acteur2):
    """la liste des collaborateurs communs entre deux acteurs

    Args:
        G (Graph): le graphe à étudier
        act1 (str): le premier acteur
        act2 (str): le deuxième acteur

    Returns:
        list: la liste des collaborateurs communs entre deux acteurs
    """
    if act1 not in G.nodes or acteur2 not in G.nodes:
        return None
    res = set()
    for voisin in G.adj[acteur1]:
        if voisin in G.adj[acteur2]:
            res.add(voisin)
    return res    

act1 = "[[Paul Reubens]]"
act2 = "[[Pat Hingle]]"

d = collaborateurs_communs(G,act1,act2)

def collaborateurs_proches(G,u,k):
    """Fonction renvoyant l'ensemble des acteurs à distance au plus k de l'acteur u dans le graphe G. La fonction renvoie None si u est absent du graphe.
    
    Parametres:
        G: le graphe
        u: le sommet de départ
        k: la distance depuis u
    """
    if u not in G.nodes:
        print(u,"est un illustre inconnu")
        return None
    collaborateurs = set()
    collaborateurs.add(u)
    print(collaborateurs)
    for i in range(k):
        collaborateurs_directs = set()
        for c in collaborateurs:
            for voisin in G.adj[c]:
                if voisin not in collaborateurs:
                    collaborateurs_directs.add(voisin)
        collaborateurs = collaborateurs.union(collaborateurs_directs)
    return collaborateurs