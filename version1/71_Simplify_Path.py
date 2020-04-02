"""
Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
"""


def simplify_path(path):
    """
    :type path: str
    :rtype: str
    """
    path += "/"
    dirs = []
    tmp_dir = ""
    for p in path:
        if p == "/":
            if len(tmp_dir):
                if tmp_dir == ".":
                    pass
                elif tmp_dir == "..":
                    if len(dirs):
                        dirs.pop()
                else:
                    dirs.append(tmp_dir)
                tmp_dir = ""
        else:
            tmp_dir += p
    return "/" + "/".join(dirs)


def simplify_path_dma(path):
    path += '/'
    dfa = [
        {"/": 1},
        {"/": 1, ".": 2, "dir": 4},
        {".": 3, "/": 1, "dir": 4},
        {"/": 1, ".": 4, "dir": 4},
        {"dir": 4, "/": 1, ".": 4},
    ]
    dirs = []
    state = 0
    tmp_dir = ""
    for p in path:
        option = p
        if not (p == "/" or p == "."):
            option = "dir"
        previous_state = state
        state = dfa[state][option]
        if state != 1:
            tmp_dir += p
        if state == 1:
            if previous_state == 4:
                dirs.append(tmp_dir)
            elif previous_state == 3 and len(dirs):
                dirs.pop()
            tmp_dir = ""
    if len(tmp_dir):
        dirs.append(tmp_dir)
    return "/" + "/".join(dirs)


examples = [
    {
        "path": "/a/./b/../../c/",
        "res": "/c"
    }, {
        "path": "/home/",
        "res": "/home"
    }, {
        "path": "/a/./b/../../../",
        "res": "/"
    }, {
        "path": "/a////b/../../c/",
        "res": "/c"
    }, {
        "path": "/...a",
        "res": "/...a"
    }, {
        "path": "/.a..a",
        "res": "/.a..a"
    }, {
        "path": "/..a...",
        "res": "/..a..."
    }, {
        "path": "/.",
        "res": "/"
    }, {
        "path": "/abc/...",
        "res": "/abc/..."
    },
]


for example in examples:
    print simplify_path(example["path"])
