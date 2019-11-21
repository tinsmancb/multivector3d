from setuptools import setup

with open('README.md', 'r') as fh:
    long_description = fh.read()

setup(name='multivector3d',
      version='0.1.1',
      description='Three Dimensional Multivector, based on numpy.',
      long_description=long_description,
      long_description_content_type='text/markdown',
      author='Colin Tinsman',
      author_email='tinsmancb@gmail.com',
      url='https://github.com/tinsmancb/multivector3d',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3'
        ],
      packages=['multivector3d'],
      install_requires=['numpy'],
      zip_safe=False)
