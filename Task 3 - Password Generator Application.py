from streamlit import *
from random import *
from string import *

def pwgen(length):
    char=ascii_letters+digits+punctuation
    password=''.join(choice(char) for i in range(length))
    return password

def main():
    title("Password Generator")
    length=slider("Select desired length for the password",min_value=1,max_value=100,value=12)
    if button("Generate password"):
        password=pwgen(length)
        success(f"Generated Password: {password}")

if __name__=="__main__":
    main()