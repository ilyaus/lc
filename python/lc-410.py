from typing import List


class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        min_chunk_size = int(len(nums) / m)
        max_chunk_size = (
            min_chunk_size + 1 if m < len(nums) and m > 1 else min_chunk_size
        )
        num_of_chunks = int(len(nums) / min_chunk_size)

        print(f"Min size: {min_chunk_size}")
        print(f"Max size: {max_chunk_size}")
        print(f"Number of chunks: {num_of_chunks}")
        print("")

        nums_max = 0

        for p in range(num_of_chunks):
            current_p = 0
            end = 0

            while end < len(nums):
                if not p == current_p or num_of_chunks == 1:
                    chunk = nums[end : min_chunk_size + end]
                    end += min_chunk_size
                else:
                    chunk = nums[end : max_chunk_size + end]
                    end += max_chunk_size

                chunk_sum = sum(chunk)
                print(f"{chunk} - {chunk_sum}")

                if len(chunk) == min_chunk_size:
                    chunk_sum = sum(chunk)
                    if chunk_sum > nums_max:
                        nums_max = chunk_sum

                current_p += 1

            print("---")

        return nums_max


def main():
    nums = [10, 5, 13, 4, 8, 4, 5, 11, 14, 9, 16, 10, 20, 8]
    m = 8

    s = Solution()
    print(s.splitArray(nums, m))


if __name__ == "__main__":
    main()
