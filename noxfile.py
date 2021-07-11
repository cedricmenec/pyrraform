import nox


@nox.session
def dev(session):
    session.install("-r", "requirements-dev.txt")
