from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# fungsi untuk menghitung tingkat kemiripan antara summary dan reference summary
def compute_rouge_1_recall(summary, reference_summary):
    # tokenisasi summary dan reference summary
    summary_tokens = word_tokenize(summary)
    reference_summary_tokens = word_tokenize(reference_summary)

    # hapus stopwords dari summary dan reference summary
    stop_words = set(stopwords.words("english"))
    summary_tokens = [token for token in summary_tokens if token not in stop_words]
    reference_summary_tokens = [token for token in reference_summary_tokens if token not in stop_words]

    # hitung jumlah kata yang muncul di reference summary
    reference_summary_word_count = len(reference_summary_tokens)

    # hitung jumlah kata yang muncul di keduanya
    common_word_count = len(set(summary_tokens).intersection(set(reference_summary_tokens)))

    # hitung ROUGE-1 (recall)
    rouge_1_recall = common_word_count / reference_summary_word_count

    return rouge_1_recall

def read(filename):
    with open(filename, "r") as file:
        filedata = file.readlines()
    return filedata[0]

# contoh penggunaan
reference = read("article.txt")
summary = read("summary-se-bot.txt")

rouge_1_recall = compute_rouge_1_recall(summary, reference)

print(f"rouge-1(recall): {rouge_1_recall:.4f}")
