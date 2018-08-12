'''
Created on Apr 3, 2018

@author: Sumeet Agrawal
'''


bs = input("Enter number of Blue rubies: ")
rs = input("Enter number of Red rubies: ")
gs = input("Enter number of Green rubies: ")
ys = input("Enter number of Yellow rubies: ")

b = int(bs)
r = int(rs)
g = int(gs)
y = int(ys)

if (b <= 0 and r <= 0 and g <= 0 and y <= 0):
    print("Invalid inputs. At least one of the rubies has to be a positive integer!")
    
if (b > 2000 or r > 2000 or g > 2000 or y > 2000):
    print("Invalid inputs. Too many rubies!")

necklace_ruby_count = 0    
total_rubies = b + r + g + y
print("Total rubies: ", total_rubies)
necklace_list = ['blue','red','green','yellow']
final_necklace = []
x = 0

# Start with Red or Blue rubies if possible
if(b != 0):
    final_necklace.append("blue")
    necklace_ruby_count = necklace_ruby_count + 1
    b = b - 1
elif(r != 0):
    final_necklace.append("red")
    necklace_ruby_count = necklace_ruby_count + 1
    r = r - 1
elif(g != 0):
    final_necklace.append("green")
    necklace_ruby_count = necklace_ruby_count + 1
    g = g - 1
else:
    final_necklace.append("yellow")
    necklace_ruby_count = necklace_ruby_count + 1
    y = y - 1
    
for i in range(1, total_rubies):
#while(necklace_ruby_count <= total_rubies):
    print("values are: ", b, r, g, y)
    if(r <= 1 and b <= 1 and g <= 1 and y <= 1): 
        break
    
    #print("The final necklace looks like this: ", final_necklace)
    current_ruby = necklace_list[x]
    print("The current ruby is: ", current_ruby)
    if(current_ruby == "yellow" and y <= 1):
        pass
    elif(current_ruby == "yellow" and (final_necklace[-1] == "red" or final_necklace[-1] == "green")):
        necklace_ruby_count = necklace_ruby_count + 1
        final_necklace.append(current_ruby)
        y = y - 1
    
    if(current_ruby == "green" and g <= 1):
        pass
    elif(current_ruby == "green" and (final_necklace[-1] == "green" or final_necklace[-1] == "red")):
        necklace_ruby_count = necklace_ruby_count + 1
        final_necklace.append(current_ruby)
        g = g - 1
    
    if(current_ruby == "red" and r <= 1):
        pass
    elif(current_ruby == "red" and (final_necklace[-1] == "blue" or final_necklace[-1] == "yellow")):
        necklace_ruby_count = necklace_ruby_count + 1
        final_necklace.append(current_ruby)
        r = r - 1
        
    if(current_ruby == "blue" and b <= 1):
        pass
    elif(current_ruby == "blue" and (final_necklace[-1] == "blue" or final_necklace[-1] == "yellow")):
        necklace_ruby_count = necklace_ruby_count + 1
        final_necklace.append(current_ruby)
        b = b - 1
    '''
    y = y - 1
    g = g - 1
    r = r - 1
    b = b - 1
    '''
    x = x + 1
    if(x > 3):
        x = 0
          
    '''   
    if(r <= 1 and b <= 1 and g <= 1 and y <= 1): 
        break

    x = x + 1
    if(x > 3):
        x = 0
    #print("The final necklace looks like this: ", final_necklace)
    '''

if(b != 0):
    final_necklace.append("blue")
    necklace_ruby_count = necklace_ruby_count + 1
    
if(r != 0):
    final_necklace.append("red")
    necklace_ruby_count = necklace_ruby_count + 1
    
if(g != 0):
    final_necklace.append("green")
    necklace_ruby_count = necklace_ruby_count + 1
    
if(y != 0):
    final_necklace.append("yellow")
    necklace_ruby_count = necklace_ruby_count + 1
print("The final necklace looks like this: ", final_necklace)
print("Final total rubies in the necklace would be: ", necklace_ruby_count)