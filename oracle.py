import requetes
import matplotlib.pyplot as plt
import networkx as nx

def afficher_graphe(G):
    """Fonction affichant le graphe G

    Args:
        G (graph): le graphe
    """
    nx.draw(G, with_labels=True)
    plt.show()

def programme_principal():
    print("Bonjour")
    quitter="_"
    fichier="_"
    while fichier not in ["data.txt","data_100.txt","data_1000.txt","data_10000.txt"]:
        fichier=input("Donner moi le nom du fichier txt \n")
    G = requetes.json_vers_nx(fichier)
    while quitter not in "O":
        quitter="_"
        que_voulez_vous="_"

        while que_voulez_vous not in ("ABCDEFGHX"):
            que_voulez_vous=input("Que voulez vous ? \n"
                                "Obtenir les collaborateurs communs à deux acteurs (A) \n"
                                "Obtenir les collaborateurs proches d'un acteur (B) \n"
                                "Savoir si 2 acteurs sont proches (C) \n"
                                "Obtenir la centralité d'un acteur (D) \n"
                                "Obtenir l'acteur le plus central du graphe (E)) \n"
                                "Obtenir l'eloignement maximale entre toute paire d'un graphe (F) \n"
                                "Obtenir la distance entre 2 acteurs (G) \n"
                                "Afficher le graphe (H) \n"
                                "Si vous voulez quitter taper 'X' \n")
        if que_voulez_vous == "A":
            colab_commun = "_"
            while colab_commun not in "ON":
                colab_commun=input("Voulez vous obtenir les collaborateurs communs à deux acteurs O/N \n")
                if colab_commun=="O":
                    colab_commun_act1="_"
                    colab_commun_act2="_"
                    while colab_commun_act1 not in G.nodes or colab_commun_act2 not in G.nodes:
                        colab_commun_act1=input("Dites moi le nom du premier acteur  \n")
                        if colab_commun_act1 in G.nodes:
                            colab_commun_act2=input("Dites moi le nom du deuxième acteur \n")
                            if colab_commun_act2 not in G.nodes:
                                print("Je ne connais pas cette acteur")
                        else:
                            print("Je ne connais pas cette acteur")
                    print(requetes.collaborateurs_communs(G, colab_commun_act1, colab_commun_act2))

        if que_voulez_vous == "B":
            colab_proches = "_"
            while colab_proches not in "ON":
                colab_proches=input("Voulez vous obtenir les collaborateurs proches à deux acteurs O/N \n")
                if colab_proches=="O":
                    colab_proches_act="_"
                    colab_proches_val="_"
                    while colab_proches_act not in G.nodes or type(colab_proches_val) != int:
                        colab_proches_act=input("Dites moi un acteur  \n")
                        if colab_proches_act in G.nodes:
                            colab_proches_val=int(input("Dites moi la distance depuis l'acteur  \n"))
                            if type(colab_proches_val) is not int:
                                print("Donnez un entier")
                        else:
                            print("Je ne connais pas cette acteur")
                    print(requetes.collaborateurs_proches(G, colab_proches_act, colab_proches_val))

        elif que_voulez_vous == "C":
            acteur_proche = "_"
            while acteur_proche not in "ON":
                acteur_proche=input("Voules vous savoir si 2 acteurs sont proches ? O/N \n")
                if acteur_proche=="O":
                    acteur_proche1="_"
                    acteur_proche2="_"
                    while acteur_proche1 not in G.nodes and acteur_proche2 not in G.nodes:
                        acteur_proche1=input("Dites moi le nom du premier acteur  \n")
                        if acteur_proche1 in G.nodes:
                            acteur_proche2=input("Dites moi le nom du deuxième acteur \n")
                            if acteur_proche2 not in G.nodes:
                                print("Je ne connais pas cette acteur")
                        else:
                            print("Je ne connais pas cette acteur")
                        
                    print(requetes.est_proche(G, acteur_proche1, acteur_proche2))
        elif que_voulez_vous == "D":
            centralite_acteur = "_"
            while centralite_acteur not in "ON":
                centralite_acteur=input("Voulez vous obtenir la centralité d'un acteur ? O/N \n")
                if centralite_acteur=="O":
                    centre_acteur="_"
                    while centre_acteur not in G.nodes:
                        centre_acteur=input("Dites moi le nom d'un acteur  \n")
                        if centre_acteur not in G.nodes:
                            print("Je ne connais pas cette acteur")
                    print(requetes.centralite(G, centre_acteur))
        elif que_voulez_vous =="E":
            centre_acteur = "_"
            while centre_acteur not in "ON":
                centre_acteur=input("Voulez vous obtenir l'acteur le plus central du graphe ? O/N\n")
                if centre_acteur=="O":
                    print(requetes.centre_hollywood(G))
        elif que_voulez_vous=="F":
            distance_max = "_"
            while distance_max not in "ON":
                distance_max=input("Voulez vous obtenir l'eloignement maximale entre toute paire d'un graphe ? O/N \n")
                if distance_max=="O":
                    print(requetes.eloignement_max(G))
        elif que_voulez_vous=="G":
            distance_act = "_"
            while distance_act not in "ON":
                distance_act=input("Voulez vous connaitre la distance entre 2 acteurs ? O/N \n")
                distance_act1="_"
                distance_act2="_"
                while distance_act1 not in G.nodes or distance_act2 not in G.nodes:
                    distance_act1=input("Dites moi le nom du premier acteur  \n")
                    if distance_act1 in G.nodes:
                        distance_act2=input("Dites moi le nom du deuxième acteur \n")
                        if distance_act2 not in G.nodes:
                            print("Je ne connais pas cette acteur")
                    else:
                        print("Je ne connais pas cette acteur")
                print(requetes.distance_naive(G, distance_act1, distance_act2))
        elif que_voulez_vous=="H":
            cond = "_"
            while cond not in "ON":
                cond = input("Voulez-vous afficher le graphe ? O/N \n ")
                if cond == "O":
                    afficher_graphe(G)
        while quitter not in "ON":
            quitter=input("Voulez vous quitter ? O/N \n")

programme_principal()