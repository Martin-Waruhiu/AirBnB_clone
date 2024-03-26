#!/usr/bin/python3
"""defines the console(entry point)"""


import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


def parse(arg):
        """tokenizing the passed commands"""
        enclosers = re.search(r"\{(.*?)\}", arg)
        funga = re.search(r"\[(.*?)\]", arg)
        if enclosers is None:
            if funga is None:
                return [a.strip(",") for a in split(arg)]
            else:
                jeep = split(arg[:funga.span()[0]])
                vl = [a.strip(",") for a in jeep]
                vl.append(funga.group())
                return vl
        else:
            jeep = split(arg[:enclosers.span()[0]])
            vl = [a.strip(",") for a in jeep]
            vl.append(enclosers.group())
            return vl

class HBNBCommand(cmd.Cmd):
    """entry point of current interpreter"""
    prompt = "(hbnb)"
    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
         }


    def do_quit(self, args):
        return True

    def do_EOF(self, args):
        return True

    def emptyline(self):
        pass

    def do_create(self, args):
        """create a new instance of the basemodel"""

        argument = parse(args)
        if len(argument) == 0:
            print("** class name missing **")
        elif argument[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argument[0])().id)
        storage.save()

    def do_show(self, args):
        """display the string rep of a given class and id"""
        argument = parse(args)
        our_dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif argument[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argument) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argument[0], argument[1]) not in our_dict:
            print("** no instance found **")
        else:
            print(our_dict["{}.{}".format(argument[0], argument[1])])

    def do_destroy(self, args):
        """deeletes an instance based on lassname and id"""
        argument = parse(args)
        our_dict = storage.all()
        if len(argument) == 0:
            print("** class name missing **")
        elif argument[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argument) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argument[0], argument[1]) not in our_dict.keys():
            print("** no instance found **")
        else:
            del our_dict["{}.{}".format(argument[0], argument[1])]
            storage.save()

    def do_all(self, args):
        """ Prints all string representation of all instances
        based or not on the class name."""

        argument = parse(args)
        if len(argument) > 0 and argument[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for ob in storage.all().values():
                if len(argl) > 0 and argument[0] == ob.__class__.__name__:
                    obj_list.append(obj.__str__())
                elif len(argl) == 0:
                    obj_list.append(ob.__str__())
            print(obj_list)

    def do_update(self, args):
        """Usage: update <class name> <id> <attribute name> "<attribute value>"
        updates and instance based n the class name and id."""
        argument = parse(args)
        our_dict = storage.all()
        if len(argument) == 0:
            print("** class name missing **")
        if argument[1] not in HBNB.Command.__classes:
            print("** class doesn't exist **")
        if len(argument == 1):
            print("** instance id missing **")
        if ("{}.{}".format(argument[0], argument[1] not in our_dict.keys())):
                print("** no instance found **")
        if len(argument) == 2:
            print("** attribute name missing **")
        elif len(argument) == 3:
            print("** value missing **")

        if len(argument) == 4:
            instance = our_dict["{}.{}".format(argument[o], argument[1])]
            if argument[2] in instance.__class__.__dict__.keys():
                att_type = type(instance.__class__.__dict__.argument[2])
                instance.__dict__[argument[2]] = att_type(argument[3])
            else:
                instance.__dict__[argument[2]] == argument[3]
        elif type(eval(argument[2])) == dict:
            instance = our_dict["{}.{}".format(argl[0], argl[1])]
            for key, value in eval(argument[2]).items():
                if (key in instance.__class__.__dict__.keys() and
                        type(instance.__class__.__dict__[key]) in {str, int, float}):
                    att_type = type(instance.__class__.__dict__[key])
                    instance.__dict__[key] = att_type(value)
                else:
                    instance.__dict__[key] = value
        storage.save()


            
if __name__ == '__main__':
        HBNBCommand().cmdloop()
