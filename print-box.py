import sys

def print_box(h, w):
    print "*" * w
    for i in xrange(0, h-2):
        sys.stdout.write("*")
        for j in xrange (0, w-2):
            sys.stdout.write(" ")
        print "*"
    print "*" * w,
    # print "\n"

w = int(raw_input("width: "))
h = int(raw_input("height: "))

print_box(h, w)
