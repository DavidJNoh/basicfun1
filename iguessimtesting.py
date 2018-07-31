def varargs(arg1, *ding):
    print("Got "+arg1+" and "+ ", ".join(ding))
varargs("one") # output: "Got one and "
varargs("one", "two") # output: "Got one and two"
varargs("one", "two", "three") # output: "Got one and two, three"
