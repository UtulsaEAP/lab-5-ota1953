#Owen Anderson THUR 2:00-3:15
def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    drive_cost = (miles_driven/miles_per_gallon)*dollars_per_gallon
    print(f'{drive_cost:.2f}')

if __name__ == '__main__':
    miles_per_gallon = float(input())
    dollars_per_gallon = float(input())
    #print your costs here like example below
    # print(f'{(driving_cost(miles_per_gallon, dollars_per_gallon, 10.0)):.2f}')
    driving_cost(miles_per_gallon, dollars_per_gallon, 10)
    driving_cost(miles_per_gallon, dollars_per_gallon, 50)
    driving_cost(miles_per_gallon, dollars_per_gallon, 400)