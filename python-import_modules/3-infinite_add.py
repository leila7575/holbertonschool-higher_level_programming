#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    args_list = sys.argv[1:]
    result = sum(int(arg) for arg in args_list)
    print(result)
