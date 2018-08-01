.PHONY: build
build:
	$(MAKE) -C worker build

.PHONY: push
push:
	$(MAKE) -C worker push
	apex deploy

.PHONY: test
test:
	apex invoke -L to_jpg < s3_event.json
