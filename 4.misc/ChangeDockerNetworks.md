https://stackoverflow.com/questions/54720587/how-to-change-the-network-of-a-running-docker-container

Note: Only works with bridge networks

docker network disconnect bridge container_name
docker network create --driver bridge alpine-net
docker network connect alpine-net container_name