class Person:
    def __init__(self, name, address, email):
        self.name = name
        self.address = address
        self.email = email
    
    # string method return only str!!
    def __str__(self):
        return f"Name: {self.name}\nAddress: {self.address}\nEmail: {self.email}\n"
    
    def __repr__(self):
        return self.name


robert = Person("Robert Vari", "Budapest", "robert@gmail.com")
tamas = Person("Kiss Tamás", "Debrecen", "tamas@gmail.com")
kriszta = Person("Nagy Krisztina", "Miskolc", "kriszta88@gmail.com")

my_friends = [robert, tamas, kriszta]

print(my_friends)
print(kriszta)