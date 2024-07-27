# -*- coding: utf-8 -*

import random
import string


def gen_string(length=10, chars=string.ascii_lowercase + string.digits):
    return ''.join([random.choice(chars) for i in range(length)])

def gen_int(start, stop):
    """[start, stop]"""
    return random.randint(a=start, b=stop)


def gen_one(populations):
    return random.choice(populations)


def gen_sample(populations, sample_size):
    return random.sample(populations, sample_size)


def gen_double(start, stop):
    return random.uniform(start, stop)
