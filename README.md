# World Attributer

## Introduction

This is an example program that users the Spirit of Korth's Software Development Wrapper for Active Worlds to interact with the [Active Worlds](https://www.activeworlds.com). This project or its contributors are not affiliated with Active Worlds. This program was written to showcase the ease of getting world attributes using a bot and text inside of Active Worlds. The Active Worlds SDK is provided in aw64.dll. By using the active worlds SDK, you are agreeing to the terms of the [Active Worlds SDK License Agreement](https://www.activeworlds.com/sdk/download.htm).

## Usage

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


## License

This project is licensed under the MIT license.

## Contribution

This project is open source. Feel free to contribute to the project by opening an issue, creating a pull request, or by contacting [Johnny Irvin](mailto:irvinjohnathan@gmail.com). I appreciate any feedback or contributions. This project is not affiliated with Active Worlds, Inc. The creator of this project is not affiliated with Active Worlds, Inc.