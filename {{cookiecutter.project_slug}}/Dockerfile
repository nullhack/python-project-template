FROM python:3.8.3-slim-buster

RUN adduser --system user

WORKDIR /home/user/app

RUN apt-get update && \
    apt-get install -y git && \
    chown user /home/user/app && \
    rm -rf /var/lib/apt/lists/*

USER user

ENV PATH /home/user/.local/bin:${PATH}

COPY {{cookiecutter.package_name}} {{cookiecutter.package_name}}
COPY tests tests
COPY pyproject.toml .
COPY poetry.lock .
COPY .pre-commit-config.yaml .
COPY .gitignore .
COPY .flake8 .

RUN pip install poetry poethepoet --user && \ 
    poe install

ENTRYPOINT ["poe", "-q"]
CMD ["run"]
