def extract_species_from_nucleotide_data(mirna_file, output_file):
    def is_nucleotide_sequence(word):
        """Vérifie si un mot est une séquence de nucléotides valide."""
        return all(c in "ACGU" for c in word) and word.isupper()

    # Ouvrir le fichier mirna.txt en mode lecture
    with open(mirna_file, 'r') as f:
        # Ouvrir le fichier de sortie en mode écriture
        with open(output_file, 'w') as out_f:
            seen_species = set()  # Ensemble pour suivre les noms d'espèces uniques
            for line in f:
                parts = line.split()  # Diviser la ligne en mots
                # Trouver l'index de la première séquence de nucléotides valide
                nucleotide_sequence_index = next(
                    (i for i, word in enumerate(parts) if is_nucleotide_sequence(word)),
                    None
                )
                
                if nucleotide_sequence_index:
                    if nucleotide_sequence_index == 8:  # 6 mots avant la séquence
                        species_name = f"{parts[4]} {parts[5]}"
                    elif nucleotide_sequence_index == 9:  # 7 mots avant la séquence
                        species_name = f"{parts[3]} {parts[4]}"
                    else:
                        # Ignorer les lignes mal formées
                        continue

                    if species_name not in seen_species:
                        out_f.write(species_name + '\n')  # Écrire le nom de l'espèce
                        seen_species.add(species_name)  # Ajouter à l'ensemble

    print(f"Extraction terminée. Les espèces ont été écrites dans : {output_file}")

# Lien des fichiers d'entrée et de sortie
    mirna_file = input("Enter the path to the mirna.txt file: ").strip()
    output_file = input("Desired output name for species.txt file: ").strip()

# Appeler la fonction
extract_species_from_nucleotide_data(mirna_file, output_file)