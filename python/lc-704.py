from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = int((low + high) / 2)

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        return -1


def main():
    nums = [-1, 0, 3, 5, 9, 12]
    target = 2

    s = Solution()
    print(s.search(nums=nums, target=target))


if __name__ == "__main__":
    main()
