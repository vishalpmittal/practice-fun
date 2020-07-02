## Coding exercise: raffle web service

In this exercise, you are to implement a REST-based web service that can be
used to power an online raffle. The raffle consists of participants
(identified by a unique username) that each have a positive number of
tickets. There’s also an exciting twist: participants are allowed to give
their tickets to someone else.

### Endpoint Descriptions

Your web service should implement REST endpoints that allow:
- Issue new raffle tickets to someone
    - Inputs:
        - Number of tickets
        - Unique username
    - The recipient may or may not already have raffle tickets
- Transfer existing raffle tickets from one participant to another
    - Inputs:
        - Number of tickets
        - Unique username for donor
        - Unique username for recipient
    - The recipient may or may not already have raffle tickets
    - If the transfer is invalid, then return an appropriate error
- Selecting a winning ticket for the raffle
    - Output:
        - Unique username for winning participant
    - Selecting a winner removes that ticket from the raffle
        - The selected person should end up with one fewer ticket
        - If the person still has tickets, they are still a participant for
          future drawings
        - If the person no longer has tickets, then they are no longer a
          participant for future drawings
    - The winner should be randomly selected such that each raffle ticket is
      equally likely
    - If the raffle does not have any raffle tickets, then return an
      appropriate error
- Listing the participants of the raffle
    - Outputs:
        - Unique usernames for each raffle participant
    - The usernames do not have to be in any particular order
    - Participants must have a positive number of tickets

Assume that the number of winners is much smaller than the number of
participants, and that the number of participants is slightly smaller than
the number of tickets. Issuing and transferring raffle tickets will be
invoked much more frequently than selecting winners or listing participants.
You do not need to implement access control for the endpoints.

### Other Functional Requirements

Your implementation does not need to be fault tolerant (i.e., no data needs
to be persisted), but it should be able to correctly and efficiently handle a
large number of raffle participants (assume it will still comfortably fit
memory). Moreover, your implementation should allow the various raffle
operations (giving tickets, selecting winners, etc.) to occur concurrently
while ensuring correctness.

### Your program

You can use any language you like. We'll be looking at the high-level
approach you take and won't be paying attention to low-level optimizations.

You can use basic in-memory data structures like arrays, hash tables, trees,
heaps, and the like from your language's standard library (or a popular
alternative). You may also use any popular frameworks for building a web
service in the language you choose, but you cannot use any libraries or
services that already implement something similar to a raffle.

### Evaluation

Please send us a .zip or .tar.gz file with your program and a writeup about
how your program works.

It is more important to have a working program than the best possible
program; there's no need to over-generalize or over-optimize. An ideal,
awesome solution would have a basic working program and a short, yet
thoughtful writeup about how it could be improved.

Feel free to use any outside resources, although any code you write should be
your own!

In the writeup, please include:

- A short description of how to build and run your web service
- The documentation for your REST APIs (e.g., endpoint verbs, names,
  request/response bodies, return codes, etc.). This should be the majority
  of the writeup.
- A brief analysis of the space and time complexity and scalability of your
  chosen approach
- Any assumptions you made
- Any improvements you could make in the future (e.g., performance,
  testability, etc.)

The writeup does not need to be very long: a few notes for each point should be enough.