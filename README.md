# Docker Project

This project build a Docker container from scratch.  
It pushes the image to Amazon Elastic Container Registry(ECR) and Docker Hub. 
Deploy it to Amazon Elastic Container Container Service(ECS). 

Deploy it in Kubernetes.

## Reference

Source code: [noahgift/container-from-scratch-python](https://github.com/noahgift/container-from-scratch-python).  
Source code: [noahgift/container-revolution-devops-microservices](https://github.com/noahgift/container-revolution-devops-microservices).  


## How to use

To build a docker image and push it to registry, you can follow these steps:

### Set up a project

Launch AWS Cloud9, choose or create an environment.  
Create ssh-keys and upload it to Github.  ``ssh-keygen -t rsa``  
Create a new repo on github, git clone it to your AWS local and cd into it.  
Create all related files, including **Dockerfile, Makefile, requirements.txt, app.py**.  
(optional) Install hadolint.  

```
sudo wget -O /bin/hadolint https://github.com/hadolint/hadolint/releases/download/v1.19.0/hadolint-Linux-x86_64
sudo chmod +x /bin/hadolint
```

(optional) Test hadolint after you call "make install" and make the app run locally.  ```make lint```  

### Run this app locally

Create a virtual environment and activate it. (To deactivate it, run "deactivate") 

```
python3 -m venv ~/.dockerproj
source ~/.dockerproj/bin/activate
```

Install the required packages. ```make install```  
Run this app. ```python main.py```  

### Build an image and run a container

We will pull down an official base image, package up our own software and runtime on top of it.  
Build an image accoridng to the setup in Dockerfile, name it "app", tag it "v1".  

```
docker build -t app:v1 .
```

```
docker run -it app:v1 bash 
```

```
python main.py
exit
```

### Push to Docker Hub

Create a new repository "dockerproj" on DockerHub.  
Login to DockerHub in your AWS local.  

```
docker login
```

Tag your image with hostname and self defined ```tag-name```.  

```
docker tag app:v1 qishen98/dockerproj:[tag-name]
```

Push it to Docker Hub.

```
docker push qishen98/dockerproj:[tag-name]
```

### Pull from Docker Hub

```
docker pull qishen98/[repo-name]:[tag-name]
```

### Push to Amazon ECR

Open Amazon ECR console.  
Create a repository, call it "dockerproj" and enable "Scan on push".  
Click on the newly created repo, and click on **"view push commands"**. It will show commands like below:  
First authenticate.  
Then build docker image.  
Then tag the image.  
Finally push this image to AWS repository.  
The command will be like:  

### Deploy to Amazon ECS fargate

Make sure you have pushed your image to Amazon ECR.  
Open ECS and "get started".  
"Container definition", choose to configure your custom container image. (You can get the image from Amazon ECR)  
 "Define your service", check load balancer for your service.  
 "Configure your cluster", name your cluster.  

And you can see the service is running and access the public IP.

### Kubernetes deployment

```
kubectl apply -f api.yaml
```

If working locally, e.g. using `minikube`, use port forwarding to expose the service:

```
kubectl port-forward service/dockerproj-svc 8080
```

To scale the deployment, apply a HorizontalPodAutoscaler. Either:

```
kubectl apply -f autoscale.yaml
```

or:

```
kubectl autoscale deployment dockerproj --cpu-percent=50 --min=1 --max=10
```
