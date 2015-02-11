import os
import os.path
import shutil
import subprocess

working_dir = os.path.realpath(os.path.dirname(__file__))
print 'Working directory: %s' % working_dir
docker_projects_dir = os.path.expanduser('~/Docker-Projects')
print 'Docker projects directory: %s' % docker_projects_dir
docker_projects = [
    {'name': 'docker-baseimage',
     'dirname': 'baseimage',
     'branches': ['master', '0.9.15']},
    {'name': 'docker-python',
     'dirname': 'python',
     'branches': ['master', '0.9.15']},
    {'name': 'docker-java-jdk7',
     'dirname': 'java-jdk7',
     'branches': ['master', '0.9.15']},
    {'name': 'docker-java-jdk',
     'dirname': 'java-jdk',
     'branches': ['oracle-java7', 'oracle-java8']},
    {'name': 'docker-tomcat7',
     'dirname': 'tomcat7',
     'branches': ['master', '0.9.15', 'oracle-java7', 'oracle-java8']},
    {'name': 'docker-apache2',
     'dirname': 'apache2',
     'branches': ['master', '0.9.15', 'oracle-java7', 'oracle-java8']},
    {'name': 'docker-gradle2',
     'dirname': 'gradle2',
     'branches': ['master', '0.9.15', 'oracle-java7', 'oracle-java8']},
    {'name': 'docker-maven',
     'dirname': 'maven',
     'branches': ['master', '0.9.15', 'oracle-java7']},
    {'name': 'docker-spring-ref',
     'dirname': 'spring-ref',
     'branches': ['master']},
    {'name': 'docker-example-apache2',
     'dirname': 'example-apache2',
     'branches': ['master']},
    {'name': 'docker-openam',
     'dirname': 'openam',
     'branches': ['master', '0.9.15']}]


def install_vundle():
    print 'Installing Vundle in home directory...'
    print subprocess.check_output(
        ['git', 'clone',
         'https://github.com/gmarik/Vundle.vim.git',
         os.path.expanduser('~/.vim/bundle/Vundle.vim')])

    print 'Copying vimrc into home directory..'
    shutil.copy(os.path.join(working_dir, 'vim', 'vimrc'),
                os.path.expanduser('~/.vimrc'))


def setup_docker():
    print 'Setting up Docker-Projects'
    if not os.path.isdir(docker_projects_dir):
        os.mkdir(docker_projects_dir)
    for project in docker_projects:
        projname = project['name']
        dirname = project['dirname']
        branches = project['branches']
        project_dir = os.path.join(docker_projects_dir, dirname)
        print 'Project: %s \n\tDirname: %s \n\tProject Dir: %s \n\tBranches: %s\n\n' \
            % (projname, dirname, project_dir, str(branches))
        if not os.path.isdir(project_dir):
            print subprocess.check_output(
                ['git', 'clone',
                 'git@github.com:milo-minderbinder/%s.git' % projname,
                 project_dir])
        os.chdir(project_dir)
        for branch in branches:
            print subprocess.check_output(['git', 'checkout', branch])
            if branch == 'master':
                command = ['docker', 'build', '-t',
                           'mminderbinder/%s' % dirname, project_dir]
                print 'Command: %s' % str(command)
                print subprocess.check_output(command)
            else:
                command = ['docker', 'build', '-t',
                           'mminderbinder/%s:%s' % (dirname, branch),
                           project_dir]
                print 'Command: %s' % str(command)
                print subprocess.check_output(command)


def main():
    setup_docker()


if __name__ == '__main__':
    main()
