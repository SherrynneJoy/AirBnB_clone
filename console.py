#!/usr/bin/python3
"""This file creates a command line interpreter"""
import cmd


class HBNBCommand(cmd.Cmd):
    """This class inherits from cmd.Cmd"""
    prompt = '(hbnb) '
    intro = "Joy"

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

    """"Hnadling the end of file or the quit function"""
    def do_EOF(self, line):
        """The end of file marker"""
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
