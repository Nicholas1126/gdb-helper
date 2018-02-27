from setuptools import setup, find_packages

setup(
    name='gdbhelper',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'pwntools',
        'psutil'
    ],
    url='https://github.com/miaouPlop/gdb-helper',
    license='MIT',
    author='miaouPlop',
    author_email='yorick.lesecque@gmail.com',
    description='GDB lightweight instrumentation'
)
