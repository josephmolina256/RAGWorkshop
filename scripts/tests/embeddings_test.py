import json
from sentence_transformers import SentenceTransformer

from scipy.spatial.distance import cosine

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
# embedding_model.encode(INPUT_STRING).tolist() will return a list representation of the embedding!
# embedding_model.encode(INPUT_STRING) will return a np array representation of the embedding! This is needed for comparisons.

mock_data = [
    "Soor is very handsome",
    "Sean has a Scion FRS",
    "Andy Gonzalez likes esspresso and cafe con leche",
    "Derek loves Pink Floyd and The Wall"
    "Andy do is a big steppa"
]

database = []
for data in mock_data:
    embedding = embedding_model.encode(data)
    database.append({"qa_item": data, "embedding": embedding})

input_string = input("Enter a string to embed: ")
input_embedding = embedding_model.encode(input_string)


best_match = None
best_score = float("inf")
for data in database:
    score = cosine(input_embedding, data["embedding"])
    print(f"Cosine distance between '{input_string}' and '{data['qa_item']}': {score}")
    if score < best_score:
        best_score = score
        best_match = data

print(f"Best match: {best_match['qa_item']} with score {best_score}")