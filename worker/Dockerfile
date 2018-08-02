FROM amazonlinux:2016.09
WORKDIR /usr/src/app
COPY deps/deps.sh  ./deps/deps.sh
RUN sh deps/deps.sh
COPY deps/requirements.txt  ./deps/requirements.txt
RUN pip install --no-cache-dir -r deps/requirements.txt
COPY deps/etc/ImageMagick/policy.xml /etc/ImageMagick/policy.xml
COPY src/ .
ENTRYPOINT ./entrypoint.sh
