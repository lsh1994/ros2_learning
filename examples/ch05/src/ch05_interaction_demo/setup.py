from setuptools import find_packages, setup

package_name = 'ch05_interaction_demo'

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
    description='Chapter 5 example: services, actions and parameters',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'status_server = ch05_interaction_demo.status_server:main',
            'param_node = ch05_interaction_demo.param_node:main',
            'fibonacci_server = ch05_interaction_demo.fibonacci_server:main',
            'fibonacci_client = ch05_interaction_demo.fibonacci_client:main',
        ],
    },
)
