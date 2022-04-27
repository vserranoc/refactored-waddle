import joblib
from src.clean_string import clean_tweet   

# Load
final_model = joblib.load('./src/objects/final_model.joblib')
count_vec = joblib.load('./src/objects/model_count_vectorizer.joblib')


def predict_sentiment(text):
    clean_text = [clean_tweet(text)]
    print(clean_text)
    transform_text = count_vec.transform(clean_text) 
    proba = final_model.predict_proba(transform_text)
    
    return f'Probability of being a positive sentiment: {proba[0,-1]}'