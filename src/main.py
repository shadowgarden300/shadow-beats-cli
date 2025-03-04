import commands

while True:
    arg = input("> ").strip()
    commands.validate_runtime_input(arg)