from setuptools import find_packages, setup

package_name = 'ch03_structure_demo'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='lsh',
    maintainer_email='lishihang@live.cn',
    description='Chapter 3 example: one package with multiple nodes',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'structure_talker = ch03_structure_demo.talker:main',
            'structure_listener = ch03_structure_demo.listener:main',
        ],
    },
)
