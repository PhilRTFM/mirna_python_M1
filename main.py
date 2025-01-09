from functions import *

def main():
    mirna_file = input("Enter the path to the mirna.txt file: ").strip()
    species_file = input("Enter the path to the species.txt file: ").strip()
    output_folder = input("Enter the desired output folder: ").strip()

    if not os.path.isfile(mirna_file):
        print(f"Error: {mirna_file} does not exist.")
        return

    if not os.path.isfile(species_file):
        print(f"Error: {species_file} does not exist.")
        return

    with open(species_file, 'r') as f:
        species_of_interest = {line.strip() for line in f if line.strip()}

    species_sequences = process_data(mirna_file, species_of_interest)

    if not species_sequences:
        print("No matching species found in the data.")
        return

    print(f"Extracted sequences for {len(species_sequences)} species of interest.")

    calculate_base_rates_and_draw_charts(species_sequences, output_folder)
    mean_overall_chart(species_sequences)

if __name__ == "__main__":
    main()