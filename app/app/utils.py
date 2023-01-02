def CleanSentence(sentence):
    # Cleaning whitespaces
    sentence = sentence.lstrip()
    sentence = sentence.rstrip()
    words = sentence.split()
    sentence = " ".join(word for word in words)
    # Add dot and space at last sentence
    if len(sentence) > 0:
        if sentence[-1] != ".":
            sentence += ". "
        else:
            sentence += " "
    # Return
    return sentence

def Logs(text, filename):
    # write text into file
    with open(f"./logs/{filename}", 'w') as f:
        f.write(text)