#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 19:00:08 2018

@author: axel
"""

def course_grader(test_scores):
    x = len(test_scores)
    sum = 0
    for i in test_scores:
        sum= sum + i/x
    
    print(sum)
    minScore = min(test_scores)
    maxScore = max(test_scores)
    for i in test_scores:
        if sum >= 70 and minScore >49:
            return "pass"
        else:
            return "fail"

    

def main():
    print(course_grader([100,75,45]))     # "fail"
    print(course_grader([100,70,85]))     # "pass"
    print(course_grader([80,60,60]))      # "fail"
    print(course_grader([80,80,90,30,80]))  # "fail"
    print(course_grader([70,70,70,70,70]))  # "pass"

if __name__ == "__main__":
    main()
