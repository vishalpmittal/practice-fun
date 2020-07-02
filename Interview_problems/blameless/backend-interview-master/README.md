# Blameless Backend and Infra Interviewing

This is the Python-based take home question for Blameless engineering.

## Blameless' Approach to Interviewing

The take-home exercise is the main coding portion of the interview process at
Blameless.  We believe that interviewing should simulate your normal work
environment, not test your ability to cram beforehand or memorize a bunch of
trivia.  We also understand that this is a two-way interview; you are also
interviewing us.  As such, the process is as follows:

- **Phone screen**: Brief intros to get to know each other, answer any
  questions and explain the take home project.

- **Take-home Project**: This project is not intended to stump you.  If you
  have a few years of software development experience, it should take not
  longer than 3-4 hours to complete, including some tests.

- **On-site**: The main purpose of the on-site is to have you meet the team
  in-person (some will be remote, but on video chat), talk about the take home
  project, run a small design session about a recent technical project you were
  particularly proud of and talk in-depth about some of your experiences.

  - **Take Home Feedback** (1 hour): This is a discussion about the take home
    portion of the interview.  Let us know what you really thought of it!
    Typical discussions talk about modifications to the requirements, modifications
    to the API and general improvements to your approach.

  - **Tech Feedback** (1 hour): You should come prepared to hit the whiteboard
    and talk with a few engineers about a recent project that you led or had a
    significant contribtuion in delivering.  We expect that you will lead the
    discussion.  Typical discussions focus on, architecture, design patterms,
    bottlenecks, testing, operations, scale, deployment and performance.  Remember
    that you are also interviewing us, so feel free to ask any questions you find
    necessary.

  - **Coffee with Founders** (30 minutes): Grab a cup of coffee with one of
    the founders.  Use this time to ask questions about the company culture, the
    product and the opportunities for and at Blameless.

  - **Professional Retrospective** (1 hour): The main goal here is to talk generally
    about your professional experience and why you are interested in Blameless.  Again,
    this is another opportunity to ask us any questions you may have.

## Instructions for the Take Home Project

The project will be described during the phone screen.  Feel free to get
clarification and provide feedback for the take home project during the phone
screen.  We welcome any and all feedback.

There are two options for the take home: Python and Golang.  In both cases, you
will implement a `ServiceMontior` interface that will be used by a provided
driver program (`main.py` for Python and `main.go` for Golang).  The
description below will give details on the interface and expected output.

### Definitions

- Service Level Indicator (SLI): a carefully defined quantitative measure of
  some aspect of the level of service that is provided.  For this project, the
  success rate of requests to a particular endpoint is the SLI.

- Service Level Objective (SLO): a target value or range of values for a
  service level that is measured by an SLI.  For this project, the minumum
  success rate of requests to a particular endpoint of a service is the SLO
  for that endpoint.

- Incident: an event that begins when the `SLI<SLO` and ends when `SLI>=SLO`

In this project, our SLI is *success rate* and our SLO is *availability*.
Availability is measured as the ratio of successful requests to all requests
over a sliding window.  We consider a healthy service to have `SLI >= SLO` in a
particular window; otherwise the service is unhealthy.  For example, if we set
the SLO to 0.9 and at this instant our window has 89 successes out of 100
requests, the service is deemed unhealthy.  If, a second later, there are 95
successes out of 101 total requests in the window, the service is deemed
healthy.

### Description

The purpose of the take home project is to determine the health of a set of API
endpoints as changes are applied to them.  Both are determined by reading
request and change events emitted by an event stream.  Using the request and
change information, you will have to detect when an incident starts, when it
ends and the changes that led to the incident and its remediation.

The description below used the Python function names.  The Golang names are similar,
but CamelCase instead of snake_case.

You will implement a function called `get_service_monitor()` that takes an
`EventStream` object as an argument and returns a an object that implements two
functions `mttr()`, `incident_details()` and `api_histogram()`:

- `mttr()`: This function returns a single value that is the mean time to repair a problem.

- `incident_details()`: This returns a dictionary keyed on `api-name`, where
  each entry contains a list of incident details.  Each entry in the list
  contains the start time, end time, commit that broke the API and the commit
  that fixed the API.

- `api_histogram()`: This function returns a dictionary keyed on `api-name`,
  where each value represents the number of issues introduced by that API.

`EventStream` provides two functions needed to implement `mttr()`,
`incident_details()` and `api_histogram()`:

- `generate_event()`: This function will return a Python dictionary with two
  entries: `type` and `value`.  The type will determine the type of event.
  - `'access'`: This is an access log event that has the following format:
    ```[timestamp] [verb] [resource] [status]```
    - `timestamp`: An integer timestamp in seconds
    - `verb`: An HTTP verb (i.e. GET, POST, etc.)
    - `resource`: An HTTP resource (e.g. /files, /api/v1/foo, etc.)
    - `status`: An HTTP status code: 200 is success, 500 is failure

  - `'change'`: This is a change log event that has the following format (Golang uses time.UnixDate for layout):
    ```
    commit: [commit-hash]
    Author: <[api-email]>
    Date: [YYYY-MM-DD HH:MM:SS]
    Service: [api-name]
    ```
  - `'end-of-stream'`: This represents the end of stream, where processing can complete

- `get_info()`: This function will return a list of dictionaries, where each dictionary has the following format:
```{ 'name': [api-name], 'email': [api-email], 'verb': [http-verb], 'resource': [http-resource], 'slo': [slo], 'window': [sli-window]}```

The information provided by `get_info()` represents all of the API endpoints emitted from both the access log and change log events.

### Example

Here we provide a very small example to illustrate the problem and format.

#### Python Solution

Implement your solution in the source file `python/solution/monitor.py`.  The
main entrypoint is located here: `python/main.py`.  See the usage to determine
how to generate different event streams.

The main requirement is that your solution implements a function called
`get_service_monitor` that takes an EventStream object as an argument (see
EventStream (see internal.events.EventStream)).  The `get_service_monitor`
must return an object that implements (each was described above):

- `service_monitor.mttr()`
- `service_monitor.api_histogram()`
- `service_monitor.incident_details()`

Test your solution by running from `python/`:

```
$ python main.py
```

#### Golang Solution

Implement your solution in the source file `golang/monitor.go`.  The main entry
point is located here: `main.go`.  See the usage to determine how to generate
different event streams.

The main requirement is that your solution implement the provided
`ServiceMonitor` interface (provided in `golang/monitor.go`), which takes an
`EventStream` as an argument.

Test you solution by building and running from `golang/`:

```
$ go build ./...
$ ./takehome
```

#### Details

Here is an example event stream (triple asterisk lines are not part of the
stream; they illustrate when an API violates its SLO and recovers.

```
{'type': 'change', 'value': 'commit: 191b6ce2fc724b37a063e8b07065f80b\nAuthor: <marcasitic@pathognomy.com>\nDate: 2018-11-28 14:11:31.071432\nService: nonexpulsion\n'}
{'type': 'access', 'value': '1543443091.1738 GET /api/v1/tricalcium 200'}
{'type': 'access', 'value': '1543443091.2745 GET /api/v1/tricalcium 500'}
*** nonexpulsion unhealthy at time 1543443091.27 ***
{'type': 'access', 'value': '1543443091.2761 GET /api/v1/nonpaying 200'}
{'type': 'access', 'value': '1543443091.3718 GET /api/v1/tricalcium 500'}
{'type': 'access', 'value': '1543443091.4735 GET /api/v1/tricalcium 500'}
{'type': 'access', 'value': '1543443091.4775 GET /api/v1/nonpaying 200'}
{'type': 'access', 'value': '1543443091.5668 GET /api/v1/tricalcium 500'}
{'type': 'access', 'value': '1543443091.6721 GET /api/v1/nonpaying 200'}
{'type': 'access', 'value': '1543443091.6733 GET /api/v1/tricalcium 500'}
{'type': 'access', 'value': '1543443091.7710 GET /api/v1/tricalcium 500'}
{'type': 'access', 'value': '1543443091.8755 GET /api/v1/nonpaying 200'}
{'type': 'access', 'value': '1543443091.8768 GET /api/v1/tricalcium 500'}
{'type': 'access', 'value': '1543443091.9852 GET /api/v1/tricalcium 500'}
{'type': 'access', 'value': '1543443092.0622 GET /api/v1/nonpaying 200'}
{'type': 'access', 'value': '1543443092.0813 GET /api/v1/tricalcium 500'}
{'type': 'change', 'value': 'commit: 6d0080aaecbf4bd69f9b8962cb007e53\nAuthor: <marcasitic@pathognomy.com>\nDate: 2018-11-28 14:11:32.081340\nService: nonexpulsion\n'}
{'type': 'access', 'value': '1543443092.1912 GET /api/v1/tricalcium 500'}
{'type': 'access', 'value': '1543443092.2751 GET /api/v1/nonpaying 200'}
{'type': 'access', 'value': '1543443092.2853 GET /api/v1/tricalcium 200'}
{'type': 'access', 'value': '1543443092.3884 GET /api/v1/tricalcium 200'}
{'type': 'access', 'value': '1543443092.4705 GET /api/v1/nonpaying 200'}
{'type': 'access', 'value': '1543443092.4967 GET /api/v1/tricalcium 200'}
{'type': 'access', 'value': '1543443092.5888 GET /api/v1/tricalcium 200'}
{'type': 'access', 'value': '1543443092.6821 GET /api/v1/nonpaying 200'}
{'type': 'access', 'value': '1543443092.6952 GET /api/v1/tricalcium 200'}
{'type': 'access', 'value': '1543443092.7932 GET /api/v1/tricalcium 200'}
{'type': 'access', 'value': '1543443092.8845 GET /api/v1/tricalcium 200'}
{'type': 'access', 'value': '1543443092.8989 GET /api/v1/nonpaying 200'}
{'type': 'access', 'value': '1543443092.9885 GET /api/v1/tricalcium 200'}
{'type': 'access', 'value': '1543443093.0855 GET /api/v1/tricalcium 200'}
{'type': 'change', 'value': 'commit: b9936e80e621448fbef0802be647bd67\nAuthor: <dikaryophytic@diarchy.com>\nDate: 2018-11-28 14:11:33.085478\nService: kioea\n'}
{'type': 'access', 'value': '1543443093.0912 GET /api/v1/nonpaying 200'}
{'type': 'access', 'value': '1543443093.1835 GET /api/v1/tricalcium 200'}
{'type': 'access', 'value': '1543443093.2896 GET /api/v1/tricalcium 200'}
*** nonexpulsion recovered at time 1543443093.29 ***
{'type': 'access', 'value': '1543443093.3109 GET /api/v1/nonpaying 500'}
*** kioea unhealthy at time 1543443093.31 ***
{'type': 'access', 'value': '1543443093.3956 GET /api/v1/tricalcium 200'}
{'type': 'access', 'value': '1543443093.4989 GET /api/v1/tricalcium 200'}
{'type': 'access', 'value': '1543443093.4991 GET /api/v1/nonpaying 500'}
{'type': 'access', 'value': '1543443093.6055 GET /api/v1/tricalcium 200'}
{'type': 'end-of-stream', 'value': 'end-of-stream'}
```

Each call to `event_stream.generate_event()` will return each of the lines above until you hit the `end-of-stream`, after which every call to `event_stream.generate_event()` will return `end-of-stream`.

Here is the return value from `event_stream.get_info()` based on the event stream above:

```
[{'name': 'kioea', 'email': 'dikaryophytic@diarchy.com', 'verb': 'GET', 'resource': '/api/v1/nonpaying', 'slo': 0.999, 'window': 1}, {'name': 'nonexpulsion', 'email': 'marcasitic@pathognomy.com', 'verb': 'GET', 'resource': '/api/v1/tricalcium', 'slo': 0.9999, 'window': 1}]
```

In this case, there are two API endpoints, each named `kioea` and
`nonexpulsion`, respectively.  Notice that the SLO for nonexpulsion is 0.9999,
which is violated after the second 500 status in the stream.  This is because
the SLI of nonexpulsion drops to 0.5 (1 successes / 2 total requests).  Also
notice the second change event for nonexpulsion.  Soon after, the errors
subside and nonexpulsion eventually recovers.

- *Key assumption*: We assume that the commit directly preceeding the detection
  of `SLI<SLO` caused the incident and the commit preceding the recovery
  remediates the incident.  Remember that it is possible that multiple detected
  incidents may contain the same commits, since the time series can natually
  oscillate above and below the SLO.

Here is the example output from each function you need to implement based on the example stream above:

- `service_monitor.mttr()`: `2.02`
- `service_monitor.api_histogram()`:
```
{'nonexpulsion': 1, 'kioea': 1}
```
- `service_monitor.incident_details()`:
```
{'nonexpulsion': [{'start': 1543443091.2745, 'end': 1543443093.2896, 'fix': '6d0080aaecbf4bd69f9b8962cb007e53', 'break': '191b6ce2fc724b37a063e8b07065f80b'}], 'kioea': [{'start': 1543443093.3109, 'end': -1, 'fix': '', 'break': 'b9936e80e621448fbef0802be647bd67'}]
```

Notice that we only have complete incident information for nonexpulsion, since
the incident in kioea does not finish before the end of the stream.

