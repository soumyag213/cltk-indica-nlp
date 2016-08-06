
# CommandLine Usage
This is used to mornalize the text i.e. if in a language another character is used to substitute for a unicode character. That subtitution is normalized. For eg.: the pipe operator (|) can be used to signify a 'deergha virama', with this function we can substitute it with its actual unicode character which is (। or \u0964)
The commandline usage is as follows:

```python
python3 normalize.py <input file> <output file> <language code> <[<replace_nukta(True,False>]>
```
