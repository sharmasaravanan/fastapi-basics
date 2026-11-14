# part-1 pulling base python interpreter
FROM python:3.9-slim

# part-2 installing libraries
# step-1 creating working directory
WORKDIR /app

#step-2 copy everything into workdir
COPY requirements.txt .

# step-3 install libraries
RUN pip install -r requirements.txt

# part-3 setting up our application
COPY fastapi_power_app.py .

EXPOSE 8000

# command to run our application
CMD ["uvicorn", "fastapi_power_app:app", "--host", "0.0.0.0", "--port", "8000"]