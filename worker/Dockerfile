FROM amazonlinux:2016.09
WORKDIR /usr/src/app
COPY deps  ./deps
RUN sh deps/deps.sh
RUN pip install --no-cache-dir -r deps/requirements.txt
COPY src/ .
ENTRYPOINT ./entrypoint.sh
