class Solution:
    def finalPositionOfSnake(self, n: int, commands: list[str]) -> int:
        position = [0, 0]

        for command in commands:
            match command[0]:
                case "U":
                    position[1] = position[1] - 1
                case "D":
                    position[1] = position[1] + 1
                case "R":
                    position[0] = position[0] + 1
                case "L": 
                    position[0] = position[0] - 1
        
        return (position[1] * n) + position[0]
