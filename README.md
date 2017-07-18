# jiraya - Simple Jira CLI

Jiraya is a simple CLI to deal with Jira issues. 


## Commands

```shell
λ jiraya --help
jiraya - Simple Jira CLI.

Usage:
  jiraya assign <issue> [<username>] [--project=<name>]
  jiraya backlog [--project=<name>]
  jiraya comment <issue> <message> [--project=<name>]
  jiraya comments <issue> [--project=<name>]
  jiraya doing [--user=<user>] [--project=<name>]
  jiraya info <issue> [--project=<name>]
  jiraya move <issue> [<status>] [--project=<name>]
  jiraya open <issue> [--project=<name>]
  jiraya review [--project=<name>]
  jiraya tasks <issue> [--project=<name>]
  jiraya todo [--project=<name>]
  jiraya unassign <issue> [--project=<name>]
  jiraya url <issue>
  jiraya (-h | --help)
  jiraya --version

Options:
  -h --help               Show this screen.
  --version               Show version.
  -p --project=<name>     Jira project name. Also configurable with JIRA_DEFAULT_PROJECT environment variable.
```

## Configuration

Jiraya uses Basic Auth for authentication on Jira API. You'll need to export the following environment variables:

- `JIRA_URL`: This is your Jira instance base endpoint, such as: https://mycompany.atlassian.net. If you use Jira on premises, point this to your internal endpoint.
- `JIRA_USERNAME`: Your Jira username.
- `JIRA_PASSWORD`: Your Jira username.
- `JIRA_DEFAULT_PROJECT`: Jira default project. (Optional, all commands support `--project`)

## Working with Jiraya

My main workflow consists on:

1. Finding a planned issue to work on: `jiraya todo`
1. Assigning it to myself: `jiraya assign RO-42`
1. Moving the issue to "In progress": `jiraya move RO-42 "In Progress"`. Use `jiraya move RO-42` to list the available statuses.
1. Adding comments: `jiraya comment RO-42 "Jiraya is awesome"`
1. Moving to next status: `jiraya move RO-42 "Review"`
1. Repeat

## License

MIT
