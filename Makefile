override SHELL := /bin/bash

.PHONY: help
help: ## Show this help message.
	@echo 'Usage:'
	@echo '  make [target] ...'
	@echo
	@echo 'Targets:'
	@grep --no-filename -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | \
	 sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'
	@echo "------------------------------------"

.PHONY: test
test: ## Run tests
	python3 -m pytest bowling_game_tests.py
