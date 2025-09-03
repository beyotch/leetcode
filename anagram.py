class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        def _count_letters(given: str) -> dict[str, int]:
            counts = {}
            for i in given:
                counts[i] = counts.get(i, 0) + 1
            return counts
        count_s = _count_letters(s)
        count_t = _count_letters(t)
        return  count_s == count_t