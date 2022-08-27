def build_command(jdk_version, project_path: str):
    docker_run_command = "docker run --rm -v"
    gradle_tasks = " gradle build run"
    docker_vol = ":/home/gradle/project -w /home/gradle/project gradle:"

    run_command = docker_run_command + project_path + docker_vol + jdk_version + gradle_tasks
    return run_command

