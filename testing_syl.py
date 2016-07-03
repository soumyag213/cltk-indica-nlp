from indic_syll import Syllabifier as SylIndic
import unittest


class testing_syl_indic(unittest.TestCase):
    def language_test(lang, word):
        sylclass = SylIndic(lang)
        syl1 = sylclass.orthographic_syllabify(word)
        print (syl1)

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

#    sylclass = SylIndic('punjabi')
#   sylclass.orthographic_syllabify('ਹੈਲੋ')

    if __name__ == '__main__':
        language_test('hindi','नमस्ते')
        language_test('punjabi', 'ਹੈਲੋ')

if __name__ == '__main__':
    unittest.main()