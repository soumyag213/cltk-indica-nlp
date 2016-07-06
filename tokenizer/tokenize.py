import string, re, sys, codecs

triv_tokenizer_pat=re.compile('(['+string.punctuation+'\u0964\u0965'+'])')

def trivial_tokenize(s):
    """
    A trivial tokenizer which just tokenizes on the punctuation boundaries. This also includes punctuations for the Indian language scripts
      - the purna virama and the deergha virama
    returns a list of tokens
    """
    tok_str=triv_tokenizer_pat.sub(r' \1 ',s.replace('\t',' '))
    return re.sub(r'[ ]+',u' ',tok_str).strip(' ').split(' ')


if __name__ == '__main__':

    triv1 = trivial_tokenize("The quick brown fox jumps over the lazy dog")
    print (triv1)

    triv2 = trivial_tokenize("प्रेमचन्द का जन्म ३१ जुलाई सन् १८८० को बनारस शहर से चार मील दूर लमही गाँव में हुआ था।")
    print (triv2)
