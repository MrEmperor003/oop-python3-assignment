# 1. School data type
class School:
    def __init__(self, name, class_room, subject):
        self.name = name
        self.class_room = class_room
        self.subject = subject

# 2. family data type
class Family:
    def __init__(self, parent, children, total):
        self.parent = parent
        self.children = children
        self.total = total

# 3. Person data type
class Person:
    def __init__(self, name, gender, status):
        self.name = name
        self.gender = gender
        self.status = status

# 4. Register data type
class Register:
    def __init__(self, student, check_in, check_out):
        self.student = student
        self.check_in = check_in
        self.check_out = check_out

# 5. Product data type
class Product:
    def __init__(self, product_name, price, quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity


# ====== Using the custom data types ======
# Create objects
A1 = School("Block fuse", "cohort 3", "python")
A2 = Family(2, 3, 5)
A3 = Person("tom", "male", "single")
A4 = Register("jerry", "10 AM", "12 PM")
A5 = Product("light bulb", 1000, 10)

# Print attributes
print("School: ", A1.name, A1.class_room,A1.subject)
print("Family: ", "This Family is made up of", A2.parent, "parent", A2.children, "children and making them a total of", A2.total)
print("Person:", "His name is", A3.name, "a", A3.gender, "and he is ", A3.status)
print("Register:", A4.student, "checked into the hall at", A4.check_in, "and checked out of the hall at", A4.check_out)
print("Product:", A5.product_name, A5.price, "USD,", A5.quantity, "in stock")
