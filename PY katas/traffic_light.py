"""You're writing code to control your town's traffic lights. You need a function to handle each change from green, to yellow, to red, and then to green again.

Complete the function that takes a string as an argument representing the current state of the light and returns a string representing the state the light should change to.

For example, when the input is green, output should be yellow."""

def update_light1(current):
    if current == 'green':
        return 'yellow'
    elif current =='yellow':
        return 'red'
    else:
        return 'green'

def update_light(current):
    current= input()    
    return {'green': 'yellow' ,'yellow': 'red' ,'red': 'green' } [current] 
 

def update_light(current):
    light_order = {'red':'green', 'yellow':'red', 'green':'yellow'}
    
    return light_order[current]
 

def update_light(current):
    color = ['green', 'yellow', 'red']
    return color[(color.index(current)+1)%len(color)]


