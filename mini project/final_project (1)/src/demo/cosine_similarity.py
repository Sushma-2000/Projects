import re, math
from collections import Counter
import fuzzywuzzy.fuzz

WORD = re.compile(r'\w+')


def get_cosine(vec1, vec2):
    intersection = set(vec1.keys()) & set(vec2.keys())
    numerator = sum([vec1[x] * vec2[x] for x in intersection])

    sum1 = sum([vec1[x] ** 2 for x in vec1.keys()])
    sum2 = sum([vec2[x] ** 2 for x in vec2.keys()])
    denominator = math.sqrt(sum1) * math.sqrt(sum2)

    if not denominator:
        return 0.0
    else:
        return float(numerator) / denominator


def text_to_vector(text):
    words = WORD.findall(text)
    return Counter(words)


def givKeywordsValue(text1, text2):
    cosine_list=[]
    text2.lower()
    for indi_text in text1:
        if(indi_text==None):
            continue
        indi_text.lower()
        vector1 = text_to_vector(indi_text+"")
        #print("indi_text:",indi_text)
        vector2 = text_to_vector(text2)
        cosine_list.append(round(get_cosine(vector1, vector2),2)*100)
    print(cosine_list)
    cosine=max(cosine_list)
    kval = 0
    if cosine > 90:
        kval = 1
    elif cosine > 80:
        kval = 2
    elif cosine > 60:
        kval = 3
    elif cosine > 40:
        kval = 4
    elif cosine > 20:
        kval = 5
    else:
        kval = 6
    return cosine,kval

