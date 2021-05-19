from typing import List

class Solution:

  def permute(self, nums: List[int]) -> List[List[int]]:
    if len(nums) <= 1:
      return [nums]

    result = [[nums[0]]]
    index = 1
    while index < len(nums):
      tmp = []
      for perm in result:
        for i in range(index + 1):
          tmp.append(perm[:i] + [nums[index]] + perm[i:])
      result = tmp
      index += 1
    return result

if __name__ == '__main__':
  nums = [1,2,3]
  solution = Solution()
  result = solution.permute(nums)
  print(result)