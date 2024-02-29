#Owen Anderson THUR 2:00-3:15
def kilo_to_pounds(kilos):
    # This statement intentionally has an error. 
    return (kilos * 2.204)


# Main part of the program starts here. Do not remove the line below.
if __name__ == '__main__':
    kilos = float(input())
    
    pounds = kilo_to_pounds(kilos)
    print(f'{pounds:.3f} lbs')