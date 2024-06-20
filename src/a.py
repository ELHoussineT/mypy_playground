from sub_folder.b import foo

def boo(x: int, y: int, z: int) -> int: 
    return foo(x, y) - z

if __name__ == "__main__": 
    print(boo(1, 2, 3))