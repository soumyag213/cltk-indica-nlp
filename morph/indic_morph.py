
import codecs, sys, string,re
import morfessor

SCRIPT_RANGES = {
    'pa': [0x0a00, 0x0a7f],
    'gu': [0x0a80, 0x0aff],
    'or': [0x0b00, 0x0b7f],
    'ta': [0x0b80, 0x0bff],
    'te': [0x0c00, 0x0c7f],
    'kn': [0x0c80, 0x0cff],
    'ml': [0x0d00, 0x0d7f],
    'si': [0x0d80, 0x0dff],
    'hi': [0x0900, 0x097f],
    'mr': [0x0900, 0x097f],
    'kK': [0x0900, 0x097f],
    'sa': [0x0900, 0x097f],
    'ne': [0x0900, 0x097f],
    'sd': [0x0900, 0x097f],
    'bn': [0x0980, 0x09ff],
    'as': [0x0980, 0x09ff],
}

NUMERIC_OFFSET_START=0x66
NUMERIC_OFFSET_END=0x6f

INDIC_RESOURCES_PATH=''

indian_punctuation_pattern = re.compile('(['+string.punctuation+'\u0964\u0965'+'])')

def indian_punctuation_tokenize_regex(input_str):
    tok_str = indian_punctuation_pattern.sub(r' \1 ',input_str.replace('\t',' '))
    return re.sub(r'[ ]+',u' ',tok_str).strip(' ').split(' ')


def common_init():
    """
    Initialize the module. The following actions are performed:

    - Checks of INDIC_RESOURCES_PATH variable is set. If not, checks if it can beb initialized from
        INDIC_RESOURCES_PATH environment variable. If that fails, an exception is raised
    """
    global INDIC_RESOURCES_PATH
    try:
        if INDIC_RESOURCES_PATH=='':
            INDIC_RESOURCES_PATH=os.environ['INDIC_RESOURCES_PATH']
    except Exception as e:
        raise IndicNlpException('Indic Resources Path not set')

    if INDIC_RESOURCES_PATH=='':
        raise IndicNlpException('Indic Resources Path not set')

class MorphAnalyzerI(object):
    """
     Interface for Morph Analyzer
    """

    def morph_analyze(word):
        pass 

    def morph_analyze_document(tokens):
        pass 

class UnsupervisedMorphAnalyzer(MorphAnalyzerI): 
    """
    Unsupervised Morphological analyser built using Morfessor 2.0
    """

    def __init__(self,lang,add_marker=False): 
        self.lang=lang
        self.add_marker=add_marker

        io = morfessor.MorfessorIO()
        self._morfessor_model=io.read_any_model(INDIC_RESOURCES_PATH+'/morph/morfessor/{}.model'.format(lang))

        self._script_range_pat='^[{}-{}]+$'.format(chr(SCRIPT_RANGES[lang][0]),chr(SCRIPT_RANGES[lang][1]))
        self._script_check_re=re.compile(self._script_range_pat)

    def _contains_number(self,text):
        if self.lang in SCRIPT_RANGES:
            for c in text: 
                offset=ord(c)-SCRIPT_RANGES[self.lang][0]
                if offset >=NUMERIC_OFFSET_START and offset <=NUMERIC_OFFSET_END:
                    return True  
        return False     

    def _morphanalysis_needed(self,word):
        return self._script_check_re.match(word) and not self._contains_number(word)

    def morph_analyze(self,word):
        """
        Morphanalyzes a single word and returns a list of component morphemes

        @param word: string input word 
        """
        m_list=[]
        if self._morphanalysis_needed(word): 
            val=self._morfessor_model.viterbi_segment(word)
            m_list=val[0]
            if self.add_marker:
                m_list= [ u'{}_S_'.format(m) if i>0 else u'{}_R_'.format(m)  for i,m in enumerate(m_list)]
        else:
            if self.add_marker:
                word=u'{}_E_'.format(word)
            m_list=[word]
        return m_list 

        ### Older implementation
        #val=self._morfessor_model.viterbi_segment(word)
        #m_list=val[0]
        #if self.add_marker:
        #    m_list= [ u'{}_S_'.format(m) if i>0 else u'{}_R_'.format(m)  for i,m in enumerate(m_list)]
        #return m_list
    

    def morph_analyze_document(self,tokens):
        """
        Morphanalyzes a document, represented as a list of tokens
        Each word  is morphanalyzed and result is a list of morphemes constituting the document 

        @param tokens: string sequence of words 

        @return seuqence of morphemes 
        """

        out_tokens=[]
        for token in tokens: 
            morphs=self.morph_analyze(token)
            out_tokens.extend(morphs)
        return out_tokens    

        #### Older implementation
        #out_tokens=[]
        #for token in tokens: 
        #    if self._morphanalysis_needed(token): 
        #        morphs=self.morph_analyze(token)
        #        out_tokens.extend(morphs)
        #    else:
        #        if self.add_marker:
        #            token=u'{}_E_'.format(token)
        #        out_tokens.append(token)
        #return out_tokens    


if __name__ == '__main__': 

    if len(sys.argv)<4:
        print ("Usage: python3 unsupervised_morph.py <infile> <outfile> <language> <indic_resources_path> [<add_marker>]")
        sys.exit(1)

    language=sys.argv[3]
    INDIC_RESOURCES_PATH='/home/soumya/cltk_data'


    add_marker=False

    if len(sys.argv)==6:
        add_marker= True if sys.argv[5] == 'True' else False

    analyzer=UnsupervisedMorphAnalyzer(language,add_marker)

    with codecs.open(sys.argv[1],'r','utf-8') as ifile:
        with codecs.open(sys.argv[2],'w','utf-8') as ofile:
            for line in ifile.readlines():
                line=line.strip()
                tokens=indian_punctuation_tokenize_regex(line)
                morph_tokens=analyzer.morph_analyze_document(tokens)
                ofile.write(' '.join(morph_tokens))
                ofile.write('\n')


