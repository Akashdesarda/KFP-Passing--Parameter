# KFP-Passing-Parameter
Passing Passing a variable(which can be used as parameter) generated from first container to next container to be used as parameter.

This is how it works:
1. 'comp1' is a container which takes a simple string and writes it to output.txt
2. Then the content inside output.txt is converted as kubeflow pipeline params which is passsed to second conatiner. 
3. String which was given as input in first container is now taken as input by second continer and printed. 

So, the overall idea here is 'How to pass some variable between two container'

<h4>Note: There are two Pipeline py files. Both are valid but pipeline.py follows more standered pythonic convention, so uesd it. 
