import wikipedia


word = input("Please enter a 'page title' or 'phrase'\n")
# I tried "Monty" and there was no error. When I tried writing the exception statement like the API doc it said
# that code is not a thing. So i just left it
while word != "":
    print("Summary:\n", wikipedia.summary(word))
    print("Title:\n", wikipedia.page(word).title)
    print("URL:\n", wikipedia.page(word).url)
    word = input("Enter another 'page title' or 'phrase'\n")
print("successfully broke")

