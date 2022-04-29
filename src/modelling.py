# Setup
import pandas as pd
import numpy as np

from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer

from nltk.tokenize import word_tokenize

def model_in_folds(model_selected, model_name, trainset, preprocessing='CountVec'):
    
    accuracies = []
    recalls = []
    f1_scores = []
    folds = []
    aucs = []
    briers=[]
    for fold_ in range(5):
        train_df = trainset[trainset.kfold != fold_].reset_index(drop=True)

        test_df = trainset[trainset.kfold == fold_].reset_index(drop=True)
        # Transformation
        if preprocessing == 'CountVec':
            count_vec = CountVectorizer(
                tokenizer=word_tokenize,
                token_pattern=None 
            )
            count_vec.fit(train_df.clean_text)
            xtrain = count_vec.transform(train_df.clean_text) 
            xtest = count_vec.transform(test_df.clean_text)
        elif preprocessing == 'tfidf':
            tfidf_vec = TfidfVectorizer(
                tokenizer=word_tokenize, 
                token_pattern=None, 
                ngram_range=(1, 3)
            )
            # fit count_vec on training data reviews
            tfidf_vec.fit(train_df.clean_text)
            # transform training and validation data reviews
            xtrain = tfidf_vec.transform(train_df.clean_text) 
            xtest = tfidf_vec.transform(test_df.clean_text)
            
        # Training
        model = model_selected
        model.fit(xtrain, train_df.sentiment) 
        
        # Scoring
        proba = model.predict_proba(xtest)[:,1]
        precision_, recall_, proba_ = metrics.precision_recall_curve(test_df.sentiment, proba)
        
        optimal_proba_cutoff = sorted(list(zip(np.abs(precision_ - recall_), proba_)), key=lambda i: i[0], reverse=False)[0][1]
        preds = proba >= optimal_proba_cutoff
        
        # Performance measure
        accuracy = metrics.accuracy_score(test_df.sentiment, preds)
        recall = metrics.recall_score(test_df.sentiment, preds)
        f1_score = metrics.f1_score(test_df.sentiment, preds)
        auc = metrics.roc_auc_score(test_df.sentiment, proba)
        brier = metrics.brier_score_loss(test_df.sentiment, proba)
        
        accuracies.append(accuracy)
        recalls.append(recall)
        f1_scores.append(f1_score)
        folds.append(fold_)
        aucs.append(auc)
        briers.append(brier)
            
    df_results = pd.DataFrame(
        {
            'fold':folds,
            'recall':recalls,
            'accuracy':accuracies,
            'f1_score':f1_scores,
            'auc':aucs,
            'brier':briers
        }
    )
    
    df_results['preprocessing'] = preprocessing
    df_results['model'] = model_name
           
    return df_results
