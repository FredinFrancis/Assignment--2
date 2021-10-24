print("\n")
print("**** Program of Shopping ****")
print("Shop at your own Convenience")
print("\n")
print( "Welcome to Abbys's Merchandizing !!")
print("\n")
name = str(input("Enter your name:- "))
age = int(input("Age:-"))
print("\n")
come= int(input("Press any number to enter to site:- "))

#loop start

while(come>= 1):

    print("Please choose your desired selection: ")
    print("1. Polo Shirts")
    print("2. Jackets")
    print("\n")
    i=int(input("Enter your Selection:- "))
    print("\n")
    if(i==1):
        print("Select your desired one from below: ")
        print("1. Item Name :   Amel Polo T-Shirt")
        print("   Size      :   XL")
        print("   Colour    :   Blue")
        print("   Price     :   $ 14 CAD")
        print("\n")
        print("2. Item Name :   Arvind Polo T-Shirt")
        print("   Size      :   XL")
        print("   Colour    :   Red")
        print("   Price     :   $ 15 CAD")
        print("\n")
        
        polo=int(input("Enter your selection:- "))
        if (polo==1):
            qty1= int(input("Please enter your required quantity:- "))
            rate=14
            hstrate=1.13
            netprice1=rate*qty1
            hst1=netprice1*hstrate
            hst=hst1-netprice1
            total=netprice1+hst

            print("\n")
            print("Confirm your order !")
            print("Type of Shirt- Polo Shirt")
            print("Quantity- "+ str(qty1))

            cust=str(input(" If Student/ Senior Citizen, Enter Y/N :- "))
            print("\n")
            if(cust == 'Y' or 'y'):
                if(age <= 21):
                        studis= (netprice1*10)/100
                        newnetp=netprice1-studis
                        print("Student Discount 10% Applied !")
                        print("Taxable Value = $ %.2f" % (newnetp))
                        newmark=(newnetp*13)/100
                        print("HST @ 13 = $ %.2f " % (newmark))
                        total1=newnetp+newmark
                        print("Total Price = $ %.2f" % (total1))
                elif(age >= 60):
                        studis= (netprice1*10)/100
                        newnetp=netprice1-studis
                        print("Senior Citizen Discount 10% Applied !")
                        print("Taxable Value = $ %.2f" % (newnetp))
                        newmark=(newnetp*13)/100
                        print("HST @ 13 = $ %.2f " % (newmark))
                        total1=newnetp+newmark
                        print("Total Price = $ %.2f" % (total1))
                elif(qty1>=3) and (cust != 'Y' or 'y'):
                        studis= (netprice1*15)/100
                        newnetp=netprice1-studis
                        print("Discount 15% Applied !")
                        print("Taxable Value = $ %.2f" % (newnetp))
                        newmark=(newnetp*13)/100
                        print("HST @ 13 = $ %.2f " % (newmark))
                        total1=newnetp+newmark
                        print("Total Price = $ %.2f" % (total1))
                else:
                        print("\n")
                        print("Confirm your order !")
                        print("Type of Shirt- Polo Shirt")
                        print("Quantity- "+ str(qty1))
                        print("Taxable Value = $ %.2f" % (netprice1))
                        print("HST @ 13 = $ %.2f" % (hst))
                        print("Total Price = $ %.2f" % (total))


            confirm=int(input("Press 1 to Confirm / Press 0 to exit: "))
            if(confirm==1):
                print("\n")
                print("Order confirmed !")
                value = int(input("Press 1 for Main menu / Press 0 to exit: "))
                if(value == 0):
                    print("Thanks for shopping with Abby's Merchandizing ! \n Come Again !!!!!!!!")
                    break
                else:
                    print("Order Not Confirmed !")
                     

                if(value ==0):
                    print("Thanks for shopping with Abby's Merchandizing ! \n Come Again !!!!!!!!")
                
        if (polo==2):
            qty1= int(input("Please enter your required quantity:- "))
            rate=15
            hstrate=1.13
            netprice1=rate*qty1
            hst1=netprice1*hstrate
            hst=hst1-netprice1
            total=netprice1+hst

            print("\n")
            print("Confirm your order !")
            print("Type of Shirt- Polo Shirt")
            print("Quantity- "+ str(qty1))

            cust=str(input(" If Student/ Senior Citizen, Enter Y/N :- "))
            print("\n")
            if(cust == 'Y' or 'y'):
                if(age <= 21):
                        studis= (netprice1*10)/100
                        newnetp=netprice1-studis
                        print("Student Discount 10% Applied !")
                        print("Taxable Value = $ %.2f" % (newnetp))
                        newmark=(newnetp*13)/100
                        print("HST @ 13 = $ %.2f " % (newmark))
                        total1=newnetp+newmark
                        print("Total Price = $ %.2f" % (total1))
                elif(age >= 60):
                        studis= (netprice1*10)/100
                        newnetp=netprice1-studis
                        print("Senior Citizen Discount 10% Applied !")
                        print("Taxable Value = $ %.2f" % (newnetp))
                        newmark=(newnetp*13)/100
                        print("HST @ 13 = $ %.2f " % (newmark))
                        total1=newnetp+newmark
                        print("Total Price = $ %.2f" % (total1))
                elif(qty1>=3) and (cust != 'Y' or 'y'):
                        studis= (netprice1*15)/100
                        newnetp=netprice1-studis
                        print("Discount 15% Applied !")
                        print("Taxable Value = $ %.2f" % (newnetp))
                        newmark=(newnetp*13)/100
                        print("HST @ 13 = $ %.2f " % (newmark))
                        total1=newnetp+newmark
                        print("Total Price = $ %.2f" % (total1))
                else:
                        print("\n")
                        print("Confirm your order !")
                        print("Type of Shirt- Polo Shirt")
                        print("Quantity- "+ str(qty1))
                        print("Taxable Value = $ %.2f" % (netprice1))
                        print("HST @ 13 = $ %.2f" % (hst))
                        print("Total Price = $ %.2f" % (total))


            confirm=int(input("Press 1 to Confirm / Press 0 to exit: "))
            if(confirm==1):
                print("\n")
                print("Order confirmed !")
                value = int(input("Press 1 for Main menu / Press 0 to exit: "))
                if(value == 0):
                    print("Thanks for shopping with Abby's Merchandizing ! \n Come Again !!!!!!!!")
                    break
                else:
                    print("Order Not Confirmed !")
                if(value ==0):
                    print("Thanks for shopping with Abby's Merchandizing ! \n Come Again !!!!!!!!")     

    if(i==2):
        print("Select your desired one from below: ")
        print("1. Item Name :   Roadster")
        print("   Size      :   XXL")
        print("   Colour    :   Black")
        print("   Price     :   $ 20 CAD")
        print("\n")
        print("2. Item Name :   Raymond Brown Black")
        print("   Size      :   XL")
        print("   Colour    :   Brwon with White Border")
        print("   Price     :   $ 28 CAD")
        print("\n")
        
        polo=int(input("Enter your selection:- "))
        if (polo==1):
            qty1= int(input("Please enter your required quantity:- "))
            rate=20
            hstrate=1.13
            netprice1=rate*qty1
            hst1=netprice1*hstrate
            hst=hst1-netprice1
            total=netprice1+hst

            print("\n")
            print("Confirm your order !")
            print("Type of Shirt- Polo Shirt")
            print("Quantity- "+ str(qty1))

            cust=str(input(" If Student/ Senior Citizen, Enter Y/N :- "))
            print("\n")
            if(cust == 'Y' or 'y'):
                if(age <= 21):
                        studis= (netprice1*10)/100
                        newnetp=netprice1-studis
                        print("Student Discount 10% Applied !")
                        print("Taxable Value = $ %.2f" % (newnetp))
                        newmark=(newnetp*13)/100
                        print("HST @ 13 = $ %.2f " % (newmark))
                        total1=newnetp+newmark
                        print("Total Price = $ %.2f" % (total1))
                elif(age >= 60):
                        studis= (netprice1*10)/100
                        newnetp=netprice1-studis
                        print("Senior Citizen Discount 10% Applied !")
                        print("Taxable Value = $ %.2f" % (newnetp))
                        newmark=(newnetp*13)/100
                        print("HST @ 13 = $ %.2f " % (newmark))
                        total1=newnetp+newmark
                        print("Total Price = $ %.2f" % (total1))
                elif(qty1>=3) and (cust != 'Y' or 'y'):
                        studis= (netprice1*15)/100
                        newnetp=netprice1-studis
                        print("Discount 15% Applied !")
                        print("Taxable Value = $ %.2f" % (newnetp))
                        newmark=(newnetp*13)/100
                        print("HST @ 13 = $ %.2f " % (newmark))
                        total1=newnetp+newmark
                        print("Total Price = $ %.2f" % (total1))
                else:
                        print("\n")
                        print("Confirm your order !")
                        print("Type of Shirt- Polo Shirt")
                        print("Quantity- "+ str(qty1))
                        print("Taxable Value = $ %.2f" % (netprice1))
                        print("HST @ 13 = $ %.2f" % (hst))
                        print("Total Price = $ %.2f" % (total))


            confirm=int(input("Press 1 to Confirm / Press 0 to exit: "))
            if(confirm==1):
                print("\n")
                print("Order confirmed !")
                value = int(input("Press 1 for Main menu / Press 0 to exit: "))
                if(value == 0):
                    print("Thanks for shopping with Abby's Merchandizing ! \n Come Again !!!!!!!!")
                    break
                else:
                    print("Order Not Confirmed !")
                     

                if(value ==0):
                    print("Thanks for shopping with Abby's Merchandizing ! \n Come Again !!!!!!!!")
                
        if (polo==2):
            qty1= int(input("Please enter your required quantity:- "))
            rate=28
            hstrate=1.13
            netprice1=rate*qty1
            hst1=netprice1*hstrate
            hst=hst1-netprice1
            total=netprice1+hst

            print("\n")
            print("Confirm your order !")
            print("Winter Jacket")
            print("Quantity- "+ str(qty1))

            cust=str(input(" If Student/ Senior Citizen, Enter Y/N :- "))
            print("\n")
            if(cust == 'Y' or 'y'):
                if(age <= 21):
                        studis= (netprice1*10)/100
                        newnetp=netprice1-studis
                        print("Student Discount 10% Applied !")
                        print("Taxable Value = $ %.2f" % (newnetp))
                        newmark=(newnetp*13)/100
                        print("HST @ 13 = $ %.2f " % (newmark))
                        total1=newnetp+newmark
                        print("Total Price = $ %.2f" % (total1))
                elif(age >= 60):
                        studis= (netprice1*10)/100
                        newnetp=netprice1-studis
                        print("Senior Citizen Discount 10% Applied !")
                        print("Taxable Value = $ %.2f" % (newnetp))
                        newmark=(newnetp*13)/100
                        print("HST @ 13 = $ %.2f " % (newmark))
                        total1=newnetp+newmark
                        print("Total Price = $ %.2f" % (total1))
                elif(qty1>=2) and (cust != 'Y' or 'y'):
                        studis= (netprice1*15)/100
                        newnetp=netprice1-studis
                        print("Discount 15% Applied !")
                        print("Taxable Value = $ %.2f" % (newnetp))
                        newmark=(newnetp*13)/100
                        print("HST @ 13 = $ %.2f " % (newmark))
                        total1=newnetp+newmark
                        print("Total Price = $ %.2f" % (total1))
                else:
                        print("\n")
                        print("Confirm your order !")
                        print("Winter Jacket")
                        print("Quantity- "+ str(qty1))
                        print("Taxable Value = $ %.2f" % (netprice1))
                        print("HST @ 13 = $ %.2f" % (hst))
                        print("Total Price = $ %.2f" % (total))


            confirm=int(input("Press 1 to Confirm / Press 0 to exit: "))
            if(confirm==1):
                print("\n")
                print("Order confirmed !")
                value = int(input("Press 1 for Main menu / Press 0 to exit: "))
                if(value == 0):
                    print("Thanks for shopping with Abby's Merchandizing ! \n Come Again !!!!!!!!")
                    break
                else:
                    print("Order Not Confirmed !")
                if(value ==0):
                    print("Thanks for shopping with Abby's Merchandizing ! \n Come Again !!!!!!!!")
                
                

    


        





