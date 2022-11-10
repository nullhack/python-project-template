ARG BUILDPLATFORM=linux/amd64
ARG BUILDTAG=3-alpine

FROM --platform=$BUILDPLATFORM python:$BUILDTAG as base_build

WORKDIR /home/user/app

COPY {{cookiecutter.package_name}} {{cookiecutter.package_name}}
COPY tests tests
COPY pyproject.toml .
COPY poetry.lock .
COPY README.md .
COPY .pre-commit-config.yaml .
COPY .gitignore .
COPY .flake8 .

ENV PATH=$PATH:/home/user/.local/bin

FROM base_build as test

ARG TESTBUILD=True
ENV TESTBUILD=$TESTBUILD

RUN pip install --no-cache poetry poethepoet
RUN poetry config --no-cache
RUN if [ "$TESTBUILD" = 'True' ]; then poe install-dev; fi
RUN poetry build --format=wheel
RUN poetry export --only main -f requirements.txt --without-hashes --output requirements.txt
RUN if [ "$TESTBUILD" = 'True' ]; then poe test; fi

ENTRYPOINT ["poe", "-q"]
CMD ["test"]

FROM --platform=$BUILDPLATFORM python:$BUILDTAG as prod

RUN addgroup --system user && adduser --system user --ingroup user
USER user

WORKDIR /home/user/app

COPY --chown=user:user --from=test /home/user/app/requirements.txt requirements.txt
COPY --chown=user:user --from=test /home/user/app/dist dist

RUN pip install --no-cache -r requirements.txt dist/*.whl --user


ENTRYPOINT ["python", "-m"]
CMD ["{{cookiecutter.package_name}}.{{cookiecutter.module_name}}"]

