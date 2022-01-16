
aws ecr get-login-password --region eu-central-1 | docker login --username AWS --password-stdin 107292555468.dkr.ecr.eu-central-1.amazonaws.com

docker pull 107292555468.dkr.ecr.eu-central-1.amazonaws.com/spark/emr-6.2.0-20210129

## build custom docker image for deployments
docker build -t emr6.2_custom .