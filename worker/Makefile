ECR=202305538718.dkr.ecr.us-east-1.amazonaws.com
IMAGE=biorender/image_converter

.PHONY: auth
auth:
	@eval $(shell aws ecr get-login --no-include-email --region us-east-1)

.PHONY: build
build:
	docker build -t ${IMAGE} .

.PHONY: test
test: build
	docker run --rm -v ${PWD}:/output_dir -e "S3_BUCKET=biorender-jpg-test" -e "S3_KEY=bar" -it ${IMAGE}:latest

.PHONY: push
push: auth build
	docker tag ${IMAGE}:latest ${ECR}/${IMAGE}:latest
	docker push ${ECR}/${IMAGE}:latest
