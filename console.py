#!/usr/bin/python3
"""This file creates a command line interpreter"""
import cmd
import re
import json
from models import storage
from models.base_model import BaseModel
from shlex import split


def parsecmd(arg):
    """parses commands typed into the console"""
    curlybraces = re.search(r"\{(.*?)\}", arg)
    boxbrackets = re.search(r"\[(.*?)\]", arg)
    if curlybraces is None:
        if boxbrackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:boxbrackets.span()[0]])
            todo = [i.strip(",") for i in lexer]
            todo.append(boxbrackets.group())
            return (todo)
    else:
        lexer = split(arg[:curlybraces.span()[0]])
        todo = [i.strip(",") for i in lexer]
        todo.append(curlybraces.group())
        return (todo)


class HBNBCommand(cmd.Cmd):
    """This class inherits from cmd.Cmd"""
    prompt = '(hbnb) '
    __classes = {
            "BaseModel",
            "User"
            }

    """other class attributes"""
    doc_header = 'Documented commands (type help <topic>): '
    misc_header = 'misc_header'
    undoc_header = 'undoc_header'

    """the ruler is used to print help"""
    ruler = "="

    """a function to ensure the prompt works well"""
    def do_prompt(self, line):
        """change the interactive prompt"""
        self.prompt = line

    """this method takes care of empty lines passed into the interpreter"""
    def emptyline(self):
        pass

    """Handling the quit command being passed into the console"""
    def do_quit(self, arg):
        """returns true to leave the program"""
        return True

    """"Handling the end of file or the quit function"""
    def do_EOF(self, line):
        """The end of file marker"""
        return True

    """a function that creates, saves and prints"""
    def do_create(self, arg):
        arg_1 = parsecmd(arg)
        if len(arg_1) == 0:
            print("** class name missing **")
        elif arg_1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(arg_1[0])().id)
            storage.save()

    """a function that prints the str represenation of an instance"""
    def do_show(self, arg):
        arg_1 = parsecmd(arg)
        objdict = storage.all()
        if len(arg_1) == 0:
            print("** class name missing **")
        elif arg_1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_1[0], arg_1[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(arg_1[0], arg_1[1])])

    """a function that destroys an instance based on name and id"""
    def do_destroy(self, arg):
        arg_1 = parsecmd(arg)
        objdict = storage.all()
        if len(arg_1) == 0:
            print("** class name missing **")
        elif arg_1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(arg_1) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(arg_1[0], arg_1[1]) not in objdict:
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(arg_1[0], arg_1[1])]
            storage.save()

    """Prints all string representation of all instances"""
    def do_all(self, arg):
        arg_1 = parsecmd(arg)
        if len(arg_1) > 0 and arg_1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            myobj = []
            for obj in storage.all().values():
                if len(arg_1) > 0 and arg_1[0] == obj.__class__.__name__:
                    myobj.append(obj.__str__())
                elif len(arg_1) == 0:
                    myobj.append(obj.__str__)
            print(myobj)

    """Updates an instance based on the class name and id"""
    def do_update(self, arg):
        """updates attributes one at a time"""
        arg_1 = parsecmd(arg)
        objdict = storage.all()

        if len(arg_1) == 0:
            print("** class name missing **")
            return False
        if arg_1[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(arg_1) == 1:
            print("** instance id missing **")
            return False
        if "{}.{}".format(arg_1[0], arg_1[1]) not in objdict:
            print("** no instance found **")
            return False
        if len(arg_1) == 2:
            print("** attribute name missing **")
            return False
        if len(arg_1) == 3:
            try:
                type(eval(arg_1[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        if len(arg_1) == 4:
            obj = objdict["{}.{}".format(arg_1[0], arg_1[1])]
            if arg_1[2] in obj.__class__.__dict__.keys():
                valuetype = type(obj.__class__.__dict__[arg_1[2]])
                obj.__dict__[arg_1[2]] = valuetype(arg_1[3])
            else:
                obj.__dict__[arg_1[2]] = arg_1[3]
        elif type(eval(arg_1[2])) == dict:
            obj = objdict["{}.{}".format(arg_1[0], arg_1[1])]
            for k, v in eval(arg_1[2]).items():
                if (k in obj.__class__.__dict__.keys and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valuetype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valuetype(v)
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
