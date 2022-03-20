# algo_and_ds
Algorithms and Data Structures

## Linked List

In computer science, a linked list is a linear collection of data elements, whose order is not given by their physical placement in memory. Instead, each element points to the next.

* linked-list.py

https://en.wikipedia.org/wiki/Linked_list

## Change-making problem

The change-making problem addresses the question of finding the minimum number of coins (of certain denominations) that add up to a given amount of money. It is a special case of the integer knapsack problem, and has applications wider than just currency.

* change_recursive.py - recursive solution
* change_memoization.py - memoization solution

https://en.wikipedia.org/wiki/Change-making_problem

## Making anagram

Given two strings in lowercase, the task is to make them anagram. The only allowed operation is to remove a character from any string. Find minimum number of characters to be deleted to make both the strings anagram? 
If two strings contains same data set in any order then strings are called Anagrams. 

Examples:


```
Input : str1 = "bcadeh" str2 = "hea"
Output: 3
We need to remove b, c and d from str1.

Input : str1 = "cddgk" str2 = "gcd"
Output: 2

Input : str1 = "bca" str2 = "acb"
Output: 0
```
