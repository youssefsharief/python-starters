from setuptools import setup

def readme():
    with open('README.md', encoding="utf-8") as f:
        return f.read()


setup(name='sample_lib',
      version='0.1',
      description='A sample library that illustrates the usage of setup.py',
      long_description=readme(),
      long_description_content_type='text/markdown',
      url='http://github.com/youssefsharief/python-setup-starter',
      author='Youssef Sherif',
      author_email='sharief@aucegypt.edu',
      license='MIT',
      packages=['sample_lib'],
      zip_safe=False)