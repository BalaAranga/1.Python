class MultiFunctionCall():
    def Subfields():
        print("Sub-fields in AI are:")
        print("Machine Learning")
        print("Neural Networks")
        print("Vision")
        print("Robotics")
        print("Speech Processing")
        print("Natural Language Processing")
    def OddEven():
        Num = int(input("Enter a number: "))
        if(Num%2 == 0):
            print(Num,"is Even number")
        else:
            print(Num,"is Odd number")
    def Elegible():
        Gender = input("Your Gender:")
        Age = int(input("Your Age:"))
        if(Gender.lower()=="male"):
            if(Age>21):
                print("ELIGIBLE")
                message = "ELIGIBLE"           
            else:
                print("NOT ELIGIBLE")
                message = "NOT ELIGIBLE"
        elif(Gender.lower()=="female"):
            if(Age>18):
                print("ELIGIBLE")
                message = "ELIGIBLE"
            else:
                print("NOT ELIGIBLE")
                message = "NOT ELIGIBLE"
        else:
            print("ENTER YOUR GENDER......")
        return message
    def percentage():
        Subject1= int(input("Subject1= "))
        Subject2= int(input("Subject2= "))
        Subject3= int(input("Subject3= "))
        Subject4= int(input("Subject4= "))
        Subject5= int(input("Subject5= "))
        Total = (Subject1+Subject2+Subject3+Subject4+Subject5)
        print("Total : ",Total)
        Percentage = (Total/500)*100
        print("Percentage : ",Percentage)
        return Subject1,Subject2,Subject3,Subject4,Subject5,Total,Percentage
    def triangle():
        Height = int(input("Height:"))
        Breadth = int(input("Breadth:"))
        print("Area formula: (Height*Breadth)/2")
        Area = (Height*Breadth)/2
        print("Area of Triangle: ",Area)
        Height1 = int(input("Height1:"))
        Height2 = int(input("Height2:"))
        Breadth1 = int(input("Breadth:"))
        print("Perimeter formula: Height1+Height2+Breadth")
        Perimeter = Height1+Height2+Breadth1
        print("Perimeter of Triangle: ",Perimeter)
        return Height,Breadth,Area,Height1,Height2,Breadth1,Perimeter
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    