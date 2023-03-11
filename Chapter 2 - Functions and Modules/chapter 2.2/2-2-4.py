import stdio
#rescaling an array


def rescale(ymin,ymax,a):
    if ymin >= ymax:
        return "minimum has to be strictly smaller than maximum"
    else:
        mini = min(a)
        maxi = max(a)
        for i in range(len(a)):
            a[i] = ((a[i] - mini)/(maxi-mini))*(ymax-ymin)+ymin
    return a


stdio.write("Input minimum Value: ")
ymin = stdio.readFloat()
stdio.write("Input maximum Value: ")
ymax = stdio.readFloat()
stdio.write("input your array: ")
a = stdio.readAllFloats()
stdio.write(rescale(ymin,ymax,a))