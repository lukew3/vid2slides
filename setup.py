from setuptools import setup, find_packages

setup(
    name='vid2slides',
    version='0.0.3',
    description='Extract a slideshow from a video presentation',
    url='https://github.com/lukew3/vid2slides',
    author='Luke Weiler',
    author_email='lukew25073@gmail.com',
    license='MIT',
    packages=find_packages(),
    install_requires=['click', 'Pillow'],
    entry_points={
        'console_scripts': ['vid2slides=vid2slides.cli:cli'],
    },
)
