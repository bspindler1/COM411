def escape_by(plan):
    if plan == "jumping over":
        return "We cannot escape that way! The boulder is too big!"

    if plan == "running around":
        return "We cannot escape that way! The boulder is moving too fast"

    elif plan == "cross bridge ahead":
        return "That might just work! Let's go!"

    return "We cannot escape that way! The boulder is in the way!"


print(escape_by("jumping over"))
print(escape_by("running around"))
print(escape_by("cross bridge ahead"))
