number_of_months = 0

while number_of_months <= 12:
   number_of_months = int(input("Enter month number: "))
   print(f'{number_of_months}' + " is: ")
   if number_of_months == 0:
      print("Invalid month! please enter a number between 1-12 : ")
   match number_of_months:
         case 1 :
            print("January")
         case 2 :
            print("February")
         case 3 :
            print("March")
         case 4 :
            print("April")
         case 5 :
            print("May")
         case 6 :
            print("June")
         case 7 :
            print("July")
         case 8 :
            print("August")
         case 9 :
            print("September")
         case 10 :
            print("October")
         case 11 :
            print("November")
         case 12 :
            print("December")
else: 
   print("Invalid month! Goodbay")
   

      


 
  
        
    
        
        
    
    