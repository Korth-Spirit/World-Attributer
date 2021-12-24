# Copyright (c) 2021 Johnathan P. Irvin
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
from typing import Callable

from korth_spirit import WorldEnum, Instance


def if_begins_with(event: "Event", beginning: str, func: Callable):
    """
    If the message begins with the string, then call the function.

    Args:
        event (Event): The event to check.
        beginning (str): The beginning of the message.
        func (Callable): The function to call.
    """
    message = event.chat_message

    if message.startswith(beginning):
        func(message. replace(beginning, "").strip())

def get_attribute(instance: Instance, attribute: str) -> str:
    """
    Get a world attribute.

    Args:
        instance (Instance): The instance to get the attribute from.
        attribute (str): The attribute to print.

    Returns:
        str: The value of the attribute.
    """
    try:
        value = instance.get_world().get_attribute(attribute)
        return f"{attribute} = {value}"
    except Exception as e:
        return f"Error: {e} -- {attribute}"

def set_attribute(instance: Instance, attribute: str, value: str) -> str:
    """
    Set a world attribute.

    Args:
        instance (Instance): The instance to set the attribute on.
        attribute (str): The attribute to set.
        value (str): The value to set the attribute to.

    Returns:
        str: The value of the attribute.
    """
    try:
        instance.get_world().set_attribute(attribute, value)
        return f"{attribute} = {value}"
    except Exception as e:
        return f"Error: {e}"

def get_all_attributes(instance: Instance) -> str:
    """
    Get all the world attributes.

    Args:
        instance (Instance): The instance to get the attributes from.

    Returns:
        str: The attributes.
    """
    for attribute in WorldEnum:
        yield get_attribute(instance, attribute)

def every_x(iterable: "Iterable", x: int, func: Callable) -> str:
    """
    Call the function every x returned items.

    Args:
        iterable (Iterable): The iterable to iterate over.
        x (int): The number of items to return.
        func (Callable): The function to call.

    Returns:
        str: The returned items.
    """
    orig = x
    stored = []
    for item in iterable:
        if x == 0:
            func(stored)
            x = orig
            stored = []
            continue

        stored.append(item)
        x -= 1
