#!/usr/bin/env python

from setuptools import setup

setup(
	name="bigreddy",
	version="0.1.0",
	description="BigReddy generates pseudo-philosophical and pseudo-poetic ramblings using a Markov chain.",
	author="Kailash Nadh",
	author_email="kailash@nadh.in",
	url="https://nadh.in",
	packages=["bigreddy"],
	download_url="https://github.com/rainmattertech/pykiteconnect",
	license="MIT",
	entry_points={
		'console_scripts': [
			'bigreddy = bigreddy:run'
		],
	},
	classifiers=[
		"Topic :: Games/Entertainment",
		"Natural Language :: English",
		"License :: OSI Approved :: MIT License",
		"Programming Language :: Python :: 3.3",
		"Programming Language :: Python :: 3.4",
		"Programming Language :: Python :: 3.5",
		"Topic :: Software Development :: Libraries :: Python Modules",
	],
	install_requires=["markovify"],
	include_package_data=True
)
