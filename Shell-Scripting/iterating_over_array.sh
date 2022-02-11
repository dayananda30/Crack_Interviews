declare -a users=("daya" "deepu" "nanda" "geetha")
printf "The size of the array is %s \n" ${#users[*]}

for (( i=0; i<${#users[*]}; i++ ));do
    echo users[$i]
done
