#!/usr/bin/python3
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
           "User"
            }

    """other attributes"""
    doc_header = 'Documented commands (type help <topic>): '
    misc_header = 'misc_header'
    undoc_header = 'undoc_header'

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
                else:
                    obj.__dict__[k] = v
        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
