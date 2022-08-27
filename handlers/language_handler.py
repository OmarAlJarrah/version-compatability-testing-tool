import handlers.java.dependency_manager_decider


def handle(config_data: dict):
    language = config_data['language']

    match language:
        case 'java':
            handlers.java.dependency_manager_decider.handle(config_data=config_data)
