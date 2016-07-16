from indic_syll import Syllabifier as SylIndic
import unittest


class testing_syl_indic(unittest.TestCase):
    def test_syllabify(self):
        '''Test Indic Syllabifier method'''
        correct = ['न', 'म', 'स्ते']
        Sylclass = SylIndic('hindi')
        current = Sylclass.orthographic_syllabify('नमस्ते')
        self.assertEqual(current, correct)

    def test_get_offset(self):
        '''Test Indic Syllabifier get_offset method'''
        correct = 40
        Sylclass = SylIndic('hindi')
        current = Sylclass.get_offset('न', 'hi')
        self.assertEqual(current, correct)

    def test_coordinated_range(self):
        '''Test Indic Syllabifier in_coordinated_range method'''
        Sylclass = SylIndic('hindi')
        current = Sylclass.get_offset('न', 'hi')
        current1 = Sylclass.in_coordinated_range_offset(current)
        self.assertTrue(current1)

        ''' def test_phonetic_vector(self):
        cor = [0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,0,1,1,0,1,0,0,0,0,0,0,0,0,0,0]
        correct = bytearray(cor)
        Sylclass = SylIndic('hindi')
        current = Sylclass.get_phonetic_feature_vector('न', 'hi')
        self.assertTrue(current, correct)
        '''

    def test_is_misc(self):
        '''Test Indic Syllabifier is_misc method'''
        Sylclass = SylIndic('hindi')
        v = Sylclass.get_phonetic_feature_vector('न', 'hi')
        self.assertFalse(Sylclass.is_misc(v))

    def test_is_consonant(self):
        '''Test Indic Syllabifier is_consonant method'''
        Sylclass = SylIndic('hindi')
        v = Sylclass.get_phonetic_feature_vector('न', 'hi')
        self.assertTrue(Sylclass.is_consonant(v))

    def test_is_vowel(self):
        '''Test Indic Syllabifier is_vowel method'''
        Sylclass = SylIndic('hindi')
        v = Sylclass.get_phonetic_feature_vector('न', 'hi')
        self.assertFalse(Sylclass.is_vowel(v))

    def test_is_anusvaar(self):
        '''Test Indic Syllabifier is_anusvaar method'''
        Sylclass = SylIndic('hindi')
        v = Sylclass.get_phonetic_feature_vector('न', 'hi')
        self.assertFalse(Sylclass.is_anusvaar(v))

    def test_is_plosive(self):
        '''Test Indic Syllabifier is_plosive method'''
        Sylclass = SylIndic('hindi')
        v = Sylclass.get_phonetic_feature_vector('न', 'hi')
        self.assertTrue(Sylclass.is_plosive(v))

    def test_is_nukta(self):
        '''Test Indic Syllabifier is_nukta method'''
        Sylclass = SylIndic('hindi')
        v = Sylclass.get_phonetic_feature_vector('न', 'hi')
        self.assertFalse(Sylclass.is_nukta(v))

    def test_is_valid(self):
        '''Test Indic Syllabifier is_valid method'''
        Sylclass = SylIndic('hindi')
        v = Sylclass.get_phonetic_feature_vector('न', 'hi')
        self.assertTrue(Sylclass.is_valid(v))

    def test_is_dependent_vowel(self):
        '''Test Indic Syllabifier is_dependent_vowel method'''
        Sylclass = SylIndic('hindi')
        v = Sylclass.get_phonetic_feature_vector('न', 'hi')
        self.assertFalse(Sylclass.is_dependent_vowel(v))


if __name__ == '__main__':
    unittest.main()