"""
days_list = ['Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
days_list.append("NewDay")
print(days_list)
days_list.pop(2)
print(days_list)
days_list.insert(2, "Tuesday")
print(days_list)
days_list.remove('Sunday')

for day in days_list:
    print(day, end=" ")

print("")

days_dict ={'day':'Sunday', 'time':3}
print(days_dict['day'], days_dict['time'])
"""
"""
userDetails = {
    'Name':'Saugat',
    'Age' : 23,
    'Address': 'Kathmandu'
}
for key,value in userDetails.items():
    print(key)
"""

def rotate_left3(nums):
    arr = []
    for i in range(len(nums)-1,-1,-1):
        arr.append(nums[i])
    return(arr)
ar = [2,3,1]
print(rotate_left3(ar))