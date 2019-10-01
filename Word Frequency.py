def create_frequency_table(text):
    stopWords=set(stopwords.words("english"))
    words=word_tokenize(text)
    ps=PorterStemmer()
    freqtable=dict()
    for word in words:
        word=ps.stem(word)
        if word in stopWords:
            continue
        if word in freqtable:
            freqtable[word]+=1
        else:
            freqtable[word]=1
    return freqtable
