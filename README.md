# World Attributer

This is an example program that uses the Spirit of Korth's Software Development Wrapper for Active Worlds to interact with the [Active Worlds](https://www.activeworlds.com). This project or its contributors are not affiliated with Active Worlds. This program was written to showcase the ease of getting world attributes using a bot and text inside of Active Worlds. The Active Worlds SDK is provided in aw64.dll. By using the active worlds SDK, you are agreeing to the terms of the [Active Worlds SDK License Agreement](https://www.activeworlds.com/sdk/download.htm).

# Usage

This program can both be used locally and through the use of the provided Docker image.

To use this program locally, you will need to have Python 3 installed. Then you can run the program with the following commands:
```bash
pip install -r requirements.txt
python ./world_attributer.py
```

You can also run the program with the following command provided you have Docker installed:
```bash
docker build -t world_attributer .
docker run -it world_attributer
```

Once in game. You can use the following commands to get the world attributes:
```
/get attribute <attribute_name>
```

(E.g.)
```
/get attribute name
/get attribute title
/get attribute size
```

```
/get all attributes
```

You may also set attributes the same way.
```
/set attribute <attribute_name> <attribute_value>
```

(E.g.)
```
/set attribute name "My World"
/set attribute title "My World"
```

# Configuration

This bot uses a json configuration file named "configuration.json" located in the same directory as the application.

| Variable | Description |
|---------|-------------|
| `BOT_NAME` | The name of the bot. |
| `CITIZEN_NUMBER` | The owner of the bot. |
| `PASSWORD` | The password of the bot. |
| `WORLD_NAME` | The name of the world to connect to. |
| `WORLD_X` | The x coordinate of the world to connect to. |
| `WORLD_Y` | The y coordinate of the world to connect to. |
| `WORLD_Z` | The z coordinate of the world to connect to. |

X coordinates are west/east where west is positive and east is negative.
Y coordinates represent height where up is positive and down is negative and ground is 0.
Z coordinates are north/south where north is positive and south is negative.

Configuration example:
```json
{
    "bot_name": "Plugin Bot",
    "world_name": "Test World",
    "world_coordinates": {
        "x": 0,
        "y": 0,
        "z": 0
    },
    "citizen_number": 123456,
    "password": "password"
}
```

# License

This project is licensed under the MIT license.

# Contribution

This project is open source. Feel free to contribute to the project by opening an issue, creating a pull request, or by contacting [Johnny Irvin](mailto:irvinjohnathan@gmail.com). I appreciate any feedback or contributions. This project is not affiliated with Active Worlds, Inc. The creator of this project is not affiliated with Active Worlds, Inc.
