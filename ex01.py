# text = "  Hello World from Python   "
# word_list = text.split(" ")
# print(word_list)

# word_list = text.strip().split(" ")
# print(word_list)

# word_list = text.strip().replace("Python", "GoIT").split(" ")
# print(word_list)

# word_list = text.strip().replace("Python", "GoIT").split(" ").append("Python")
# print(word_list)

# word_list = text.strip().replace("Python", "GoIT").split(" ").append("Python").replace()
# print(word_list)

text = " Ми вчимо Java?  "
text = text.lstrip()
text = text.replace("Java", "Python")
text = text.removesuffix("?")
print(text)

text = " Ми вчимо Java?  "
text = text.strip()
text = text.replace("Java", "Python")
text = text.removesuffix("?")
print(text)

list_of_words = ["We", "learn", "Python!"]
result = ". ".join(list_of_words)
print(result)