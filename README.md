# Cipher Break
A winter project to break a cipher using some basic cryptanalysis techniques.

Notice that we have that each DNA cipher is of the form "ZABCDEFGHIJKLMOPQRSTUVWXY," which will be the DNA strand in our project. We want to find the closest DNA strand to the correct DNA strand that outputs the appropriate sentence. 

## Getting Started

### Using the GUI 

***Note:*** With this configuration, the GUI will output all 26 possible decyphered combinations of the cyphered text. If you want it to print just the one correct english output, you will need to download the Enchant library which uses C++. Installation is explained in the **Optional Enchant Library** section below. 

Simply run the gui_cypher.py program and the GUI will initialize and launch. 

Enter your encrypted text in the "Encrypted Text" entry box. When you hit the "Decrypt!" button below this field, the program will output all possible combinations of the decyphered text. 

## Optional C++ Enchant Library

With the Enchant library, the program will try to "guess" the best outcome. The guessing method is by going through each possible Caesar Cipher permutation, and using the enchant library finding the guess which has the most English words. 

### Installation Guide

Start by pulling the file from Github, and then go to the directory. Once in the directory, follow the directions below.

For Linux/Mac:

Run the command

```
pip install -r requirements.txt
```

For Windows:

Follow the directions for installing PyEnchant [here](http://pythonhosted.org/pyenchant/download.html). 


## Authors

* **James Marshall Reber** 
* **Drake White**

## Acknowledgements
* [PyEnchant](http://pythonhosted.org/pyenchant/)
* [J Duncan, IU Informatics](https://www.sice.indiana.edu/all-people/profile.html?profile_id=193)



