#!/usr/bin/python3
"""defines a class that creates a commandline interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """creates a subclass of Cmd class & creates an interpreter"""
    intro = "june"
    prompt = '(hbnb) '
    
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
        """returns true on success"""
        return True


if __name__ == '__main__':
        HBNBCommand().cmdloop()
