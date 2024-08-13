#Variables

pi=3.14
option=0
r=0
l=0
h=0
H=0
a=0
b=0
Surface_area_of_a_cone=0
volume_of_a_cone=0
base_area_of_a_cone=0
Volume_of_rectangular_pyramid=0
Surface_area_of_Pyramid=0
need_to_continue= True


#Ask question(repeat)
while (need_to_continue):
    
    
#Main Menu
    
    print("")
    print("SHAPES CALCULATOR")
    print("")
    print("1.Calculate surface area of cone")
    print("2.Calculate volume of cone")
    print("3.Calculate base area of cone")
    print("4.Calculate volume of a rectangular pyramid")
    print("5.Calculate surface area of rectangular pyramid")
    print("")

    option=int(input("Enter your preffered option:"))

#option1

    if option==1:
        print("")
        r=float(input("Enter the radius in centimeters:"))
        if (r<=0):
            print("")
            print("Radius value can not be negative or zero.")
            need_to_continue= True if str(input("Do you need to continue? (yes/no)")) == "yes" else False
            continue


        print("")
        l=float(input("Enter the slant height in centimeters:"))
        if (l<=0):
            print("")
            print("slant height value can not be negative or zero.")
            need_to_continue= True if str(input("Do you need to continue? (yes/no)")) == "yes" else False
            continue

        print("")
        Surface_area_of_a_cone=pi*r**2+pi*r*l
        print("Surface area of a cone is",Surface_area_of_a_cone,"cm")


#option2    
        
    if option==2:
        print("")
        r=float(input("Enter the radius in centimeters:"))
        if (r<=0):
            print("")
            print("Radius value can not be negative or zero.")
            need_to_continue= True if str(input("Do you need to continue? (yes/no)")) == "yes" else False
            continue


        print("")
        h=float(input("Enter the height in centimeters:"))
        if (h<=0):
            print("")
            print("Height value can not be negative or zero.")
            need_to_continue= True if str(input("Do you need to continue? (yes/no)")) == "yes" else False
            continue

        print("")
        volume_of_a_cone=1/3*pi*r**2*h
        print("volume of a cone is",volume_of_a_cone,"cm")


#option3

    if option==3:
        print("")
        r=float(input("Enter the radius in centimeters:"))
        if (r<=0):
            print("")
            print("Radius value can not be negative or zero.")
            need_to_continue= True if str(input("Do you need to continue? (yes/no)")) == "yes" else False
            continue
        print("")
        base_area_of_a_cone=pi*r**2
        print("base area of a cone is",base_area_of_a_cone,"cm")

#option4

    if option==4:
        print("")
        H=float(input("Enter the height in centimeters:"))
        if (H<=0):
            print("")
            print("height value can not be negative or zero.")
            need_to_continue= True if str(input("Do you need to continue? (yes/no)")) == "yes" else False
            continue


        print("")
        a=float(input("Enter the a base edge in centimeters:"))
        if (a<=0):
            print("")
            print("a base edge value can not be negative or zero.")
            need_to_continue= True if str(input("Do you need to continue? (yes/no)")) == "yes" else False
            continue

        print("")
        b=float(input("Enter the b base edge in centimeters:"))
        if (b<=0):
            print("")
            print("b base edge value can not be negative or zero.")
            need_to_continue= True if str(input("Do you need to continue? (yes/no)")) == "yes" else False
            continue

        print("")
        Volume_of_rectangular_pyramid=a*b*H/3
        print("volume of a rectangular pyramid is",Volume_of_rectangular_pyramid,"cm")

#option5
        
    if option==5:
        print("")
        H=float(input("Enter the height in centimeters:"))
        if (H<=0):
            print("")
            print("height value can not be negative or zero.")
            need_to_continue= True if str(input("Do you need to continue? (yes/no)")) == "yes" else False
            continue


        print("")
        a=float(input("Enter the a base edge in centimeters:"))
        if (a<=0):
            print("")
            print("a base edge value can not be negative or zero.")
            need_to_continue= True if str(input("Do you need to continue? (yes/no)")) == "yes" else False
            continue

        print("")
        b=float(input("Enter the b base edge in centimeters:"))
        if (b<=0):
            print("")
            print("b base edge value can not be negative or zero.")
            need_to_continue= True if str(input("Do you need to continue? (yes/no)")) == "yes" else False
            continue

        print("")
        Surface_area_of_Pyramid=a*b+(a*(b/2)**2+(H**2)**1/2+(b*(a/2)**2+(H**2))**1/2)
        print("Surface area of a Pyramid is",Surface_area_of_Pyramid,"cm")

#Ask to COntinue (repeat)     

    print("")
    need_to_continue= True if str(input("Do you need to continue? (yes/no)")) == "yes" else False
