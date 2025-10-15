# sentiment_analysis.py
import pandas as pd
import re
import torch
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification, Trainer, TrainingArguments

# ============== Step 1: Load dataset ==============
print("Loading dataset...")
data = pd.read_csv("Tweets.csv")  # Replace with your dataset filename

# Some Kaggle datasets use different column names, so adjust accordingly:
if 'text' not in data.columns:
    text_col = [col for col in data.columns if 'text' in col.lower()][0]
    data.rename(columns={text_col: 'text'}, inplace=True)
if 'airline_sentiment' not in data.columns:
    label_col = [col for col in data.columns if 'sentiment' in col.lower()][0]
    data.rename(columns={label_col: 'airline_sentiment'}, inplace=True)

# ============== Step 2: Clean tweets ==============
print("Cleaning tweets...")
def clean_tweet(text):
    text = re.sub(r'http\S+', '', str(text))  # remove URLs
    text = re.sub(r'@\w+', '', text)          # remove mentions
    text = re.sub(r'#', '', text)             # remove hashtags
    text = re.sub(r'[^A-Za-z0-9 ]+', '', text)
    return text.lower()

data['clean_text'] = data['text'].apply(clean_tweet)

# ============== Step 3: Encode labels ==============
print("Encoding labels...")
encoder = LabelEncoder()
data['label'] = encoder.fit_transform(data['airline_sentiment'])

# ============== Step 4: Train-test split ==============
X_train, X_test, y_train, y_test = train_test_split(
    data['clean_text'].tolist(),
    data['label'].tolist(),
    test_size=0.2,
    random_state=42
)

# ============== Step 5: Tokenization ==============
print("Tokenizing...")
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')

train_encodings = tokenizer(X_train, truncation=True, padding=True, max_length=128)
test_encodings = tokenizer(X_test, truncation=True, padding=True, max_length=128)

class TweetDataset(torch.utils.data.Dataset):
    def __init__(self, encodings, labels):
        self.encodings = encodings
        self.labels = labels
    def __getitem__(self, idx):
        item = {key: torch.tensor(val[idx]) for key, val in self.encodings.items()}
        item['labels'] = torch.tensor(self.labels[idx])
        return item
    def __len__(self):
        return len(self.labels)

train_dataset = TweetDataset(train_encodings, y_train)
test_dataset = TweetDataset(test_encodings, y_test)

# ============== Step 6: Load Model ==============
print("Loading model...")
model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased', num_labels=len(encoder.classes_))

# ============== Step 7: Training setup ==============
training_args = TrainingArguments(
    output_dir='./results',
    num_train_epochs=1,  # increase to 2–3 for better accuracy
    per_device_train_batch_size=8,
    per_device_eval_batch_size=8,
    logging_dir='./logs',
    logging_steps=100,
    evaluation_strategy="epoch"
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_dataset,
    eval_dataset=test_dataset
)

# ============== Step 8: Train ==============
print("Training model...")
trainer.train()

# ============== Step 9: Evaluate ==============
print("Evaluating model...")
predictions = trainer.predict(test_dataset)
preds = torch.argmax(torch.tensor(predictions.predictions), dim=1)
print(classification_report(y_test, preds, target_names=encoder.classes_))

# ============== Step 10: Test with new text ==============
def predict_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=128)
    outputs = model(**inputs)
    prediction = torch.argmax(outputs.logits).item()
    return encoder.inverse_transform([prediction])[0]

print("\nExample Predictions:")
print("I love this new phone! →", predict_sentiment("I love this new phone!"))
print("This is terrible. →", predict_sentiment("This is terrible."))
print("It's okay, not bad. →", predict_sentiment("It's okay, not bad."))
