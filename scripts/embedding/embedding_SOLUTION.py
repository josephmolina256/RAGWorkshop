import json
from sentence_transformers import SentenceTransformer


embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
# embedding_model.encode(INPUT_STRING).tolist() will return a list representation of the embedding!
# embedding_model.encode(INPUT_STRING) will return a np array representation of the embedding! This is needed for comparisons.

mock_data = [
    "Florida Tech Pathways (FTP) is a club at UF which strengthens student placements in the technology industry by creating a structured recruitment pipeline for top job opportunities.",
    "The four tracks in the program are: Tech Sales, Product Management, Consulting & Analytics, or Software Engineering.",
    "Through our 10-week analyst program, members receive dedicated mentorship.",
    "Joseph Molina is one of our software engineering mentors who has experience at Amazon Robotics, LinkedIn, and Collins Aerospace."
]

def embed_data(data):
    database = []
    for data in mock_data:
        embedding = embedding_model.encode(data).tolist() 
        database.append({"text": data, "embedding": embedding})

    with open("data/output/ftp_data_SOLUTION.json", "w") as file:
        json.dump(database, file, indent=4)
        
    print("Data embedded and saved to data/output/ftp_data_SOLUTION.json")

embed_data(mock_data)
