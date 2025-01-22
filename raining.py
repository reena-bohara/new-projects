import time

rain=input("is it raining?\n") .lower()

while True:
    if(rain == 'yes' or rain == 'no'):
            if (rain =='yes'):
                umbrella = input("do you have umbrella?\n") .lower()
                if(umbrella == 'yes' or umbrella == 'no'):
                     if (umbrella == 'yes'): 
                         #rain = 'no'
                         print("you can go outside!")
                         break
                     else:
                         #print("wait for a while")
                        for i in range(5,0,-1):
                            print("wait for %d seconds" % (i))
                            time.sleep(1)
                        rain = input("is it still raining\n").lower()
                        if (rain== 'no'):
                             print("you can go outside")
                             break
    else:
            print("error: please type only 'yes' or 'no' as your input\n")
            #break
  
else:
    print("error: please type only 'yes' or 'no' as your input")
    rain = input("is it raining?\n".lower())


