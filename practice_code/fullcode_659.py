#!/usr/bin/python3
import unittest
from typing import List

from collections import Counter


"""
https://leetcode.com/problems/split-array-into-consecutive-subsequences/
Solution Note

1 <= nums.length <= 10**4
-1000 <= nums[i] <= 1000
nums is sorted in non-decreasing order.
"""

# Leet Code Solution
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        start = 0
        end = -1
        for i in range(len(nums) - 1):
            if (nums[i] == nums[i + 1]) or ((nums[i] + 1) == nums[i + 1]):
                continue
            end = i + 1
            c_len = end - start
            # c_len < 3 -> False
            if c_len < 3:
                return False

            # function
            res = self.possible(nums[start:end + 1])
            if res == False:
                return False
            start = end

        end = len(nums) - 1;
        c_len = end - start + 1
        if c_len < 3:
            return False

        return self.possible(nums[start:end + 1])


    def possible(self, lst):
        counter = Counter(lst).most_common()
        count = -1
        num_count = 0
        for i in range(len(counter)):
            if num_count == 0:
                count = counter[i][1]
                num_count += 1
                continue

            if not count == counter[i][1]:
                if num_count >= 3:
                    num_count = 0
                    count = -1
                    continue
                return False

            num_count += 1

        return True




# python unit test
class UnitTest(unittest.TestCase):

    # 클래스 생성 시 1회 실행
    @classmethod
    def setUpClass(self):
        self.solution = Solution();

    # 클래스 소멸 시 1회 실행
    @classmethod
    def tearDownClass(self):
        pass

    # 테스트 케이스 전 실행
    def setUp(self):
        pass

    # 테스트 케이스 후 실행
    def tearDown(self):
        pass

    def test_case_normal_1(self):
        res = self.solution.isPossible([1,2,3,3,4,5])
        self.assertEqual(res, True)

    def test_case_normal_2(self):
        res = self.solution.isPossible([1,2,3,3,4,4,5,5])
        self.assertEqual(res, True)

    def test_case_normal_3(self):
        res = self.solution.isPossible([1,2,3,4,4,5])
        self.assertEqual(res, False)

    def test_case_normal_4(self):
        res = self.solution.isPossible([1,2,3,4,7,8])
        self.assertEqual(res, False)




if __name__ == "__main__":
    # 스크립트 실행 시, 해당 부분 동작
    unittest.main(verbosity=0)
    pass