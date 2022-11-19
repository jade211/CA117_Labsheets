#!/usr/bin/env python3

def swap_unique_keys_values(my_dict):
   list = []
   list2 = []
   d = {}
   for key, value in my_dict.items():
      list.append(value)
      list2.append(key)
   i = 0
   while i < len(list) and i < len(list2):
      if list.count(list[i]) == 1:
         d[list2[i]] = list[i]
      i = i + 1
   new_dict = dict([(value, key) for key, value in d.items()])
   return new_dict


def main():
   my_dict = {'a': 4, 'b': 7, 'c': 10, 'd': 7}
   new_dict = swap_unique_keys_values(my_dict)
   print(sorted(new_dict.items()))


if __name__ == '__main__':
   main()
