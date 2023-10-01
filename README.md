# Cogniezer-Backend

![GitHub license](https://img.shields.io/github/license/InsiderCloud/Cogniezer-Backend)
![GitHub repo size](https://img.shields.io/github/repo-size/InsiderCloud/Cogniezer-Backend)
![GitHub issues](https://img.shields.io/github/issues/InsiderCloud/Cogniezer-Backend)
![GitHub pull requests](https://img.shields.io/github/issues-pr/InsiderCloud/Cogniezer-Backend)
![GitHub last commit](https://img.shields.io/github/last-commit/InsiderCloud/Cogniezer-Backend)

## About

This is the backend of the Cogniezer project, which is developed for the 2nd year project for the BSc Hons Computer Science degree at the University of Kelaniya. This is a REST API built using FastAPI. This API is used to predict the sentiment of a given text. The model is trained using the [samsum dataset](https://huggingface.co/datasets/samsum) and [MeetingBank-transcript dataset](https://huggingface.co/datasets/lytang/MeetingBank-transcript).


## Installation

### Clone

- Clone this repo to your local machine using
```shell
$ git clone https://github.com/InsiderCloud/Cogniezer-Backend
```

or use your own forked repo

### Setup

> setup the environment and install the dependencies

```shell
$ conda create -n cogniezer python=3.7
$ conda activate cogniezer
$ pip install -r requirements.txt
```

> configure the project with your own configurations in the following files

```shell
.
├── config
│   ├── config.yaml
├── params.yaml
.
```

> run the project

```shell
$ python main.py
```

## Usage

> To use the project, you can use the following endpoints

```shell
$ curl -X POST http://{host}:{port}/predict \
    -H 'Content-Type: application/json' \
    -d '{"text": "This is a sample text"}'
```

## Documentation

> To get the documentation of the project, you can use the following endpoints

```shell
$ curl -X GET http://{host}:{port}/docs
```

## License

MIT© [InsiderCloud](https://github.com/InsiderCloud)

---

## Aknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [HuggingFace](https://huggingface.co/)
- [Samsum dataset](https://huggingface.co/datasets/samsum)
- [MeetingBank-transcript dataset](https://huggingface.co/datasets/lytang/MeetingBank-transcript)
- [University of Kelaniya](https://www.kln.ac.lk/)