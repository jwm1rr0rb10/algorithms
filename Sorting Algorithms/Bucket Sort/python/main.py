# bucket_sort sorts a list of floating-point numbers between 0.0 and 1.0
# num_buckets - the number of buckets
def bucket_sort(arr, num_buckets):
    n = len(arr)
    if n == 0 or num_buckets <= 0:
        return

    # 1. Create buckets
    # Use a list of lists to represent the buckets
    buckets = [[] for _ in range(num_buckets)]

    # 2. Distribute elements into buckets
    for value in arr:
        # Determine the bucket index. value * num_buckets gives a number in [0, num_buckets) (almost)
        # Integer truncation gives the bucket index.
        # Ensure that value = 1.0 goes into the last bucket (num_buckets - 1)
        bucket_index = int(value * num_buckets)
        if bucket_index == num_buckets:  # If value = 1.0, the index would be num_buckets
            bucket_index -= 1  # Move it to the last bucket
        if bucket_index < 0 or bucket_index >= num_buckets:
             # You could add handling for values outside the [0.0, 1.0) range,
             # but for simplicity we assume all values are within the range.
             continue

        buckets[bucket_index].append(value)

    # 3. Sort each bucket and 4. Merge the buckets
    # Merging takes place while copying back into the original list
    k = 0  # Index for the original list
    for i in range(num_buckets):
        # Sort the current bucket.
        # In Python, you can use list.sort() for in-place sorting.
        # This could be any other sorting algorithm, such as insertion_sort for small lists.
        buckets[i].sort()

        # Copy the sorted elements from the bucket back into the original list
        for value in buckets[i]:
            arr[k] = value
            k += 1

# Examples of using Bucket Sort:
data_bucket = [0.78, 0.17, 0.39, 0.26, 0.72, 0.94, 0.21, 0.12, 0.23, 0.68]
print("Original list (Bucket Sort):", data_bucket)
bucket_sort(data_bucket, 10)  # 10 buckets
print("Sorted list (Bucket Sort):", data_bucket)

data_bucket_2 = [0.5, 0.1, 0.9, 0.3, 0.7, 0.2, 0.8, 0.4, 0.6, 1.0]
print("Original list (Bucket Sort):", data_bucket_2)
bucket_sort(data_bucket_2, 10)  # 10 buckets
print("Sorted list (Bucket Sort):", data_bucket_2)

data_bucket_3 = [0.05, 0.95, 0.001, 0.15, 0.85, 0.25, 0.75, 0.35, 0.65, 0.45]
print("Original list (Bucket Sort):", data_bucket_3)
bucket_sort(data_bucket_3, 5)  # 5 buckets
print("Sorted list (Bucket Sort):", data_bucket_3)
