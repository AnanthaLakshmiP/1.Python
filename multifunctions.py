list=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
class multifunctions():
    def Subfields():
        print("Sub-fields in AI are:")
        for x in list:
            print(x)
            
            
    def OddEven():
        num=int(input("Enter a number:"))
        if (num%2)==0:
            print(num,"is Even number")
            message="Even number"
        
        else:
            print(num,"is odd number")
            message="odd number"
            return meassage
        
    def Eligible():
        name=input("Your Gender:")
        age=int(input("Your Age:"))
        if (age<25):
            print("NOT ELIGIBLE")
            message="NOT ELIGIBLE"
        
        else:
            print("ELIGIBLE")
            message="ELIGIBLE"
            return meassage
        
        
    def percentage():
        mark=int(input("Subject1="))
        mark=int(input("Subject2="))
        mark=int(input("Subject3="))
        mark=int(input("Subject4="))
        mark=int(input("Subject5="))
        add=Subject1+Subject2+Subject3+Subject4+Subject5
        print("Total:",add)
        per=add/5
        print("Percentage:",per)
        
    def triangle():
        H=int(input("Height:"))
        B=int(input("Breadth:"))
        print("Area Formula: Height*Breadth/2")
        f=(Height*Breadth)/2
        print("Area of Formula:",f)
        H=int(input("Height1:"))
        H=int(input("Height2:"))
        B=int(input("Breadth:"))
        print("Perimeter Formula:Height1+Height2+Breadth2")
        add=Height1+Height2+Breadth2
        print("Perimeter of Triangle:",add)