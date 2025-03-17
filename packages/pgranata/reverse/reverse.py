def reverse(args):
    inp = args.get("input", "")
    out = "Enter text to rever"
    if inp != "":
        out = inp[::-1]
    return { "output": out}