import matplotlib.pyplot as plt
from collections import defaultdict
import os

def is_nucleotide_sequence(word):
    """Check if a word is a valid nucleotide sequence."""
    return all(c in "ACGU" for c in word) and word.isupper()

def is_valid_species_name(word):
    """Check if a word starts with a single uppercase letter followed by lowercase letters."""
    return word[0].isupper() and word[1:].islower()

def process_data(mirna_file, species_of_interest):
    """
    Process the data from the file to extract species and their nucleotide sequences,
    filtered by the species of interest.
    """
    species_sequences = defaultdict(list)

    with open(mirna_file, 'r') as f:
        for line in f:
            parts = line.split()
            species_name_index = next(
                (i for i, word in enumerate(parts) if is_valid_species_name(word)),
                None
            )

            if species_name_index is not None and species_name_index + 1 < len(parts):
                species_name = f"{parts[species_name_index]} {parts[species_name_index + 1]}"

                if species_name in species_of_interest:
                    sequences = [word for word in parts if is_nucleotide_sequence(word)]
                    species_sequences[species_name].extend(sequences)
    return species_sequences

def calculate_base_rates_and_draw_charts(species_sequences, output_folder):
    """
    Calculate base rates and draw pie charts for each species.
    """
    os.makedirs(output_folder, exist_ok=True)

    for species, sequences in species_sequences.items():
        concatenated_sequence = "".join(sequences)
        total_bases = len(concatenated_sequence)
        base_counts = {
            "A": concatenated_sequence.count("A"),
            "C": concatenated_sequence.count("C"),
            "G": concatenated_sequence.count("G"),
            "U": concatenated_sequence.count("U")
        }

        # Calculate percentages
        base_percentages = {base: (count / total_bases) * 100 for base, count in base_counts.items()}

        # Draw pie chart
        plt.figure(figsize=(6, 6))
        plt.pie(
            base_percentages.values(),
            labels=base_percentages.keys(),
            autopct='%1.1f%%',
            startangle=140
        )

        plt.title(f"Base Composition for {species}")
        output_file = os.path.join(output_folder, f"{species.replace(' ', '_')}_base_composition.png")
        plt.savefig(output_file)
        plt.close()
    print(f"Pie charts saved in: {output_folder}")

def mean_overall_chart(species_sequences):
    """
    Calculate mean base rates across all species and draw a single overall pie chart.
    """
    total_bases_across_species = {"A": 0, "C": 0, "G": 0, "U": 0}
    total_sequences_length = 0

    # Aggregate base counts
    for sequences in species_sequences.values():
        concatenated_sequence = "".join(sequences)
        total_bases = len(concatenated_sequence)
        total_sequences_length += total_bases
        total_bases_across_species["A"] += concatenated_sequence.count("A")
        total_bases_across_species["C"] += concatenated_sequence.count("C")
        total_bases_across_species["G"] += concatenated_sequence.count("G")
        total_bases_across_species["U"] += concatenated_sequence.count("U")

    # Calculate mean proportions
    mean_base_percentages = {
        base: (count / total_sequences_length) * 100
        for base, count in total_bases_across_species.items()
    }

    # Draw the overall pie chart
    plt.figure(figsize=(8, 8))
    plt.pie(
        mean_base_percentages.values(),
        labels=mean_base_percentages.keys(),
        autopct='%1.1f%%',
        startangle=140
    )
    plt.title("Mean Base Composition Across All Species")
    overall_chart_file = os.path.join("overall_base_composition.png")
    plt.savefig(overall_chart_file)
    plt.close()

    print(f"Overall pie chart saved at: {overall_chart_file}")