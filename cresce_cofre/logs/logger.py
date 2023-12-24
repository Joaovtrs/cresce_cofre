from loguru import logger

method_call = logger.level('METHOD', no=21, color='<b><g>')
class_call = logger.level('CLASS', no=22, color='<b><fg 50,50,250>')


def class_method_init(f):
    def func(*args, **kwargs):
        logger.log('METHOD', f'Chamando a função "{f.__qualname__}"')
        return f(*args, **kwargs)

    return func


def class_init(f):
    def func(*args, **kwargs):
        logger.log('CLASS', f'Criando objeto classe "{type(args[0]).__name__}"')
        return f(*args, **kwargs)

    return func


def trace(*args, **kwargs):
    return logger.trace(*args, **kwargs)


def debug(*args, **kwargs):
    return logger.debug(*args, **kwargs)


def info(*args, **kwargs):
    return logger.info(*args, **kwargs)


def success(*args, **kwargs):
    return logger.success(*args, **kwargs)


def warning(*args, **kwargs):
    return logger.warning(*args, **kwargs)


def error(*args, **kwargs):
    return logger.error(*args, **kwargs)


def critical(*args, **kwargs):
    return logger.critical(*args, **kwargs)
