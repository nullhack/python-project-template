FROM python:3.8.3-slim-buster

RUN adduser --system user

WORKDIR /home/user/app

RUN apt-get update && \
    apt-get install -y git && \
    chown user /home/user/app && \
    rm -rf /var/lib/apt/lists/*

USER user

ENV PATH /home/user/.local/bin:${PATH}

COPY src src
COPY tests tests
COPY noxfile.py .
COPY pyproject.toml .
COPY poetry.lock .
COPY .pre-commit-config.yaml .
COPY .gitignore .
COPY .flake8 .

RUN pip install nox --user && \
    nox -s install

ENTRYPOINT ["nox", "-s"]
CMD ["run"]
