
def log(file, message):
    with open(file, 'wa') as f:
        f.write(message)
