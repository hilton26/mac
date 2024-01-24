def isPhoneNumber(text):
    if len(text) != 12:
        return False
    for i in range(0,3):  
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
            return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-': # missing second dash
        return False
    for i in range(8,12):
        if not text[i].isdecimal():
            return False # missing last four digits
    return True





message = 'Call me at 415-555-7543 tomorrow, or at 417-555-8932 at my office line.'
foundNumber = False
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Found phone number: ' + chunk)
        foundNumber = True
if not foundNumber:
    print('Could not find any phone numbers')
    
        
            
