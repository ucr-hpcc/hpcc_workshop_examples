from vars import COLOR
#import vars

## Note the different styles of importing, and how it changes the way we call
## external symbols (functions and variables).

def say_hi():
    print(f"Hello. Today's color is {COLOR}.")
    #print(f"Hello. Today's color is {vars.COLOR}.")
    return
