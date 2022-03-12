#!/bin/bash

# by lukas , 20/11-2021


if [ "$1" == "" ]
then
echo "
	usage: ./pingsweep.sh [network-addr]
      example: ./pingsweep.sh 192.168.52

      						"
else
	# Iterate 1-254
	# Grab successful ping and cut with " " as delimiter
	# Fetch the fourth field
	# Delete the final character from each line using sed
echo "
Sweeping....
"
for x in {1..254}
do
	ping -c 1 $1.$x | grep "64 bytes" | cut -d" " -f4 | sed 's/.$//' 
done
fi
