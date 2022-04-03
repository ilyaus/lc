def guess(num: int) -> int:
    pick = 2

    if num == pick:
        return 0

    return -1 if num > pick else 1


class Solution:
    def guessNumber(self, n: int) -> int:
        low = 1
        high = n

        result = -1

        while not result == 0:
            my_guess = int((high + low) / 2) if n > 1 else 1
            result = guess(my_guess)

            if result == -1:
                high = my_guess - 1
            else:
                low = my_guess + 1

        return my_guess


def main():
    n = 2

    s = Solution()
    print(s.guessNumber(n))


if __name__ == "__main__":
    main()
