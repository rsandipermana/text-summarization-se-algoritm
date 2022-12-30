# import library yang dibutuhkan
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def rouge_n(summary, reference, n=1):
    # tokenisasi kalimat menjadi kata-kata
    summary_tokens = word_tokenize(summary)
    reference_tokens = word_tokenize(reference)

    # hapus stop words
    stop_words = set(stopwords.words('english'))
    summary_tokens = [token for token in summary_tokens if token not in stop_words]
    reference_tokens = [token for token in reference_tokens if token not in stop_words]

    # hitung jumlah kata yang sama dalam resumenya dan teks asli
    same_word_count = 0
    for i in range(len(summary_tokens) - n + 1):
        if summary_tokens[i:i+n] == reference_tokens[i:i+n]:
            same_word_count += 1

    # hitung ROUGE-N
    rouge_n = same_word_count / len(summary_tokens)

    return rouge_n

def read(filename):
    with open(filename, "r") as file:
        filedata = file.readlines()
    print(filedata[0])
    return filedata[0]

# contoh penggunaan
reference = read("article.txt")
summary = read("summary.txt")
rouge_n_score = rouge_n(summary, reference, n=1)
print(rouge_n_score)