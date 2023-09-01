def word_frequency(sentence, words):
    word_freq = {}
    
    sentence = sentence.lower()
    sentence_words = sentence.split()
    
    for word in words:
        word_freq[word] = sentence_words.count(word)
    
    return word_freq

sentence = input("Enter a sentence: ")
search_words = input("Enter words separated by spaces: ").split()
result = word_frequency(sentence, search_words)
print("Word frequency:", result)
