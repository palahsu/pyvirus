#This script make unlimited folders!

import os

counter = 1

while True:
    os.mkdir('folder{}'.format(str(counter)))
    counter += 1
    
