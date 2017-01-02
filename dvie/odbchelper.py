#!/usr/bin/env python
# -*- coding: UTF-8 -*-

def buildConnectionString(params):
    """
    Build a connection string from a dictionary of parameters.
    Returuns string.
    """
    return ";".join(["%s=%s" % (k,v) for k,v in params.items()] )

if __name__=="__main__":
    myParams={"server":"mpilgrim",
              "database":"master",
              "uid":"da",
              "pwd":"secret"}
    print buildConnectionString(myParams)

