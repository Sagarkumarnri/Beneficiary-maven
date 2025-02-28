import pandas as pd
from sentence_transformers import SentenceTransformer, losses, InputExample
from torch.utils.data import DataLoader
import torch

# Step 1: Load the pre-trained model
model = SentenceTransformer("./paraphrase-MiniLM-L6-v2")

# Step 2: Load training data (CSV format with comma delimiter)
df = pd.read_csv("name_similarity.csv", delimiter=",")

# Step 3: Convert data into InputExamples with stricter similarity labels
train_examples = [
    InputExample(texts=[row["Name1"], row["Name2"]], label=float(row["Similarity"]))
    for _, row in df.iterrows()
]

# Step 4: Create DataLoader with a smaller batch size (stricter updates)
train_dataloader = DataLoader(train_examples, shuffle=True, batch_size=8)

# Step 5: Define Loss Function (Cosine Similarity Loss)
train_loss = losses.CosineSimilarityLoss(model)

# Step 6: Train the Model with stricter parameters
print("Training started...")
model.fit(
    train_objectives=[(train_dataloader, train_loss)],
    epochs=10,  # More training for better accuracy
    warmup_steps=200,  # Gradual warmup
    optimizer_params={"lr": 2e-5},  # Lower learning rate for precise tuning
    show_progress_bar=True
)
print("Training completed!")

# Step 7: Save the fine-tuned model
model.save("./fine_tuned_name_similarity_model")
print("Model saved successfully!")

# Step 8: Clear GPU cache (for strict memory management, if running on GPU)
if torch.cuda.is_available():
    torch.cuda.empty_cache()
