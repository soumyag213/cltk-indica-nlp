
# API usage for syllabifier (Indic NLP)
First set these resources on your machine

```python
INDIC_NLP_LIB_HOME="/home/soumya/indic_syllabifier"
INDIC_NLP_RESOURCES="/home/soumya/Documents/indic_nlp3/indic_nlp_resources-master"

```
This sets the path of the syllabifier

```python
import sys
sys.path.append('{}/src'.format(INDIC_NLP_LIB_HOME))

from indic_syl import indic_syll
indic_syll.set_resources_path(INDIC_NLP_RESOURCES)

```
Initialize the Indic NLP Library, by loading it

```python
indic_syll.load()
```
Now, to call the syllabifying function itself 

```python
indic_syll.orthographic_syllabify('नमस्ते','hi')

```


```python
/usr/bin/python3.4 /home/soumya/upython/sylapi.py
['न', 'म', 'स्ते']

Process finished with exit code 0
```
