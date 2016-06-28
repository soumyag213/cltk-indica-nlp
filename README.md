
# API usage for syllabifier (Indic NLP)
Slight technicality that is needed to be straightened out, I've set the document resources according to the local git repository. Although I've uploaded the same on the github repo (you can find both the sheets under src), I don't how to give it a path. 
A choice is between the two sheets based on the language code chosen. This conditional path is set in the function ```python scriptsinit()``` 


The path for the resources, and the word to be syllabified altogether is defined through a call from the initialization of an object of the class


```python
x = Syllabifier("/home/soumya/Documents/indic_nlp3/indic_nlp_resources-master", 'नमस्ते', 'hi')

```
The output is as follows:

```python
/usr/bin/python3.4 /home/soumya/upython/sylapi.py
['न', 'म', 'स्ते']

Process finished with exit code 0
```
