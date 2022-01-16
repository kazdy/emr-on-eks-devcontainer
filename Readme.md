# Local development setup for EMR on EKS 

1. install docker desktop
1. install vscode
1. install vscode remote - container extension https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers
1. login to aws ecr: `aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 107292555468.dkr.ecr.eu-central-1.amazonaws.com`
1. in vscode run command `remote-containers:rebuild container` (you can also click on the remote-container extension icon)
1. choose python interpreter located at `usr/bin/python3`

VSCode should automatically pick up configurations.
You can run main.py from vscode using `Run > Run without debugging` to run spark code inside the container.

## Use AWS services
S3 and Glue Data Catalog can be accessed by spark job.
Specify env variables in `.devcontainers/Dockerfile`

## build custom docker image for deployments
docker build -t emr6.2_custom .
