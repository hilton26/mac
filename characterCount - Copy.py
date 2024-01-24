message ='It was a bright cold day in April, and the cloecks were striking thirteen'
count={} # e.g. 'r': 12

for character in message:
    count.setdefault(character,0)
    count[character]=count[character]+1

print(count)

