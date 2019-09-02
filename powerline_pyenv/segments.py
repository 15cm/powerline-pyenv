import os
import subprocess

from powerline.theme import requires_segment_info

env_pyenv_keys = ["PYENV_VERSION", "PYENV_DIR"]

# Remove ENV vars injected to powershell by pyenv
for key in env_pyenv_keys:
    os.unsetenv(key)


@requires_segment_info
def pyenv(pl, segment_info):
    global env_pyenv_keys
    env = segment_info["environ"]
    for key in env_pyenv_keys:
        if key in env:
            os.putenv(key, env[key])
    cwd = segment_info["getcwd"]()
    pyenv_version = subprocess.check_output(
        ["pyenv", "version-name"], cwd=cwd, encoding="utf8"
    ).strip()
    return [
        {
            "name": "pyenv_version",
            "type": "string",
            "contents": " {}".format(pyenv_version),
            "highlight_groups": ["pyenv:version"],
        }
    ]
