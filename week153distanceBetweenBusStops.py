class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        s=sum(distance)
        d=sum(distance[min(start,destination):max(start,destination)])
        return(min(d,s-d))
