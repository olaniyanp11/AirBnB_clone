#!/usr/bin/python3
"""
    a program that contains the entry point of the command interpreter
"""
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, lone):
        """
        Quit command to exit the program"""
        return True

    def do_EOF():
        """
        signal to exit the program"""
        return True

    def emptyline(self):
        """
        return empty line"""
        return


if __name__ == '__main__':
    HBNBCommand().cmdloop()
