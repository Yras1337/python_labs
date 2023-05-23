FROM python
WORKDIR /lab1
COPY . .
CMD ["python", "lagb1/main.py"]