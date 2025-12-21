class Solution(object):
    def findAllPeople(self, n, meetings, firstPerson):
        # Step 1: sort meetings by time
        meetings.sort(key=lambda x: x[2])

        # People who know the secret
        secret = set([0, firstPerson])

        i = 0
        while i < len(meetings):
            time = meetings[i][2]

            # Temporary graph for this time
            graph = defaultdict(list)
            people = set()

            # Collect all meetings at the same time
            while i < len(meetings) and meetings[i][2] == time:
                x, y, _ = meetings[i]
                graph[x].append(y)
                graph[y].append(x)
                people.add(x)
                people.add(y)
                i += 1

            # BFS from people who already know the secret
            queue = deque()
            visited = set()

            for p in people:
                if p in secret:
                    queue.append(p)
                    visited.add(p)

            while queue:
                u = queue.popleft()
                for v in graph[u]:
                    if v not in visited:
                        visited.add(v)
                        queue.append(v)

            # Add newly informed people
            for p in visited:
                secret.add(p)

        return list(secret)
