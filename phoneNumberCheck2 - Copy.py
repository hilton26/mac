import re # import the Regular Expression module

message = message = 'Call me at 415-555-7543 tomorrow, or at 417-555-892 at my office line.'

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d') # the r (raw string) at the beginning means ignore the backslash escape characters. \d is for a digit numeric character
print(phoneNumRegex.findall(message)) # findall method creates a list of all instances searched for
# mo = phoneNumRegex.search(message) # "mo" for "match object"

# print(mo.group())
  
