# -*- coding: utf-8 -*-
"""
Created on Wed Feb  7 23:19:06 2024

@author: raghu
"""

class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        len1,len2=len(word1),len(word2)
        max_size=max(len1,len2)
    
        together=""
        for i in range(max_size):
            if i<len1:
                together=together+word1[i]
            if i<len2:
                together=together+word2[i]
        return together