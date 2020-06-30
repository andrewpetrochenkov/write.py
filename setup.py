import setuptools

setuptools.setup(
    name='write',
    install_requires=open('requirements.txt').read().splitlines(),
    packages=setuptools.find_packages()
)
