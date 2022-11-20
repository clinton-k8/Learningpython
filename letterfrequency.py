sentence = "This is a common interview question"
letterfreg = {}
for i in sentence:
    if i in letterfreg:
        letterfreg[i] += 1
    else:
        letterfreg[i] = 1
print(sorted(letterfreg.items(), key=lambda kv: kv[1], reverse=True))
