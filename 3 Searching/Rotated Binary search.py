class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums) - 1

        # ---------- Step 1: Find Pivot ----------
        def Find_pivot(nums):
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = start + (end - start) // 2
                # Check if mid is pivot (next element smaller)
                if mid < end and nums[mid] > nums[mid + 1]:
                    return mid
                # Check if mid-1 is pivot
                if mid > start and nums[mid] < nums[mid - 1]:
                    return mid - 1
                # Search in left or right half
                if nums[start] >= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            return -1  # no pivot (means array not rotated)

        # ---------- Step 2: Normal Binary Search ----------
        def Finding_Answer(nums, target, start, end):
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1

        # ---------- Step 3: Main Logic ----------
        pivot = Find_pivot(nums)

        # Case 1: No rotation → normal binary search
        if pivot == -1:
            return Finding_Answer(nums, target, 0, len(nums) - 1)

        # Case 2: If pivot element is target
        if nums[pivot] == target:
            return pivot

        # Case 3: Target lies in left half
        if target >= nums[0]:
            return Finding_Answer(nums, target, 0, pivot - 1)

        # Case 4: Target lies in right half
        return Finding_Answer(nums, target, pivot + 1, len(nums) - 1)
