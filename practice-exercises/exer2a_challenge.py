# Functions to manipulate global variable count

count = 0

###################################################
# Student should enter function on the next lines.
# Reset global count to zero.
# Increment global count.
# Decrement global count.
# Print global count.

def reset():
    global count
    count = 0
    print count
    
def increment():
    global count
    count += 1   
    print count
    
def decrement():
    global count
    count -= 1
    print count

def print_count():
    global count
    print count
    
###################################################
# Test

# note that the GLOBAL count is defined inside a function
reset()		
increment()
print_count()
increment()
print_count()
reset()
decrement()
decrement()
print_count()

####################################################
# Output
#1
#2
#-2