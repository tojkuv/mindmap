# Unified Modeling Language (UML)
this modeling language can be used to model static and dynamic systems.

## components:
### things:
#### structural
define the static part of the model, that is, they represent the physical and conceptual elements (e.g. classes and interfaces).
  - <img src="file:///home/machine/Pictures/Screenshots/Screenshot%20from%202023-02-03%2010-16-00.png" title="" alt="" width="282">

#### behavioral
define the dynamic part of the model (e.g. a state machine from a method or function)
  - <img src="file:///home/machine/Pictures/Screenshots/Screenshot%20from%202023-02-03%2010-24-41.png" title="" alt="" width="158">

### grouping
define a mechanism to group elements of a UML model together (e.g. a library package).
- annotatorial - define a mechanism to capture remarks, descriptions and comments of UML model elements. the note component is the only annotatorial thing available.
  - <img src="file:///home/machine/Pictures/Screenshots/Screenshot%20from%202023-02-03%2010-45-59.png" title="" alt="" width="155">

### relationships
#### dependency
a relationship between two things in which change in one element also affects the other.
  - <img src="file:///home/machine/Pictures/Screenshots/Screenshot%20from%202023-02-03%2010-51-21.png" title="" alt="" width="217">
#### association 
a set of links that connects the elements of a UML model. it also describes how many objects are taking part in that relationship (e.g. array list).
  - <img src="file:///home/machine/Pictures/Screenshots/Screenshot%20from%202023-02-03%2010-54-28.png" title="" alt="" width="219">
  - <img title="" src="file:///home/machine/Pictures/Screenshots/Screenshot%20from%202023-02-03%2010-55-01.png" alt="" width="221">
  - <img src="file:///home/machine/Pictures/Screenshots/Screenshot%20from%202023-02-03%2010-55-31.png" title="" alt="" width="224">

#### generalization
defined as a relationship which connects a specialized element with a generalized element. (e.g. the inheritance relationship in object-oriented programming).
  - <img src="file:///home/machine/Pictures/Screenshots/Screenshot%20from%202023-02-03%2011-01-02.png" title="" alt="" width="217">

#### realization
define an implementation relationship (e.g. implementations of interfaces)
  - ![](/home/machine/Pictures/Screenshots/Screenshot%20from%202023-02-03%2011-02-58.png)

## diagrams:
### class diagrams
represent the relationships between classes.
- ![](/home/machine/Pictures/Screenshots/Screenshot%20from%202023-02-03%2011-22-29.png)

### component diagrams
represents the structural relationship of components of a software system.
  - ![](/home/machine/Pictures/Screenshots/Screenshot%20from%202023-02-03%2011-27-19.png)

### use case diagrams
describes the actors involved in a system and the different functions needed by those actors.
- ![](/home/machine/Pictures/Screenshots/Screenshot%20from%202023-02-03%2012-08-05.png)
  - actor - an entity that performs a role in the system (person figure)
  - use case - a function or action within the system (oval shape)
  - system - defines the scope of th system (rectangle)
  - package - used to group together use cases (folder shape)

### activity diagram
flowchart of actions without actors explicitly stated
- ![](/home/machine/Pictures/Screenshots/Screenshot%20from%202023-02-03%2012-11-51.png)
  - rounded rectangles - represent actions
  - diamonds - represent decisions
  - bars - represent the start (split) or end (join) of concurrent activities
  - black circle - represents the start (initial node) of the workflow
  - encircled black circle - represents the end (final node)

### sequence diagram
flowchart of actions with actors explicitly stated
- ![](/home/machine/Pictures/Screenshots/Screenshot%20from%202023-02-03%2012-21-22.png)
  - lifetimes - actors inside rectangles
  - interactions - represented as arrows
  - messages - written with the message name above the interaction arrows

# software testing overview
software quality is defined by:
- accuracy
- maintainability
- reliability
- portability
- usability

software testing is the process of running a piece of software with the intent of finding faults, which could lead to failures. testing software does not guarantee that there will not be errors in the software. therefore the goal of testing is to find errors, not to demonstrate correctness.

broadest terms of software testing:
- validation - tests if the product fits the acceptance criteria
- verification - tests if the product was built correctly

methods of software testing:
- static testing - tests that do not run the software (e.g. manual review, passing the software to analytical software)
- dynamic testing - tests that do run the software

exhaustive testing is usually infeasible. thus test cases that test a large domain should be split into subsets and the test cases inputs should be chosen from the subsets, appropriately.

testing visibility:
- black-box testing - derives cases from external descriptions of the software, including specifications, requirements and design. (e.g. requirement documents, sprint backlog, sprint user stories, and UML sequence diagrams, method's pre-conditions and post-conditions).
  - this type of testing is commonly used at the broader levels of testing (e.g. system and acceptance testing).

- white-box testing - derives test cases from the source code of the software, specially from branches, individual conditions and statements. this type of testing has the following tests scopes:
  - acceptance testing - is that which is conduced by the owner of the software.
    - usually when one company contracts to build software for another company, the artifact delivered to the contracting company is the executable version of the program, not the source code. thus, the client must perform black-box tests for the acceptance criteria. the contractee company could also perform white-box acceptance testing.
    - testing here is also based on test cases that are developed from requirements (sometimes referred to as *use cases*or *user stories*). the company may have method of requirements tracing in which they map requirements to the test cases that validate these requirements.
  
  - regression testing - a set of test cases are developed to test a version ov the software and is then applied to subsequent versions to assure that the newer versions maintain the same functionality as the previous version.
  
  - unit testing - focuses on testing units of the software after they are developed. a unit is considered to be the smallest testable part of an application (e.g. method, class or individual code segment).
  
  - integration testing - 
  
  - user testing:
    - alpha testing - involves a group of a small set of users, typically inside the same company or trusted external partners. this testing is usually done near the completion of the software. user are instructed to use the software as opposed to test cases. this may not test every feature of the software.
    - beta testing - involves a larger group of external trusted users. this is done when the software is complete. users are instructed to use th software as opposed to test cases. this tests the reliability of the software. if major problems or critical failures are discovered, they can be fixed before an official release.  

# integration testing
software components, hardware components, or both are combined and tested to evaluate the interaction between them. 

components are integrated and tested, if no faults are revealed then additional components are added and tested. the most recently added component is usually the one that triggers the most recently discovered fault. the order in which components are integrated influences the total testing effort (i.e. the creation of stubs and drivers).

done after unit testing is performed on the various parts of the software. 

typically separate teams of software engineers independently develop the various parts of the software that are to be integrated. thus, it is common for there to be error when these pieces are integrated. black-box testing is typically done at this point to test completed components.

regression testing is usually done after integration testing.

## big bang testing
assumes that all components are first tested individually and then tested together as a single system.
- debugging is a problem, i.e., where is the fault of system-wide tests?
- reduces the # of stubs and drivers required.

## bottom-up testing
individually test each component of the bottom layer and then integrate them with components of the next layer (assumes a hierarchical structure).
- drivers are required to simulate the components of higher layers.
- no test stups are required.

## top-down testing
unit test the components of the top layer first and then integrate the components of the next layer down.
- stubs used to simulate the components of lower layers
- drivers are not required.

## sandwich testing
is a combination of toy-down and bottom-up integration.

## ordering based on dependencies
a dependency graph is created (similar to a class diagram), then an order is generated. the leaf components are tested first then the inner components.
- issues arise if the dependency graph is a cyclic graph.
  - use of stubs in the event of cycles.

# system testing
testing of a completed application to determine that it provides all the behaviors required of the application.

test scopes:
- functional (input/output)
- performance (response time and resource utilization)
- stress or load (response under maximum or overload)
- acceptance testing and installation testing

## configuration and compatibility
application systems are often designed to run on many target environment configurations ar are required to interoperate with many combinations of hardware and software.

hardware:
- existing computer systems, 
- different OSs and/or different versions of OS

software:
- existing applications
- different GUIs and/or versions of a particular GUI
- different DBMSs and/or version of a particular DBMS
- APIs ind interface definition language
- data interchange formats

## performance
software systems must produce results within acceptable time intervals. inability to meet the performance objective is no less a bug than incorrect output or a system crash.

### load testing
a set of transactions is automatically submitted to the system at varying rates, simulating the effect of many concurrent users entering transactions at client nodes.

### volume testing
largest volume input file is used or a large file is generated. the idea is to transmit a high quantity of input under normal system loading. usually associated with batch-processing systems.

## integrity and fault tolerance
### concurrency testing
### stress testing
### restart/recovery testing

## human-computer interaction
the correct and effective use of some systems depends on the software, its relative ease of use, and collateral materials that provide necessary information to human users. all these factors must be evaluated together to identify HCI bugs. the testing typically relies more on skillful testing than on high-volume automated testing.

testing criteria:
- usability - evaluates the ergonomics of a human-computer interaction design
- security - evaluates concerns such as log-on, log-off, and among other things
- localization - evaluates the ability to configure the system for use in different local environments (e.g. translating text on the UI to several languages, framing of content on different display aspect ratios)
- installation - evaluates the ability to install the software with the documentation provided

## security testing
reveals flaw in the security mechanisms of an information system that protects data and maintains functionality as intended. testing requirements may include specific elements of confidentiality, integrity, authentication, availability, authorization, non-repudiation





















