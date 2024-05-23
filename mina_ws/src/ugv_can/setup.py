from setuptools import find_packages, setup

package_name = 'ugv_can'

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
    maintainer='jetson',
    maintainer_email='jetson@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'sender = ugv_can.scaled_offset:main',
            'converter = ugv_can.value_converter:main',
            'pub = ugv_can.can_pub2:main',
            'ps_node = ugv_can.navrover_ps4_ctrl:main',
            'odom_pub = ugv_can.odom_pub:main',
            'odom_publisher = ugv_can.odom_publisher:main',
            'first_odom_publisher = ugv_can.first_odom_publisher:main',
            'first_odom_while_pub = ugv_can.first_odom_while_pub:main',
            'odom_while_pub = ugv_can.odom_while_pub:main',
            'sample = ugv_can.sample_odom_publisher:main',
            'imu_node = ugv_can.imu:main',
            'odom_final = ugv_can.odom_final:main',
            'imu_mad = ugv_can.imu_mad:main'
        ],
    },
)
