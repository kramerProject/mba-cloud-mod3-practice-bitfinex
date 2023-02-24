## Description

This a practical activity part of the MBA in Data Engineering from XPE. It is expected to create a data proccess using docker and kubernetes. In this case was created an endpoint that accesses bitfinex api an returns criptocoin information in json format. 

## What was Done

- [X] Develop a data process api
- [X] Develop the Dockerfile for encapsulating the solution in
a docker image
- [X] Build the docker image and push it to some repository
images (public or private)
- [X] Implement a manifest
- [X] Run kubectl commands to deploy the solution to a cluster
kubernetes
- [X] Verify that the solution was successfully deployed
- [X] Check logs   


## Requirements

If you wish to run this api you should have **docker**, **kubernetes** and a docker hub account. Follow the steps bellow.

1. Clone this repo

```
git clone 

cd mba-cloud-mod3-practice-bitfinex
```

2. Build the image locally

```
docker build -t {{YOU_APP_NAME_HERE}:1.0.0 .
```

3. Run the container locally

After the command bellow you can check your browser on localhost:5000/tickers
to see the coins

```
docker run -p 5000:5000 --rm -d {{YOU_APP_NAME_HERE}:1.0.0
```

4. Create the repository on docker hub

5. Tag your image

```
docker tag {{YOU_APP_NAME_HERE}:1.0.0 {{YOUR_DOCKER_HUB_USER}}/mycoins:1.0.0
```

6. Publish your image on docker hub

```
docker push {{YOUR_DOCKER_HUB_USER}}/{{YOU_APP_NAME_HERE}:1.0.0
```
If you wish to do the same process but using kubernetes you can continue the following steps

7. Start minikube

```
minikube start
```

8. Create a name space called site

```
kubectl create ns site
```

9. In the project root run

```
kubectl apply -f manifests/
```

10. Connect your local port with the container running on kubernetes

```
kubectl port-forward pod/mycoins -n site 5000:5000
```


11. Check your browser on localhost:5000/tickers

Helpful **docker** commands:

1. Search for images

```
docker search {{IMAGE_NAME}}
```

2. Listing images

```
docker images
```

3. Listing local active containers

```
docker ps
```

4. Getting an image from docker hub

```
docker pull {{IMAGE_NAME}}
```

5. Building an image with an specific tag

```
docker build -t {{IMAGE_NAME}}:1.0.0 .
```

6. Running an image an associate a local port with containers port, the -rm
will remove the container after is finished.

```
docker run -p {{LOCAL_PORT}}:{{CONTAINER_PORT}} --rm -d {{IMAGE_NAME}}:1.0.0
```