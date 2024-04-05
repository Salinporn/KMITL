"""Lab 3D"""
col_num, row_num = map(int, input().split())
maze = []

for index in range(col_num):
    row = list(map(int, input().split()))
    maze.append(row)

def min_cookies_required(maze):
    """Minimum Cookies Required Function"""
    rows = len(maze)
    cols = len(maze[0])
    directions = (-1, 0, 1, 0, -1)
    queue = [(0, 0)]
    cookies = [[float('inf')] * cols for _ in range(rows)]
    cookies[0][0] = maze[0][0]

    while queue:
        i_val, j_val = queue.pop(0)
        for k in range(4):
            direction_a = directions[k]
            direction_b = directions[k + 1]
            x_val = i_val
            y_val = j_val
            current_cookies = cookies[i_val][j_val]

            while 0 <= x_val + direction_a < rows and 0 <= y_val + direction_b < cols:
                x_val += direction_a
                y_val += direction_b
                current_cookies += maze[x_val][y_val]
                if current_cookies < cookies[x_val][y_val]:
                    cookies[x_val][y_val] = current_cookies
                    queue.append((x_val, y_val))
    return cookies[rows - 1][cols - 1]

print(min_cookies_required(maze))
