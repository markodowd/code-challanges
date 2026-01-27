#with open("example.txt", "r") as file:
#    content = file.read()
#
#    print(content)
#

def count_word_in_grid(grid, word):
    # Define dimensions of the grid
    rows = len(grid)
    cols = len(grid[0])
    
    # Length of the word
    word_len = len(word)
    
    # All possible directions as (dx, dy)
    directions = [
        (0, 1),  # Right
        (0, -1), # Left
        (1, 0),  # Down
        (-1, 0), # Up
        (1, 1),  # Diagonal Down-Right
        (1, -1), # Diagonal Down-Left
        (-1, 1), # Diagonal Up-Right
        (-1, -1) # Diagonal Up-Left
    ]
    
    # Helper function to check if the word exists in a given direction
    def is_word_at(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if nx < 0 or nx >= rows or ny < 0 or ny >= cols or grid[nx][ny] != word[i]:
                return False
        return True

    # Count occurrences
    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if is_word_at(x, y, dx, dy):
                    count += 1

    return count

# Example grid
grid = [
    "MMMSXXMASM",
    "MSAMXMSMSA",
    "AMXSXMAAMM",
    "MSAMASMSMX",
    "XMASAMXAMM",
    "XXAMMXXAMA",
    "SMSMSASXSS",
    "SAXAMASAAA",
    "MAMMMXMMMM",
    "MXMXAXMASX"
]

# Convert grid to a list of lists
grid = [list(row) for row in grid]

# Word to search for
word = "XMAS"

# Find occurrences
result = count_word_in_grid(grid, word)
print(f"The word '{word}' appears {result} times.")

