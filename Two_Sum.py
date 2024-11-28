class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}  # Dictionary to store the values and their indices
        for i, num in enumerate(nums):
            complement = target - num  # Find the complementary value
            if complement in seen:  # If it's already in the dictionary
                return [seen[complement], i]
            seen[num] = i  # Store the value and its index
        return []  # If no solution is found


solution = Solution()

# Example 1:
assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]

# Example 2:
assert solution.twoSum([3, 2, 4], 6) == [1, 2]

# Example 3:
assert solution.twoSum([3, 3], 6) == [0, 1]
