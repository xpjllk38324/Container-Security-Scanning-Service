import numpy as np
import copy
from multiprocessing import Process,Manager
from itertools import permutations

# Put queens
def Put_Queens():

  global chessboards_list
  list_1=[0,1,2,3,4,5,6,7]
  for i in permutations(list_1,8):
      chessboards_list.append(i)


# Check main diagonal
def Check_Main_Diagonal():

  global chessboards_list
  temp_chessboards_list = copy.deepcopy(chessboards_list)

  for i in range(len(chessboards_list)):
    chessboard = chessboards_list[i]
    chessboard_real = np.zeros((8,8),dtype=int)
    for i,j in enumerate(chessboard):
      chessboard_real[i][j] = 1

    for i in range(chessboard_real.shape[0]):
      if (np.trace(chessboard_real,offset=i) > 1):
        if chessboard in temp_chessboards_list:
          temp_chessboards_list.remove(chessboard)
      if (np.trace(chessboard_real,offset=-i) > 1):
        if chessboard in temp_chessboards_list:
          temp_chessboards_list.remove(chessboard)

  chessboards_list = temp_chessboards_list

# Check secondary diagonal
def Check_Secondary_Diagonal():

  global chessboards_list
  temp_chessboards_list = copy.deepcopy(chessboards_list)

  for i in range(len(chessboards_list)):
    chessboard = chessboards_list[i]
    chessboard_real = np.zeros((8,8),dtype=int)
    for i,j in enumerate(chessboard):
      chessboard_real[i][j] = 1
    chessboard_real = np.fliplr(chessboard_real)

    for i in range(chessboard_real.shape[0]):
      if (np.trace(chessboard_real,offset=i) > 1):
        if chessboard in temp_chessboards_list:
          temp_chessboards_list.remove(chessboard)
      if (np.trace(chessboard_real,offset=-i) > 1):
        if chessboard in temp_chessboards_list:
          temp_chessboards_list.remove(chessboard)

  chessboards_list = temp_chessboards_list

# Print result
def Print_Result(file_path):
  print("The number of solutions:",len(chessboards_list))
  print("\n")

  for chessboard in chessboards_list:
    chessboard_real = np.zeros((8,8),dtype=int)
    for i,j in enumerate(chessboard):
      chessboard_real[i][j] = 1
    with open(file_path,"a") as f:
      for row in chessboard_real:
        f.write(' '.join(map(str,row)) + '\n')
      f.write('\n')
      f.close()
    print(chessboard_real)
    print("\n")


# Main
if __name__ == '__main__':
  with Manager() as manager:
    chessboards_list = manager.list([])

    p1 = Process(target=Put_Queens())
    p1.start()
    p1.join()

    p2 = Process(target=Check_Main_Diagonal())
    p2.start()
    p2.join()

    p3 = Process(target=Check_Secondary_Diagonal())
    p3.start()
    p3.join()

    p4 = Process(target=Print_Result("Result_8Q.txt"))
    p4.start()
    p4.join()