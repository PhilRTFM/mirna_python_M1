from functions import *

def main():
    # Input and output file paths
    mirna_file = "input/mirna.txt"  # Replace with the path to your mirna.txt file
    output_folder = "output_charts"  # Replace with your desired output folder

    # Step 1: Process data to extract species and sequences
    species_sequences = process_data(mirna_file)
    print(f"Extracted sequences for {len(species_sequences)} species.")

    # Step 2: Calculate base rates and draw pie charts
    calculate_base_rates_and_draw_charts(species_sequences, output_folder)

    # Step 3: Calculate mean base rates and draw the overall chart
    calculate_mean_base_rates_and_draw_overall_chart(species_sequences, output_folder)


if __name__ == "__main__":
    main()
