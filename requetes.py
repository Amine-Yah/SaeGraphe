#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Code diffusé aux étudiants de BUT1 dans le cadre de la SAE 2.02: Exploration algorithmique d'un problème.

IUT d'Orleans BUT1 Informatique 2021-2022 
"""

import matplotlib.pyplot as plt
import networkx as nx
import json
from collections import deque

# Q1

def json_vers_nx(chemin):
    """Convertir un fichier TXT au format JSON en un graphe NetworkX.

    Args:
        chemin (str): chemin vers un fichier txt

    Returns:
        Graph: un graphe
    """
    listes = []
    fic = open(chemin,"r",encoding='utf-8')
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
    #nx.draw(res,with_labels=False, node_size=3)
    #plt.show() 
    return res

# Q2

def collaborateurs_communs(G,u,v): 
    """la liste des collaborateurs communs entre deux acteurs

    Args:
        G (Graph): le graphe à étudier
        u (str): le premier acteur
        v (str): le deuxième acteur

    Returns:
        set: l'ensemble des collaborateurs communs entre deux acteurs
    """
    if u not in G.nodes or v not in G.nodes:
        return None
    res = set()
    for voisin in G.adj[u]:
        if voisin in G.adj[v]:
            res.add(voisin)
    return res    

# Q3
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

def est_proche(G,u,v,k=1):
    """
    Fonction qui retourne True si les 2 acteurs sont proche sinon False.
    
    Parametres:
        G(graph): le graphe
        u(str): le premier acteur
        v(str): le deuxième acteur

    Returns:
        bool: True si les 2 acteurs sont proche sinon False
    """  
    try:
        return u in collaborateurs_proches(G,v,k)
    except:
        return None

def distance(G,act1,act2):
    """
    Fonction qui retourne la distance entre deux acteurs.
    
    Parametres:
        G(graph): le graphe
        act1(str): le premier acteur
        act2(str): le deuxième acteur

    Returns:
        int: distance entre deux acteurs
    """  
    visited = set()
    queue = deque()
    distance = 0
    queue.append((act1,0))
    while queue:
        node,distance = queue.popleft()
        visited.add(node)
        if node == act2:
            return distance
        for n in G.adj[node] :
            if n == act2:
                return distance+1
            elif n not in visited:
                queue.append((n,distance+1))
                visited.add(n)
    return distance

def distance_naive(G,act1,act2):
    """
    Fonction qui retourne la distance entre deux acteurs.
    
    Parametres:
        G(graph): le graphe
        act1(str): le premier acteur
        act2(str): le deuxième acteur

    Returns:
        int: distance entre deux acteurs
    """  
    try:
        return nx.shortest_path_length(G,act1,act2)
    except:
        return None

# Q4
def centralite(G,acteur):
    """Fonction renvoyant la plus grande distance entre un acteur et les autres acteurs du graphe G avec le parcours en largeur et la distances entre acteurs.

    Args:
        G (graph): le graphe
        acteur (str): un acteur

    Returns:
        int : la plus grande distance entre un acteur et les autres acteurs du graphe G.
    """
    somme = None
    for voisin in G.nodes():
        val = distance_naive(G, acteur, voisin)
        if val is not None and (somme is None or val > somme[-1]):
            if somme is None:
                somme = [val]
            else:
                somme.append(val)
    if somme is None:
        return None
    return somme[-1]


def centre_hollywood(G):
    """Fonction renvoyant l'acteur le plus au centre du graphe.

    Args:
        G (graph): le graphe

    Returns:
        str : l'acteur le plus au centre du graphe
    """
    val_centre = None
    centre = "_"
    for voisin in G.nodes():
        val = centralite(G,voisin)
        if (val_centre is None ):
            val_centre = val
            centre=voisin
        if val_centre<val:
            val_centre = val   
    return centre

# Q5
def eloignement_max(G:nx.Graph):
    """Fonction renvoyant l'eloignement maximum entre tout les acteurs

    Args:
        G (graph): le graphe

    Returns:
        int: l'eloignement maximum entre tout les acteurs
    """
    distance_max = 0
    for a1 in G.nodes():
        for a2 in G.nodes():
            if a1 != a2:
                d = distance_naive(G,a1,a2)
                if d > distance_max:
                    distance_max = d
    return distance_max

# Bonus
def centralite_groupe(G,S):
    return centre_hollywood(G.subgraph(S))