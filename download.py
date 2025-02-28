from sentence_transformers import SentenceTransformer

# Load a pre-trained model from Hugging Face instead of local directory
model = SentenceTransformer("sentence-transformers/paraphrase-MiniLM-L6-v2")

# Save it locally for fine-tuning
model.save("./paraphrase-MiniLM-L6-v2")
print("Base model downloaded and saved locally.")
