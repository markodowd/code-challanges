class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        inner_len = len(image[0])
        output = []

        for group in image:
            output.append(group[::-1])

        for i in range(len(output)):
            for j in range(inner_len):
                if output[i][j] == 1:
                    output[i][j] = 0
                else:
                    output[i][j] = 1

        return output
