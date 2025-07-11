day, night, goal = map(int, input().split())

if goal <= day:
    print(1)  
else:
    location = goal - day  
    one_day = day - night  
    
    result = (location + one_day - 1) // one_day
    print(1 + result)  