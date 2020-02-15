f = open("Wörterbuch.txt", "a")
with open("myfile.txt", "r") as s:
    for i in s:
        for word in i.split():
            print(word.strip(",.?()/&%$=´}{[]~^°`§+#*;:«"), file=f)
f.close()
