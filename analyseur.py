import argparse

# Parser used for the CLI help prompt
parser = argparse.ArgumentParser(description='Analyse fréquentielle d\'un texte.')

parser.add_argument('texte', metavar='texteAnalyse', type=str, nargs=1,
                    help='chemin vers le fichier txt à analyser')
parser.add_argument('-d', '--destination', type=str, metavar='DEST', default='.',
                    help='destination du fichier d\'analyse (défaut : .)')

args = parser.parse_args()