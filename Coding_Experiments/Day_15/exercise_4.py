import webbrowser

user_term = input("What you want to search: ")
# user_term = input("What you want to search: ").replace(" ", "+")

webbrowser.open("https://www.google.com/search?q=" + user_term)

