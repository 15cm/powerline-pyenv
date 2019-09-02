A Powerline segment for showing pyenv version

# Installation
```
pip install powerline-pyenv
```

# Usage
## Segment
Activate the `pyenv` segment in `~/.config/powerline/themes/shell/default.json`
```json
{
    "priority": 10,
    "function": "powerline_pyenv.pyenv"
}
```

## Colorscheme
Config highlight groups in colorscheme files, e.g. `~/.config/powerline/colorschemes/shell/nord.json`:

### Dark(Nord)
```json
{
    "groups": {
        "pyenv:version": {
            "bg": "gray1",
            "fg": "green"
        }
    }
}
```

### Light(Solarized Light)
```json
{
    "groups": {
        "pyenv:version": {
            "fg": "solarized:green",
            "bg": "solarized:base2"
        },
    }
}
```
