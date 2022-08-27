from handlers import language_handler


def run_handlers_chain(config_data: dict):
    language_handler.handle(config_data=config_data)
