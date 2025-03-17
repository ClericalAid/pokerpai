FROM python:3.12.8-slim

WORKDIR /app

# Copy requirements and install dependencies
COPY pyproject.toml .
RUN pip install --no-cache-dir build && \
    pip install --no-cache-dir -e .

# Copy source code
COPY poker_engine/ ./poker_engine/

# Set environment variables for RabbitMQ connection
ENV RABBITMQ_HOST=localhost
ENV RABBITMQ_QUEUE=poker_engine_queue

CMD ["python", "-m", "poker_engine.message_handler"]
