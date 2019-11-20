from setuptools import setup

setup(name='multivector3d',
      version='0.1',
      description='Three Dimensional Multivector, based on numpy.',
      author='Colin Tinsman',
      author_email='tinsmancb@gmail.com',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3'
        ],
      packages=['multivector3d'],
      install_requires=['numpy'],
      zip_safe=False)
