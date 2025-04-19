ARG BUILDPLATFORM=linux/amd64

FROM --platform=$BUILDPLATFORM python:3-alpine as test

WORKDIR /home/user/app

ENV PATH=$PATH:/home/user/.local/bin

RUN apk add --no-cache build-base linux-headers
RUN pip install --no-cache uv taskipy

COPY ./ ./

RUN pip install '.[dev]'

ARG TESTBUILD=True
ENV TESTBUILD=$TESTBUILD
RUN if [ "$TESTBUILD" = 'True' ]; then task lint; fi
RUN if [ "$TESTBUILD" = 'True' ]; then task test; fi

RUN uv build --wheel --out-dir dist

CMD ["task", "test"]

FROM --platform=$BUILDPLATFORM python:3-alpine as prod

RUN addgroup --system user && adduser --system user --ingroup user
USER user

WORKDIR /home/user/app

COPY --chown=user:user --from=test /home/user/app/dist dist

RUN pip install --no-cache dist/*.whl

CMD ["python", "-m", "{{cookiecutter.package_name}}.{{cookiecutter.module_name}}"]

