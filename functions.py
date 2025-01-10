import matplotlib.pyplot as plt  # Importer la bibliothèque matplotlib pour créer des graphiques
from collections import defaultdict  # Importer defaultdict pour créer des dictionnaires avec des valeurs par défaut
import os  # Importer le module os pour interagir avec le système d'exploitation

def is_nucleotide_sequence(word):
    """Vérifie si un mot est une séquence de nucléotides valide."""
    # Vérifier que chaque caractère du mot est un nucléotide valide (A, C, G, U) et que le mot est en majuscules
    return all(c in "ACGU" for c in word) and word.isupper()

def is_valid_species_name(word):
    """Vérifie si un mot commence par une lettre majuscule suivie de lettres minuscules."""
    # Vérifier que le premier caractère est une majuscule et que les caractères suivants sont des minuscules
    return word[0].isupper() and word[1:].islower()

def process_data(mirna_file, species_of_interest):
    """
    Traite les données du fichier pour extraire les espèces et leurs séquences de nucléotides,
    filtrées par les espèces d'intérêt.
    """
    # Créer un dictionnaire pour stocker les séquences de chaque espèce
    species_sequences = defaultdict(list)

    # Ouvrir le fichier mirna.txt en mode lecture
    with open(mirna_file, 'r') as f:
        # Lire chaque ligne du fichier
        for line in f:
            # Séparer la ligne en mots
            words = line.strip().split()
            # Vérifier que la ligne contient au moins deux mots (une espèce et une séquence)
            if len(words) >= 2:
                species = words[0]  # Le premier mot est le nom de l'espèce
                sequence = words[1]  # Le deuxième mot est la séquence de nucléotides
                # Vérifier que le nom de l'espèce est valide et que la séquence est valide
                if is_valid_species_name(species) and is_nucleotide_sequence(sequence):
                    # Vérifier que l'espèce est dans la liste des espèces d'intérêt
                    if species in species_of_interest:
                        # Ajouter la séquence au dictionnaire sous le nom de l'espèce
                        species_sequences[species].append(sequence)

    # Retourner le dictionnaire des séquences par espèce
    return species_sequences

def calculate_base_rates_and_draw_charts(species_sequences, output_folder):
    """
    Calculer les taux de bases et dessiner des graphiques en secteurs pour chaque espèce.
    """
    # Créer le dossier de sortie s'il n'existe pas
    os.makedirs(output_folder, exist_ok=True)

    # Pour chaque espèce et ses séquences
    for species, sequences in species_sequences.items():
        # Concaténer toutes les séquences en une seule chaîne
        concatenated_sequence = "".join(sequences)
        # Calculer le nombre total de bases
        total_bases = len(concatenated_sequence)
        # Compter le nombre de chaque base (A, C, G, U)
        base_counts = {
            "A": concatenated_sequence.count("A"),
            "C": concatenated_sequence.count("C"),
            "G": concatenated_sequence.count("G"),
            "U": concatenated_sequence.count("U")
        }

        # Calculer les pourcentages de chaque base
        base_percentages = {base: (count / total_bases) * 100 for base, count in base_counts.items()}

        # Dessiner un graphique en secteurs
        plt.figure(figsize=(6, 6))
        plt.pie(
            base_percentages.values(),
            labels=base_percentages.keys(),
            autopct='%1.1f%%',
            startangle=140
        )

        # Ajouter un titre au graphique
        plt.title(f"Base Composition for {species}")
        # Définir le chemin du fichier de sortie pour le graphique
        output_file = os.path.join(output_folder, f"{species.replace(' ', '_')}_base_composition.png")
        # Sauvegarder le graphique en tant qu'image
        plt.savefig(output_file)
        # Fermer la figure pour libérer de la mémoire
        plt.close()
    # Afficher un message indiquant où les graphiques ont été sauvegardés
    print(f"Pie charts saved in: {output_folder}")

def mean_overall_chart(species_sequences):
    """
    Calculer et dessiner un graphique des taux de bases moyens pour toutes les espèces combinées.
    """
    # Concaténer toutes les séquences de toutes les espèces en une seule chaîne
    concatenated_sequence = "".join(sequence for sequences in species_sequences.values() for sequence in sequences)
    # Calculer le nombre total de bases
    total_bases = len(concatenated_sequence)
    # Compter le nombre de chaque base (A, C, G, U)
    base_counts = {
        "A": concatenated_sequence.count("A"),
        "C": concatenated_sequence.count("C"),
        "G": concatenated_sequence.count("G"),
        "U": concatenated_sequence.count("U")
    }

    # Calculer les pourcentages de chaque base
    base_percentages = {base: (count / total_bases) * 100 for base, count in base_counts.items()}

    # Dessiner un graphique en secteurs
    plt.figure(figsize=(6, 6))
    plt.pie(
        base_percentages.values(),
        labels=base_percentages.keys(),
        autopct='%1.1f%%',
        startangle=140
    )

    # Ajouter un titre au graphique
    plt.title("Mean Base Composition for All Species")
    # Sauvegarder le graphique en tant qu'image
    plt.savefig("mean_base_composition.png")
    # Fermer la figure pour libérer de la mémoire
    plt.close()
    # Afficher un message indiquant où le graphique a été sauvegardé
    print("Mean base composition chart saved as mean_base_composition.png")