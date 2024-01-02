n1=float(input("Enter a number:"))
n2=float(input("Enter a nummber:"))

class Calculator:
    def __init__(self,n1,n2):
        self.x=n1
        self.y=n2
    def addition(self):
        return self.x+self.y
    def substraction(self):
        return self.x-self.y
    def multiplication(self):
        return  self.x*self.y
    def division(self):
        return  self.x/self.y  
calculation=Calculator(n1,n2)
    
print("Select Operation")
print("""  1.Addition
           2.Substraction
           3.Multiplication
           4.Division""") 
Select=(int(input("Enter choice of Operation: 1/2/3/4:")))

if Select==1:
    print(calculation.addition())
elif Select==2:
    print(calculation.substraction())
elif Select==3:
    print(calculation.multiplication())
elif Select==4:
    print(calculation.division())
else:
    print("Invalid Input")

