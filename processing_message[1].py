def message(a):
    import nltk
    from nltk.stem import WordNetLemmatizer
    lemmatizer = WordNetLemmatizer()
    import json
    import random
    def clean_up_sentence(sentence):
        sentence_words = nltk.word_tokenize(sentence)
        sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
        return sentence_words
    def getResponse(ints,intents_json):
        d = {'greeting': 0, 'goodbye': 0, 'thanks': 0, 'info': 0, 'precautions': 0, 'symptoms':0, 'severe':0, 'treatment':0, 'food':0, 'spread':0, 'life':0, 'death':0, 'variant':0, 'vaccine':0, 'bot':0, 'fine':0}
        a = {'greeting': 0, 'goodbye': 1, 'thanks': 2, 'info': 3, 'precautions': 4, 'symptoms':5, 'severe':6, 'treatment':7, 'food':8, 'spread':9, 'life':10, 'death':11, 'variant':12, 'vaccine':13, 'bot':14, 'fine':15}
        tag = ints
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            for j in tag:
                for k in i['patterns']:
                    if (k == j):
                        d[i['tag']]=d[i['tag']]+1
        t=a[max(d,key=d.get)]
        if max(d.values())==0: z = "Sorry! I didnt understand. Please try again"
        else: z=random.choice(list_of_intents[t]['responses'])
        return z
    def chatbot_response(a):
        ints = clean_up_sentence(a)
        res = getResponse(ints,intents)
        return res
    def send(a):
        global res
        if a != '': res = chatbot_response(a)
        return res
    intents = json.loads(open('intents.json').read())
    return send(a)
