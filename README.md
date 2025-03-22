# TODO Application With Lato 🚀

This is a sample application built using the Lato microframework for Python.  It demonstrates basic usage of Lato, including creating an application, defining commands, and implementing command handlers.

## Introduction

[Lato](https://lato.readthedocs.io/en/latest/) is a microframework for building modular Python applications. It provides a simple and flexible way to organize your code into reusable components. This example showcases how to use Lato to create a simple greeting application.

## Features

*   Uses the Lato microframework.
*   Demonstrates defining commands and handlers.
*   Includes dependency injection.
*   Provides a basic command-line interface.

## Installation

1.  Make sure you have Python 3.11 or higher installed.
2.  Install Lato:

    ```
    poetry install
    ```

## Usage

1.  Save the code above as `main.py`.
2.  Run the application from your terminal:

    ```
    uvicorn api:api --reload
    ```

## Test API Endpoint

To test the API endpoint, you can use the following `curl` command:

```bash
    curl -X 'GET'
    'http://localhost:8000/'
    -H 'accept: application/json'
```