class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        max_count = 0
        visited = {}
        results = []
        words = sorted(words)
        for i in words:
            if i in visited:
                visited[i] += 1
                if visited[i] + 1 > max_count:
                    max_count = visited[i]
            else:
                visited[i] = 1
                if max_count == 0:
                    max_count = 1

        while k != 0 and len(visited) != 0:
            new_visited = visited.copy()
            for i in visited:
                if visited[i] == max_count:
                    results.append(i)
                    del new_visited[i]
                    print(results)
                    k -= 1
                    if k == 0:
                        break
            visited = new_visited
            max_count -= 1
        return results



