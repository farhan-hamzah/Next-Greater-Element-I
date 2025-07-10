from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Map untuk menyimpan hasil next greater element dari setiap angka di nums2
        next_greater = {}
        stack = []

        # Proses nums2 dari kiri ke kanan
        for num in nums2:
            # Jika stack tidak kosong dan elemen sekarang lebih besar dari elemen stack terakhir,
            # maka elemen sekarang adalah next greater dari elemen stack terakhir
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)

        # Elemen yang tidak punya next greater diset ke -1
        while stack:
            next_greater[stack.pop()] = -1

        # Buat hasil untuk nums1 dengan mencocokkan dari dictionary
        return [next_greater[num] for num in nums1]
