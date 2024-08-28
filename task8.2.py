old=int(input("enter num of old bread"))
fresh=int(input("enter num of fresh bread"))
def mon(old,fresh):
    frsh=3.49*fresh
    oldd=(3.49*old)%6
    total=frsh+oldd
    print(f"the fresh bread costs {frsh}")
    print(f"the old bread costs {oldd}")
    print(f"the total is {total}")
mon(old,fresh)