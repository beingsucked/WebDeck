DC = docker compose
APP_FILE = docker_compose/app.yaml
STORAGE_FILE = docker_compose/storage.yaml

.PHONY: app
app-start:
	${DC} -f ${APP_FILE} up -d

.PHONY: app-drop
app-drop:
	${DC} -f ${APP_FILE} down

.PHONY: all
all:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} up --build -d

.PHONY: all-drop
all-drop:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} down

.PHONY: storage
storage:
	${DC} -f ${STORAGE_FILE} up --build -d

.PHONY: storage-drop
storagep-down:
	${DC} -f ${STORAGE_FILE} down

.PHONY: logs
logs:
	${DC} -f ${APP_FILE} -f ${STORAGE_FILE} logs -f