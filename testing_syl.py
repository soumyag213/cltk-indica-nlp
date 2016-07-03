from indic_syll import Syllabifier as SylIndic
import unittest


class testing_syl_indic(unittest.TestCase):
    def test_syllabify(self):
        correct = ['न', 'म', 'स्ते']
        sylclass = SylIndic('hindi')
        syl1 = sylclass.orthographic_syllabify('नमस्ते')
        self.assertEqual(syl1, correct)

#   sylclass = SylIndic('punjabi')
#   sylclass.orthographic_syllabify('ਹੈਲੋ')


if __name__ == '__main__':
    unittest.main()