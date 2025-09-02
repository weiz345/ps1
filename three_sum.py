class Solution:
    def three_sum(self, nums):
        nums.sort()
        n = len(nums)
        result = []
        seen_triplets = set()

        for i in range(n):
            seen = {}
            for j in range(i + 1, n):
                complement = -nums[i] - nums[j]
                if complement in seen:
                    triplet = (nums[i], complement, nums[j])  # tuple for set
                    if triplet not in seen_triplets:
                        seen_triplets.add(triplet)
                        result.append(list(triplet))
                seen[nums[j]] = True

        return result

sol = Solution()
print(sol.three_sum([-1, 0, 1, 2, -1, -4]))
# Output: [[-1, -1, 2], [-1, 0, 1]]
