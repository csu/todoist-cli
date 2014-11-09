import click
import AccountCredentials
import requests
token = AccountCredentials.TODOIST_API_TOKEN

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
        request = 'https://api.todoist.com/API/addItem?content=' + item + '&token=' + token
        if project:
            request += '&project_id=' + project
        if priority:
            request += '&priority=' + priority
        if indent:
            request += '&indent=' + indent
        if date:
            request += '&date_string' + date
        r = requests.get(request)

if __name__ == '__main__':
    add_tasks_from_file()