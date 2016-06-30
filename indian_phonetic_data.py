
import pandas as pd
import numpy as np
PHONETIC_VECTOR_START_OFFSET = 6

all_phonetic_data = pd.read_csv('/home/soumya/src/all_script_phonetic_data.csv', encoding='utf-8')
tamil_phonetic_data = pd.read_csv('/home/soumya/src/tamil_script_phonetic_data.csv', encoding='utf-8')

all_phonetic_vectors = all_phonetic_data.ix[:, PHONETIC_VECTOR_START_OFFSET:].as_matrix()
tamil_phonetic_vectors = tamil_phonetic_data.ix[:, PHONETIC_VECTOR_START_OFFSET:].as_matrix()

phonetic_vector_length = all_phonetic_vectors.shape[1]

ALL_PHONETIC_DATA = all_phonetic_data
TAMIL_PHONETIC_DATA = tamil_phonetic_data
ALL_PHONETIC_VECTORS = all_phonetic_vectors
TAMIL_PHONETIC_VECTORS = tamil_phonetic_vectors
PHONETIC_VECTOR_LENGTH = phonetic_vector_length


