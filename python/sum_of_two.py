#!/bin/env python

#Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
#You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
#You can return the answer in any order.
#
#Example 1:
#Input: nums = [2,7,11,15], target = 9
#Output: [0,1]
#Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
#Example 2:
#Input: nums = [3,2,4], target = 6
#Output: [1,2]
#
#Example 3:
#Input: nums = [3,3], target = 6
#Output: [0,1]



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # Slower and less memory
        # Runtime: 6576 ms, faster than 8.81% of Python online submissions for Two Sum.
        # Memory Usage: 14.2 MB, less than 87.07% of Python online submissions for Two Sum.

        # for i,a in enumerate(nums):
        #     diff = target - a
        #     for j, b in enumerate(nums):
        #         if i == j:
        #             continue
        #         if b == diff:
        #             return [i, j]

        # Faster and more memory
        # Runtime: 61 ms, faster than 73.95% of Python online submissions for Two Sum.
        # Memory Usage: 14.8 MB, less than 5.36% of Python online submissions for Two Sum.

        # indexes =
        # {
        #   5: [1,2,3]
        # }

        indexes = {}
        for i, v in enumerate(nums):
            if v in indexes:
                index_list = indexes[v]
                index_list.append(i)
            else:
                indexes[v] = [i]
            diff = target - v
            if diff in indexes:
                diff_indexes = indexes[diff]
                for j in diff_indexes:
                    if i == j:
                        continue
                    return [i,j]

