cmake_minimum_required(VERSION 3.8)
project(warthog_mapping)

set(CMAKE_BUILD_TYPE "Release")

find_package(ament_cmake REQUIRED)

install(DIRECTORY 
    launch params scripts
    DESTINATION share/${PROJECT_NAME}
)

ament_package()
