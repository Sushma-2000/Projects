import math
import re
import nav_test as nav_test
import pyrebase
import requests
from fuzzywuzzy import fuzz
import cosine_similarity as keywordVal

def givVal(model_answer,answer):
    out_of=5
    if (len(answer.split())) <= 5:
        return 0
    k1 = keywordVal.givKeywordsValue(model_answer, answer)
    k=x[1]
    req = requests.get("https://api.textgears.com/check.php?text=" + answer + "&key=iJyw2qQ7eLW5iUFd")
    no_of_errors = len(req.json()['errors'])
    if no_of_errors > 5 or k == 6:
        g = 0
    else:
        g = 1
    #q = math.ceil(fuzz.token_set_ratio(model_answer, answer) * 6 / 100)
    q=5
    print("Keywords : ", k)
    print("Grammar  : ", g)
    print("QST      : ", q)
    predicted = nav_test.predict(k, g, q)
    result = predicted * out_of / 10
    return str("Keywords: ",k,"Grammar: ",g,"QST: ",q,"class: ",result[0])
   