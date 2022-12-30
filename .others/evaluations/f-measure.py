# import library yang dibutuhkan
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

def f_measure(summary, reference):
    # tokenisasi kalimat menjadi kata-kata
    summary_tokens = word_tokenize(summary)
    reference_tokens = word_tokenize(reference)

    # hapus stop words
    stop_words = set(stopwords.words('indonesian'))
    summary_tokens = [token for token in summary_tokens if token not in stop_words]
    reference_tokens = [token for token in reference_tokens if token not in stop_words]

    # hitung jumlah kata yang sama dalam resumenya dan teks asli
    same_word_count = 0
    for token in summary_tokens:
        if token in reference_tokens:
            same_word_count += 1

    # hitung precision
    precision = same_word_count / len(summary_tokens)

    # hitung recall
    recall = same_word_count / len(reference_tokens)

    # hitung F-measure
    f_measure = 2 * (precision * recall) / (precision + recall)

    return f_measure

def read(filename):
    with open(filename, "r") as file:
        filedata = file.readlines()
    return filedata[0]

# contoh penggunaan
reference = read("article.txt")
summary = read("summary-se30.txt")
f_measure_score = f_measure(summary, reference)
print(f_measure_score)