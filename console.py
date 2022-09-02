#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This class handles the implementation of the
    command interpreter attributes"""

    # def do_help(self, arg: str) -> 'type' | 'NoneType':
    #     """lists commands with detailed help"""
    #     return super().do_help(arg)

    def do_EOF(self, line):
        """exits the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        raise SystemExit

    def emptyline(self):
        """an emptyline + ENTER executes nothing"""
        pass


    prompt = "(hbnb) "


if __name__ == '__main__':
    HBNBCommand().cmdloop()
