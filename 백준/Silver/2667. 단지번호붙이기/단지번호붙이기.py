import sys

sys.setrecursionlimit(10**6)  # 재귀 깊이 설정
input = sys.stdin.readline

N = int(input().strip())  # 지도 크기
graph = [list(map(int, input().strip())) for _ in range(N)]  # 지도 정보 입력
visited = [[False] * N for _ in range(N)]  # 방문 여부 체크

dx = [-1, 1, 0, 0]  # 상하좌우 이동
dy = [0, 0, -1, 1]

def dfs(x, y):
    visited[x][y] = True  # 방문 처리
    count = 1  # 현재 집(1개) 포함

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:  # 범위 체크
            if not visited[nx][ny] and graph[nx][ny] == 1:  # 방문 안 했고 집이 있는 경우
                count += dfs(nx, ny)  # 재귀 호출하여 단지 크기 증가

    return count  # 현재 단지 크기 반환

result = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1 and not visited[i][j]:  # 집이 있고 방문 안 했을 때
            result.append(dfs(i, j))  # DFS 실행 후 단지 크기 저장

result.sort()  # 단지 크기 정렬
print(len(result))  # 총 단지 개수 출력
for num in result:
    print(num)  # 각 단지 크기 출력
