from distutils.core import setup

setup(
    name='randomnumbers',
    version='0.3',
    packages=['randomnumbers'],
    license='Full freedom to distribute and use for commerical and non-commercial reasons',
    test_suite='nose.collector',
    tests_require=['nose'],
    install_requires=['numpy', 'nose'],
    author='Alfie Smith',
    author_email='alfiex1994@gmail.com'
)
