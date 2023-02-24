cmake_minimum_required(VERSION 3.8)
project(warthog_mapping)

find_package(ament_cmake REQUIRED COMPONENTS roslaunch)

install(DIRECTORY launch
    DESTINATION share/${PROJECT_NAME})

install(DIRECTORY params
    DESTINATION share/${PROJECT_NAME})

ament_package()