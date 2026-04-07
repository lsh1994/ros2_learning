from setuptools import find_packages, setup

package_name = 'ch04_topic_demo'

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
    description='Chapter 4 example: topic publisher and subscriber',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'topic_talker = ch04_topic_demo.talker:main',
            'topic_listener = ch04_topic_demo.listener:main',
        ],
    },
)
