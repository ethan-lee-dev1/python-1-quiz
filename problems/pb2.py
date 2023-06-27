def max_values(nums):
  #find first max
  max1 = float('-inf')
  for num in nums:
        if num > max1:
            max1 = num
  #grab the index of first max and remove it from list
  index_of_max1 = nums.index(max1)
  nums.remove(max1)
  
  #find second max
  max2 = float('-inf')
  for num in nums:
        if num > max2:
            max2 = num
  #add the firstmax back to where it was
  # and find the indexes of two maxes
  nums.insert(index_of_max1, max1)
  return [nums.index(max1), nums.index(max2)]
  



# print(max_values([4, 7, 2, 8, 10, 9])) # -> [4, 5]
# print(max_values([-5, -2, -1, -11])) # -> [1, 2]