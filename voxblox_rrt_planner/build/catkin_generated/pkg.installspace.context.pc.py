# generated from catkin/cmake/template/pkg.context.pc.in
CATKIN_PACKAGE_PREFIX = ""
PROJECT_PKG_CONFIG_INCLUDE_DIRS = "${prefix}/include".split(';') if "${prefix}/include" != "" else []
PROJECT_CATKIN_DEPENDS = "mav_msgs;mav_path_smoothing;mav_planning_common;mav_trajectory_generation_ros;roscpp;std_msgs;tf;visualization_msgs;voxblox_ros".replace(';', ' ')
PKG_CONFIG_LIBRARIES_WITH_PREFIX = "-lvoxblox_rrt_planner;/usr/lib/x86_64-linux-gnu/libompl.so".split(';') if "-lvoxblox_rrt_planner;/usr/lib/x86_64-linux-gnu/libompl.so" != "" else []
PROJECT_NAME = "voxblox_rrt_planner"
PROJECT_SPACE_DIR = "/usr/local"
PROJECT_VERSION = "0.0.0"
