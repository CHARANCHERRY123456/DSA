def two_distances(c1 , c2):
    '''
    find the distance between two given character in the clock wise direction
    and also anti clock wise direction in a cicrculat alpahbet
    '''
    clock = (ord(c2) - ord(c1)) % 26
    anti = (ord(c1) - ord(c2)) % 26
    print(f"distance between {c1} and {c2} in clock and antiClock :",clock , anti)
    return [clock , anti]

c1 , c2 = "a" , "b"
ans = [1,25]
print(ans == two_distances(c1=c1 , c2=c2))