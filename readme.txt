With pip and python already installed

pip install python-dotenv

always set your API keys locally in .env file and add it to .gitignore on root directory

randsome_anu.py
Will create 100 files in './anu' folder as a response JSON with 1024 array of numbers containing uint16 values from 0 to 65,536

randsome_fullstring.py
Will convert all 100 JSON into a single binary string

randsome_count.py
Will count the total '0's and '1's that ANU returned

randsome.py
Will return true random integer or true random choices based on population

randsome_enlarge.py
Will use randsome.py to randomly inject '0' or '1' into the a new string that will have the same amount of '0's and '1's

References
https://quantumnumbers.anu.edu.au/
https://arxiv.org/pdf/1604.03304.pdf
