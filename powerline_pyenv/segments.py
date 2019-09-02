import os
import subprocess

from powerline.theme import requires_segment_info

g_env_pyenv_keys = ["PYENV_VERSION", "PYENV_DIR"]
g_env_virtualenv_key = "VIRTUAL_ENV"


# Remove ENV vars injected to powershell by pyenv
for key in g_env_pyenv_keys:
    os.unsetenv(key)


@requires_segment_info
def pyenv(pl, segment_info):
    global g_env_pyenv_keys, g_env_virtualenv_key
    env = segment_info["environ"]
    # Check for shell spawned by virtualenv(maybe used by pipenv) first
    if g_env_virtualenv_key in env:
        py_version = "{}(venv)".format(os.path.basename(env[g_env_virtualenv_key]))
    else:
        for key in g_env_pyenv_keys:
            if key in env:
                os.putenv(key, env[key])
        cwd = segment_info["getcwd"]()
        pyenv_version = subprocess.check_output(
            ["pyenv", "version-name"], cwd=cwd, encoding="utf8"
        ).strip()
        py_version = "{}(pyenv)".format(pyenv_version)

    return [
        {
            "name": "pyenv_version",
            "type": "string",
            "contents": " {}".format(py_version),
            "highlight_groups": ["pyenv:version"],
        }
    ]
