def score_sentences(sentences,freq_table):
    value=dict()
    stopWords=set(stopwords.words("english"))
    ps=PorterStemmer()
    for sentence in sentences:
        value[sentence]=0
        count=len(word_tokenize(sentence))
        words=word_tokenize(sentence)
        for word in words:
            word=ps.stem(word)
            if word in stopWords:
                continue
            else:
                value[sentence]+=freq_table[word]
        value[sentence]=value[sentence]/count
    
    return value
