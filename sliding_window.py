nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3

def maxSlidingWindow(nums):
    if not nums:
        return nums

    result = []
    for i in range(len(nums) - k + 1):
        result.append(max(nums[i:i + k]))
    
    return result

print(maxSlidingWindow(nums))


from collections import deque

def maxSlidingWindow(nums, k):
    results = []
    window = deque()
    
    for i, v in enumerate(nums):
        # 윈도우의 범위를 넘은 인덱스는 제거
        if window and window[0] <= i - k:
            window.popleft()
        
        # 새로 들어온 값이 윈도우 내의 값보다 크다면 작은 값들을 모두 제거
        while window and nums[window[-1]] <= v:
            window.pop()
        
        window.append(i)
        
        # 첫 번째 윈도우가 끝난 후부터 결과에 최대값 추가
        if i >= k - 1:
            results.append(nums[window[0]])
    
    return results

print(maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))