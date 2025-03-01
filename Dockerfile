FROM python:3.12-slim

# install system dependencies needed for playwright and other libraries

RUN apt-get update && apt-get install -y \
    curl \
    wget \
    gnupg \
    libnss3 \
    libx11-6 \
    libxcomposite1 \
    libxcursor1 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpangocairo-1.0-0 \
    && rm -rf /var/lib/apt/lists/*

# set the work directory
WORKDIR /app

# copy the requirements file
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# copy the rest of the files
COPY . .

# install playwright browsers (required by crawl4ai)
RUN playwright install

EXPOSE 8501

#start the streamlit app
CMD ["streamlit", "run", "app.py", "--server.enableCORS", "false"]