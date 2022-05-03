from setuptools import setup

package_name = 'fsds_visuals'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Alastair Bradford',
    maintainer_email='team@qutmotorsport.com',
    description='Publishes FSDS visuals for RVIZ2',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'track = fsds_visuals.node_track:main'
        ],
    },
)