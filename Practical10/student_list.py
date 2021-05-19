#creat the class
class students:
    def __init__(self, first_name, last_name, undergraduate_programme):
        #define some attribute
        self.first_name=first_name
        self.last_name=last_name
        self.undergraduate_programme=undergraduate_programme
    def message(self):
        #put in the introduction operator and method
        print(self.first_name,self.last_name,self.undergraduate_programme)
#example
x=students('Yu','Yue','BMI')
x.message()