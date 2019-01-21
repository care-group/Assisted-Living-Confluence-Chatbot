import re

import string
from string import punctuation

Expected = "Hello, I am going to work/employment using an einstein-rosen bridge! Will you be here -fully dressed- when I come back? If not (which would be strange), please die."

Expected = Expected.replace('/',' ')#turns things like "either/or" into things like "either or"

Expected = Expected.replace('-',' ')#turn things like "high-capacity" into things like "high capacity"

Expected = Expected.translate(str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ","abcdefghijklmnopqrstuvwxyz",string.punctuation))#strip out all puctuation, and make everything lower-case

Expected = re.sub("[ ]+"," ",Expected)#remove multiple spacing

print(Expected)

#total expression: re.sub("[ ]+"," ",Expected.replace('/',' ').replace('-',' ').translate(str.maketrans("ABCDEFGHIJKLMNOPQRSTUVWXYZ","abcdefghijklmnopqrstuvwxyz",string.punctuation)))
