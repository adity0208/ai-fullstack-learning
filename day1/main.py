from utils import add, sub, mul, div

def main():
    x=10
    y=20
    z=0
    print(f"Addition of {x} and {y} is {add(x,y)}")

    print(f"Subtraction of {x} and {y} is {sub(x,y)}")

    print(f"Multiplication of {x} and {y} is {mul(x,y)}")

    print(f"Division of {x} and {y} is {div(x,y)}")

    #test divsion error handling
    try:
        print(f"Division of {x} and {z} is {div(x,z)}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
