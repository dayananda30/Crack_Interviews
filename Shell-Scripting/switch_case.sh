"""
case $var in pattern|pattern1|pattern2) list of commands need to execute;;
pattern3| pattern4| pattern5) list of commands need to execute;;
pattern6) commands need to execute;;
*)
Default condition and statements need to execute
esac

"""

case $MONTH in JAN) echo "I am in JAN";;
FEB) echo "I am in FEB";;
MAR) echo "I am in MAR";;
APR) echo "I am in APR";;
MAY|JUN|JUL) echo "I am in MAY JUN JUL";;
*) echo "default case statements";;
esac


