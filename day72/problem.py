def find_leap_years(given_year):
    list_of_leap_years=[]
    # Write your logic her
    count=0
    for i in range(1,64):
        if(given_year%400==0):
            list_of_leap_years.append(given_year)
            count+=1
        elif(given_year%100==0):
            j=0           
        elif(given_year%4==0):
             list_of_leap_years.append(given_year)
             count+=1
        else:
            j=0
        if(count==15):
            break
        given_year=given_year+1
    return list_of_leap_years
list_of_leap_years=find_leap_years(2002)
print(list_of_leap_years)
