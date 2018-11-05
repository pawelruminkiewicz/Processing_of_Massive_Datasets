FROM ubuntu:latest

# Install latest updates
RUN apt-get update
RUN apt-get upgrade -y

# Install your software
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install sqlite3

# Set working dir
WORKDIR .

# Copy dataset to working dir
COPY unique_tracks.txt .
COPY triplets_sample_20p.txt .

# Copy your code
COPY execute.sh .
COPY sqlite_example.sh .
COPY tasks.sh .

# Set starting command (run your code)
CMD bash execute.sh