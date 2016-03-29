def sanitize(string):
    tokens = string.strip().split()
    string = " ".join(tokens)
    string = string.title()
    return string
