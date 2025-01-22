def main():
    print(square_root(2,0.0001))
    
def square_root(x, E = 0.1):
    x=float(x)
    left = 0.0
    right = max(1.0, x)
    mid = (left+right)*0.5
    while (abs(mid*mid-x) >= E):
        mid = (left+right)*0.5 
        if (mid*mid < x):
            left = mid
        if (mid*mid > x):
            right = mid
    return mid

main()