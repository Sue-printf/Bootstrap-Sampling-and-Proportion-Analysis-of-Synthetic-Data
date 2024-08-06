Guidelines on running the Python program

* To run the Python program, ensure that you have the latest Python installed on your PC.

* Also, ensure you have the necessary libraries installed to run the code. 

* You can install them using pip, python's package installer. 

* Run the following command in your command prompt to install the packages: 
    pip install pandas numpy matplotlib

* Once the installation is successful, use the command cd to take you to where the Python file is. 

* For example, if it is in the Downloads folder, you should use the following command: 
    cd Downloads

* Run your program with:
   python bootstrap_simulation.py
 
* Your code will generate a histogram plot showing the distribution of the proportions of samples not selected in the bootstrap sampling process.

* You will also notice that the histogram is centered around 0.368 since the 'n' parameter in the 'synthetic_dataset_and_sampling' function call is set to 1000 and the 'num_trials' parameter is set to 1000 in the python code.


* The above output meets the expected requirements.


