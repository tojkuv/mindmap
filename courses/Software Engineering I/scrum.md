# scrum (sprint development cycle)

## framework



### definition

- done - a features is considered done when a feature is a tested and potentially shippable product increment
  - questions the be answered:
    - functionality has been completed based on the user stories completed and the agreed to sprint goals
    - quality has been verified with a hign degree of confidence
    - can the features be shipped? questions to consider:
      - has the customer been trained?
      - does it integrate with out features that have not been developed?
      - has there been a change in managemennt communication?
- product backlog => sprint backlog => sprint implementation => potentially a shipable version

## attributes

- organized meetings
- time-boxed iterations (~7..30 days range) that may or may not remain static until the end of the product's development
  - work not completed in an iteration gets added back into the product backlog

## artifacts

- **product backlog** - prioriitized list of features to be implemented into the product
- **sprint backlog** - a temporary backlog that only lasts until the end of the respective sprint
  - each feature contains tasks that must be complete before the feature is considered done
- **shippable product incremet** - completed functionality that has been completed, tested and demoed for the given sprint and can be deplaoyed to production
- **user story** - a description of the functionality from the backlog point of view if a person (or user) of the system, and what value it delivers
  - document template:
    - title:
      - \<user story title\>
    - body:
      - \<as a \<user role\> i want to \<goal\> so that \<benefit\>\>
    - acceptance criteria:
      - a list of [and/or] elements, functionalities, spesification compliances that must be implemented before the user story can be considered complete
- **sprint** - a timeboxed iteration where thhe development of user stories gets done

## roles

- **scrum master**
  - responsibilities:
    - mentors the team members
    - listens to the team member's concerns
    - resolves the team member's concerns
- **product owner**
  - responsibilities:
    - prioritizes the product backlog
    - creates user stories for the backlog items
    - picks the product backlog items to move to the sprint backlog
- **cross-functional team**
  - responsibilities:
    - implement the user stories created by the product owner into deliverable functionality
    - self-organized and product-focused
  - roles:
    - software developers
    - software testing
    - development operations
    - user testing

## meetings

- planning (first meeting)
  - product owner and the team timebox a sprint and agree on the features to pull from the product backlog into the sprint backlog
  - the time allocation should be 1 hour per week of sprint work.
- stand-up (intermediate meetings)
  - sprint progress report
  - questions answered during the meeting:
    - what have you done since the last stand-up meeting?
    - what are you going to do until the next stand-up meeting?
    - what implementations are standing in your way?
  - time allocation should me 15 minutes max (topics that need to be discussed in more detail should be discussed outside the meeting in the appropriate matter)
  - the meetings are usually scheduled during daily at the same time.
- sprint review (demonstration meeting)
  - completed stories are demonstrated to the product owner and other stakeholders
  - feedback is collected from the stakeholders for the next sprint
    - information flow is bi-directional
  - time allocation should not exceed more that 1 hour per week of sprint
- sprint retrospective (last meeting) - teams review the completed features with the stakeholders for feedback
  - this feedback is used to [and] pick the next items from the backlog, improve the approach of the next sprint
  - questions to be answered:
    - what has been going well in the last sprint and how do we continue to do it?
    - what hasn't been working well in the sprint and how do we improve?
    - time allocation should not exceed more than 2 hours per week of sprint

## notes:

- a release may or may not be possible after each sprint
- scrum was created for software development, but was adopted to to cycle work of other fields
- stakeholders provide immediate feedback
- changes can be implemented after each iteration instead of at the end
- inspection of software
- customers provide immediate feedback

## alternative development frameworks

- waterfall (plan drive develpoment) ***(too rigid and inefficient)***
  - step 1: analysis from customer interaction
  - step 2: design
  - step 3: testing
  - step 5: production from customer iteraction with product
  - disadvantages:
    - no immediate feedback
    - costly to implement any changes late in the process
    - no way to inspect and adapt or pivot
    - customers were usually kept away from the project until the very end
- cynefin framework domains (non-developpment cycle domains)
  - complex - exploratory
  - compilcated  - specialized knowledge
  - simple - easy to solve
  - chaotic - emergencies
  - disorder - unknown domain that must be dissambiguated into a known domain
    - this is usually done by breaking down the situation into smaller components and categorizing these components
- kanban (interrupt-drive overlay)