import setuptools

if __name__ == '__main__':
    setuptools.setup(
        name='pyskai',
        version='0.1',
        packages=setuptools.find_packages(),
        install_requires=['pandas'],
        author='Galen Terziysky',
        author_email='galen[dot]terziysky[at]somewhere[dot]com',
        description='''PySkai is a set of tools to help developers use AWS cloud services with ease''',
        long_description='''PySkai is a set of tools to help developers use AWS cloud services with ease''',
        # Homepage url for the package
        url='https://github.com/gterziysky/pyskai',
    )
