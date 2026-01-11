import heapq

def min_cost_to_connect_cables(cables):
    heapq.heapify(cables)
    total_cost = 0

    while len(cables) > 1:
        a = heapq.heappop(cables)
        b = heapq.heappop(cables)

        cost = a + b
        total_cost += cost

        heapq.heappush(cables, cost)

    return total_cost

# перевірка прикладу
print(f'Мінімальна вартість зʼєднання кабелів: {min_cost_to_connect_cables([3, 2, 1, 4])}')  # 19
