FROM ubuntu:noble

# Set environment variables
ENV DEBIAN_FRONTEND=noninteractive
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y python3 python3-venv python3-pip curl gnupg nodejs rsync && \
    # Install pnpm
    curl -fsSL https://get.pnpm.io/install.sh | bash - && \
    # Add pnpm to PATH
    ln -s /root/.local/share/pnpm/pnpm /usr/local/bin/pnpm && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Copy project files
COPY . /app

# Create and activate Python virtual environment, install requirements
RUN python3 -m venv /app/venv && \
    . /app/venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.lock && \
    pip install gunicorn

RUN bash ./build.sh


# Set default command
CMD ["/app/venv/bin/noaha.org"]