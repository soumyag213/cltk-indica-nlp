from indic_syll import Syllabifier
import unittest


class testing_syl_indic(unittest.TestCase):
    def test_syllabify(self):
        """Test Indic Syllabifier method"""
        correct = ['न', 'म', 'स्ते']
        syllabizer = Syllabifier('hindi')
        current = syllabizer.orthographic_syllabify('नमस्ते')
        self.assertEqual(current, correct)

    def test_get_offset(self):
        """Test Indic Syllabifier get_offset method"""
        correct = 40
        syllabizer = Syllabifier('hindi')
        current = syllabizer.get_offset('न', 'hi')
        self.assertEqual(current, correct)

    def test_coordinated_range(self):
        """Test Indic Syllabifier in_coordinated_range method"""
        syllabizer = Syllabifier('hindi')
        current = syllabizer.get_offset('न', 'hi')
        current1 = syllabizer.in_coordinated_range_offset(current)
        self.assertTrue(current1)

    """
    def test_phonetic_vector(self):
        cor = [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0]
        correct = bytearray(cor)
        syllabizer = Syllabifier('hindi')
        current = syllabizer.get_phonetic_feature_vector('न', 'hi')
        self.assertTrue(current, correct)
    """

    def test_is_misc(self):
        """Test Indic Syllabifier is_misc method"""
        syllabizer = Syllabifier('hindi')
        v = syllabizer.get_phonetic_feature_vector('न', 'hi')
        self.assertFalse(syllabizer.is_misc(v))

    def test_is_consonant(self):
        """Test Indic Syllabifier is_consonant method"""
        syllabizer = Syllabifier('hindi')
        v = syllabizer.get_phonetic_feature_vector('न', 'hi')
        self.assertTrue(syllabizer.is_consonant(v))

    def test_is_vowel(self):
        """Test Indic Syllabifier is_vowel method"""
        syllabizer = Syllabifier('hindi')
        v = syllabizer.get_phonetic_feature_vector('न', 'hi')
        self.assertFalse(syllabizer.is_vowel(v))

    def test_is_anusvaar(self):
        """Test Indic Syllabifier is_anusvaar method"""
        syllabizer = Syllabifier('hindi')
        v = syllabizer.get_phonetic_feature_vector('न', 'hi')
        self.assertFalse(syllabizer.is_anusvaar(v))

    def test_is_plosive(self):
        """Test Indic Syllabifier is_plosive method"""
        syllabizer = Syllabifier('hindi')
        v = syllabizer.get_phonetic_feature_vector('न', 'hi')
        self.assertTrue(syllabizer.is_plosive(v))

    def test_is_nukta(self):
        """Test Indic Syllabifier is_nukta method"""
        syllabizer = Syllabifier('hindi')
        v = syllabizer.get_phonetic_feature_vector('न', 'hi')
        self.assertFalse(syllabizer.is_nukta(v))

    def test_is_valid(self):
        """Test Indic Syllabifier is_valid method"""
        syllabizer = Syllabifier('hindi')
        v = syllabizer.get_phonetic_feature_vector('न', 'hi')
        self.assertTrue(syllabizer.is_valid(v))

    def test_is_dependent_vowel(self):
        """Test Indic Syllabifier is_dependent_vowel method"""
        syllabizer = Syllabifier('hindi')
        v = syllabizer.get_phonetic_feature_vector('न', 'hi')
        self.assertFalse(syllabizer.is_dependent_vowel(v))


if __name__ == '__main__':
    unittest.main()