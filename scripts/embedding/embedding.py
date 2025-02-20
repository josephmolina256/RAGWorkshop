import json
from sentence_transformers import SentenceTransformer

from scipy.spatial.distance import cosine

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
# embedding_model.encode(INPUT_STRING).tolist() will return a list representation of the embedding!
# embedding_model.encode(INPUT_STRING) will return a np array representation of the embedding! This is needed for comparisons.

