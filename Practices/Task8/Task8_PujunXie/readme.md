# Practice Task8 Report
by Pujun Xie

## Problem A: Key Word in Context (KWIC)
In this problem, I use Method 3: Pipes-and-filters. The software architecture diagram is below:

![image](https://github.com/xpjllk38324/Container-Security-Scanning-Service/blob/main/Practices/Task8/Task8_PujunXie/figure/KWIC.svg)

The code of problem a is in [Key Word in Context Code](KWIC.py). This code put every functions in different threads as filters and use the class of Pipeline as pipe. I use module of multiprocessing.Queue for threads communication. You need to enter the filepath of input file and output file in main fuction. 

### Input and Output
The Running example is below: We use the [KWIC orignal text](Orignal_KWIC.txt) as input and get [KWIC result text](Result_KWIC.txt) as output.

![image](https://github.com/xpjllk38324/Container-Security-Scanning-Service/blob/main/Practices/Task8/Task8_PujunXie/figure/KWIC.png)

## Problem B: Eight Queens (8Q)
In this problem, I use the Method 2: Main/Subroutine with stepwise refinement (also Shared Data). The software architecture diagram is below:

![image](https://github.com/xpjllk38324/Container-Security-Scanning-Service/blob/main/Practices/Task8/Task8_PujunXie/figure/8Q.svg)

The code of problem b is in [Eight Queens Code](8Q.py). This code put every functions in different processes and use multiprocessing manager to share the data.
You need to enter the filepath of output file in main fuction.

### Input and Output
The Running example is below: We get [8Q result text](Result_8Q.txt) as output file and also get the output answer in the terminal
which includes the number of the 8Queen solutions and 8Queen solutions.

![image](https://github.com/xpjllk38324/Container-Security-Scanning-Service/blob/main/Practices/Task8/Task8_PujunXie/figure/8Q.png)

## The compare of the solution
