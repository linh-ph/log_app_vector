FROM debian:latest

# Install dependencies
RUN apt-get update && apt-get install -y \
    curl \
    net-tools

# Download and install Vector
# for mac m1
# RUN curl -LO https://packages.timber.io/vector/latest/vector-aarch64-unknown-linux-gnu.tar.gz && \
#     tar -xzf vector-aarch64-unknown-linux-gnu.tar.gz && \
#     mv vector-aarch64-unknown-linux-gnu/bin/vector /usr/local/bin/vector && \
#     rm -rf vector-aarch64-unknown-linux-gnu vector-aarch64-unknown-linux-gnu.tar.gz

RUN curl -LO https://packages.timber.io/vector/latest/vector-x86_64-unknown-linux-gnu.tar.gz && \
    tar -xzf vector-x86_64-unknown-linux-gnu.tar.gz && \
    mv vector-x86_64-unknown-linux-gnu/bin/vector /usr/local/bin/vector && \
    rm -rf vector-x86_64-unknown-linux-gnu vector-x86_64-unknown-linux-gnu.tar.gz
# Copy the configuration file
COPY vector.toml /etc/vector/vector.toml

# Expose the necessary port
EXPOSE 8686

# Set the entrypoint
ENTRYPOINT ["/usr/local/bin/vector", "--config", "/etc/vector/vector.toml"]