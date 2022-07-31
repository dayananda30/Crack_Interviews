if [[ ! $1 ]]; then
        echo "Branch name as argument is required"
fi
isReleaseBranch=false
if [[ $1 == 202* ]] ; then
        echo "It is a release branch";
        export isReleaseBranch=true
fi
echo $isReleaseBranch
export isReleaseBranch=false