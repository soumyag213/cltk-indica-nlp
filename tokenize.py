import string, re, sys, codecs

triv_tokenizer_pat=re.compile(ur'(['+string.punctuation+ur'\u0964\u0965'+ur'])')

def trivial_tokenize(s):
    """
    A trivial tokenizer which just tokenizes on the punctuation boundaries. This also includes punctuations for the Indian language scripts
      - the purna virama and the deergha virama
    returns a list of tokens
    """
    tok_str=triv_tokenizer_pat.sub(r' \1 ',s.replace('\t',' '))
    return re.sub(r'[ ]+',u' ',tok_str).strip(' ').split(' ')


if __name__ == '__main__':

    if len(sys.argv)<4:
        print "Usage: python indic_tokenize.py <infile> <outfile> <language>"
        sys.exit(1)

    with codecs.open(sys.argv[1],'r','utf-8') as ifile:
        with codecs.open(sys.argv[2],'w','utf-8') as ofile:
            for line in ifile.readlines():
                tokenized_line=string.join(trivial_tokenize(line),sep=' ')
                ofile.write(tokenized_line)
