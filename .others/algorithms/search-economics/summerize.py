# import library yang dibutuhkan
import sys
sys.path.append("~/Thesis/Code")
import nltk
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import networkx as nx
import time
import json
import math
 
# SEARCH ECONOMICS
def read_article(file_name):
    # baca teks dari file / teks mentah
    with open(file_name, "r") as file:
        filedata = file.readlines()
    article = filedata[0].split(".")
    sentences = []
 
    for sentence in article:
        # hapus stop words dan tokenisasi kalimat
        sentence = sentence.replace("[^a-zA-Z]", " ")
        sentence = sentence.lower()
        sentence = sentence.split(" ")
        sentence = [word for word in sentence if word not in stopwords.words("indonesian")]
        sentences.append(sentence)
 
    # kembalikan vektor kalimat
    return sentences
 
def sentence_similarity(sent1, sent2, stopwords=None):
    # hitung vektor sentimen kedua kalimat
    if stopwords is None:
        stopwords = []
 
    sent1 = [w.lower() for w in sent1]
    sent2 = [w.lower() for w in sent2]
 
    all_words = list(set(sent1 + sent2))
 
    vector1 = np.zeros(len(all_words))
    vector2 = np.zeros(len(all_words))
 
    # mengisi vektor dengan bobot sentimen
    for w in sent1:
        if w in stopwords:
            continue
        vector1[all_words.index(w)] += 1
 
    for w in sent2:
        if w in stopwords:
            continue
        vector2[all_words.index(w)] += 1
 
    # hitung kosinus distance antara kedua vektor
    return 1 - cosine_distance(vector1, vector2)

def build_similarity_matrix(sentences, stop_words):
    # membuat matriks kemiripan kalimat
    similarity_matrix = np.zeros((len(sentences), len(sentences)))
 
    for idx1 in range(len(sentences)):
        for idx2 in range(len(sentences)):
            if idx1 == idx2: # skip kalimat yang sama
                continue 
            similarity_matrix[idx1][idx2] = sentence_similarity(sentences[idx1], sentences[idx2], stop_words)
 
    return similarity_matrix
 
def generate_summary(file_name, top_n=5):
    stop_words = stopwords.words('indonesian')
    summarize_text = []
 
    # baca teks dan hitung matriks kemiripan kalimat
    sentences = read_article(file_name)
    # top_n = math.ceil(len(sentences)/100*cr)
    # print(top_n)
    sentence_similarity_matrix = build_similarity_matrix(sentences, stop_words)
 
    # membuat graf dari matriks kemiripan kalimat
    sentence_similarity_graph = nx.from_numpy_array(sentence_similarity_matrix)
    scores = nx.pagerank(sentence_similarity_graph)
 
    # urutkan kalimat berdasarkan skor pagerank
    ranked_sentences = sorted(((scores[i],s) for i,s in enumerate(sentences)), reverse=True)
 
    # ambil top_n kalimat terbaik
    for i in range(top_n):
        summarize_text.append(" ".join(ranked_sentences[i][1]))
    write_summary(json.dumps(ranked_sentences), "se-ranked.json")
 
    # kembalikan hasil resumisasi
    return ". ".join(summarize_text)

def write_summary(text, filename):
    with open(filename, 'w') as f:
        # tulis teks ke dalam file
        f.write(text)

summary = generate_summary("articles/article.txt", top_n=6)
write_summary(summary, "algorithms/search-economics/output/test.txt")
print(summary)