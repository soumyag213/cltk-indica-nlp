"""Every phonetic of every language is given similar positions in the vectors. Therefore transliterations
happen when each offset is calculated relative to the ranges of the languages specified.
Every phonetic has a dedicated phonetic vector which describes all the facets of the character, whether it is
a vowel or a consonant whe ther it has a halanta, etc.
"""

import numpy as np
import pandas as pd

"""Indexes into the phonetic vector"""
PVIDX_BT_VOWEL = 0
PVIDX_BT_CONSONANT = 1
PVIDX_BT_NUKTA = 2
PVIDX_BT_HALANT = 3
PVIDX_BT_ANUSVAAR = 4
PVIDX_BT_MISC = 5
PVIDX_BT_S = PVIDX_BT_VOWEL
PVIDX_BT_E = PVIDX_BT_MISC + 1

PVIDX_VSTAT_DEP = 12

LC_TA = 'ta'

"""The phonetics of every script exist in the ranges of the dictionary mentioned below"""
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

COORDINATED_RANGE_START_INCLUSIVE = 0
COORDINATED_RANGE_END_INCLUSIVE = 0x6f

PV_PROP_RANGES = dict(basic_type=[0, 6], vowel_length=[6, 8], vowel_strength=[8, 11], vowel_status=[11, 13],
                      consonant_type=[13, 18], articulation_place=[18, 23], aspiration=[23, 25], voicing=[25, 27],
                      nasalization=[27, 29], vowel_horizontal=[29, 32], vowel_vertical=[32, 36],
                      vowel_roundness=[36, 38])

PHONETIC_VECTOR_START_OFFSET = 6


class Syllabifier:
    def __init__(self, resources_path, word, lang):
        """
            Initializes the Indic NLP library. Clients should call this method before using the library.

            Any module requiring initialization should have a init() method,
            to which a call must be made from this method
        """

        self.commoninit(resources_path)
        self.scriptsinit()
        self.orthographic_syllabify(word, lang)

    def scriptsinit(self):
        """Define and call data for future use
            Initializes and defines all variables which define the phonetic vector
        """
        global ALL_PHONETIC_DATA, ALL_PHONETIC_VECTORS, TAMIL_PHONETIC_DATA, TAMIL_PHONETIC_VECTORS, PHONETIC_VECTOR_LENGTH, PHONETIC_VECTOR_START_OFFSET

        ALL_PHONETIC_DATA = pd.read_csv(self.get_resources_path() + '/script/all_script_phonetic_data.csv', encoding='utf-8')
        TAMIL_PHONETIC_DATA = pd.read_csv(self.get_resources_path() + '/script/tamil_script_phonetic_data.csv',
                                          encoding='utf-8')

        ALL_PHONETIC_VECTORS = ALL_PHONETIC_DATA.ix[:, PHONETIC_VECTOR_START_OFFSET:].as_matrix()
        TAMIL_PHONETIC_VECTORS = TAMIL_PHONETIC_DATA.ix[:, PHONETIC_VECTOR_START_OFFSET:].as_matrix()

        PHONETIC_VECTOR_LENGTH = ALL_PHONETIC_VECTORS.shape[1]


    def commoninit(self, resources_path):
        """
        Initialize the module. The following actions are performed:

        - Checks if INDIC_RESOURCES_PATH variable is set. If not, checks if it can be initialized from
            INDIC_RESOURCES_PATH environment variable. If that fails, an exception is raised
        """
        global INDIC_RESOURCES_PATH
        self.set_resources_path(resources_path)
        try:
            if INDIC_RESOURCES_PATH == '':
                INDIC_RESOURCES_PATH = os.environ['INDIC_RESOURCES_PATH']
        except Exception as e:
            raise IndicNlpException('Indic Resources Path not set')

        if INDIC_RESOURCES_PATH == '':
            raise IndicNlpException('Indic Resources Path not set')

    @staticmethod
    def set_resources_path(resources_path):
        """
            Set the path to the Indic NLP Resources directory
        """
        global INDIC_RESOURCES_PATH
        INDIC_RESOURCES_PATH = resources_path

    @staticmethod
    def get_resources_path():
        """ Get the path to the Indic NLP Resources directory"""

        return INDIC_RESOURCES_PATH

    class IndicNlpException(Exception):
        def __init__(self, msg):
            self.msg = msg

        def __str__(self):
            return repr(self.msg)

    @staticmethod
    def in_coordinated_range_offset(c_offset):
        """Applicable to Brahmi derived Indic scripts"""
        return COORDINATED_RANGE_START_INCLUSIVE <= c_offset <= COORDINATED_RANGE_END_INCLUSIVE

    @staticmethod
    def is_supported_language(lang):
        return lang in SCRIPT_RANGES.keys()

    @staticmethod
    def invalid_vector():
        return np.array([0] * PHONETIC_VECTOR_LENGTH)


    def get_offset(self, c, lang):
        if not self.is_supported_language(lang):
            raise IndicNlpException('Language {}  not supported'.format(lang))
        # print ord(c)
        # print li.SCRIPT_RANGES[lang][0]
        return ord(c) - SCRIPT_RANGES[lang][0]


    def get_phonetic_info(self, lang):
        if not self.is_supported_language(lang):
            raise IndicNlpException('Language {}  not supported'.format(lang))
        phonetic_data = ALL_PHONETIC_DATA if lang != LC_TA else TAMIL_PHONETIC_DATA
        phonetic_vectors = ALL_PHONETIC_VECTORS if lang != LC_TA else TAMIL_PHONETIC_VECTORS

        return phonetic_data, phonetic_vectors


    def get_phonetic_feature_vector(self, c, lang):
        offset = self.get_offset(c, lang)
        if not self.in_coordinated_range_offset(offset):
            return invalid_vector()

        phonetic_data, phonetic_vectors = self.get_phonetic_info(lang)

        if phonetic_data.ix[offset, 'Valid Vector Representation'] == 0:
            return self.invalid_vector()

        return phonetic_vectors[offset]

    @staticmethod
    def get_property_vector(v, prop_name):
        return v[PV_PROP_RANGES[prop_name][0]:PV_PROP_RANGES[prop_name][1]]

    @staticmethod
    def is_consonant(v):
        """ Checks the property of the character selected against its phonetic vector
        """
        return v[PVIDX_BT_CONSONANT] == 1

    @staticmethod
    def is_misc(v):
        return v[PVIDX_BT_MISC] == 1

    @staticmethod
    def is_valid(v):
        return np.sum(v) > 0

    @staticmethod
    def is_vowel(v):
        return v[PVIDX_BT_VOWEL] == 1

    @staticmethod
    def is_anusvaar(v):
        return v[PVIDX_BT_ANUSVAAR] == 1

    @staticmethod
    def is_plosive(v):
        return is_consonant(v) and get_property_vector(v, 'consonant_type')[0] == 1


    def is_dependent_vowel(self, v):
        return self.is_vowel(v) and v[PVIDX_VSTAT_DEP] == 1

    @staticmethod
    def is_nukta(v):
        return v[PVIDX_BT_NUKTA] == 1

    def orthographic_syllabify(self, word, lang):
        """Main syllablic function"""
        p_vectors = [self.get_phonetic_feature_vector(c, lang) for c in word]

        syllables = []

        for i in range(len(word)):
            v = p_vectors[i]

            syllables.append(word[i])

            if i + 1 < len(word) and (not self.is_valid(p_vectors[i + 1]) or self.is_misc(p_vectors[i + 1])):
                syllables.append(u' ')

            elif not self.is_valid(v) or self.is_misc(v):
                syllables.append(u' ')

            elif self.is_vowel(v):

                anu_nonplos = (i + 2 < len(word) and
                               self.is_anusvaar(p_vectors[i + 1]) and
                               not self.is_plosive(p_vectors[i + 2])
                               )

                anu_eow = (i + 2 == len(word) and
                           is_anusvaar(p_vectors[i + 1]))

                if not (anu_nonplos or anu_eow):
                    syllables.append(u' ')

            elif i + 1 < len(word) and (self.is_consonant(v) or self.is_nukta(v)):
                if self.is_consonant(p_vectors[i + 1]):
                    syllables.append(u' ')
                elif self.is_vowel(p_vectors[i + 1]) and not self.is_dependent_vowel(p_vectors[i + 1]):
                    syllables.append(u' ')
                elif self.is_anusvaar(p_vectors[i + 1]):
                    anu_nonplos = (i + 2 < len(word) and not self.is_plosive(p_vectors[i + 2]))

                    anu_eow = i + 2 == len(word)

                    if not (anu_nonplos or anu_eow):
                        syllables.append(u' ')

        print(u''.join(syllables).strip().split(u' '))


x = Syllabifier("/home/soumya/Documents/indic_nlp3/indic_nlp_resources-master", 'नमस्ते', 'hi')
