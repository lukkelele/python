
indent_sensitivity = 2      # Used for the indentation BEFORE string begins
                            # To compensate for the loss of symmetry across the print outputs


def border(length=0):
    if length == 0:
        length = 30
    border = "=" * (length + indent_sensitivity) 
    print(border)


def count_words(text):
    words = text.split(" ")
    len_words = len(words)
    return len_words


def adjust_indent(s, linesize, indent):
    slen = len(s)
    blanks = linesize - slen
    total_indent = indent + blanks
    indentation = (total_indent) * " " + "|"
    s = "|" + (indent+indent_sensitivity) * " " + s     # indent sens use for whitespace compensation
    return s + indentation


def write_line(text, linesize, indent):
    characters = len(text)
    lines = characters // linesize                      # Lines needed to write text
    if lines == 0:
        print(text)
    else:
        words = text.split(" ")
        s = ""
        border(linesize + 2*indent)
        for word in words:
            s += word + " "
            if len(s) > linesize:
                overflow = word + " "
                s = s[:-len(overflow)]
                s = adjust_indent(s, linesize, indent)
                print(s)
                s = overflow
        print(adjust_indent(s, linesize, indent))       # Indentation before gets skipped w/o adjust_indent here
        border(linesize + 2*indent)


