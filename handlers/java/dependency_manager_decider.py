import handlers.java.gradle_handler


def handle(config_data: dict):
    dependency_manager = config_data['dependency_manager']

    match dependency_manager:
        case 'maven':
            pass
        case 'gradle':
            handlers.java.gradle_handler.handle(config_data)
