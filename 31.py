def next_permutation(nums):
    """
    Return the next permutation from list of sorted permutations

    E.g. arr = [1,3,2] -> output = [3,1,2]
    E.g. arr =  [4,2,3,5,2,8,5,1,2,3] -> output = [4,2,3,5,7,8,5,1,3,2]
                [4,2,3,5,2,8,5,1,3,2]
                [4,2,3,5,2,8,5,2,1,3]
                [4,2,3,5,2,8,5,2,3,1]
                [4,2,3,5,2,8,5,3,1,2]
                [4,2,3,5,2,8,5,3,2,1]
                [4,2,3,5,3,1,2,2,5,8]

                [4,2,3,5,4,8,5,3,2,1]
                [4,2,3,5,5,1,2,3,4,8]
                

    E.g. arr = [4,2,3,5,7,8,5,3,2,1] -> output = [4,2,3,5,8,7,1,2,3,5]

    We have to identify the longest reverse-sorted subarray that includes the end.
    That's O(n), where n = len(arr)
    We leave everything that came before alone
    The element right before the subarray (pre) will become the smallest element in the
     subarray that is bigger than itself (post)
    To identify post we can do a linear search, O(n)
    Swap elements pre and post, constant
    Everything after the new post will be the subarray in the reverse order, O(n)
    Reverse the subarray should be handled as an iterator to avoid extra space

    Time complexity: O(n)
    Space complexity: O(1)
    """
    def reverse_sorted(nums, pointer_end):
        sym_pointer = len(nums)-1
        while pointer_end < sym_pointer:
            nums[pointer_end],nums[sym_pointer] = nums[sym_pointer],nums[pointer_end]
            pointer_end += 1
            sym_pointer -= 1

    if len(nums) < 2:
        return nums
    
    pointer_end = len(nums)-1

    # Find longest streak of descending subnumsay at the end
    while pointer_end > 0 and nums[pointer_end] <= nums[pointer_end-1]: pointer_end -= 1

    # Return sorted numsay if numsay is reverse-sorted
    if pointer_end == 0:
        return reverse_sorted(nums, pointer_end)
    
    pre_index = pointer_end-1
    pre = nums[pre_index]
    diff = nums[pointer_end]-pre # minimize this while positive

    # Search for smallest element bigger than pre
    iterate_index = len(nums) - 1
    while iterate_index >= pointer_end:
        if nums[iterate_index] > pre:
            post_index = iterate_index  # This is the smallest element > pre
            break
        iterate_index -= 1

    post = nums[post_index]

    # Swap pre and post
    nums[pre_index], nums[post_index] = post,pre

    # Change remaining of nums
    reverse_sorted(nums, pointer_end)


arr = [1,4,2,3,2,8,5,3,2,1]
next_permutation(arr)
print(arr)

