from bs4 import BeautifulSoup
import re
from emot.emo_unicode import UNICODE_EMOJI

def clean_tweet(x):
    clean_x = BeautifulSoup(x,features='html.parser').get_text()
    clean_x = ' '.join(re.sub("(@[A-Za-z0-9]+)|(#[A-Za-z0-9]+)", " ", clean_x).split())
    clean_x = ' '.join(re.sub("(\w+:\/\/\S+)", " ", clean_x).split())
    clean_x = ' '.join(re.sub("[\.\,\!\?\:\;\-\=]", " ", clean_x).split())
    clean_x = clean_x.lower()

    for emot in UNICODE_EMOJI:
        clean_x = clean_x.replace(emot, "_".join(UNICODE_EMOJI[emot].replace(",","").replace(":","").split()))

    return clean_x