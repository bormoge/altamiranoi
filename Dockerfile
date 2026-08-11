## -*- dockerfile-image-name: "altamiranoi:latest" -*-

# Tested with podman
# podman build -t altamiranoi:latest .
# podman run --rm -v "$HOME:$HOME" -e HOME="$HOME" --name altamiranoi altamiranoi:latest

# You can pass args like this: podman run --rm -v "$HOME:$HOME" -e HOME="$HOME" altamiranoi:latest --version

# .bashrc alias:
# alias altamiranoi='podman run -v "$HOME:$HOME" -e HOME="$HOME" altamiranoi:latest'

# Note that if you use arguments those commands will be considered different containers
# (e.g. altamiranoi --help and altamiranoi --version would be different containers).

FROM python:3.13 as build
WORKDIR /altamiranoi

# Copy the metadata
# COPY pyproject.toml ./

# Copy the source
# COPY src ./src

# Copy all the files
COPY ./ ./

# Install the package
RUN pip3 install --no-cache-dir --upgrade pip
RUN pip3 install --no-cache-dir .

# Container entrypoint
ENTRYPOINT ["altamiranoi"]
