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
        mark1=int(input("Subject1="))
        mark2=int(input("Subject2="))
        mark3=int(input("Subject3="))
        mark4=int(input("Subject4="))
        mark5=int(input("Subject5="))
        add=mark1+mark2+mark3+mark4+mark5
        print("Total:",add)
        per=add/5
        print("Percentage:",per)
        
    def triangle():
        H=int(input("Height:"))
        B=int(input("Breadth:"))
        print("Area Formula: Height*Breadth/2")
        f=(H*B)/2
        print("Area of Formula:",f)
        H1=int(input("Height1:"))
        H2=int(input("Height2:"))
        B1=int(input("Breadth:"))
        print("Perimeter Formula:Height1+Height2+Breadth2")
        add=H1+H2+B1
        print("Perimeter of Triangle:",add)