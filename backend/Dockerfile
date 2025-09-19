FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN addgroup --system appgroup && adduser --system --ingroup appgroup appuser
RUN chown -R appuser:appgroup /app
USER appuser
ENV PYTHONUNBUFFERED=1
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8000", "--workers", "2"]
