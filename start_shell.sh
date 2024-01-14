#!/bin/bash

RUN pip install virtualenv
RUN virtualenv env --python=python3.8
RUN /bin/bash -c "source env/bin/activate"
RUN pip install --no-cache-dir -r requirements.txt