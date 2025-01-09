from functions import *  # Importer toutes les fonctions du fichier functions.py

def main():
    # Demander à l'utilisateur de saisir le chemin vers le fichier mirna.txt
    mirna_file = input("Enter the path to the mirna.txt file: ").strip()
    # Demander à l'utilisateur de saisir le chemin vers le fichier species.txt
    species_file = input("Enter the path to the species.txt file: ").strip()
    # Demander à l'utilisateur de saisir le dossier de sortie souhaité
    output_folder = input("Enter the desired output folder: ").strip()

    # Vérifier si le fichier mirna.txt existe
    if not os.path.isfile(mirna_file):
        print(f"Error: {mirna_file} does not exist.")  # Afficher un message d'erreur si le fichier n'existe pas
        return  # Arrêter l'exécution de la fonction

    # Vérifier si le fichier species.txt existe
    if not os.path.isfile(species_file):
        print(f"Error: {species_file} does not exist.")  # Afficher un message d'erreur si le fichier n'existe pas
        return  # Arrêter l'exécution de la fonction

    # Ouvrir le fichier species.txt en mode lecture
    with open(species_file, 'r') as f:
        # Lire les lignes du fichier et créer un ensemble des espèces d'intérêt
        species_of_interest = {line.strip() for line in f if line.strip()}

    # Traiter les données du fichier mirna.txt en utilisant les espèces d'intérêt
    species_sequences = process_data(mirna_file, species_of_interest)

    # Vérifier si des séquences correspondantes ont été trouvées
    if not species_sequences:
        print("No matching species found in the data.")  # Afficher un message si aucune espèce correspondante n'a été trouvée
        return  # Arrêter l'exécution de la fonction

    print(f"Extracted sequences for {len(species_sequences)} species of interest.")

    calculate_base_rates_and_draw_charts(species_sequences, output_folder)
    mean_overall_chart(species_sequences)

if __name__ == "__main__":
    main()