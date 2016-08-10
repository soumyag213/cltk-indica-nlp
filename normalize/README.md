
# API Usage
This is used to mornalize the text i.e. if in a language another character is used to substitute for a unicode character. That subtitution is normalized. For eg.: the pipe operator (|) can be used to signify a 'deergha virama', with this function we can substitute it with its actual unicode character which is (। or \u0964)

```python
if __name__ == '__main__': 

  factory=IndicNormalizerFactory()
    
    language='hindi'
    remove_nuktas=False
    
    # create normalizer
    normalizer=factory.get_normalizer(language,remove_nuktas)

    input_string = "अलसस्य कुतो विद्या, अविद्यस्य:कुतो धनम् | अधनस्य कुतो मित्रम्, अमित्रस्य कुतःसुखम् ||"
    print (input_string)
    print (normalizer.normalize(input_string))

```


```python
अलसस्य कुतो विद्या, अविद्यस्य:कुतो धनम् | अधनस्य कुतो मित्रम्, अमित्रस्य कुतःसुखम् ||
अलसस्य कुतो विद्या, अविद्यस्यःकुतो धनम् । अधनस्य कुतो मित्रम्, अमित्रस्य कुतःसुखम् ।।
```
