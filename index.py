import heapq
island, bridge, max_bridge = map(int, input().split())
island_info = [[] for _ in range(island+1)]
for _ in range(bridge):
	a, b = map(int, input().split())
	island_info[a].append(b)
	island_info[b].append(a)

dist = [float('inf') for _ in range(island+1)]

def shortest(map_info, start):
	queue = []
	heapq.heappush(queue, (0, start))
	dist[start] = 0
	
	while queue:
		distance, current = heapq.heappop(queue)
		if dist[current] < distance: continue
		
		for i in map_info[current]:
			cost = dist[current] + 1
			if cost < dist[i]:
				dist[i] = cost
				heapq.heappush(queue, (cost, i))
	
shortest(island_info, 1)

if dist[island] <= max_bridge:
	print("YES")
else:
	print("NO")