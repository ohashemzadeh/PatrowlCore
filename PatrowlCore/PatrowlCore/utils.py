import os

from django.core.exceptions import ImproperlyConfigured


skip_hard_env_check = os.environ.get("SKIP_HARD_ENV_CHECK", None)


def get_env_variable(env_var_name, default_value=None) -> str:
    """
    Get the environment variable or return exception. (if default value not set.)
    :param env_var_name: Environment variable that it's value is desired
    :param default_value: Default value of the environment variable
    :raise ImproperlyConfigured: when corresponding env has not been set

    Normally you should not import ANYTHING from Django directly into your settings,
     but ImproperlyConfigured is an exception.
    """

    if default_value is not None:
        return str(os.environ.get(env_var_name, default_value))

    # if no default_value set;
    try:
        return str(os.environ[env_var_name])
    except KeyError as exp:
        error_msg = f'Set the `{env_var_name}` environment variable'
        if skip_hard_env_check:
            return ""
        raise ImproperlyConfigured(error_msg) from exp
