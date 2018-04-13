#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for str in dir():
        if str[:2] != "__":
            print("{}".format(str))
