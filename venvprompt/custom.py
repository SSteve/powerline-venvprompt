import configparser
import os

from powerline.theme import requires_segment_info


@requires_segment_info
def venvprompt(ps, segment_info, ignore_venv=False, ignore_conda=False):
    """Return the prompt of the current Python venv. If the venv doesn't have a prompt set, 
    return the name of the current Python or conda virtualenv. This is based on the stock powerline
    segment "powerline.segments.common.env.virtualenv".

	:param bool ignore_venv:
		Whether to ignore virtual environments. Default is False.
	:param bool ignore_conda:
		Whether to ignore conda environments. Default is False.
    """
    if (ignore_venv):
        return not ignore_conda and segment_info['environ'].get('CONDA_DEFAULT_ENV', '') or None

    venv_path = segment_info['environ'].get('VIRTUAL_ENV', '')

    if venv_path is None:
        return None
    
    config_file_name = os.join(venv_path, "pyvenv.cfg")
    if (os.path.exists(config_file_name) is False):
        return os.path.basename(venv_path)
    
    config = configparser.ConfigParser()
    config.read(config_file_name)
    return config['prompt'] or os.path.basename(venv_path)
