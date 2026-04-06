# Binary Search
**What it is:**
* `Binary Search` is a highly efficient algorithm for finding an element in a sorted array or list. It works on the "divide and conquer" principle by repeatedly cutting the search space in half.

---

**How it works:**

* Start searching in a specified segment of the array (initially, this is the entire array).
* Find the middle element of the current segment.
* Compare the target value to this middle element:
* If they are equal, the element is found – return its index.
* If the target is less than the middle element, it can only (if it exists) be in the left half of the current segment.  Discard  the right half and repeat steps 1–3 on the left half.
* If the target is greater than the middle element, it can only (if it exists) be in the right half. Discard the left half and repeat steps 1–3 on the right half.
* This process continues until the element is found or the search segment becomes empty (which means the element is not in the array).

---

## **⚠️ Important requirement:** The `array (or list)` must be sorted.

**Complexity:**

`**Time Complexity:**`
* Best case: O(1) (the element is found on the first try, right in the middle)
* Average case: O(log n)
* Worst case: O(log n)
* `Why O(log n)? Because each step roughly halves the search space. To reduce a search space of size n down to 1, it takes approximately log₂(n) steps.`

---

`**Space Complexity:**``
* Iterative implementation: O(1) (uses only a small, fixed number of extra variables)
* Recursive implementation: O(log n) (due to the recursion call stack depth)

---

# Golang Example

```go 
package main

import "fmt"

// BinarySearch searches for target in a sorted slice data.
// Returns the index of target if found, otherwise -1.
func BinarySearch(data []int, target int) int {
	low := 0              // Lower bound of the current search segment
	high := len(data) - 1 // Upper bound of the current search segment

	// While the lower bound has not exceeded the upper bound
	for low <= high {
		// Find the index of the middle element
		mid := low + (high-low)/2 // Avoids potential overflow for very large low/high values

		// Compare the middle element with the target value
		if data[mid] == target {
			return mid // Element found, return its index
		} else if data[mid] < target {
			// If the middle element is less than target, the target can only be to the right of mid
			low = mid + 1 // Shift the lower bound to the right
		} else { // data[mid] > target
			// If the middle element is greater than target, the target can only be to the left of mid
			high = mid - 1 // Shift the upper bound to the left
		}
	}

	// If the loop ends, the element was not found
	return -1
}

func main() {
	sortedData := []int{2, 5, 8, 12, 16, 23, 38, 56, 72, 91}
	target1 := 23
	target2 := 10

	// Search for target1
	index1 := BinarySearch(sortedData, target1)
	if index1 != -1 {
		fmt.Printf("Element %d found at index %d\n", target1, index1)
	} else {
		fmt.Printf("Element %d not found\n", target1)
	}

	// Search for target2
	index2 := BinarySearch(sortedData, target2)
	if index2 != -1 {
		fmt.Printf("Element %d found at index %d\n", target2, index2)
	} else {
		fmt.Printf("Element %d not found\n", target2)
	}
}
```

Explanation of the Go Code:

`**func BinarySearch(data []int, target int) int:**``
* Declares the BinarySearch function, which takes a sorted slice of integers (data) and a target integer (target). The function returns an integer (either the index of the found element or -1 if not found).

`**low := 0, high := len(data) - 1:**`
* Initializes the low and high variables to mark the bounds of the current search segment. `low is the index of the first element (0)`, and high is the index of the last element.

`**for low <= high:**`
* The main search loop. It continues as long as the lower bound does not exceed the upper bound. If that happens, it means the search segment has collapsed to an empty range.

`**mid := low + (high-low)/2:**`
* Calculates the index of the middle element. The formula `low + (high - low) / 2` is used instead of `(low + high) / 2` to avoid potential integer overflow if low and high are very large.

`**if data[mid] == target:**`
* Compares the middle element with the target. If they are equal, the element has been found and its index mid is returned immediately.

`**else if data[mid] < target:**`
* If the middle element is less than the target, then (since the array is sorted), the target can only be in the right half. We shift the lower bound low to mid + 1 to search the right half next.

`**else:**`
* If the middle element is greater than the target, then the target can only be in the left half. We shift the upper bound high to mid - 1 to continue the search in the left segment.

`**return -1:**`
* If the loop ends (i.e., low > high), the search segment has become empty and the element was not found. In this case, return -1.

`**The main function:**`
* Demonstrates how to use the BinarySearch function with examples of searching for an existing element (target1) and a non-existent one (target2).

---

# Python Example:

```python
# Binary Search (must-know)
def binary_search(data, target):
    """
    Searches for target in a sorted list data using binary search.
    Returns the index of target if found, otherwise -1.
    """
    low = 0              # Lower bound of the current search segment
    high = len(data) - 1 # Upper bound of the current search segment

    # While the lower bound has not exceeded the upper bound
    while low <= high:
        # Find the index of the middle element
        mid = (low + high) // 2 # In Python, there is no overflow risk with standard int

        # Compare the middle element with the target value
        if data[mid] == target:
            return mid # Element found, return its index
        elif data[mid] < target:
            # If the middle element is less than the target, it can only be to the right of mid
            low = mid + 1 # Shift the lower bound to the right
        else: # data[mid] > target
            # If the middle element is greater than the target, it can only be to the left of mid
            high = mid - 1 # Shift the upper bound to the left

    # If the loop ends, the element was not found
    return -1

# Example usage
sorted_data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
target1 = 23
target2 = 10

# Search for target1
index1 = binary_search(sorted_data, target1)
if index1 != -1:
    print(f"Element {target1} found at index {index1}")
else:
    print(f"Element {target1} not found")

# Search for target2
index2 = binary_search(sorted_data, target2)
if index2 != -1:
    print(f"Element {target2} found at index {index2}")
else:
    print(f"Element {target2} not found")
```

# Explanation of the Python Code:

`**def binary_search(data, target):**`
* Declares the binary_search function, which takes a sorted list (data) and a target number (target).

`**Docstring (the triple-quoted string below the function header):**`
* This is the standard way to document a function in Python. It briefly describes the purpose of the function, its arguments, and its return value.

`**low = 0, high = len(data) - 1:**`
* Initializes the low and high variables to define the bounds of the search segment, just like in the Go example.

`**while low <= high:**`
* The main while loop. The condition is the same as in Go and means that the search continues as long as the segment is not empty.

`**mid = (low + high) // 2:**`
* Calculates the index of the middle element. In Python 3, the // operator performs integer (floor) division.
There is virtually no risk of integer overflow from low + high due to Python's dynamic typing and its support for arbitrarily large integers.

`**if data[mid] == target:**`
* Compares the middle element with the target. If they are equal, return mid.

`**elif data[mid] < target:**`
*If the middle element is less than the target, shift the lower bound low to mid + 1 to search the right half.
elif is short for else if.

`**else:**`
* If the middle element is greater than the target, shift the upper bound high to mid - 1 to search the left half.

`**return -1:**`
* If the loop ends without finding the element, return -1.

`**Example block:**`
* Demonstrates calling the binary_search function and printing the results using f-strings for formatted output.

---

# Easy Level Binary Search Problems

| Problem Number | Problem Name                                               | Acceptance Rate |
|:---------------|:-----------------------------------------------------------|:----------------|
| 35             | Search Insert Position                                     | 48.7%           |
| 69             | Sqrt(x)                                                    | 40.3%           |
| 222            | Count Complete Tree Nodes                                  | 69.6%           |
| 268            | Missing Number                                             | 69.8%           |
| 270            | Closest Binary Search Tree Value                           | 49.9%           |
| 278            | First Bad Version                                          | 45.8%           |
| 349            | Intersection of Two Arrays                                 | 76.3%           |
| 350            | Intersection of Two Arrays II                              | 59.0%           |
| 367            | Valid Perfect Square                                       | 44.1%           |
| 374            | Guess Number Higher or Lower                               | 55.6%           |
| 441            | Arranging Coins                                            | 47.3%           |
| 704            | Binary Search                                              | 59.4%           |
| 744            | Find Smallest Letter Greater Than Target                   | 53.9%           |
| 888            | Fair Candy Swap                                            | 63.1%           |
| 1064           | Fixed Point                                                | 63.9%           |
| 1099           | Two Sum Less Than K                                        | 62.0%           |
| 1150           | Check If a Number Is Majority Element in a Sorted Array    | 59.0%           |
| 1213           | Intersection of Three Sorted Arrays                        | 80.1%           |
| 1337           | The K Weakest Rows in a Matrix                             | 73.9%           |
| 1346           | Check If N and Its Double Exist                            | 41.2%           |
| 1351           | Count Negative Numbers in a Sorted Matrix                  | 77.6%           |
| 1385           | Find the Distance Value Between Two Arrays                 | 70.0%           |
| 1539           | Kth Missing Positive Number                                | 62.1%           |
| 1608           | Special Array With X Elements Greater Than or Equal X      | 66.6%           |
| 2089           | Find Target Indices After Sorting Array                    | 77.1%           |
| 2389           | Longest Subsequence With Limited Sum                       | 72.7%           |
| 2529           | Maximum Count of Positive Integer and Negative Integer     | 74.5%           |
| 2540           | Minimum Common Value                                       | 58.2%           |
| 2824           | Count Pairs Whose Sum is Less than Target                  | 87.5%           |
| 2970           | Count the Number of Incremovable Subarrays I               | 54.5%           |
| 3477           | Fruits Into Baskets II                                     | 52.0%           |

--- 

## Medium Level Binary Search Problems

| Problem Number | Problem Name                                               | Acceptance Rate |
|:---------------|:-----------------------------------------------------------|:----------------|
| 33             | Search in Rotated Sorted Array                             | 42.6%           |
| 34             | Find First and Last Position of Element in Sorted Array    | 46.6%           |
| 74             | Search a 2D Matrix                                          | 52.1%           |
| 81             | Search in Rotated Sorted Array II                          | 38.8%           |
| 153            | Find Minimum in Rotated Sorted Array                       | 52.5%           |
| 162            | Find Peak Element                                          | 46.5%           |
| 167            | Two Sum II - Input Array Is Sorted                         | 63.2%           |
| 209            | Minimum Size Subarray Sum                                  | 49.1%           |
| 240            | Search a 2D Matrix II                                      | 54.9%           |
| 259            | 3Sum Smaller                                               | 51.0%           |
| 275            | H-Index II                                                 | 38.8%           |
| 287            | Find the Duplicate Number                                  | 62.6%           |
| 300            | Longest Increasing Subsequence                             | 57.5%           |
| 362            | Design Hit Counter                                         | 69.1%           |
| 378            | Kth Smallest Element in a Sorted Matrix                    | 63.4%           |
| 400            | Nth Digit                                                  | 35.6%           |
| 436            | Find Right Interval                                        | 53.7%           |
| 456            | 132 Pattern                                                | 34.0%           |
| 475            | Heaters                                                    | 39.8%           |
| 497            | Random Point in Non-overlapping Rectangles                 | 38.0%           |
| 528            | Random Pick with Weight                                    | 48.1%           |
| 532            | K-diff Pairs in an Array                                   | 44.5%           |
| 540            | Single Element in a Sorted Array                           | 59.2%           |
| 611            | Valid Triangle Number                                      | 52.2%           |
| 633            | Sum of Square Numbers                                      | 36.4%           |
| 658            | Find K Closest Elements                                    | 48.5%           |
| 702            | Search in a Sorted Array of Unknown Size                   | 72.7%           |
| 713            | Subarray Product Less Than K                               | 52.7%           |
| 718            | Maximum Length of Repeated Subarray                        | 51.0%           |
| 729            | My Calendar I                                              | 58.1%           |
| 731            | My Calendar II                                             | 62.3%           |
| 754            | Reach a Number                                             | 43.8%           |
| 786            | K-th Smallest Prime Fraction                               | 68.5%           |
| 792            | Number of Matching Subsequences                            | 50.7%           |
| 825            | Friends Of Appropriate Ages                                | 49.0%           |
| 826            | Most Profit Assigning Work                                 | 55.9%           |
| 852            | Peak Index in a Mountain Array                             | 67.7%           |
| 875            | Koko Eating Bananas                                        | 49.0%           |
| 911            | Online Election                                            | 51.8%           |
| 981            | Time Based Key-Value Store                                 | 49.3%           |
| 1004           | Max Consecutive Ones III                                   | 65.7%           |
| 1011           | Capacity To Ship Packages Within D Days                    | 71.8%           |
| 1027           | Longest Arithmetic Subsequence                             | 49.4%           |
| 1055           | Shortest Way to Form String                                | 61.3%           |
| 1060           | Missing Element in Sorted Array                            | 58.5%           |
| 1062           | Longest Repeating Substring                                | 63.0%           |
| 1102           | Path With Maximum Minimum Value                            | 54.0%           |
| 1146           | Snapshot Array                                             | 36.7%           |
| 1170           | Compare Strings by Frequency of the Smallest Character     | 62.6%           |
| 1182           | Shortest Distance to Target Color                          | 55.4%           |
| 1198           | Find Smallest Common Element in All Rows                   | 76.4%           |
| 1201           | Ugly Number III                                            | 30.3%           |
| 1208           | Get Equal Substrings Within Budget                         | 58.8%           |
| 1214           | Two Sum BSTs                                               | 67.4%           |
| 1237           | Find Positive Integer Solution for a Given Equation        | 69.4%           |
| 1268           | Search Suggestions System                                  | 65.0%           |

## Hard Level Binary Search Problems

| Problem Number | Problem Name                                            | Acceptance Rate |
|:---------------|:--------------------------------------------------------|:----------------|
| 4              | Median of Two Sorted Arrays                             | 43.5%           |
| 154            | Find Minimum in Rotated Sorted Array II                 | 44.1%           |
| 302            | Smallest Rectangle Enclosing Black Pixels              | 60.6%           |
| 315            | Count of Smaller Numbers After Self                     | 42.8%           |
| 327            | Count of Range Sum                                      | 36.9%           |
| 352            | Data Stream as Disjoint Intervals                       | 59.5%           |
| 354            | Russian Doll Envelopes                                  | 37.3%           |
| 363            | Max Sum of Rectangle No Larger Than K                   | 44.6%           |
| 410            | Split Array Largest Sum                                 | 57.8%           |
| 483            | Smallest Good Base                                      | 43.1%           |
| 493            | Reverse Pairs                                           | 31.9%           |
| 644            | Maximum Average Subarray II                             | 37.4%           |
| 668            | Kth Smallest Number in Multiplication Table             | 52.7%           |
| 710            | Random Pick with Blacklist                              | 33.8%           |
| 719            | Find K-th Smallest Pair Distance                        | 45.7%           |
| 732            | My Calendar III                                         | 70.6%           |
| 774            | Minimize Max Distance to Gas Station                    | 52.9%           |
| 778            | Swim in Rising Water                                    | 62.6%           |
| 793            | Preimage Size of Factorial Zeroes Function              | 45.6%           |
| 862            | Shortest Subarray with Sum at Least K                   | 32.2%           |
| 878            | Nth Magical Number                                      | 35.7%           |
| 887            | Super Egg Drop                                          | 28.6%           |
| 902            | Numbers At Most N Given Digit Set                       | 43.3%           |
| 1044           | Longest Duplicate Substring                             | 30.7%           |
| 1095           | Find in Mountain Array                                  | 40.4%           |
| 1157           | Online Majority Element In Subarray                     | 39.0%           |
| 1187           | Make Array Strictly Increasing                          | 57.8%           |
| 1231           | Divide Chocolate                                        | 59.8%           |
| 1235           | Maximum Profit in Job Scheduling                        | 54.4%           |
| 1439           | Find the Kth Smallest Sum of a Matrix With Sorted Rows  | 61.9%           |
| 1483           | Kth Ancestor of a Tree Node                             | 35.5%           |
| 1521           | Find a Value of a Mysterious Function Closest to Target | 45.7%           |
| 1649           | Create Sorted Array through Instructions                | 39.9%           |
| 1671           | Minimum Number of Removals to Make Mountain Array       | 55.0%           |
| 1713           | Minimum Operations to Make a Subsequence                | 48.7%           |
| 1739           | Building Boxes                                          | 51.8%           |
| 1751           | Maximum Number of Events That Can Be Attended II        | 60.9%           |
| 1782           | Count Pairs Of Nodes                                    | 40.6%           |
| 1793           | Maximum Score of a Good Subarray                        | 64.2%           |
| 1847           | Closest Room                                            | 39.5%           |
| 1851           | Minimum Interval to Include Each Query                  | 52.0%           |
| 1862           | Sum of Floored Pairs                                    | 29.6%           |
| 1889           | Minimum Space Wasted From Packaging                     | 32.5%           |
| 1923           | Longest Common Subpath                                  | 28.0%           |
| 1932           | Merge BSTs to Create Single BST                         | 35.6%           |
| 1956           | Minimum Time For K Virus Variants to Spread             | 49.2%           |
| 1964           | Find the Longest Valid Obstacle Course at Each Position | 62.5%           |
| 1970           | Last Day Where You Can Still Cross                      | 62.2%           |
| 2009           | Minimum Number of Operations to Make Array Continuous   | 52.2%           |
| 2035           | Partition Array Into Two Arrays to Minimize Sum Diff    | 21.5%           |
