class Solution:
    def trafficSignal(self, timer: int) -> str:
        match timer:
            case 0:
                return "Green"
            case 30:
                return "Orange"
            case t if 30 < t <= 90:
                return "Red"
            case _:
                return "Invalid"
