def extract_species_from_nucleotide_data(mirna_file, output_file):
    def is_nucleotide_sequence(word):
        """Check if a word is a valid nucleotide sequence."""
        return all(c in "ACGU" for c in word) and word.isupper()

    with open(mirna_file, 'r') as f:
        with open(output_file, 'w') as out_f:
            seen_species = set()  # Set to track unique species names
            for line in f:
                parts = line.split()  # Split the line into words
                # Find the index of the first valid nucleotide sequence
                nucleotide_sequence_index = next(
                    (i for i, word in enumerate(parts) if is_nucleotide_sequence(word)),
                    None
                )
                
                if nucleotide_sequence_index:
                    if nucleotide_sequence_index == 8:  # 6 words before the sequence
                        species_name = f"{parts[4]} {parts[5]}"
                    elif nucleotide_sequence_index == 9:  # 7 words before the sequence
                        species_name = f"{parts[3]} {parts[4]}"
                    else:
                        # Skip malformed lines
                        continue

                    if species_name not in seen_species:
                        out_f.write(species_name + '\n')  # Write the species name
                        seen_species.add(species_name)  # Add to the set

    print(f"Extraction completed. Species have been written to: {output_file}")

# File paths
    mirna_file = input("Enter the path to the mirna.txt file: ").strip()
    output_file = input("Desired output name for species.txt file: ").strip()

# Run the function
extract_species_from_nucleotide_data(mirna_file, output_file)