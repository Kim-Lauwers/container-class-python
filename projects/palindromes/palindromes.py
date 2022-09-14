my_list = ["chef", "kok", "boom", "droommoord", "kajak", "boot"]

result = list(filter(lambda word: (word == "".join(reversed(word))), my_list))

print(result)
