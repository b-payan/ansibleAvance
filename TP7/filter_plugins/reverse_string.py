def reverse_string(value):
    return value[::-1]

class FilterModule(object):
     def filters(self):
          return {
               'reverse_string_perso': reverse_string
          } 