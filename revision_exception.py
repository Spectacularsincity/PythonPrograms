a=5
b=0
try:
    print("resource opened") #this resouce is metaphorical as it represents a file or a database connections.
    print(a/b)

except ZeroDivisionError as e:
    print("hey u cannot divide number by zero" , e)

except ValueError as e:
    print("invalid output")

except Exception as e:
    print("Something went wrong")

finally:
    print("resource closed")

