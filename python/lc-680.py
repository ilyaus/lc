from typing import Tuple


class Solution:
    def validPalindrome(self, s: str) -> bool:
        result, index = self.vp(s)

        if not result:
            result, l_index = self.vp(s[index + 1 : len(s) - index])

            if not result:
                result, r_index = self.vp(s[index : len(s) - 1 - index])

        return result

    def vp(self, s: str) -> Tuple[bool, int]:
        steps = int(len(s) / 2)

        for i in range(steps):
            if not s[i] == s[(len(s) - 1) - i]:
                print(f"{s[i]} != {s[(len(s) - 1) - i]}")
                return False, i

        return True, -1

    def remove_char(self, s: str, index: int) -> str:
        ret_val = ""
        for i in enumerate(s):
            if not index == i[0]:
                ret_val += i[1]

        return ret_val


def main():
    string = "aba"

    s = Solution()
    print(s.validPalindrome(string))


if __name__ == "__main__":
    main()
