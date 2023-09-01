import string

def word_counter(text):
    word_freq = {}
    
    # Remove punctuation and convert to lowercase
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    words = text.split()
    
    for word in words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    return word_freq

sample_text = "Hello world! Hello Python. Python is great."
result = word_counter(sample_text)
print("Word frequency:", result)
