import argparse

# Parser used for the CLI help prompt
parser = argparse.ArgumentParser(description='Génère des mots à partir de probabilités d\'apparition.')

parser.add_argument('fichier', metavar='fichierProba', type=str, nargs=1,
                    help='chemin vers le fichier contenant les probas')
parser.add_argument('-q', '--quantite', type=int, metavar='QTE', default=1,
                    help='nombre de mots générés (défaut : 1)')
parser.add_argument('-t', '--taille', type=int, metavar='TAILLE', default='-1',
                    help='taille des mots générés (défaut : aléatoire)')

args = parser.parse_args()