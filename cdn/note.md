# active win + office 
```
irm https://get.activated.win | iex
```
## Fix downline on opencode terminal windows

On WSL with the Windows Terminal(Preview), go to Settings--> Open JSON file(bottom left).
Add an action for input:

```json
{
    "actions": [
        {
            "command": 
            {
                "action": "sendInput",
                "input": "\n"
            },
            "id": "User.sendInput.DFCDAF06"
        }
    ]
}
```
Add the keybinding(note the id) under 
```json
{
  "keybindings": {
    "id": "User.sendInput.DFCDAF06",
    "keys": "shift+enter"
  }
}
```
