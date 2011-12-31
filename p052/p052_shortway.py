from func_time import func_time

def f(n):
    return set(str(n))

@func_time
def ff():
    return [n for n in range(1,1000000) if f(n)==f(n*2)==f(n*3)==f(n*4)==f(n*5)==f(n*6)]

if __name__ == "__main__":
    print ff()
