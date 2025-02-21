from setuptools import setup, find_packages

setup(
    name='modAL',
    version='0.4.1',
    author='Tivadar Danka',
    author_email='85a5187a@opayq.com',
    description='A modular active learning framework for Python3',
    license='MIT',
    url='https://modAL-python.github.io/',
    packages=setuptools.find_packages(),
    classifiers=['Development Status :: 4 - Beta'],
    install_requires=['numpy>=1.13', 'scikit-learn>=0.18', 'scipy>=0.18', 'pandas>=1.1.0'],
    python_requires='>=3.7',
)
