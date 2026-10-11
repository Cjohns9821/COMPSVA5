# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.

def most_frequent(numbers):
    if not numbers:
        return None

    freq = {}
    for num in numbers:
        freq[num] = freq.get(num, 0) + 1

    # Find the key with the highest frequency
    max_count = -1
    max_val = None
    for num, count in freq.items():
        if count > max_count:
            max_count = count
            max_val = num

    return max_val


# ---- TEST CASES ----
print(most_frequent([1, 3, 2, 3, 4, 1, 3]))  # 3
print(most_frequent([5, 5, 6, 6]))           # 5 or 6
print(most_frequent([10]))                   # 10
print(most_frequent([]))                     # None

"""
Time and Space Analysis for problem 1:
- Best-case: O(n) — must count all elements.
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n) due to dictionary storing frequencies.
- Why this approach? Counting is the most direct and optimal method.
- Could it be optimized? Not asymptotically; counting is required.
"""


# 🔍 Problem 1 (Optimized Version)
# Optimization: Track max while counting to avoid second loop.

def most_frequent_optimized(numbers):
    if not numbers:
        return None

    freq = {}
    max_val = None
    max_count = 0

    for num in numbers:
        freq[num] = freq.get(num, 0) + 1
        if freq[num] > max_count:
            max_count = freq[num]
            max_val = num

    return max_val

"""
Optimization Explanation:
- Original version: Two passes (count, then find max).
- Optimized version: One pass, updating max as we go.
- Time: Still O(n), but fewer operations.
- Space: Same O(n).
"""


# 🔍 Problem 2: Remove Duplicates While Preserving Order

def remove_duplicates(nums):
    seen = set()
    result = []

    for n in nums:
        if n not in seen:
            seen.add(n)
            result.append(n)

    return result


# ---- TEST CASES ----
print(remove_duplicates([4, 5, 4, 6, 5, 7]))  # [4, 5, 6, 7]
print(remove_duplicates([]))                  # []
print(remove_duplicates([1, 1, 1]))           # [1]

"""
Time and Space Analysis for problem 2:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n) due to set + result list.
- Why this approach? Set lookup is O(1), preserving order is required.
- Could it be optimized? Sorting would reduce space but break order.
"""


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Input list has no duplicates.

def find_pairs(nums, target):
    seen = set()
    pairs = []

    for n in nums:
        complement = target - n
        if complement in seen:
            pairs.append((complement, n))
        seen.add(n)

    return pairs


# ---- TEST CASES ----
print(find_pairs([1, 2, 3, 4], 5))     # [(1,4), (2,3)]
print(find_pairs([10, 20, 30], 100))   # []
print(find_pairs([], 5))               # []

"""
Time and Space Analysis for problem 3:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n) for the set.
- Why this approach? Hash lookup gives O(1) complement checks.
- Could it be optimized? Sorting + two-pointer also works (O(n log n)).
"""


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)

def add_n_items(n):
    capacity = 1
    size = 0
    arr = [None] * capacity

    for i in range(n):
        if size == capacity:
            print(f"Resizing from {capacity} to {capacity * 2}")
            new_capacity = capacity * 2
            new_arr = [None] * new_capacity

            # Copy old values
            for j in range(size):
                new_arr[j] = arr[j]

            arr = new_arr
            capacity = new_capacity

        arr[size] = i
        size += 1

    return arr


# ---- TEST CASES ----
add_n_items(6)

"""
Time and Space Analysis for problem 4:
- Resizes happen when size == capacity.
- Worst-case for a single append: O(n) due to copying.
- Amortized time per append: O(1).
- Space complexity: O(n) for final array.
- Why doubling reduces cost: Fewer resizes; total copies form a geometric series.
"""


# 🔍 Problem 5: Compute Running Totals

def running_total(nums):
    result = []
    current_sum = 0

    for n in nums:
        current_sum += n
        result.append(current_sum)

    return result


# ---- TEST CASES ----
print(running_total([1, 2, 3, 4]))   # [1, 3, 6, 10]
print(running_total([]))             # []
print(running_total([5]))            # [5]

"""
Time and Space Analysis for problem 5:
- Best-case: O(n)
- Worst-case: O(n)
- Average-case: O(n)
- Space complexity: O(n) for output list.
- Why this approach? Single pass accumulation is optimal.
- Could it be optimized? No; must compute each prefix sum.
"""
