from fabric import task


PROJ_DIR = '/srv/social_network'
VIRTUALENV_CMD = '/srv/.virtualenvs/vault77/social_network/bin/activate'


@task
def deploy(c):
    c.run('cd {}; git pull'.format(PROJ_DIR))
    c.run(
        'cd {}; source {}; pip install -r requirements.txt'.format(
            PROJ_DIR, VIRTUALENV_CMD
        )
    )
    c.sudo('supervisorctl restart gunicorn')
