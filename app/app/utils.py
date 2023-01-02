import math

def CleanSentence(sentence):
    # Cleaning whitespaces, Add dot and space at last sentence
    sentence = sentence.lstrip()
    sentence = sentence.rstrip()
    words = sentence.split()
    sentence = " ".join(word for word in words)
    if len(sentence) > 0:
        if sentence[-1] != ".":
            sentence += ". "
        else:
            sentence += " "
    return sentence

def Article2Sentences(article):
    sentences = article.split(". ")
    sentences = [CleanSentence(sentence) for sentence in sentences]
    return sentences

def CleanSentences(sentences):
    sentences = [CleanSentence(item) for item in sentences if "Baca juga:" not in item and item != ""]
    return sentences

def CR2N(length, cr):
    return math.ceil(length*cr)

def Logs(text, filename):
    # write text into file
    with open(f"./logs/{filename}", 'w') as f:
        f.write(text)