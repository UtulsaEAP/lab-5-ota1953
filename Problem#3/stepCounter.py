def feet_to_steps(user_feet):
   steps_taken = int(user_feet//2.5)
   print (steps_taken)

if __name__ == '__main__':
    #take input feet steps here
    user_feet = float(input())
    #store it into the function
    feet_to_steps(user_feet)
    #print your steps here