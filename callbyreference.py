string = "Greek"

def test(string):
    string = "Greeksforgreeks"
    print("Inside function:",string)

test(id(string))
print("outside Function:", string)