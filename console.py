#!/usr/bin/python3
"""
    a program that contains the entry point of the command interpreter
"""
import cmd
from models.base_model import BaseModel
from models import storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    __classes = ['BaseModel']

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

    def do_create(self, arg):
        """
        Creates a new instance of BaseModel, saves it (to the JSON file) and prints the id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            new_model = eval(f"{args[0]}")()
            print(new_model.id)
            storage.save()

    def do_show(self, arg):
        """
         Prints the string representation of an instance based on the class name and id
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instance = f"{args[0]}.{args[1]}"
            fil = storage.all()
            if instance in fil:
                print(fil[instance])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and id (save the change into the JSON file)
        """
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            instance = f"{args[0]}.{args[1]}"
            fil = storage.all()
            if instance in fil:
                del fil[instance]
            else:
                print("** no instance found **")
        storage.save()

    def do_all(self, arg):
        """
         Prints all string representation of all instances based or not on the class name
        """
        args = arg.split()
        if len(args) == 0:
            fil = storage.all()
            print([str(v) for k, v in storage.all().items()])
        elif args[0] not in self.__classes:
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in storage.all().items() if k.startswith(args[0])])

    def do_update():
        """Updates an instance based on the class name and id by adding or updating attribute
        """
        
if __name__ == '__main__':
    HBNBCommand().cmdloop()
