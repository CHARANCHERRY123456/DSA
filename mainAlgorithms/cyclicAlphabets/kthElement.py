# question : 
def kthElement(start_char, k):
    '''
    find the kth element from given character in clockwise and anticlockwise direction 
    in a circular alphabets
    '''
    first = chr((ord(start_char) - ord('a') + k)%26 + ord('a'))
    second = chr((ord(start_char) - ord('a') - k)%26 + ord('a'))
    print(f"{k} th character from '{start_char}' on clock and anticlock is =" ,first , second)
    return [first , second]

# Example Usage
start_char = 'a'
k = 26

def scanInput():
    start_char = input("Enter the startign character :")
    k = int(input("Enter the k value "))
    return start_char , k
start_char , k = scanInput()
kthElement(start_char , k)
