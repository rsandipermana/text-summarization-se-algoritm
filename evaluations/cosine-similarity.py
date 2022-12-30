from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer

# fungsi untuk menghitung cosine similarity antara summary dan reference summary
def compute_cosine_similarity(summary, reference_summary):
    # ubah summary dan reference summary menjadi vektor menggunakan CountVectorizer
    vectorizer = CountVectorizer().fit_transform([summary, reference_summary])
    vectors = vectorizer.toarray()
    
    # hitung cosine similarity
    cosine_sim = cosine_similarity(vectors)
    
    return cosine_sim[0][1]

def read(filename):
    with open(filename, "r") as file:
        filedata = file.readlines()
    return filedata[0]

# contoh penggunaan
reference = read("article.txt")
summary = read("summary-se🏆.txt")

cosine_sim = compute_cosine_similarity(summary, reference)
print(f"Cosine similarity: {cosine_sim:.4f}")