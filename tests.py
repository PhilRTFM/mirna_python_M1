import unittest
from functions import is_nucleotide_sequence, is_valid_species_name, process_data, calculate_base_rates_and_draw_charts, mean_overall_chart
import os
import tempfile

class TestFunctions(unittest.TestCase):

    def test_is_nucleotide_sequence(self):
        self.assertTrue(is_nucleotide_sequence("AUGCUACG"))
        self.assertFalse(is_nucleotide_sequence("AUGXTACG"))
        self.assertFalse(is_nucleotide_sequence("augcuacg"))
        self.assertFalse(is_nucleotide_sequence("12345"))

    def test_is_valid_species_name(self):
        self.assertTrue(is_valid_species_name("Homo"))
        self.assertTrue(is_valid_species_name("Mus"))
        self.assertFalse(is_valid_species_name("homo"))
        self.assertFalse(is_valid_species_name("HOMO"))

    def test_process_data(self):
        with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
            temp_file.write(
                """64685 MI0000001 cel-let-7 cel-let-7L Caenorhabditis elegans let-7 stem-loop UACACUGUGGAUCCGGUGAGGUAGUAGGUUGUAUAGUUUGGAAUAUUACCACCGGUGAACUAUGCAAUUUUCUACCUUACCGGAGACAGAACUCUUCGA\n"""
            )
            temp_file_path = temp_file.name

        species_of_interest = {"Caenorhabditis elegans"}
        result = process_data(temp_file_path, species_of_interest)
        os.unlink(temp_file_path)

        expected_species = "Caenorhabditis elegans"
        self.assertIn(expected_species, result)
        self.assertIn("UACACUGUGGAUCCGGUGAGGUAGUAGGUUGUAUAGUUUGGAAUAUUACCACCGGUGAACUAUGCAAUUUUCUACCUUACCGGAGACAGAACUCUUCGA", result[expected_species])

    def test_calculate_base_rates_and_draw_charts(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            species_sequences = {
                "Caenorhabditis elegans": ["AUGCUACG", "CUGAAC"]
            }
            calculate_base_rates_and_draw_charts(species_sequences, temp_dir)

            output_file = os.path.join(temp_dir, "Caenorhabditis_elegans_base_composition.png")
            self.assertTrue(os.path.exists(output_file))

    def test_mean_overall_chart(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            species_sequences = {
                "Caenorhabditis elegans": ["AUGCUACG", "CUGAAC"],
                "Homo sapiens": ["UUUCCGG", "AACGUU"]
            }
            current_dir = os.getcwd()  # Sauvegarde du répertoire courant
            try:
                os.chdir(temp_dir)  # Change temporairement de répertoire
                mean_overall_chart(species_sequences)

                output_file = os.path.join(temp_dir, "overall_base_composition.png")
                self.assertTrue(os.path.exists(output_file))
            finally:
                os.chdir(current_dir)  # Restauration du répertoire courant


if __name__ == '__main__':
    unittest.main()