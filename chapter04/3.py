n, m = map(int, input().split())
x, y, d = map(int, input().split())
board = list()
for i in range(n):
  data = list(map(int, input().split()))
  board.append(data)

def rotate(degrees):
  global d
  d -= degrees
  if d < 0:
    d += 4

def new_coordinate():
  global x
  global y
  global d
  global move
  new_x = x + move[d][0]
  new_y = y + move[d][1]
  return new_x, new_y

def get_move(new_x, new_y):
  global x
  global y
  global rotate_count
  global result
  global board
  board[x][y] = 2
  x, y = new_x, new_y
  rotate_count = 0
  result += 1


move = [(-1, 0), (0, 1), (1, 0), (0, -1)]

result = 0 # number of passed block

rotate_count = 0 # when is 4, go back
while True:
  if rotate_count == 4:
    rotate(2) # turn back
    new_x, new_y = new_coordinate()
    # ocean behind
    if (new_x < 0) or (n-1 < new_x) or (new_y < 0) or (m-1 < new_y) or (board[new_x][new_y] == 1):
      break
    else:
      get_move(new_x, new_y)
      rotate(2)

  rotate(1) # rotate 90degree left
  rotate_count += 1
  # calculate new coordinate
  new_x, new_y = new_coordinate()
  if (new_x < 0) or (n-1 < new_x) or (new_y < 0) or (m-1 < new_y) or (board[new_x][new_y] == 1) or (board[new_x][new_y] == 2): continue
  
  # board[new_x][new_y] == 0
  get_move(new_x, new_y)

print(result)