f = open("Wörterbuch.txt", "a", encoding="utf-8")
with open("quelle.txt", "r", encoding="utf-8") as s:
    for i in s:
        for word in i.split():
            print(word.strip("""'0123456789\",.?\(\)»/\][&%$=´}{~^°`§+#*;:«""").lower(), file=f)
f.close()
open("quelle.txt", "w").close()
