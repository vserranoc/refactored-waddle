import numpy as np
import pandas as pd


# Preprocesing
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from nltk.tokenize import word_tokenize

# Modelling
from sklearn import model_selection
from sklearn import linear_model
from sklearn import naive_bayes

# own modules
from src.clean_string import clean_tweet
from src.modelling import model_in_folds

pipelines = [
    {
        'model':naive_bayes.MultinomialNB(),
        'model_name':'Naive Bayes',
        'preprocessing':'CountVec',
    },
    {
        'model':naive_bayes.MultinomialNB(),
        'model_name':'Naive Bayes',
        'preprocessing':'tfidf',
    },
    {
        'model':linear_model.LogisticRegression(solver='lbfgs', max_iter=1000),
        'model_name':'Logistic Regression',
        'preprocessing':'CountVec',
    },
    {
        'model':linear_model.LogisticRegression(solver='lbfgs', max_iter=1000),
        'model_name':'Logistic Regression',
        'preprocessing':'tfidf',
    }
]

def run_autoML(trainset, pipelines=pipelines,eval_metric='brier', order='min'):
    trainset_ = trainset.copy()
    trainset_['clean_text'] = trainset_.texto.apply(clean_tweet)
    trainset_['sentiment'] = trainset_.sentimiento.apply(
        lambda x: 1 if x == 1 else 0
    )

    # Folds creation
    trainset_["kfold"] = -1
    trainset_ = trainset_.sample(frac=1).reset_index(drop=True)
    y = trainset_.sentiment.values
    kf = model_selection.StratifiedKFold(n_splits=5, shuffle=True, random_state=23)

    for f, (t_, v_) in enumerate(kf.split(X=trainset_, y=y)): 
        trainset_.loc[v_, 'kfold'] = f

    lst_results = []
    for pipeline in pipelines:
        aux_results = model_in_folds(pipeline['model'], pipeline['model_name'], trainset_, pipeline['preprocessing'])
        lst_results.append(aux_results)

    df_results = pd.concat(lst_results)
    df_results = df_results.groupby(['model','preprocessing'])[['recall', 'accuracy', 'f1_score', 'auc','brier']].mean()
    ascending_order = order == 'min'
    df_results = df_results.sort_values(by=eval_metric, ascending=ascending_order)
    best_model_results = df_results.iloc[0,:]

    # preprocessing selection
    if best_model_results.name[1] == 'CountVec':
        best_preprocessing = CountVectorizer(
                tokenizer=word_tokenize,
                token_pattern=None 
            )

    elif best_model_results.name[1] == 'tfidf':
        best_preprocessing = TfidfVectorizer(
                tokenizer=word_tokenize, 
                token_pattern=None, 
                ngram_range=(1, 3)
        )


    best_preprocessing.fit(trainset_.clean_text)
    train = best_preprocessing.transform(trainset_.clean_text) 


    # model selection
    if best_model_results.name[0] == 'Naive Bayes':
        best_model = naive_bayes.MultinomialNB()
    elif best_model_results.name[0] == 'Logistic Regression':
        best_model = linear_model.LogisticRegression(solver='lbfgs', max_iter=1000)

    best_model.fit(train, trainset_.sentiment)

    final_results = {
        'trained_model':{
            'object':best_model,
            'name':best_model_results.name[0]
        },
        'preprocessing':{
            'object':best_preprocessing,
            'name':best_model_results.name[1]
        },
        'performance':{
            'final':best_model_results,
            'all':df_results
        }
    }

    return final_results


def train_final_model(selected_pipeline, trainset):

    run_autoML()



    count_vec = CountVectorizer(
        tokenizer=word_tokenize,
        token_pattern=None 
    )

    count_vec = count_vec.fit(trainset.clean_text)
    transformed_text = count_vec.transform(trainset.clean_text) 
    final_model = linear_model.LogisticRegression(solver='lbfgs', max_iter=1000)
    final_model.fit(transformed_text, trainset.sentiment)

    return


