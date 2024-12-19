# PatrowlCore
Project that handles requests between Microservices


### HOW TO RUN THE PROJECT

- Change `LLM_PROJECT_ADDR` & `LLM_PROJECT_X_API_KEY` variables in settings.py

```bash
source scripts/prepare_dev.sh
python3 manage.py runserver
```



### Development

```bash
sh scripts/generate_openapi_schema.sh
```

```bash
source scripts/prepare_dev.sh
source scripts/pre-commit-check.sh
```