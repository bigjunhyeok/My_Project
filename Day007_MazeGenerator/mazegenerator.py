import random
import os

"""미로 생성"""
def generate_maze(width, height):
    # 미로 벽 생성
    maze = [['#'] * width for _ in range(height)]

    # DFS 방식으로 미로 생성
    def carve(x, y):
        maze[y][x] = ' '
        directions = [(0, -2), (0, 2), (-2, 0), (2, 0)]
        random.shuffle(directions)
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 1 <= nx < width - 1 and 1 <= ny < height - 1:
                if maze[ny][nx] == '#':
                    maze[ny - dy // 2][nx - dx // 2] = ' '
                    carve(nx, ny)

    carve(1, 1)
    maze[1][1] = '' # 시작
    maze[height - 2][width - 2] = '🏁'   # 끝
    return maze

"""미로 출력"""
def print_maze(maze, player_pos):
    os.system('cls' if os.name == 'nt' else 'clear')    # 콘솔 화면 삭제
    for y in range(len(maze)):
        row = ''
        for x in range(len(maze[0])):
            if (x, y) == player_pos:
                row += '🚶'
            else:
                row += maze[y][x]
        print(row)

"""mazegenerator"""
def play_maze_game():
    width, height = 5, 5  # 미로 크기 설정
    maze = generate_maze(width, height) # 미로 생성
    player_pos = [1, 1] # 플레이어 시작 위치

    while True:
        print_maze(maze, tuple(player_pos))
        move = input("이동 (WASD) : ").lower()
        dx, dy = 0, 0
        if move == 'w': dy = -1 # 위로 이동
        elif move == 's': dy = 1    # 아래로 이동
        elif move == 'a': dx = -1   # 왼쪽으로 이동
        elif move == 'd': dx = 1    # 오른쪽으로 이동
        else:
            print("❗ 잘못된 입력입니다. W, A, S, D 중 하나를 눌러주세요.")
            continue

        new_x = player_pos[0] + dx
        new_y = player_pos[1] + dy

        # 벽이 아닐 경우 이동
        if maze[new_y][new_x] != '#':
            player_pos = [new_x, new_y]

        # 도착 지점 도착 시 게임 종료
        if maze[new_y][new_x] == '🏁':
            print_maze(maze, tuple(player_pos))
            print("🎉 탈출 성공!")
            break

if __name__ == "__main__":
    play_maze_game()