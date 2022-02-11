declare -i days=31 #declaring variable days as type integer

if [[ $days -lt 1 || $days -gt 30 ]]
then
echo "Enter the correct value"
fi