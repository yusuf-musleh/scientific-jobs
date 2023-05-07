# README

This is a basic Python app that runs a job worker powered by [pyworker](https://github.com/yusuf-musleh/pyworker) that processes jobs that are enqueued from Ruby on Rails's [DelayedJob](https://github.com/collectiveidea/delayed_job).

## Getting Started

Make sure you have the latest Python version installed.

Install the requirements:

```sh
$ pip install -r requirements.txt
```

(Optional) See various metrics on NewRelic, define the following Environment Variables:

- **NEW_RELIC_LICENSE_KEY**
- **NEW_RELIC_APP_NAME**

Run the worker

```sh
$ python main.py
```