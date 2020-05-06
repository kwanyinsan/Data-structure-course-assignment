from josephusm import *

def main():
    print("\n")
    print("\n")
    print("\n")
    print("========= IDSA Assign2 Q2 (Josephus Problem), by Kwan Yin San, 2020 =========")
    print("\nEnter n, total number of people (Integer >1) :    ")
    n = int(input())
    print("\nEnter m, number of counts for each step (Integer >0):    ")
    m = int(input())
    print(f"\n>>> Result of input [{n}] people and [{m}]-counts, starting from 2nd person:\n")
    jose(n, m)
    print("\n")
    print("\n")
    print("\n")
    
main()