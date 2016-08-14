from morph import indic_morph
import unittest

INDIC_RESOURCES_PATH = '/home/soumya/cltk_data'


class testing_indic_morph(unittest.TestCase):
    def test_morph_analyze(self):
        input_str = "प्रेमचन्द"
        current = indic_morph.UnsupervisedMorphAnalyzer.morph_analyze(self,input_str, 'hi')
        correct = ['प्रेम', 'चन्द']
        self.assertEqual(current,correct)

    def test_morph_analyze_documents(self):
        input_str = "प्रेमचन्द का जन्म ३१ जुलाई सन् १८८० को बनारस शहर।"
        current = indic_morph.UnsupervisedMorphAnalyzer.morph_analyze_document(self, input_str, 'hi')
        correct = ['प्रेम', 'चन्द', 'का', 'जन्म', '३१', 'जुलाई', 'सन्', '१८८०', 'को', 'बनारस', 'शहर', '।']
        self.assertEqual(current, correct)


if __name__  == '__main__':
    unittest.main()