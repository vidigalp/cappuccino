from setuptools import setup

with open("README.md", "r") as fp:
    six_long_description = fp.read()

setup(
    name='cappucino',
    version='0.1.4',
    packages=['Cappucino'],
    url='https://github.com/vidigalp/cappucino',
    license='',
    author='vidigalp',
    author_email='pedro.vidigal@instaclustr.com',
    description='Java GC Log Parser written in Python',
    long_description=six_long_description,
    long_description_content_type="text/markdown",
    install_requires = [
                           'numpy',
                           'pandas',
                           'python-dateutil',
                           'pytz',
                           'six',
                           'tqdm'
                       ],
)
