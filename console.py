#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""


import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from sys import argv

classes = ['BaseModel']


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

    def do_create(self, arg):
        """creates an instance of BaseModel"""
        if len(arg) == 0:
            print("** class is missing **")
        elif arg not in classes:
            print("** class doesn't exist **")
        else:
            new = BaseModel()
            new.save()
            print(new.id)

    def do_show(self, arg):
        """prints the string representaion of an instance
        based on the class name and id"""
        if len(arg) == 0:
            print("** class name missing **")
            return False
        show = storage.all()
        cmd_arg = arg.split()
        if cmd_arg[0] in classes:
            class_id = '.'.join(cmd_arg)
            if len(cmd_arg) == 2:
                if class_id not in show:
                    print("** no instance found **")
                else:
                    print(show[class_id])
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)."""
        if len(arg) == 0:
            print("** class is missing **")
            return False
        show = storage.all()
        cmd_arg = arg.split()
        if cmd_arg[0] in classes:
            class_id = '.'.join(cmd_arg)
            if len(cmd_arg) == 2:
                if class_id not in show:
                    print("** no instance found **")
                else:
                    show.pop(class_id)
                    storage.save()
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    prompt = "(hbnb) "


if __name__ == '__main__':
    HBNBCommand().cmdloop()
