.PHONY: activate
activate:
	@if [ -f ".venv/bin/activate" ]; then \
		printf 'source .venv/bin/activate\n'; \
	elif [ -f "venv/bin/activate" ]; then \
		printf 'source venv/bin/activate\n'; \
	else \
		echo "No virtualenv found (.venv or venv). Create one with: python3 -m venv .venv"; exit 1; \
	fi