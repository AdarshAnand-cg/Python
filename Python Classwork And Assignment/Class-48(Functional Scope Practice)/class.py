message = "global"
def function():
    global message
    print(message)   #1st print
    message = "nonlocal"
    print(message)  #2nd Print
    def inner():
        global message
        print(message)  #3rd Print
        message = "local"
        print(message)   #4th Print
    inner()
    print(message)       #5th Print
function()
print(message)           #6th Print