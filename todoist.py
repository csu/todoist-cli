import click
import AccountCredentials
import requests
import urllib

token = AccountCredentials.TODOIST_API_TOKEN

def add_task(task, project=None, priority=None, indent=None, date=None):
    task = urllib.quote(task)
    if date:
        date = urllib.quote(date)

    request = 'https://api.todoist.com/API/addItem?content=' + task + '&token=' + token
    if project:
        request += '&project_id=' + project
    if priority:
        request += '&priority=' + priority
    if indent:
        request += '&indent=' + indent
    if date:
        request += '&date_string=' + date
    r = requests.get(request)

@click.command()
@click.option('--project', '-po', help='a project id')
@click.option('--priority', '-pi', help='priority (1 to 4, 4 highest)')
@click.option('--indent', '-i', help='indent level (1 to 4, 1 top-level)')
@click.option('--date', '-d', help='due date (Todoist-formatted date string)')
@click.argument('file')
def add_tasks_from_file(file, project, priority, indent, date):
    """Add tasks from a file"""
    with open(file) as f:
        content = f.readlines()
    for item in content:
        add_task(item, project, priority, indent, date)

if __name__ == '__main__':
    add_tasks_from_file()