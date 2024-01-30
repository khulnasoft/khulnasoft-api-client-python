# Unless explicitly stated otherwise all files in this repository are licensed
# under the 3-clause BSD style license (see LICENSE).
# This product includes software developed at Khulnasoft (https://www.khulnasoft.com/).
# Copyright 2019 Khulnasoft, Inc.

import os

from setuptools import setup

version_template = """\
# Unless explicitly stated otherwise all files in this repository are licensed
# under the 3-clause BSD style license (see LICENSE).
# This product includes software developed at Khulnasoft (https://www.khulnasoft.com/).
# Copyright 2020-Present Khulnasoft, Inc.

__version__ = "{version}"
"""

# Allows the fetching of tags even from shallow clones
# https://github.com/pypa/setuptools_scm/pull/118#issuecomment-255381535
def parse_fetch_on_shallow(*args, **kwargs):
    from setuptools_scm.git import parse, fetch_on_shallow

    kwargs["pre_parse"] = fetch_on_shallow

    return parse(*args, **kwargs)


setup(
    use_scm_version={
        "local_scheme": "dirty-tag",
        "write_to": os.path.join("src", "khulnasoft_api_client", "version.py"),
        "write_to_template": version_template,
        "parse": parse_fetch_on_shallow,
    }
)
