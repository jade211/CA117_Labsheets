#!/usr/bin/env python3

def swap_keys_values(my_dict):
   new_dict = dict([(value, key) for key, value in my_dict.items()])  # dict() is a function that creates a dictionary
   return new_dict


def main():
   my_dict = {'a': 4, 'b': 7, 'c': 10}
   new_dict = swap_keys_values(my_dict)
   print(sorted(new_dict.items()))


if __name__ == '__main__':
   main()
