import heapq

def merge_k_lists(lists):
    min_heap = []
    result = []

    for i, lst in enumerate(lists):
        if lst:
            heapq.heappush(min_heap, (lst[0], i, 0))

    while min_heap:
        value, list_index, element_index = heapq.heappop(min_heap)
        result.append(value)

        next_index = element_index + 1
        if next_index < len(lists[list_index]):
            next_value = lists[list_index][next_index]
            heapq.heappush(min_heap, (next_value, list_index, next_index))

    return result
# приклад використання
lists = [[1, 4, 5], [1, 3, 4], [2, 6]]
merged_list = merge_k_lists(lists)
print("Відсортований список:", merged_list)
