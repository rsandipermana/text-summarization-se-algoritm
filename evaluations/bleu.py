from nltk.translate.bleu_score import sentence_bleu

def read(filename):
    with open(filename, "r") as file:
        filedata = file.readlines()
    return filedata[0]

# contoh penggunaan
reference = read("article.txt")
summary = read("summary-pr.txt")

# hitung BLEU dengan menggunakan teks sumber sebagai reference
bleu_score = sentence_bleu([reference], summary)

print("BLEU score:", bleu_score)