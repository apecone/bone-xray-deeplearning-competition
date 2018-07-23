from setuptools import setup, find_packages
setup(
    name="Bone Xray Deeplearning Competition",
    version="0.1",
    packages=find_packages(),

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=[
                      'docutils == 0.14',
                      'lockfile == 0.12.2',
                      'luigi == 2.7.6',
                      'numpy==1.14.5',
                      'python-daemon == 2.1.2',
                      'python-dateutil==2.7.3',
                      'pytz==2018.5',
                      'scikit-learn==0.19.2',
                      'six==1.11.0',
                      'sklearn==0.0',
                      'tornado == 4.5.3',
                      ],

)