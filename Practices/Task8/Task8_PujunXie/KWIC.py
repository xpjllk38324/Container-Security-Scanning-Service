import threading
import multiprocessing

# Create a queue for thread communication
data_queue = multiprocessing.Queue()

# Input_
def Input_(file_path):
  data = []
  try:
    with open(file_path, "r") as f:
      for line in f.readlines():
        line = line.strip('\n')
        data.append(line.split())
  except IOError:
    print("Error: Failed to read")
  else:
    data_queue.put(data)
    print("Success to read.")

# Move_
def Move_():
  data = data_queue.get()
  data_new = []
  for str_s in data:
    for i in range(len(str_s)):
        data_new.append(str_s[i:]+str_s[:i])

  data_queue.put(data_new)

# Sort_
def Sort_():
  data = data_queue.get()
  data_new = sorted(data)
  data_queue.put(data_new)

# Output_
def Output_(file_path):
  data = data_queue.get()
  try:
    with open(file_path, 'w') as f:
      for i,j in enumerate(data):
        if i != (len(data)-1):
          f.write(str(j) + '\n')
        else:
          f.write(str(j))
      f.close()

  except IOError:
    print("Error: Failed to write.")
  else:
    print("Success to write.")

# The class of pipeline
class Pipeline():

  def __init__(self,i,o):
    self.threadA = threading.Thread(target=Input_(i))
    self.threadB = threading.Thread(target=Move_())
    self.threadC = threading.Thread(target=Sort_())
    self.threadD = threading.Thread(target=Output_(o))

  def run(self):
    self.threadA.start()
    self.threadA.join()
    self.threadB.start()
    self.threadB.join()
    self.threadC.start()
    self.threadC.join()
    self.threadD.start()
    self.threadD.join()


# Main
def main():
    pipeline = Pipeline("Orignal_KWIC.txt","Result_KWIC.txt")
    pipeline.run()

if __name__ == '__main__':
    main()
