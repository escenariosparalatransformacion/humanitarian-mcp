#!/usr/bin/env python3
"""
Setup script for Humanitarian Negotiation MCP Package

This file is kept for backwards compatibility and for users who prefer setup.py.
For new installations, pyproject.toml is recommended.

Usage:
    pip install -e .
    pip install -e ".[http]"
    pip install -e ".[dev]"
    pip install -e ".[all]"
"""

from setuptools import setup, find_packages
import os

# Read the contents of README file
this_directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

# Read requirements
with open(os.path.join(this_directory, 'requirements_mcp.txt'), encoding='utf-8') as f:
    requirements = [line.strip() for line in f if line.strip() and not line.startswith('#')]

setup(
    name='humanitarian-negotiation-mcp',
    version='1.0.0',
    author='Humanitarian MCP Contributors',
    author_email='contact@humanitarian-mcp.org',
    description='MCP server for humanitarian negotiation analysis using proven methodologies',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/humanitarian-negotiation-mcp',
    project_urls={
        'Bug Tracker': 'https://github.com/yourusername/humanitarian-negotiation-mcp/issues',
        'Documentation': 'https://github.com/yourusername/humanitarian-negotiation-mcp#readme',
    },
    packages=find_packages(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Intended Audience :: Other Audience',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Programming Language :: Python :: 3.13',
        'Topic :: Software Development :: Libraries',
        'Topic :: Office/Business',
        'Topic :: Communications',
    ],
    python_requires='>=3.10',
    install_requires=requirements,
    extras_require={
        'http': [
            'fastapi>=0.100.0',
            'uvicorn>=0.24.0',
        ],
        'dev': [
            'pytest>=7.4.0',
            'pytest-asyncio>=0.21.0',
            'pytest-cov>=4.1.0',
            'black>=23.0.0',
            'isort>=5.12.0',
            'mypy>=1.4.0',
            'ruff>=0.0.285',
        ],
    },
    entry_points={
        'console_scripts': [
            'humanitarian-mcp=humanitarian_negotiation_mcp:main',
            'humanitarian-mcp-http=http_server:main',
        ],
    },
    include_package_data=True,
    zip_safe=False,
)
