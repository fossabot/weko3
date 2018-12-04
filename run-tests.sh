#!/usr/bin/env bash
# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 NII.
#
# WEKO3 is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

# Ignoring flask-admin XSS vulnerability 36437, remove when
# https://github.com/flask-admin/flask-admin/pull/1699 is merged an released.
pipenv check --ignore 36437 && \
pipenv run pydocstyle weko3 tests docs && \
pipenv run isort -rc -c -df -s version/ -s versions/ && \
pipenv run check-manifest --ignore ".travis-*,docs/_build*" && \
pipenv run sphinx-build -qnNW docs docs/_build/html && \
pipenv run test
