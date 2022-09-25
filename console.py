#!/usr/bin/python3
"""This module contains the entry point of the command interpreter"""


import cmd
from models.base_model import BaseModel
from models.__init__ import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

classes = ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']


class HBNBCommand(cmd.Cmd):
    """This class handles the implementation of the
    command interpreter attributes"""

    def precmd(self, line):
        new = line.split(".")
        if len(new) == 2:
            if 'update' in new[1]:
                classname, cmddetails = new
                cmddetails = cmddetails.split('(')
                cmd_name, details = cmddetails
                details = details.rstrip(')')
                details = details.split(' ')
                details_list = list()
                for detail in details:
                    detail = detail.rstrip(',')
                    detail = detail.replace('"', '')
                    details_list.append(detail)
                id_, key, value = details_list
                line = cmd_name + ' ' + classname + ' '
                line += id_ + ' ' + key + ' ' + value
                return (line)

            else:
                cls_nm, cmd_all = new
                command, cmd_info = cmd_all.split("(")
                cmd_info = cmd_info.rstrip(")")
                cmd_info = cmd_info.replace('"', '')
                line = command + " " + cls_nm + " " + cmd_info
                return (line)
        return cmd.Cmd.precmd(self, line)

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
        """creates an instance of a class. Example: $ create BaseModel"""
        if len(arg) == 0:
            print("** class name missing **")
        elif arg in classes:
            new = eval(arg + '()')
            storage.save()
            print(new.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """prints the string representaion of an instance
        based on the class name and id.\
                Example: show BaseModel 1234-1234-1234"""
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
        (save the change into the JSON file).
        Example:  destroy BaseModel 1234-1234-1234"""
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
                    show.pop(class_id)
                    storage.save()
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """prints all string representation of all instances
        based or not on the class name.
        Example: all BaseModel or  all"""
        cmd_arg = arg.split()
        all_list = []
        if len(arg) > 0:
            if cmd_arg[0] in classes:
                all_dict = storage.all()
                for key in all_dict.keys():
                    ref = key.split('.')
                    if ref[0] == cmd_arg[0]:
                        all_list.append(all_dict[key])
                print(all_list)
            else:
                print("** class doesn't exist **")
        elif len(arg) == 0:
            all_dict = storage.all()
            for key in all_dict.keys():
                all_list.append(str(all_dict[key]))
            print(all_list)

    def do_update(self, arg):
        """update an instance based on class and id
        Usage: update <class name> <id> <attribute name> <attribute value>"""
        c_arg = arg.split()
        show = storage.all()
        if len(c_arg) == 0:
            print("** class name missing **")
            return False
        if c_arg[0] in classes:
            if len(c_arg) > 1:
                class_id = '.'.join([c_arg[0], c_arg[1]])
                if class_id in show:
                    if len(c_arg) > 2:
                        if len(c_arg) == 4:
                            c_arg[3] = eval(c_arg[3])
                            show[class_id].__dict__[c_arg[2]] = c_arg[3]
                            storage.save()
                        else:
                            print("** value missing **")
                    else:
                        print("** attribute name missing **")
                else:
                    print("** no instance found **")
            else:
                print("** instance id missing **")
        else:
            print("** class doesn't exist **")

    def do_count(self, arg):
        """ retrieve the number of instances of a class
        Usage: count classname"""
        count = 0
        cmd_arg = [arg]
        for key in storage.all().keys():
            key = key.split('.')
            if key[0] == cmd_arg[0]:
                count += 1
        print(count)

    prompt = "(hbnb) "


if __name__ == '__main__':
    HBNBCommand().cmdloop()
