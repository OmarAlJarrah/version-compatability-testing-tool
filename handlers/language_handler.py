import handlers.java.gradle_handler


def handle_language(config_data: dict):
    language = config_data['language']

    match language:
        case 'java':
            handlers.java.gradle_handler.handle(config_data)