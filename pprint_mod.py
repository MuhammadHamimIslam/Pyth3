"pprint means pretty printing. So this module is used for printing anything pretty"
import pprint

"pprint.PrettyPrinter(indent, width, depth, stream, compact)"

info = {"name": "mno", "id": "12ab", "marks": [67, 86, 90, 89, 78]}

print("normal printing: ", info)

# using pretty printer 
pretty_printer = pprint.PrettyPrinter(indent=4, width=1)
print("using pprint: ", end="")
pretty_printer.pprint(info)

string = pretty_printer.pformat(info)
print(string)