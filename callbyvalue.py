string = "Greek"

def test(string):
    string = "Greeksforgreeks"
    print("Inside function:",string)

test(string)
print("outside Function:", string)