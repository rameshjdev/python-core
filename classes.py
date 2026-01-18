import json

class Employee:


    def __init__(self, first_name, last_name, age, designation):
        
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.designation = designation
        self.email = first_name + '.' + last_name + '@gmail.com'
        

    def designation_level(self):
        designation_list = ["Software Developer", "Software Engineer",
                         "UI Developer", "QA Engineer", "Scrum Master", "Product Owner"]
        
        if self.designation in designation_list:
            return True


emp1 = Employee('John', 'Carpenter', 34, 'Software Developer')

# Convert into a JSON string
json_string = json.dumps(emp1.__dict__) # Using indent for pretty-printing

print(json_string)
print(Employee.designation_level(emp1))