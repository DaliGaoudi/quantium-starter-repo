from app import app


def walk(c, path='root'):
    cid = getattr(c, 'id', None)
    print(f"{path}: type={type(c).__name__}, id={cid}")
    children = getattr(c, 'children', None)
    if children is None:
        return
    if isinstance(children, (list, tuple)):
        for i, ch in enumerate(children):
            walk(ch, f"{path}.{i}")
    else:
        walk(children, f"{path}.child")


if __name__ == '__main__':
    walk(app.layout)
