class Solution:
    def three_sum(self, nums):
        nums.sort()
        n = len(nums)
        result = []
        seen_triplets = set()

        for i in range(n):
            for j in range(i + 1, n):
                complement = -(nums[i] + nums[j])

                # binary search for complement in nums[j+1:]
                left, right = j + 1, n - 1
                while left <= right:
                    mid = (left + right) // 2
                    if nums[mid] == complement:
                        triplet = (nums[i], nums[j], nums[mid])
                        if triplet not in seen_triplets:
                            seen_triplets.add(triplet)
                            result.append(list(triplet))
                        break
                    elif nums[mid] < complement:
                        left = mid + 1
                    else:
                        right = mid - 1

        # final lexicographic order
        return result
    
sol = Solution()
print(sol.three_sum([-1, 0, 1, 2, -1, -4]))
# Output: [[-1, -1, 2], [-1, 0, 1]]

