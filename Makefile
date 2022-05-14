# Variables
APP_NAME=analysis-ufrn
ROOT=$(shell pwd)

## Lint
DOCKER_IMAGE_LINTER=alvarofpp/python:linter
LINT_COMMIT_TARGET_BRANCH=origin/main

# Commands
.PHONY: install-hooks
install-hooks:
	git config core.hooksPath .githooks

.PHONY: build
build: install-hooks
	@docker-compose build --pull

.PHONY: build-no-cache
build-no-cache: install-hooks
	@docker-compose build --no-cache --pull

.PHONY: lint
lint:
	@docker pull ${DOCKER_IMAGE_LINTER}
	@docker run --rm -v ${ROOT}:/app ${DOCKER_IMAGE_LINTER} " \
		lint-commit ${LINT_COMMIT_TARGET_BRANCH} \
		&& lint-markdown \
		&& lint-python"

.PHONY: shell
shell:
	@docker-compose run --rm ${APP_NAME} bash
