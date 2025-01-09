from functions import *

def main():
    # Input and output file paths
    mirna_file = input("Enter the path to the mirna.txt file: ").strip()
    species_file = input("Enter the path to the species.txt file: ").strip()
    output_folder = input("Enter the desired output folder: ").strip()

    # Check if files exist
    if not os.path.isfile(mirna_file):
        print(f"Error: {mirna_file} does not exist.")
        return
    
    if not os.path.isfile(species_file):
        print(f"Error: {species_file} does not exist.")
        return

    # Step 1: Read species of interest
    with open(species_file, 'r') as f:
        species_of_interest = {line.strip() for line in f if line.strip()}

    # Step 2: Process data to extract species and sequences
    species_sequences = process_data(mirna_file)
    filtered_sequences = {species: seqs for species, seqs in species_sequences.items() if species in species_of_interest}

    print(f"Extracted sequences for {len(filtered_sequences)} species of interest.")

    # Step 3: Calculate base rates and draw pie charts for each species
    calculate_base_rates_and_draw_charts(filtered_sequences, output_folder)

    # Step 4: Calculate mean base rates and draw the overall chart
    calculate_mean_base_rates_and_draw_overall_chart(filtered_sequences, output_folder)

if __name__ == "__main__":
    main()
