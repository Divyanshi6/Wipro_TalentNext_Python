# Q. Perform Text Preprocessing on the SMSSpamCollection Dataset.
import pandas as pd
import re

data = pd.read_csv("C:/Users/sdivy/WiproTalentnext/SMSSpamCollection.csv",sep="\t", names=["label", "message"])
print("Dataset Shape:", data.shape)
print(data.head())

def preprocess_text(text):
    text = text.lower()                     
    text = re.sub(r'\d+', '', text)         
    text = re.sub(r'[^\w\s]', '', text)    
    text = text.strip()                    
    return text

data["clean_message"] = data["message"].apply(preprocess_text)
print("\nSample Preprocessed Messages:")
print(data[["message", "clean_message"]].head(10))
