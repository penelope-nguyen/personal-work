# VERSION 1.4
# PURPOSE: Given a list of numbers, function returns the start and end position of the continguous set with the largest sum.
# List of numbers can contain 0, negative numbers, or positive numbers.
# This function works by comparing every permutation of the list to find the largest sum. 
# It will not repeat sets so its runtime is O(n!), n being the size of the list. 

def max_cont (num_set):
    
    size = len(num_set)
    current_total = None 
    max_pos = []
    total = -float('inf')
    
    for pos in range(size):
        
        end_pos = size - 1 
    
        while end_pos >= pos:
            
            current_total = sum(num_set[pos:end_pos + 1])
            
            if current_total > total:
                total = current_total
                max_pos = (pos, end_pos)
                
            end_pos -= 1
        
    return (max_pos, total) 

test = [-4, 0, 2, 4, -2, -3, 5, 1]
test2 = [-2, -19, -4, -1, -2, -5]
test3 = [0, 0, 0, 0]
test4 = [-1, 0, 0, -4]
test5 = [-1, 0, 1, -4]
test6 = [-3]

print(max_cont(test), "// test:", test)
print(max_cont(test2), "// test:", test2)
print(max_cont(test3), "// test:", test3)
print(max_cont(test4), "// test:", test4)
print(max_cont(test5), "// test:", test5)
print(max_cont(test6), "// test:", test6)

"""

//////
OUTPUT
//////

([1, 7], 7) // test: [-4, 0, 2, 4, -2, -3, 5, 1]
([3, 3], -1) // test: [-2, -19, -4, -1, -2, -5]
([0, 3], 0) // test: [0, 0, 0, 0]
([1, 2], 0) // test: [-1, 0, 0, -4]
([1, 2], 1) // test: [-1, 0, 1, -4]
([0, 0], -3) // test: [-3]

""" 

"""
/// BEWARE: DOWN BELOW ARE PROTOTYPES OF THIS FUNCTION /// 

///////////
VERSION 1.1 
///////////

def max_cont(num_set):
    #num_list = []
    #pos_list = []
    current_set = []
    set_list = [] 
    pos = 0
    totals_list = []
    total = 0 
    for num in num_set:
        '''
        If there is no current subset, and the number is not negative, add it to the current subset
        '''
        pos += 1 
        if not current_set: 
            if num >= 0:     
                current_set.append(num)
                current_pos = [pos] 
            continue
        '''
        If there is a current subset, and the number is negative, end the subset.
        '''
        if num < 0:
            num_list.append(current_set)
            current_set = [] 
            current_pos.append(end)
            pos_list.append(current_pos)
            current_pos = [] 
        else: 
            end = pos 
            current_set.append(num)
    if current_set:
        pos_list.append(current_pos)
        num_list.append(current_set)
        
 ///////////
 VERSION 1.2 
 ///////////
 
        if num < 0:
            if current_set: 
                num_list.append(current_set)
                current_set = [] 
                current_pos.append(end)
                pos_list.append(current_pos)
                current_pos = [] 

        else: 
            current_set.append(num)
            if len(current_set) == 1: 
                current_pos = [pos] 
            else: 
                end = pos 
        if num > max_num: 
            max_num = num
            max_pos = pos 
    if current_pos:
        num_list.append(current_set)
        current_pos.append(end)
        pos_list.append(current_pos)
        if num < 0:
            if current_set: 
                current_set.append(end)
                set_list.append(current_set) 
                current_set = [] 
                totals_list.append(total)
                total = 0

        else: 
            if not current_set: 
                current_set = [pos]
            total += num  
            end = pos 
        pos +=1
    if current_set:
        current_set.append(end)
        set_list.append(current_set)
        totals_list.append(total)

    
    if not set_list:
        max_pos = num_set.index(max(num_set))
        return [max_pos, max_pos]          
    
    total_pos = totals_list.index(max(totals_list))
    return set_list[total_pos]
  

test = [-4, 0, 1, 4, -2, -3, 5, 1]
test2 = [-2, -19, -4, -1, -2, -5]
test3 = [0, 0, 0, 0]
test4 = [-1, 0, 0, -4]
test4 = [-1, 0, 1, -4]
test5 = [-3]
print(max_cont(test))
print(max_cont(test2))
print(max_cont(test3))
print(max_cont(test4))
print(max_cont(test5))


""" 
""" 
///////////
VERSION 1.3
///////////
def max_cont(num_set):

    current_set = [] # current_set is a list of the start and end position of a contiguous non-negative set 
    set_list = []    # set_list stores all the non-negative sets 
    pos = 0          # the position of the current number 
    total = 0        # stores the total of the current_set
    totals_list = [] 

    for num in num_set:

        # If the number is positive, then it needs to be added to a set. 
        # If the set is empty, then current number's position is the starting and ending positions of a new set. 
        # If the set is not empty, the current number's position is the ending position of a new set. 
        # The number will then be added to the total. 

        if num > 0: 
            if not current_set: 
                current_set = [pos]
            end = pos 
            total += num  

        # If the number is negative and there is no set,  move on to the next number.
        # If there is a set, then current_set has already stored the starting positon. We will add the end position to current_set. 
        # After adding current_set and total to their respective lists, reset the current_set and total. 
         
        else:
            if current_set: 
                current_set.append(end)
                set_list.append(current_set) 
                current_set = [] 
                totals_list.append(total)
                total = 0

        pos +=1
    

    # If the last number is positive, then the if statement in the previous loop will not capture the set it belonged to. 
    # We will close off the last set, by appending the final number's position to current_set and adding that to the list of sets.  

    if current_set:
        current_set.append(end)
        set_list.append(current_set)
        totals_list.append(total)


    # If the numbers given are all negative, then there will not be any set of numbers. 
    # Instead, the position of the largest number will be found and returned. 

    if not set_list:
        max_pos = num_set.index(max(num_set))
        return [max_pos, max_pos]          
    
    # If there are sets, find the largest total of all the sets. The total's position in totals_list will be the same 
    # as the set it belonged to, in the set_list. 
    total_pos = totals_list.index(max(totals_list))
    return set_list[total_pos]
""" 
'''
test = [-4, 0, 2, 4, -2, -3, 5, 1]
test2 = [-2, -19, -4, -1, -2, -5]
test3 = [0, 0, 0, 0]
test4 = [-1, 0, 0, -4]
test5 = [-1, 0, 1, -4]
test6 = [-3]

print(max_cont(test), "// test:", test)
print(max_cont(test2), "// test:", test2)
print(max_cont(test3), "// test:", test3)
print(max_cont(test4), "// test:", test4)
print(max_cont(test5), "// test:", test5)
print(max_cont(test6), "// test:", test6)
'''
""" 

OUTPUT 

[6, 7] // test: [-4, 0, 1, 4, -2, -3, 5, 1]
[3, 3] // test: [-2, -19, -4, -1, -2, -5]
[0, 3] // test: [0, 0, 0, 0]
[1, 2] // test: [-1, 0, 0, -4]
[1, 2] // test: [-1, 0, 1, -4]
[0, 0] // test: [-3]
[Finished in 0.1s]

"""
