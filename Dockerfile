FROM alpine:latest

# Set environment variables
WORKDIR /app

# Install system dependencies
RUN apk add nodejs npm python3 curl bash rsync && \
    # Install pnpm
    curl -fsSL https://get.pnpm.io/install.sh | ENV=~/.bashrc bash - && \
    # Add pnpm to PATH
    ln -s /root/.local/share/pnpm/pnpm /usr/local/bin/pnpm

# Copy project files
COPY . /app

# Create and activate Python virtual environment, install requirements
RUN python3 -m venv /app/venv && \
    . /app/venv/bin/activate && \
    pip install --upgrade pip && \
    pip install -r requirements.lock

RUN bash ./build.sh


# Set default command
CMD ["/app/venv/bin/noaha.org"]