# -*- coding: utf-8 -*-
#
# Copyright (C) 2018 NII.
#
# WEKO3 is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

FROM weko3-base:latest

COPY ./ .
COPY ./docker/uwsgi/ ${INVENIO_INSTANCE_PATH}

RUN ./scripts/bootstrap

USER ${INVENIO_USER_ID}
