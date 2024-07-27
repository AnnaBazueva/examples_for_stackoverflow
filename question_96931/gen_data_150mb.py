# Be prepared to spend a few hours on this.
with open("data_150mb.txt", "+a", encoding="utf-8") as f:
    for i in range(1, 16839794):
        print(i, file=f)
