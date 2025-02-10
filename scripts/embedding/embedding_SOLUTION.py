import json
from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

def embed_qa_data(input_file_path="data/input/dummy_data.json", output_file_path="data/output/embedded_data.json"):
    try:
        with open(input_file_path, "r") as file:
            qa_data = json.load(file)

        qa_embeddings = []
        for qa_item in qa_data:
            qa_embeddings.append(
                {
                    "embedding": embedding_model.encode(qa_item["question"]).tolist(),
                    "qa_item": qa_item
                }
            )

        with open(output_file_path, "w") as file:
            json.dump(qa_embeddings, file, indent=4) 
        return True
    except Exception as e:
        print(f"Error: {e}")
        return False  # Failure
    
print(embed_qa_data())