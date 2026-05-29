#input = list of dicts
#process - aggregates hrs for each employees - loop throught the input and then add the hours 
# for each user - if they are already in the resulting list -if not inthe list we add the hours or defualt to 0 
#if in list add on the extra records hours
#if user["emplyee"] -> if None then continue
#if hours not  
#ouput = dict
records = [
    {"employee": "Alice", "project": "A", "hours": 5},
    {"employee": "Bob", "project": "B", "hours": 3},
    {"employee": "Alice", "project": "C", "hours": 2}
]

def aggregated_employee_hours(records):
    results = {}
    
    if not records:
        return {}
    
    for user in records:
        if "employee" not in user or "hours" not in user:
            continue
        employee_name = user["employee"]
        employee_hours = user["hours"]
    
        if not isinstance(employee_hours, (int,float)) or employee_hours is None:
            continue
        results[employee_name] = results.get(employee_name,0) + employee_hours
    return results
    
# print(aggregated_employee_hours(records))

        #l            #r
nums = [[1,1],[1],[1,1]]

#input of sorted arrays 
#process -> loop through all the lists and then loop through the elements of each list 
#we can just add to a new list and then srt the new list 
#output is combined sorted array

# have 2 pointers which start at the beginnign of the inner lists and compare which is greater
#if the right greate then we apend to a new array if left we appened to the new array
#and then we move the pointers
#case- where the list could be shorter -> have a runign loop that apends the left overs

def sort_merge(nums):
    #edges case when list is empty
    merged_results = []
    
    if not nums:
        return []
    
    l_pointer, r_pointer = 0,0
    left_list = nums[0]
    right_list = nums[len(nums)-1]
    
    while l_pointer < len(left_list) and r_pointer < len(right_list):
        # for when both lists are of equal length
        if left_list[l_pointer] >= right_list[r_pointer]:
            merged_results.append(right_list[r_pointer])
            r_pointer += 1
            
        else:
            merged_results.append(left_list[l_pointer])
            l_pointer += 1

        
        #for when there is left overs
        
    while l_pointer < len(left_list):
        merged_results.append(left_list[l_pointer])
        l_pointer += 1
    
    while r_pointer < len(right_list):
        merged_results.append(right_list[r_pointer])
        r_pointer += 1
        
    return merged_results


            

    
    
    
    #O(n)
#     for lists in nums:
#         for numbers in lists:
#             merged_results.append(numbers)
#     return sorted(merged_results)
# #O(nlogn)
# print(sort_merge(nums))


left = [1, 2, 2, 3, 4]
right = [2, 2, 4, 4]
# expected output
[2, 4]

#input - 2 sorted arrays
#brute force - add left array to a counter hashmap (dict)
# then check if the elements of the right array are in the left:
# append then to a results list
#if not:
#continue 
#ouput - sorted array containing elements that appear in both lists

def find_common_elements(left_arr, right_arr):
    #if left or right is empty
    if not left_arr or not right_arr:
        return []
    
    results = []
    left,right = 0,0
    while left < len(left_arr) and right < len(right_arr):
        if left_arr[left] == right_arr[right]:
            results.append(right_arr[right])
            left += 1
            right += 1
        elif left_arr[left] > right_arr[right]:
            right += 1
        else:
            left += 1
    return results
print(find_common_elements(left,right))


records = [
    {"category": "travel", "amount": 50},
    {"category": "food", "amount": 20},
    {"category": "travel", "amount": 30}
]

#input- a list of dictions has cat and amount
#process - parse through the list of dictionaries 
# get the category and the amount
#we need a seen dictionary
#we check if the category has been added already  and if addd
#we add more hours 
#if not there then we just assign the category with it original value
#ouput - a dictionary with catergoty and amount

def total_category_ammounts(records):
    seen = {}
    for record in records:
        category = record["category"]
        amount = record["amount"]
        seen[category] = seen.get(category,0) + amount
    
    highest_total = max(seen, key=seen.get)
    
    return highest_total,seen[highest_total]

print(total_category_ammounts(records))
 
from collections import Counter      
sym =[[1, 2, 5], [2, 3, 5], [3, 4, 5]]
# if in a and b dont append if only in a append
# input is list of arrs
# process - we could import a counter then check the vlaues for each key where the key is the number and the coutn is the value
# if the value > 1 then dicard 
# else append to a list 
# output is an array that contain things that arent common 
# def symmetry_diff(block):
          
    # merged = []
    # results = []
    # for arr in block:
    #     for elements in arr:
    #         merged.append(elements)
    
    # count = Counter(merged)
    
    # for key, val in count.items():
    #     if val == 1:
    #         results.append(key)
    #     else:
    #         continue
    # return results
            
            

    
# print(symmetry_diff(sym))
            
def sym_two(a, b):
    a = set(a)
    b = set(b)
    result = []

    for x in a:
        if x not in b:
            result.append(x)

    for x in b:
        if x not in a:
            result.append(x)

    return result

def sym(arrays):
    result = arrays[0]

    for i in range(1, len(arrays)):
        result = sym_two(result, arrays[i])

    return result


sym_data = [[3, 3, 3, 2, 5], [2, 1, 5, 7], [3, 4, 6, 6], [1, 2, 3], [5, 3, 9, 8], [1]]
print(sym(sym_data))

'''
sorted lists and return common user
inout 2 lists output - one list of users in both -sort
process two poniters are - weather then names are equal - if the left os smaller than the right - else: rightpoints
'''
left = ["alice", "bob", "bob", "charlie"]
right = ["bob", "bob", "david"]

def common_users(left, right):
    l_pointer, r_pointer = 0, 0
    left_1 = [i.lower() for i in left]
    right_1 = [i.lower() for i in right]
    
    results = []
    while l_pointer < len(left_1) and r_pointer < len(right_1):
        if left_1[l_pointer] == right_1[r_pointer]:
            if not results or left_1[l_pointer] != results[-1].lower():
                results.append(left[l_pointer])
            l_pointer += 1
            r_pointer += 1
        elif left_1[l_pointer] < right_1[r_pointer]:
            l_pointer += 1
        else:
            r_pointer += 1
    return results


print(common_users(left,right))

'''
input - string
process - make the sentence case insensitive
-split the setence
-loop throught the array creatd by the split
chcek with a seen hashmap if word already encounter else we set a dfault to 0
ouput is a dictionary
'''

sentence = "apple banana apple orange banana apple"

def count_word_freq(s):
    s = s.lower()
    words = sentence.lower().split()
    word_freqency_total = {}
    for word in words:
        word_freqency_total[word] = word_freqency_total.get(word,0) + 1
        
    highest_freq = max(word_freqency_total, key=word_freqency_total.get)
        
    return highest_freq

print(count_word_freq(sentence))
    