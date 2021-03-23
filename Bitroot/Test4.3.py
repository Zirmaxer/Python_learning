def make_operation (singht, *args):
    try:
        if singht == '+' or singht == '-' or singht == '*':
            pass
        else:
            raise TypeError
        for item in args:
            i = int(item)
        if singht == '+':
            return sum([l for l in args])
        elif singht == '-':
            answer = args[0]
            for item in args[1:]:
                answer -= item
            return answer
        elif singht == '*':
            answer = args[0]
            for item in args[1:]:
                answer *= item
            return answer
    except TypeError:
        print ('TypeError')
        raise
    except ValueError:
        print ('ValueError')
        raise

print (make_operation('-', 6,7))