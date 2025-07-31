question = input("Type any word: ")

print(f"""This word is{type(question)}
This word is alpha num? {question.isalnum()}
This word is alpha? {question.isalpha()}
This word is number? {question.isnumeric()}
This word is ascii? {question.isascii()}
This word has space? {question.isspace()}
""")
