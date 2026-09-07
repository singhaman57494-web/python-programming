import heapq

hospital = []

heapq.heappush(hospital, (3, "broken finger"))
heapq.heappush(hospital, (1, "Hart atteck"))
heapq.heappush(hospital, (2, "hand broken"))

print(heapq.heappop(hospital))
print(heapq.heappop(hospital))
print(heapq.heappop(hospital))