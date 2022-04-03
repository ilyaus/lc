from typing import List, Tuple


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> int:
        row_ids = [i[0] for i in matrix]
        index, found = self.search(row_ids, target)

        if not found:
            index, found = self.search(matrix[index], target)

        return found

    def search(self, l: List[int], target: int) -> Tuple[int, bool]:
        high = len(l) - 1
        low = 0

        while high >= low:
            mid = int((high + low) / 2)
            if l[mid] == target:
                return mid, True
            elif l[mid] > target:
                high = mid - 1
            else:
                low = mid + 1

        if l[mid] > target:
            mid -= 1

        return mid, False


def main():
    matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 61

    s = Solution()
    print(s.searchMatrix(matrix=matrix, target=target))


if __name__ == "__main__":
    main()
