
## red-black
you have your original environment, you have the new environment, 
and they're both running. You've set up the records and DNS for both endpoints 
and data is being replicated across the environments. 
Once everything is ready to go, you simply switch the DNS over to the new environment. 

You still keep the original environment running and if you experience any issues with 
the migrated application, you can cut back to the original. 

## blue-green
Setup is the exact same with both environments being up, tested, and running and DNS setup 
is still there. The big difference here is that your cut-over needs to be more gradual. 
With this setup, instead of an instant cut-over, you're only shifting a small percentage 
of traffic at a time, maybe 5%, maybe 10. 

### Comparison
* Down time
  + RB: if you have an issue once traffic has been shifted, the application could be
    down until you're able to move traffic back to the original environment
  + BG: The major reason for the use of blue green is to avoid downtime.
* Issues
  + RB: more concentrated
  + BG: issues are less widespread and the number of affected users due to an issue is easier to manage
* Complexity
  + RB: less complex
  + BG: you have to be using a DNS service that gives you the ability to control
    the amount of traffic going to each endpoint.
    More management
* Cost
  + RB: less cost
  + BG: usually higher cost
