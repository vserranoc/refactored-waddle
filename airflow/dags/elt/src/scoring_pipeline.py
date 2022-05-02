from clean_string import clean_tweet

def predict_sentiment(text,model, preprocessing):
    clean_text = [clean_tweet(text)]
    transform_text = preprocessing.transform(clean_text) 
    proba = model.predict_proba(transform_text)
    
    return proba[0,-1]