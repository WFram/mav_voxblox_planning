set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)
cmake_minimum_required(VERSION 2.8.3)
project(voxblox_rrt_planner)

find_package(catkin_simple REQUIRED)
catkin_simple(ALL_DEPS_REQUIRED)

#add_definitions(-std=c++11)

#############
# LIBRARIES #
#############
include_directories(${OMPL_INCLUDE_DIRS})
#message(STATUS "Variable: ${OMPL_LIBRARIES}")
#message(STATUS "Variable: ${OMPL_INCLUDE_DIRS}")
#add_library(libompl SHARED IMPORTED)
#set_target_properties(libompl PROPERTIES IMPORTED_LOCATION ${OMPL_LIBRARIES})
cs_add_library(${PROJECT_NAME}
  src/voxblox_ompl_rrt.cpp
  src/voxblox_rrt_planner.cpp
)
target_link_libraries(${PROJECT_NAME} ${OMPL_LIBRARIES})

############
# BINARIES #
############
cs_add_executable(voxblox_rrt_planner_node
  src/voxblox_rrt_planner_node.cpp
)
target_link_libraries(voxblox_rrt_planner_node ${PROJECT_NAME})

##########
# EXPORT #
##########
cs_install()
cs_export(LIBRARIES ${OMPL_LIBRARIES})
#message(STATUS "Variable: ${OMPL_LIBRARIES}")
#cs_export()
