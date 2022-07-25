import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
print("      ___________________  ")
print("  -->|   Data Analysis   |<---")
print("     |     on Garbage    |    ")
print("     |___________________|     ")
dataset = pd.read_csv("data.csv")

print("WELCOME TO Garbage Data Analysis\n")  
  
while True:  
    print("MENU")  
    print("1. Graph of 2007/08")  
    print("2. Graph of 2008/09")  
    print("3. Graph of 2009/10")  
    print("4. Graph of 2010/11")  
    print("5. Graph of 2011/12")  
    print("6. Graph of 2012/13") 
    print("7. Exit")
    users_choice = int(input("\nEnter your Choice: "))  
  
    if users_choice == 1:  
          dataset['2007-08'].value_counts().plot(kind='bar' , figsize=(12,12))
        
  
    elif users_choice == 2:  
        dataset['2008-09'].value_counts().plot(kind='bar' , figsize=(12,12))
       

    elif users_choice == 3:  
        dataset['2009-10'].value_counts().plot(kind='bar' , figsize=(12,12))

  
    elif users_choice == 4:  
        dataset['2010-11'].value_counts().plot(kind='bar' , figsize=(12,12))


    elif users_choice == 5:  
        dataset['2011-12'].value_counts().plot(kind='bar' , figsize=(12,12))
        
    elif users_choice == 6:  
        dataset['2012-13'].value_counts().plot(kind='bar' , figsize=(12,12))
        
    elif users_choice == 7:
        break 
    else:  
        print( "Please enter a valid Input from the list")  