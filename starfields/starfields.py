import random

stars= ['✫', '✹', '✵', '✦', '✧']
small_stars = [ '.', '*', '·', '⊹', '˚', '+'] 
max_chars = 140 #for twitter
starfield = []
row_size = 28
index = 0

'''
integers from -15 to 0 will be a space
integers from 1 to 5 will be a small star
integer 6 will be a big star
'''

print ("generating starfield...")

for char in range(max_chars):
    star = " " 
    isStar = random.randint(-20, 5)
    if isStar == 5:
        star = random.choice(stars)
    if isStar in [1, 2, 3, 4]:
        star = random.choice(small_stars)
        
    starfield.append(star) 

for row in range(5):
    star = index 
    line = [] 
    for star in range(row_size):
        line.append(starfield[star + index])
    print (''.join(line)) 
    index += 28 
