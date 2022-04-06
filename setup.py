from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in mohamedabdulsalam/__init__.py
from mohamedabdulsalam import __version__ as version

setup(
	name="mohamedabdulsalam",
	version=version,
	description="Mohamedabdulsalam app",
	author="Mohamed Abdulsalam",
	author_email="moha2016it@gmail.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
