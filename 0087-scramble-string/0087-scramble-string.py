class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        @cache
        def dp(a: str, b: str) -> bool:
            if a == b:
                return True

            if Counter(a) != Counter(b):
                return False

            return any(
                dp(a[:i], b[:i]) and dp(a[i:], b[i:]) or \
                dp(a[:i], b[-i:]) and dp(a[i:], b[:-i])
                for i in range(1, len(a))
            )

        return dp(s1, s2)