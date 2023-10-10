#!/usr/bin/python3
"""This file creates a command line interpreter"""
import cmd


class interpreter(cmd.Cmd):
    """This class inherits from cmd.Cmd"""
    prompt = '(hbnb) '
    intro = "Joy"

    """other class attributes"""
    doc_header = 'Documented commands (type help <topic>): \n'
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

    def do_EOF(self, line):
        """The end of file marker"""
        return True


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        interpreter().onecmd()(' '.join(sys.argv[1:]))
    else:
        interpreter().cmdloop()
