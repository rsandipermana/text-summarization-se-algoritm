from rouge import Rouge

rouge = Rouge()


def read(filename):
    with open(filename, "r") as file:
        filedata = file.readlines()
    return filedata[0]

# contoh penggunaan
reference = read("article.txt")
summary = read("summary-ga.txt")

scores = rouge.get_scores(summary, reference)
rouge_1 = scores[0]['rouge-1']['f']
print(f"ROUGE-1: {rouge_1:.4f}")