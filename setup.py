#!/usr/bin/env python
# encoding: utf-8

import sys, os

from setuptools import setup, find_packages


if sys.version_info <= (2, 5):
    raise SystemExit("Python 2.5 or later is required.")

execfile(os.path.join('pulp', 'wsgi', 'graph', 'release.py'))



setup(
        name = name,
        version = version,
        
        description = summary,
        long_description = description,
        author = author,
        author_email = email,
        url = url,
        download_url = download_url,
        license = license,
        keywords = '',
        
        install_requires = [],
        
        test_suite = 'nose.collector',
        tests_require = ['nose', 'coverage'],
        
        classifiers = [
                "Development Status :: 1 - Planning",
                "Environment :: Console",
                "Intended Audience :: Developers",
                "License :: OSI Approved :: MIT License",
                "Operating System :: OS Independent",
                "Programming Language :: Python",
                "Topic :: Internet :: WWW/HTTP :: WSGI",
                "Topic :: Software Development :: Libraries :: Python Modules"
            ],
        
        packages = find_packages(exclude=['examples', 'tests', 'tests.*', 'docs']),
        include_package_data = True,
        package_data = {
                '': ['README.textile', 'LICENSE'],
                'docs': ['Makefile', 'source/*']
            },
        zip_safe = True,
        
        namespace_packages = ['pulp', 'pulp.wsgi'],
        
        entry_points = {
                # 'paste.app_factory': [
                #         'main = web.core:Application.factory'
                #     ],
                # 'paste.paster_command': [
                #         'shell = web.commands.shell:ShellCommand'
                #     ],
            }
    )
