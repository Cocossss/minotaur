#!/bin/bash
echo -e '\n\n\033[7mTest1:\033[0m'
cat ./Tests/input_data1.txt
cat ./Tests/input_file1.txt
echo -e '\n'
python3 generator.py < ./Tests/input_data1.txt

echo -e '\n\n\033[7mTest2:\033[0m'
cat ./Tests/input_data2.txt
cat ./Tests/input_file2.txt
echo -e '\n'
python3 generator.py < ./Tests/input_data2.txt

echo -e '\n\n\033[7mTest3:\033[0m'
cat ./Tests/input_data3.txt
cat ./Tests/input_file3.txt
echo -e '\n'
python3 generator.py < ./Tests/input_data3.txt

echo -e '\n\n\033[7mTest4:\033[0m'
cat ./Tests/input_data4.txt
cat ./Tests/input_file4.txt
echo -e '\n'
python3 generator.py < ./Tests/input_data4.txt

echo -e '\n\n\033[7mTest5:\033[0m'
cat ./Tests/input_data5.txt
cat ./Tests/input_file5.txt
echo -e '\n'
python3 generator.py < ./Tests/input_data5.txt

