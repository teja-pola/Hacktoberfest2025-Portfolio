# LeetCode 239. Sliding Window Maximum
# Deque-based O(n) solution.

from collections import deque

def maxSlidingWindow(nums, k):
    dq = deque()
    res = []
    for i, num in enumerate(nums):
        # remove out-of-window indexes
        if dq and dq[0] == i - k:
            dq.popleft()
        # remove smaller numbers from end
        while dq and nums[dq[-1]] < num:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            res.append(nums[dq[0]])
    return res

# test
if __name__ == "__main__":
    print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # [3,3,5,5,6,7]
