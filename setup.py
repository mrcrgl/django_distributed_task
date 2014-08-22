from setuptools import setup, find_packages

EXCLUDE_FROM_PACKAGES = []

setup(
    name='Distributed Task',
    version='1.0.0',
    author='Marc Riegel',
    author_email='mail@marclab.de',
    packages=find_packages(exclude=EXCLUDE_FROM_PACKAGES),
    url='http://pypi.python.org/pypi/django-distributed-task/',
    license='MIT',
    description='Django application to delegate tasks asynchronously to worker processes.',
    long_description=open('README.txt').read(),
    install_requires=[
        "Django >= 1.6",
        "pika >= 0.9.0",  # Maybe this should be optional
    ],
)
