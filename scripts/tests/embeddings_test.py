import json
from sentence_transformers import SentenceTransformer

from scipy.spatial.distance import cosine

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
# embedding_model.encode(INPUT_STRING).tolist() will return a list representation of the embedding!
# embedding_model.encode(INPUT_STRING) will return a np array representation of the embedding! This is needed for comparisons.

mock_data = [
    "Florida Tech Pathways (FTP) is a club at UF which strengthens student placements in the technology industry by creating a structured recruitment pipeline for top job opportunities.",
    "The four tracks in the program are: Tech Sales, Product Management, Consulting & Analytics, or Software Engineering.",
    "Through our 10-week analyst program, members receive dedicated mentorship.",
    "Joseph Molina is one of our software engineering mentors who has experience at Amazon Robotics, LinkedIn, and Collins Aerospace."
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