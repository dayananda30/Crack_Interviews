#OR statement or double vertical bar
#The second command only runs if the first fails
docker pull ${docker_image} || docker build -t ${docker_image} -f Dockerfile

echo hello || echo bye
#Output hello

#AND statement or double ampersand
#Second command executes only if the first command succeeds.
docker build -t ${docker_image} -f Dockerfile && docker push ${docker_image}

echo hello && echo bye
#hello
#bye



