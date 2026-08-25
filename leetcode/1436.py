class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        starts = []

        for place in paths:
            starts.append(place[0])

        for place in paths:
            if place[1] not in starts:
                return place[1]
