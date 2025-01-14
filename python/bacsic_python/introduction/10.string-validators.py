#In the first line, print True if  has any alphanumeric characters. Otherwise, print False.
#In the second line, print True if  has any alphabetical characters. Otherwise, print False.
#In the third line, print True if  has any digits. Otherwise, print False.
#In the fourth line, print True if  has any lowercase characters. Otherwise, print False.
#In the fifth line, print True if  has any uppercase characters. Otherwise, print False.
s="qA2"

if __name__ == '__main__':
    s = input()
    print(len([c for c in s if c.isalnum()])>0) # alphanumeric
    print(len([c for c in s if c.isalpha()])>0) # alphabetical 
    print(len([c for c in s if c.isdigit()])>0) # isdigit 
    print(len([c for c in s if c.islower()])>0) # lowercase  
    print(len([c for c in s if c.isupper()])>0) # uppercase   