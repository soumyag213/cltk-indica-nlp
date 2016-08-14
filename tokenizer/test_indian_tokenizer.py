from tokenizer import indian_tokenizer
import unittest

class testing_tokenizer_indic(unittest.TestCase):

    def test_punctuation_tokenize(self):
        input_str = "The quick brown fox jumps over the lazy dog"
        current = indian_tokenizer.indian_punctuation_tokenize_regex(input_str)
        correct = ['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']
        self.assertEqual(current,correct)



if __name__ == '__main__':
    unittest.main()