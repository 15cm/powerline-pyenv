import subprocess

from powerline.theme import requires_segment_info


@requires_segment_info
def pyenv(pl, segment_info):
    cwd = segment_info["getcwd"]()
    pyenv_version = subprocess.check_output(
        ["pyenv", "version-name"], cwd=cwd, encoding="utf8"
    ).strip()
    return [
        {
            "name": "pyenv_version",
            "type": "string",
            "contents": " {}".format(pyenv_version),
            "highlight_groups": ["pyenv_version"],
        }
    ]
