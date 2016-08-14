
#  API Usage
This function can be used to break down into morphemes all the words present in the input text, it works by using a third library called morfessor (which will have to be specifically downloaded to run this feature). Input is: 

```python
if __name__ == '__main__': 

    language='hindi'
    INDIC_RESOURCES_PATH= '/home/soumya/cltk_data'
    add_marker=False
    input_string = "प्रेमचन्द का जन्म ३१ जुलाई सन् १८८० को बनारस शहर।"

    language = LANGUAGE_NAME_TO_CODE[language]
    analyzer = UnsupervisedMorphAnalyzer(add_marker)

    morph_word = analyzer.morph_analyze("प्रेमचन्द", language)
    print (morph_word)

    morph_tokens = analyzer.morph_analyze_document(input_string, language)
    print(morph_tokens)

```
Output: 

```python
/usr/bin/python3.4 /home/soumya/indic_cltkk/morph/indic_morph.py
['प्रेम', 'चन्द']
['प्रेम', 'चन्द', 'का', 'जन्म', '३१', 'जुलाई', 'सन्', '१८८०', 'को', 'बनारस', 'शहर', '।']

Process finished with exit code 0

```
But on upon running the test_indic_morph.py, the testcases for the morph function, it returns the following error: 

```python
EE
======================================================================
ERROR: test_morph_analyze (__main__.testing_indic_morph)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/soumya/indic_cltkk/morph/test_indian_morph.py", line 10, in test_morph_analyze
    current = indic_morph.UnsupervisedMorphAnalyzer.morph_analyze(self,input_str, 'hi')
  File "/home/soumya/indic_cltkk/morph/indic_morph.py", line 97, in morph_analyze
    val=UnsupervisedMorphAnalyzer._morfessor_model(self, word, lang)
  File "/home/soumya/indic_cltkk/morph/indic_morph.py", line 71, in _morfessor_model
    morfessor_model=io.read_any_model(INDIC_RESOURCES_PATH+'/morph/morfessor/{}.model'.format(lang))
  File "/usr/local/lib/python3.4/dist-packages/Morfessor-2.0.1-py3.4.egg/morfessor/io.py", line 203, in read_any_model
    model.load_segmentations(self.read_segmentation_file(file_name))
  File "/usr/local/lib/python3.4/dist-packages/Morfessor-2.0.1-py3.4.egg/morfessor/baseline.py", line 487, in load_segmentations
    for count, segmentation in segmentations:
  File "/usr/local/lib/python3.4/dist-packages/Morfessor-2.0.1-py3.4.egg/morfessor/io.py", line 53, in read_segmentation_file
    for line in self._read_text_file(file_name):
  File "/usr/local/lib/python3.4/dist-packages/Morfessor-2.0.1-py3.4.egg/morfessor/io.py", line 240, in _read_text_file
    encoding = self._find_encoding(file_name)
  File "/usr/local/lib/python3.4/dist-packages/Morfessor-2.0.1-py3.4.egg/morfessor/io.py", line 309, in _find_encoding
    file_obj = open(f, 'rb')
FileNotFoundError: [Errno 2] No such file or directory: '/morph/morfessor/hi.model'

======================================================================
ERROR: test_morph_analyze_documents (__main__.testing_indic_morph)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/home/soumya/indic_cltkk/morph/test_indian_morph.py", line 16, in test_morph_analyze_documents
    current = indic_morph.UnsupervisedMorphAnalyzer.morph_analyze_document(self, input_str, 'hi')
  File "/home/soumya/indic_cltkk/morph/indic_morph.py", line 127, in morph_analyze_document
    morphs=UnsupervisedMorphAnalyzer.morph_analyze(self,token, lang)
  File "/home/soumya/indic_cltkk/morph/indic_morph.py", line 97, in morph_analyze
    val=UnsupervisedMorphAnalyzer._morfessor_model(self, word, lang)
  File "/home/soumya/indic_cltkk/morph/indic_morph.py", line 71, in _morfessor_model
    morfessor_model=io.read_any_model(INDIC_RESOURCES_PATH+'/morph/morfessor/{}.model'.format(lang))
  File "/usr/local/lib/python3.4/dist-packages/Morfessor-2.0.1-py3.4.egg/morfessor/io.py", line 203, in read_any_model
    model.load_segmentations(self.read_segmentation_file(file_name))
  File "/usr/local/lib/python3.4/dist-packages/Morfessor-2.0.1-py3.4.egg/morfessor/baseline.py", line 487, in load_segmentations
    for count, segmentation in segmentations:
  File "/usr/local/lib/python3.4/dist-packages/Morfessor-2.0.1-py3.4.egg/morfessor/io.py", line 53, in read_segmentation_file
    for line in self._read_text_file(file_name):
  File "/usr/local/lib/python3.4/dist-packages/Morfessor-2.0.1-py3.4.egg/morfessor/io.py", line 240, in _read_text_file
    encoding = self._find_encoding(file_name)
  File "/usr/local/lib/python3.4/dist-packages/Morfessor-2.0.1-py3.4.egg/morfessor/io.py", line 309, in _find_encoding
    file_obj = open(f, 'rb')
FileNotFoundError: [Errno 2] No such file or directory: '/morph/morfessor/hi.model'

----------------------------------------------------------------------
Ran 2 tests in 0.033s

FAILED (errors=2)
```
