# vim:fileencoding=utf-8:noet
from __future__ import absolute_import, division, print_function, unicode_literals

import configparser
import os

from powerline.theme import requires_segment_info


@requires_segment_info
def prompt(pl, segment_info, ignore_venv=False, ignore_conda=False, ignored_names=("venv", ".venv")):
    """Return the prompt of the current Python venv. If the venv doesn't have a prompt set, 
    return the name of the current Python or conda virtualenv. This is based on the this
    version from the develop branch: 
    https://github.com/powerline/powerline/blob/develop/powerline/segments/common/env.py.

	:param bool ignore_venv:
		Whether to ignore virtual environments. Default is False.
	:param bool ignore_conda:
		Whether to ignore conda environments. Default is False.
	:param list ignored_names:
		Names of venvs to ignore. Will then get the name of the venv by ascending to the parent directory.
    """
    pl.error("In powerline-venvprompt")
    return "blah"
    if not ignore_venv:
        for candidate in reversed(segment_info['environ'].get('VIRTUAL_ENV', '').split("/")):
            if candidate and candidate not in ignored_names:
                return candidate
    if not ignore_conda:
        for candidate in reversed(segment_info['environ'].get('CONDA_DEFAULT_ENV', '').split("/")):
            if candidate and candidate not in ignored_names:
                return candidate
    return None

    venv_path = segment_info['environ'].get('VIRTUAL_ENV', '')

    if venv_path is None:
        return None
    
    config_file_name = os.join(venv_path, "pyvenv.cfg")
    if (os.path.exists(config_file_name) is False):
        return os.path.basename(venv_path)
    
    config = configparser.ConfigParser()
    config.read(config_file_name)
    return config['prompt'] or os.path.basename(venv_path)
