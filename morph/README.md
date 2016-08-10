
# API Usage
This function can be used to break down into morphemes all the words present in the input text, it works by using a third library called morfessor (which will have to be specifically downloaded to run this feature).

```python
if __name__ == '__main__': 

    language='hindi'
    INDIC_RESOURCES_PATH= '/home/soumya/cltk_data'
    add_marker=False
    input_string = "प्रेमचन्द का जन्म ३१ जुलाई सन् १८८० को बनारस शहर।"

    language = LANGUAGE_NAME_TO_CODE[language]
    analyzer=UnsupervisedMorphAnalyzer(language,add_marker)
    morph_tokens = analyzer.morph_analyze_document(indian_punctuation_tokenize_regex(input_string))
    print (morph_tokens)

```


```python
['प्रेम', 'चन्द', 'का', 'जन्म', '३१', 'जुलाई', 'सन्', '१८८०', 'को', 'बनारस', 'शहर', '।']
```
