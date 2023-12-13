from setuptools import find_packages, setup

package_name = 'my_robot_controller'

data_files = []
data_files.append(('share/' + package_name + '/launch', ['launch/robot_launch.py']))

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/robot_launch.py'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ale',
    maintainer_email='aledeum.saf@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest', 'setuptools', 'launch'],
    entry_points={
        'console_scripts': [
        	"test_node = my_robot_controller.my_first_node:main",
            "draw_circle = my_robot_controller.draw_circle:main",
            "pose_subscriber = my_robot_controller.subscriber:main",
            "teleop = my_robot_controller.teleop:main"
        ],

        'launch.frontend.launch_extension': ['launch_ros = launch_ros'],
    },
)
