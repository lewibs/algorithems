import unittest

def lcs(s1, s2):
    table = [[0] * len(s2) for _ in s1]
    m = 0

    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                table[i][j] = table[i-1][j-1] + 1
            else:
                table[i][j] = max(table[i][j-1], table[i-1][j])

            if table[i][j] > m:
                m = table[i][j]

    return m

class TestLCS(unittest.TestCase):
    def test(self):
        self.assertEqual(lcs("abcde", "ace"), 3)
        self.assertEqual(lcs("bbcde", "ace"), 2)
        self.assertEqual(lcs("abcde", "acd"), 3)
        self.assertEqual(lcs("abcde", "abcde"), 5)
        self.assertEqual(lcs("abcde", "c"), 1)
        self.assertEqual(lcs("abcde", "z"), 0)