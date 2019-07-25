def string_to_array(s):
    
    if s == '\0':
        arr = ['\0']
    else:
        arr = s.split()
    return arr

print(string_to_array("\0"))