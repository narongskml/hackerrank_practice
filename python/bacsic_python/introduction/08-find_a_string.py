def count_substring(string, sub_string):
    c=0 
    pos=0
    while (pos>=0): 
        pos = string.find(sub_string,pos)
        if (pos==-1):
            break  
        c+=1      
        pos = pos+1
    return c   

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)