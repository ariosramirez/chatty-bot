# Use the base image with nonroot user setup
FROM khalosa/rasa-aarch64:3.5.2
# From: https://github.com/khalo-sa/rasa-apple-silicon/blob/main/Dockerfile

LABEL authors="andresrios"

# Switch to root user
USER root

# Set working directory
WORKDIR /app

# Copy the necessary files into the container
COPY ./rasa /app

# Ensure you have spaCy installed and the Spanish language model downloaded
RUN pip install spacy
RUN python -m spacy download es_core_news_md

# Train the Rasa model
RUN rasa train

# Expose Rasa server and action server ports
EXPOSE 5005 5055

USER rasa

ENTRYPOINT ["rasa"]