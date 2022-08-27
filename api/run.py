from handlers.handlers_chain_starter import run_handlers_chain


def run_testing(config_dict: dict):
    run_handlers_chain(config_data=config_dict)

