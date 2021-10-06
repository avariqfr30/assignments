## Exercise 2 - No 3 ##
def wind_chill_temp():
    ta= int(input("Input outside temprature (F) : "))
    while not -58 < ta < 41 :
        print ("Temprature must be between -58F and 41F")
        ta = int(input("Re-enter temprature (F) : "))
        
    v = int(input("Enter wind speed (mph) : "))
    while v < 2 :
        print("Speed must be greater than or equal to 2")
        v = int(input("Re-enter wind speed (mph) : "))
        
    twc = 35.74 + (0.6215 * ta) - (35.75 * (v**0.16)) + (0.4275 * ta * (v**0.16))
    print ("The wind chill index is", format(twc, '.3f'))
    
    
wind_chill_temp()
####