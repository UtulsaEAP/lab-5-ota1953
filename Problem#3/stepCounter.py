def feet_to_steps(user_feet):
   user_feet =  int(user_feet//2.5)
   print (user_feet)

if __name__ == '__main__':
    #take input feet steps here
    steps_taken = float(input())
    #store it into the function
    feet_to_steps(steps_taken)
    #print your steps here