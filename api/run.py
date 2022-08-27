import handlers.handlers_chain


def run(config_dict: dict):
    handlers.handlers_chain.run_handlers_chain(config_data=config_dict)

