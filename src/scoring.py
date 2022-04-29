import joblib
from src.clean_string import clean_tweet   

# Load
final_model = joblib.load('./src/objects/final_model.joblib')
best_preprocessing = joblib.load('./src/objects/feature_extractor.joblib')


def predict_sentiment(text):
    clean_text = [clean_tweet(text)]
    print(clean_text)
    transform_text = best_preprocessing.transform(clean_text) 
    proba = final_model.predict_proba(transform_text)
    
    return f'Probability of being a positive sentiment: {proba[0,-1]}'