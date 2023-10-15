#!/usr/bin/python3
<<<<<<< HEAD
"""defines a class that creates a commandline interpreter"""
import cmd
import re
from shlex import split
from models import storage
from models.base_model import BaseModel


def parse(arg):
    """splits a command typed into the interpreter"""
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[.*?]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retOne = [i.strip(",") for i in lexer]
            retOne.append(brackets.group())
            return retOne
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retOne = [i.strip(",") for i in lexer]
        retOne.append(curly_braces.group())
        return retOne


class HBNBCommand(cmd.Cmd):
    """creates a subclass of Cmd class & creates an interpreter"""
    prompt = '(hbnb) '
    __classes = {
           "BaseModel",
           "User",
           "State",
           "City",
           "Amenity",
           "Place",
           "Review"
            }

    """other attributes"""
=======
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
            "User",
            "State",
            "City",
            "Amenity",
            "Place",
            "Review"
            }

    """other class attributes"""
>>>>>>> c466ac3e4a65d74a757863cd3fa536f894dcc0a7
    doc_header = 'Documented commands (type help <topic>): '
    misc_header = 'misc_header'
    undoc_header = 'undoc_header'

<<<<<<< HEAD
    """to separate/divide the content, the ruler is used"""
    ruler = '='

    """method to ensure the prompt works"""
    def do_prompt(self, line):
        self.prompt = line

    """if an empty line is inserted, ignore"""
    def emptyline(self):
        pass

    """implement the command quit to leave the console/interpreter"""
    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    """to terminate the interpreter, the EOF is invoked"""
    def do_EOF(self, line):
        """EOF command to exit the program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel,
        saves it (to the JSON file) and prints the id"""
        argOne = parse(arg)
        if len(argOne) == 0:
            print("** class name missing **")
        elif argOne[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(argOne[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id"""
        argOne = parse(arg)
        objdict = storage.all()
        if len(argOne) == 0:
            print("** class name missing **")
        elif argOne[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argOne) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argOne[0], argOne[1]) not in objdict:
            print("** no instance found **")
        else:
            print(objdict["{}.{}".format(argOne[0], argOne[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        argOne = parse(arg)
        objdict = storage.all()
        if len(argOne) == 0:
            print("** class name missing **")
        elif argOne[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(argOne) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(argOne[0], argOne[1]) not in objdict:
            print("** no instance found **")
        else:
            del objdict["{}.{}".format(argOne[0], argOne[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances
        based or not on the class name"""
        argOne = parse(arg)
        if len(argOne) > 0 and argOne[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            objOne = []
            for obj in storage.all().values():
                if len(argOne) > 0 and argOne[0] == obj.__class__.__name__:
                    objOne.append(obj.__str__())
                elif len(argOne) == 0:
                    objOne.append(obj.__str__())
            print(objOne)

    def do_update(self, arg):
        """Updates an instance based on the class name and id
        by adding or updating attribute"""
        argOne = parse(arg)
        objdict = storage.all()
        if len(argOne) == 0:
            print("** class name missing **")
        if argOne[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        if len(argOne) == 1:
            print("** instance id missing **")
        if "{}.{}".format(argOne[0], argOne[1]) not in objdict:
            print("** no instance found **")
        if len(argOne) == 3:
            try:
                type(eval(argOne[2])) != dict
            except NameError:
                print("** value missing **")
        if len(argOne) == 4:
            obj = objdict["{}.{}".format(argOne[0], argOne[1])]
            if argOne[2] in obj.__class__.__dict__.keys():
                val = type(obj.__class__.__dict__argOne[2])
                obj.__dict__[argOne[2]] = val(argOne[3])
            else:
                obj.__dict__[argOne[2]] = argOne[3]
        elif type(eval(argOne[2])) == dict:
            obj = objdict["{}.{}".format(argOne[0], argOne[1])]
            for k, v in eval(argOne[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                        type(obj.__class__.__dict__[k]) in {str, int, float}):
                    val = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = val(v)
=======
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
>>>>>>> c466ac3e4a65d74a757863cd3fa536f894dcc0a7
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
