def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def main():
    print("wheeeee")
    t='y'
    while(t=='y'):
        print("add or subtract?")
        x=input()
        print("enter the numbers")
        y=input()
        z=input()
        if( x==1):
            print(add(int(y),int(z)))
        else:
            print(sub(int(y),int(z)))
        print("continue")
        t=input()

main()
        
