

fetch-spec:
	wget http://127.0.0.1:8001/api/openapi.json -O openapi.json


build: fetch-spec
	docker run --rm -v ${PWD}:/local openapitools/openapi-generator-cli generate     \
	-i /local/openapi.json     \
	-g python     \
	-o /local/     \
	-p packageName=kitchenai_python_sdk && \
	sudo chown -R 1000.1000 . 