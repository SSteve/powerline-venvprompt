# powerline-venvprompt

`powerline-venvprompt` is a [Powerline](https://github.com/powerline/powerline) status segment that displays the prompt set by the `venv --prompt` option.

For example, if a virtual environment was created with the command `python3 -m venv venv --prompt "my_prompt"`, the prompt will be "my_prompt" instead of "venv" or the name of the folder containing *venv*.

## Installation

1. Make sure Powerline is installed and functioning and that you have a custom configuration (most likely in *~/.config/powerline*).

2. Install the package with `pip` or `pipx`.

```bash
pip install --user powerline-venvprompt
```
or
```bash
pipx install powerline-venvprompt
```

3. Add to your theme.

Typically, the *config.json* file that controls your Powerline setup is in *~/.config/powerline*. The theme itself will be in *~/.config/powerline/themes/shell*. Add the following lines to your theme JSON file:

```JSON
{
    "function": "powerline_venvprompt.segments.prompt",
    "priority": 10
},
```

Set the priority however you like. 

`powerline-venvprompt` takes the place of the `powerline.segments.common.env.virtualenv` segment, so if that one is already in your config file you should remove it. If there is no prompt set in the venv, it will display the same thing that `powerline.segments.common.env.virtualenv` would have shown.

## Options

The options for `powerline-venvprompt` are inherited from the default `powerline.segments.common.env.virtualenv` segment [in version 2.8.3](https://github.com/powerline/powerline/blob/2.8.3/powerline/segments/common/env.py).

- **ignore_venv**

If true, the venv virtual environment will be ignored (including the --prompt option). Default value is false.

- **ignore_conda**

If true, the conda virtual environment will be ignored. Default value is false.

- **ignored_names**

A list of names that will be ignored. If a virtual environment has one of these names (and no explicit prompt defined), the prompt will be the name of the folder containing venv.

Here is an example configuration with the default values:

```JSON
{
    "function": "powerline_venvprompt.segments.prompt",
    "priority": 10,
    "args": {
        "ignore_venv": false,
        "ignore_conda": false,
        "ignored_names": ["venv", ".venv"]
    }
},
```

## Troubleshooting

If you activate a virtual environment and the prompt isn't displayed, here are some potential solutions.

### Restart Powerline

Use the command `powerline-daemon -r` to restart Powerline after any change to your configuration.

### Check for errors

Use the command `powerline-lint` to display configuration errors. 

You may see a number of unrelated issues (my installation has over a dozen errors in the stock *colorschemes/vim/\_\_main\_\_.json* file). Ignore those.

You will see the following message. You can ignore this. `powerline-venvprompt` uses the same *virtualenv* color scheme that the default `powerline.segments.common.env.virtualenv` uses.

```
found highlight group prompt not defined in the following colorschemes: default, solarized
(If not specified otherwise in documentation, highlight group for function segments
is the same as the function name.)
  in "~/.config/powerline/themes/shell/steve.json", line 17, column 49:
     ...  "powerline_venvprompt.segments.prompt",
```

If you see the message "failed to import module powerline_venvprompt.segments" that might mean Powerline is not searching the folder containing your *powerline_venvprompt* folder. If this is the case, add the folder to your *config.json* file. This folder will depend on how you installed `powerline-venvprompt`. Example:

```json
"paths": [
    "/path/to/folder"
],
```


If all else fails, use GitHub Issues to report your problem and I'll do my best to help.