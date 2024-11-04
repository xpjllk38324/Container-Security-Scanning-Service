# Practice Task8 Report
by Pujun Xie

## Problem A: Key Word in Context (KWIC)
In this problem, I use Method 3: Pipes-and-filters. 

###  software Architecture Diagram
The software architecture diagram is below:

![image](https://github.com/xpjllk38324/Container-Security-Scanning-Service/blob/main/Practices/Task8/Task8_PujunXie/figure/KWIC.svg)

The code of problem a is in [Key Word in Context Code](KWIC.py). This code put every modules in different threads as filters and use the class of Pipeline as pipe. I use module of multiprocessing.Queue for threads communication. 

### Input and Output
You need to enter the filepath of input file and output file in main fuction. The Running example is below: We use the [KWIC orignal text](Orignal_KWIC.txt) as input and get [KWIC result text](Result_KWIC.txt) as output.

![image](https://github.com/xpjllk38324/Container-Security-Scanning-Service/blob/main/Practices/Task8/Task8_PujunXie/figure/KWIC.png)

### How to run the code

1. Clone from the Github repository.
2. Write the input file Orignal_KWIC.txt.
3. Run the code with the following command:

```
python3 KWIC.py
```

## Problem B: Eight Queens (8Q)
In this problem, I use the Method 2: Main/Subroutine with stepwise refinement (also Shared Data). 

###  software Architecture Diagram
The software architecture diagram is below:

![image](https://github.com/xpjllk38324/Container-Security-Scanning-Service/blob/main/Practices/Task8/Task8_PujunXie/figure/8Q.svg)

The code of problem b is in [Eight Queens Code](8Q.py). This code put every modules in different processes and use multiprocessing manager to share the data.

### Input and Output
You need to enter the filepath of output file in main fuction. The Running example is below: We get [8Q result text](Result_8Q.txt) as output file and also get the output answer in the terminal
which includes the number of the 8Queen solutions and 8Queen solutions.

![image](https://github.com/xpjllk38324/Container-Security-Scanning-Service/blob/main/Practices/Task8/Task8_PujunXie/figure/8Q.png)

### How to run the code

1. Clone from the Github repository.
2. Run the code with the following command:

```
python3 8Q.py
```

## The compare of the solution

| Problem | Center-aligned | Right-aligned |
| :---         |     :---:      |          ---: |
| Key Word in Context   | git status     | git status    |
| Eight Queens     | git diff       | git diff      |
