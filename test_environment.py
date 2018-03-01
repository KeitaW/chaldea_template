import sys
import subprocess

REQUIRED_PYTHON = "python3"
REQUIRED_JULIA  = "julia0.6"
REQUIRED_JAVA   = "java1.8.0"

def main():
    # Test Pytohn Env
    system_python = sys.version_info.major
    if REQUIRED_PYTHON == "python":
        required_python = 2
    elif REQUIRED_PYTHON == "python3":
        required_python = 3
    else:
        raise ValueError("Unrecognized python interpreter: {}".format(
            REQUIRED_PYTHON))

    if system_python != required_python:
        raise TypeError(
            "This project requires Python {}. Found: Python {}".format(
                required_python, sys.version))
    
    # Test Julia Env
    julia_v = subprocess.check_output(["julia", "-v"]).decode("utf-8")[:-1]
    system_julia = julia_v.split(' ')[-1][:-2]
    if REQUIRED_JULIA == "julia0.6":
        required_julia = "0.6"
    if system_julia != required_julia:
        raise TypeError(
            "This project requires Julia {}. Found: Julia {}".format(
                required_julia, system_julia))
    
    # Test Java Env
    java_v = subprocess.check_output(
             ["java", "-version"], stderr=subprocess.STDOUT
             ).decode("utf-8").split("\n")[0].split(' ')[-1]
    system_java = java_v[1:-1].split('.')[:2]
    system_java = float('.'.join(system_java))
    if REQUIRED_JAVA == "java1.8.0":
        required_java = 1.8
    if system_java < required_java:
        raise TypeError(
            "This project requires Java {} or higher. Found: Java {}".format(
                required_java, system_java))


if __name__ == '__main__':
    main()
    print(">>> Development environment passes all tests!")
