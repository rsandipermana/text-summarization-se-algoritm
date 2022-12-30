import networkx as nx
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# PAGE RANK
# fungsi untuk membuat graf dari teks
def create_graph(text):
    # tokenisasi teks
    tokens = word_tokenize(text)

    # hapus stopwords dari teks
    stop_words = set(stopwords.words("english"))
    tokens = [token for token in tokens if token not in stop_words]

    # membuat graf
    graph = nx.Graph()
    for i, token in enumerate(tokens):
        for j in range(i+1, len(tokens)):
            graph.add_edge(token, tokens[j])

    return graph

# fungsi untuk melakukan text summarization menggunakan PageRank
def summarize(text, n):
    # membuat graf dari teks
    graph = create_graph(text)

    # menghitung PageRank dari graf
    pagerank = nx.pagerank(graph)

    # mengurutkan kata berdasarkan PageRank
    sorted_pagerank = sorted(pagerank.items(), key=lambda x: x[1], reverse=True)

    # memilih n kata dengan PageRank tertinggi sebagai summary
    summary = [word for word, _ in sorted_pagerank[:n]]

    return " ".join(summary)

def read(filename):
    with open(filename, "r") as file:
        filedata = file.readlines()
    return filedata[0]

def write_summary(text):
    with open(f"./output/summary.txt", 'w') as f:
        # tulis teks ke dalam file
        f.write(text)

# contoh teks yang akan dirangkum
text = read("./../articles/article.txt")
n = 10
summary = summarize(text, n)
write_summary(summary)
print(summary)