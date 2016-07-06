
# API usage for tokenizer (Indic NLP)

The tokenizer tokenizes the sentences on the basis of any special characters encountered. It works on all languages. 


```python
if __name__ == '__main__':

    triv1 = trivial_tokenize("The quick brown fox jumps over the lazy dog")
    print (triv1)

    triv2 = trivial_tokenize("प्रेमचन्द का जन्म ३१ जुलाई सन् १८८० को बनारस शहर से चार मील दूर लमही गाँव में हुआ था।")
    print (triv2)

```
The output is as follows:

```python
/usr/bin/python3.4 /home/soumya/indic_cltkk/tokenize.py
['The', 'quick', 'brown', 'fox', 'jumps', 'over', 'the', 'lazy', 'dog']

['प्रेमचन्द', 'का', 'जन्म', '३१', 'जुलाई', 'सन्', '१८८०', 'को', 'बनारस', 'शहर', 'से', 'चार', 'मील', 'दूर', 'लमही', 'गाँव', 'में', 'हुआ', 'था', '।', 'आपके', 'पिता', 'का', 'नाम', 'अजायब', 'राय', 'था', '।']

Process finished with exit code 0
```


