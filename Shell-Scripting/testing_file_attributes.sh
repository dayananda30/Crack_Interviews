"""
-f
To test for a regular file.
"""

if [[ -f /etc/hosts ]]
then
echo "Yes, file exists"
fi

"""
-d
To test for a directory
"""

if [[ -d /home/dayananda ]]
then
echo "Yes, directory exists"
fi

"""
-L
To test for symbolic link
"""

"""
-e
To test for a file , irrespective of file type
"""

"""
-r , -w and -x for execute permission
To tests for read permission of a file
"""

if [[ -r /etc/hosts ]]
then
echo "It has read permission"
fi

