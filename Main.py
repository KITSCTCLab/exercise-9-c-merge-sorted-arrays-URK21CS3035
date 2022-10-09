from typing import List

def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    '''
    We have 4 attributes
    nums1 : which is the list1 with sorted numbers
    nums2 : which is the list2 withn sorted numbers
    m: m is the number of elements we take from nums1
    n: n is the number of elements we take from nums2
    '''
    smalla = nums1[0:m] # make a new list to keep elements till m and n respectivly
    smallb = nums2[0:n]
    # using merge sort, sort both the array and add the result in nums1
    i = 0  
    j = 0
    k = 0
    while(i<len(smalla) and j<len(smallb)):
        if (smalla[i] <= smallb[j]):
            nums1[k] = smalla[i]
            i+=1
        else:
            nums1[k] = smallb[j]
            j+=1
        k+=1
    while i<len(smalla):
        nums1[k] = smalla[i]
        i+=1
        k+=1
    while j<len(smallb):
        nums1[k] = smallb[j]
        j+=1
        k+=1
  
# Do not change the following corde
nums1 = []
nums2 = []
for item in input().split(', '):
  nums1.append(int(item))
for item in input().split(', '):
  nums2.append(int(item))
m = int(input())
n = int(input())
merge(nums1, m, nums2, n)
print(nums1)
