import logging as lg
def even_num(a,b):
    """give even numbers from a to b"""
    lg.basicConfig(filename="even.log",level=lg.INFO)
    l = []

    try:
        if a>b:
            lg.error("a>b")
            raise Exception("a>b")
        while a<=b:
            if a%2==0:
                l.append(a)
            a = a+1
    except Exception as e:
        lg.error(e)