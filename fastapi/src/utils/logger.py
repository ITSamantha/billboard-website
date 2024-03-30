
def log(file, message):
    with open(file, 'a') as f:
        f.write(message + "\n")
