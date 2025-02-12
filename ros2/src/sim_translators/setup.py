from glob import glob
import os

from setuptools import setup

package_name = "sim_translators"

setup(
    name=package_name,
    version="0.0.0",
    packages=[package_name],
    data_files=[
        ("share/ament_index/resource_index/packages", ["resource/" + package_name]),
        ("share/" + package_name, ["package.xml"]),
        (os.path.join("share", package_name), glob("launch/*.launch.py")),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="Alistair English, Alastair Bradford",
    maintainer_email="team@qutmotorsport.com",
    description="Translates FSDS topics to Driverless topics",
    license="MIT",
    tests_require=["pytest"],
    entry_points={
        "console_scripts": [
            "control_to_sim = sim_translators.node_control_to_sim:main",
            "map_to_cone_detection = sim_translators.node_map_to_cone_detection:main",
            "map_to_path = sim_translators.node_map_to_path:main",
            "sim_to_odom = sim_translators.node_sim_to_odom:main",
            "sim_to_cam = sim_translators.node_sim_to_cam:main",
            "sim_to_velodyne = sim_translators.node_sim_to_velodyne:main",
            "sim_transform = sim_translators.node_transform:main",
        ],
    },
)
