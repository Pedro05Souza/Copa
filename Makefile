UVICORN = uvicorn
APP_MODULE = controller:app
HOST = 127.0.0.1
PORT = 5500
RELOAD = --reload
TARGET_DIR = back-end
run:
	cd $(TARGET_DIR) && $(UVICORN) $(APP_MODULE) --host $(HOST) --port $(PORT) $(RELOAD)
clean:
	rm -rf __pycache__ *.pyc
.PHONY: run clean
