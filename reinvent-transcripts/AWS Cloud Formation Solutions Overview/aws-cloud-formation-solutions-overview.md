# AWS Cloud Formation Solutions Overview

**Date:** December 08, 2025
**Source:** otter.ai

<audio controls>
  <source src="./AWS Cloud Formation Solutions Overview.mp3" type="audio/mpeg">
  Your browser does not support the audio element. <a href="./AWS Cloud Formation Solutions Overview.mp3">Download audio</a>
</audio>

## AI Summary
### Overview

The meeting covered AWS cloud solutions, focusing on cloud permission and smartphone provisioning at AWS. AWS CDK was highlighted for its ability to write high-level programs in various languages. The discussion emphasized the importance of guardrails, parameter validation, and intrinsic functions. Strategies for managing large stacks, such as breaking them into smaller, more manageable units, were discussed. The use of CloudFormation for creating resources and the benefits of using AWS CDK for better management were also covered. The session included a demo on using AWS CDK for template creation and drift remediation, showcasing features like early validation, rollback, and drift detection.

Action Items

More options

Automate provisioning in CI/CD so commits to Git trigger template deployment (set up pipeline automation).

Use change sets to preview and validate deltas before executing updates in accounts.

Refactor large/monolithic stacks into smaller stacks (foundation / network / application / service) to reduce blast radius and improve ownership.

Evaluate and/or adopt AWS StackSets for organization-level stack deployment where appropriate.

Replace brittle cross-stack exports where necessary by using SSM Parameter Store or dynamic references to reduce coupling when values may change.

Try stack refactoring (CLI/console) to move resources between stacks; attendees should test the console stack-refactor experience for their use cases.

Share the stack refactoring blog post and reference documentation with the team (link/resources).

Install the AWS Toolkit for VS Code and test the in-IDE authoring, static validation (cfn-lint), and Cloud Control API import features.

Use Cloud Control API and the IAC Generator to inventory accounts and import/manage existing manually-created resources into CloudFormation/CDK.

Enable early validation of change sets in CI/CD pipelines and integrate guard rules (or custom guard files) to catch runtime/property issues before execution.

Integrate drift detection and adopt drift-aware change-sets (revert-drift) in deployment workflows to remediate unauthorized or ad-hoc changes back to template state.

Implement server-side validation hooks (Lambda hooks) and consider Control Tower managed rules to enforce critical guard rules for deployments.

### Outline


**AWS Cloud Permission and AWS CDK Overview**

- Speaker 1 discusses the popularity of cloud permission and smartphone provisioning at AWS, emphasizing the importance of infrastructure awareness.
- Unknown Speaker mentions the ability to detect and manage drift, and introduces AWS CDK.
- Speaker 1 explains the use of AWS CDK for writing high-level programs in various languages and the synthesized desired end state.
- The process of using templates in production or staging environments and the role of CRPD automation pipelines is detailed.

**Template Deployment and Guardrails**

- Speaker 1 describes the use of templates in CloudFormation and the importance of guardrails, including preventative policy checks and customer-managed key resources.
- The concept of parameter validation to ensure correct parameter values is introduced.
- Speaker 1 explains the use of conditions and rules to conditionally create resources based on the environment, such as production versus dev-test setups.
- The day-two workflow for making changes in IAC templates and the importance of using change sets for previews is discussed.

**Validation and Reusability in Templates**

- Speaker 1 emphasizes the importance of validation and reusability in templates, including the application of validation to parameters and the use of intrinsic functions.
- The discussion includes the use of AWS CDK for creating multiple resources with similar properties and the benefits of using AWS CDK for troubleshooting.
- Speaker 1 introduces the concept of large stacks and the need for breaking them down into smaller, more manageable stacks.
- The benefits of using sets for organization and ownership are highlighted, along with the importance of using sets in organizations.

**Strategies for Managing Large Stacks**

- Speaker 1 discusses strategies for managing large stacks, including breaking them down into smaller stacks for better management and faster changes.
- The importance of ownership and the role of different teams in managing specific stacks is emphasized.
- Speaker 1 introduces the concept of using sets for organization and the benefits of using sets in organizations.
- The discussion includes the importance of using sets for reusability and the role of different teams in managing specific stacks.

**AWS CDK and Intrinsic Functions**

- Speaker 1 explains the use of AWS CDK for creating resources and the benefits of using intrinsic functions for managing resources.
- The discussion includes the use of AWS CDK for creating multiple resources with similar properties and the benefits of using AWS CDK for troubleshooting.
- Speaker 1 introduces the concept of using AWS CDK for creating large stacks and the importance of using AWS CDK for better management.
- The benefits of using AWS CDK for creating large stacks and the importance of using AWS CDK for better management are highlighted.

**Stack Refactoring and CDK World**

- Speaker 3 discusses the concept of stack refactoring and the benefits of using CDK for managing resources.
- The discussion includes the use of CDK for creating resources and the benefits of using CDK for better management.
- Speaker 3 introduces the concept of using CDK for creating large stacks and the importance of using CDK for better management.
- The benefits of using CDK for creating large stacks and the importance of using CDK for better management are highlighted.

**CloudFormation and CDK Integration**

- Speaker 3 explains the integration of CloudFormation and CDK for better management of resources.
- The discussion includes the use of CloudFormation for creating resources and the benefits of using CloudFormation for better management.
- Speaker 3 introduces the concept of using CloudFormation for creating large stacks and the importance of using CloudFormation for better management.
- The benefits of using CloudFormation for creating large stacks and the importance of using CloudFormation for better management are highlighted.

**Validation and Deployment in CloudFormation**

- Speaker 3 discusses the validation and deployment process in CloudFormation, including the use of change sets and early validation.
- The discussion includes the use of CloudFormation for creating resources and the benefits of using CloudFormation for better management.
- Speaker 3 introduces the concept of using CloudFormation for creating large stacks and the importance of using CloudFormation for better management.
- The benefits of using CloudFormation for creating large stacks and the importance of using CloudFormation for better management are highlighted.

**Drift Remediation and Revert Drift**

- Speaker 3 explains the concept of drift remediation and the ability to revert drift in CloudFormation.
- The discussion includes the use of CloudFormation for creating resources and the benefits of using CloudFormation for better management.
- Speaker 3 introduces the concept of using CloudFormation for creating large stacks and the importance of using CloudFormation for better management.
- The benefits of using CloudFormation for creating large stacks and the importance of using CloudFormation for better management are highlighted.

**Cross-Account Drift Detection**

- Speaker 4 asks about cross-account drift detection, and Speaker 3 explains the current limitations and potential solutions.
- The discussion includes the use of CloudFormation for creating resources and the benefits of using CloudFormation for better management.
- Speaker 3 introduces the concept of using CloudFormation for creating large stacks and the importance of using CloudFormation for better management.
- The benefits of using CloudFormation for creating large stacks and the importance of using CloudFormation for better management are highlighted.

## Speakers

- Speaker 1
- Speaker 2
- Speaker 3
- Speaker 4
- Speaker 5
- Speaker 6
- Speaker 7
- Speaker 8
- Unknown Speaker

## Transcript

**Speaker 1 (00:00):**  
For us, cloud permission, smartphone being the two most popular ways people provision things at AWS, and these are space to applications so they are aware of the infrastructure that already exists in the back end, so they can help you,

**Unknown Speaker (00:15):**  
kind of detect their drift and Manage drift for you as well.

**Unknown Speaker (00:22):**  
And we

**Unknown Speaker (00:42):**  
have my abstract.

**Speaker 1 (00:46):**  
From there, we have AWS CDK, of hardware. Started with CDK, you can write your desired entity in a high level program members like Java, Python, Google, right services, approximation user a

**Unknown Speaker (01:08):**  
number of technologies,

**Unknown Speaker (01:11):**  
such as community. There's also

**Speaker 1 (01:22):**  
January for the powerful. With multi

**Unknown Speaker (01:53):**  
server, open source your

**Speaker 1 (01:59):**  
desired end state, and That gives you a synthesized desire are Very powerful. So which helps you also be there to help you offer this template. So you start with the template that you wrote, and then generally your production or staging type of environment you're committing to actually, I mean, you're letting your CRPD automation pipeline give that deployed or submit those template to their staff Foundation service. But when you're doing more depth, it might be the other way around, where your

**Unknown Speaker (03:14):**  
original works.

**Speaker 1 (03:21):**  
If you're not using that so that can help you automate once you have committed your code to a Git repo, to help you provision that as well. Then you know, once the template is submitted to CloudFormation, you have sort of guardrails. We'll go over some of that today as well, using your preventative policy as code checks. There are various ways to do that.

**Speaker 1 (04:00):**  
Customer managed key resources. You can apply those type of deploy time checks or pre deploy checks within the template itself. You also have mechanism to do some validation, like you can have parameter validation to make sure the parameters you're putting in and here's the certain value, like it's not more earlier in the workflow. I can also have things like conditions and rules. So just to conditionally create resources, for example, like in production, you might want public private summit setup with Nat gateway provision in each AV versus dev test, and you might only have just a single NAT

**Unknown Speaker (04:49):**  
gateway. Similarly, your customers will often have different

**Speaker 1 (04:56):**  
instance sizes based on the environment, and then once you get to the address, you get provisioned at stats in your AWS account. So that's the kind of day one provisioning cycle. So as you know, most of you are likely from DevOps team, platform engineering, SRE etc. So infrastructures have to be very dynamic in our bigger usually add a new subnet or add some instances or add some REST API endpoint, potentially. So then you have your big potentially. So then you have your day two workflow where you're again making the changes in your IAC template. And then you can go into the same workflow to get whatever is changed, like that delta provision to create on this account. The recommendation is to make sure you use change steps to get a preview of what's about to change to make sure that's in line and you're not doing anything potentially disruptive.

**Unknown Speaker (05:48):**  
So that's a little bit about the overall AWS cloud

**Unknown Speaker (05:52):**  
solution workflow. Anybody had any questions? Cool.

**Speaker 1 (06:01):**  
Just raise your hand if you have a question. If you have a question. And then this is the last slide I'm going to display. Most of you are familiar with these different parts of the population complex. We're just going to go over it real quick, some of the name of the parameters you're using these for your input. So this is where you should also apply, like some of the validation that I talked about, validation these will promote reusability. So the idea is you can take the same template and then reuse it across multiple environments. Then you have your rules and your condition. So with conditions, conditionally create resources. Resources are what you're building, and that's the required part of the template that you need to put in and then output for what you want to export. So when you have sort of large stats, you want to have some relationships within them. For example, an application stack needs to understand which subnets it will provide your resources into outputs and exports are very useful for that. One thing that's not on here, right? It's more intrinsic functions. The intrinsic functions are also very valuable. So one of the newer things that came about are 4h loops. Any of you already using 4h loops? A couple of you, password can get really long. Let's definitely if you're creating multiple reasons. So just to take an example like you need to create SNS queues. And you need to create four SNS queues that are fairly identical in their properties, the queue name will be different. Compressed down

**Unknown Speaker (07:47):**  
to how long your Yan will be, how long you

**Unknown Speaker (07:52):**  
know, how many lines of that template?

**Speaker 1 (07:55):**  
Easier to troubleshoot, awesome. So that's all I have on the essentials I remember on the whiteboard, and just cover some best

**Unknown Speaker (08:06):**  
practices around how to work with large staff, etc, while

**Unknown Speaker (08:09):**  
I switch over. You know, I don't know if

**Speaker 1 (08:13):**  
you have any questions from the service team, so I'm sure he'll be able to

**Unknown Speaker (08:22):**  
answer. Things that aren't supported through

**Unknown Speaker (08:28):**  
proclamation where you actually have

**Speaker 2 (08:31):**  
to do that? Here's the readme to log into the console to set up. Here's your Ebs building, or the things where, okay, this is really only for the

**Speaker 3 (08:42):**  
CLI and the have, we are working hard to close that gap first of all, right, and there's been a lot of work in trying to bring our coverage up and cover things, but they're always going to be little things like that that we run into for certain reasons or another that ends up in that

**Unknown Speaker (08:59):**  
space. The ideal way you do it is the same way that

**Speaker 3 (09:04):**  
we develop a resource and like solution asking you to create a resource to manage AWS, which we should have given you the resource we didn't have to do it. But when you use our registry model to create the resource, you get a lot more management and control the features with that as well. So it's right way to do it. A lot of people just end up doing custom land their resources, right? Call the API directly if they need to and configure the thing. That can be a little trickier, because you have to sometimes control the environment, so if you mess up something that can cause your staff to be in your space and things like that. But that's why we like to have people use the registry model when they break those resources and do it that way to provide better guardrails. So yeah, and like I said, the team is seriously working to try to close all those gaps, but some of those things are a little

**Speaker 1 (09:57):**  
tricky. So what I want to talk about are the large gaps, right? So often we end up with often we ended up in a situation where monolithic

**Unknown Speaker (10:10):**  
gas 1000s of resources

**Unknown Speaker (10:12):**  
sometimes. So that's something that we

**Speaker 1 (10:16):**  
encourage the resource to do. If you have existing large stacks, encourage you to look at console. Now we have a enhanced experience for scratch recently, so we encourage you to kind of break it up for a few different reasons, or if you're building an application from scratch. So let me go over some strategies on how you can think about how you should decouple or demarcation. I'm just gonna draw a few boxes

**Unknown Speaker (10:55):**  
just to represent some stack.

**Unknown Speaker (10:58):**  
So whenever you deploy on

**Speaker 1 (11:00):**  
Amazon, you're gonna have some foundation around the first subnets and things like that. You might call things that in a

**Unknown Speaker (11:08):**  
single template instead, and

**Unknown Speaker (11:12):**  
I'll call that foundation so

**Speaker 1 (11:20):**  
I have my I am in DGC stack here, because I'm going up the stack right. I might have an application stack here. I might have

**Unknown Speaker (11:31):**  
some EC, two instances, etc.

**Speaker 1 (11:40):**  
From just for back then you might separate that out

**Unknown Speaker (11:58):**  
of your own stack, okay? And I might also have a battery and

**Speaker 1 (12:01):**  
stack, right? So that might be your that might be your safety more of a web application. You might end up, if it's more of a serverless model, and you might have, like a platform distribution back by where you're posting a web application. You might also have some API gateway back, API

**Speaker 1 (12:42):**  
endpoint, right? So what? Currently and part of this type of approach, is just the rate of change, but generally, your foundational elements aren't going to change as much, right? Once you have provisioned your VPC, there's some net unless there's a reason to expand or add another Secondary IP state, IP state that's going to stay more or less the same, and then your other place revenue more dynamic. But over time, you probably need to add more API gateway endpoint. When you add an endpoint, you may need to add sort of backing micro services like lambda functions, like Eks, ETF, powering service, API endpoint, so endpoint, so that just goes into a separate step. So think about whatever your Bitcoin application. Just think about the entire scan and the rate of change. Things have changed more often. Locate them into its own stack, and that gives us a couple of benefits, that there's a blast radius of a protection. So if something goes wrong, you're not resources are in the stack. Whenever your Bitcoin changes, it's a little bit faster, but there are fewer resources in the stack you're going to reason about. And then when you do a chase that, it's also kind of easier just to say, Hey, what is changing? And just within this stack or so, they got a stack with hundreds of hundreds of hundreds and hundreds of resources, right? Generally, getting over three 400 resources, it's a lot just to review whether this is a change to make, it can be a lot as well. So that perspective changes demarcation that way. Another is ownership. You might have a sort of back end team, like a database team, that's taking care of the more database stack. They will also understand the best practices on how to provision a manual DB or RDL database, and they can encapsulate that in their template, right so they can manage that stack. They can manage ownership as well. Similarly, you might have a network of security team that you're managing on the foundation of Parliament so

**Unknown Speaker (14:54):**  
that VPC, etc can be reused across the more

**Unknown Speaker (14:59):**  
shared infrastructure. The rate of

**Unknown Speaker (15:02):**  
change, change,

**Speaker 1 (15:02):**  
one key ownership, we encourage you to use that set that will work really well with organizations, right? So that's another thing you can do as you think about

**Unknown Speaker (15:22):**  
how you how do you scale your IAC across

**Speaker 1 (15:32):**  
your organization? So I'll kind of end this here. Any questions from staff

**Unknown Speaker (15:41):**  
organization? How many of you are using sets already, great through control tower or on your own? Yeah, okay, and then

**Speaker 3 (15:54):**  
organization based, I'm guessing, for everybody, hopefully or they're doing a self managed does anybody know

**Unknown Speaker (16:02):**  
that's very good? Organizations self managing staff.

**Unknown Speaker (16:06):**  
Everything is synchronized, basically is consistent.

**Unknown Speaker (16:20):**  
Everything is synchronized, basically. But here, if some team is running one of these

**Speaker 3 (16:35):**  
gaps, you know, they introduce an issue, yeah, yeah, I would agree with that. I understand you're saying that, so yeah, hopefully you're testing and validating those changes throughout the you know, the pipeline of deployment, but yeah, obviously that

**Speaker 3 (16:59):**  
can be an issue in that world. So, yeah, so there are the question there was related to so when you have these stacks, right, there's this thing where you just start sharing stuff between the stacks, right? And there's a couple of ways you can do that, import, export is one way, and you create an export of your stack or value from the one set, so maybe a VPC ID, right, that the mighty two instances would depend on, and you import it in on this other stack. When we do that, when you create that, you can't change the underlying value or that resource, and that's because you have things that depend on it that can be beneficial in some cases, because you're hoping the VPC Id never changes. But then there's certain other things that sometimes it does change and you have to break that relationship, make the update and then reestablish the relationship. What we've seen more people kind of sliding into is using, like the SSM parameter store and like doing dynamic references or SSM parameters inside their templates. So they just are reading from the parameter store, because then they can change the values and then, you know, read it. There's a little bit of quirkiness in that. And how, when they decide to read, you know what, you know the exact you know format is, and stuff like that. So there's some little bit of wapiness there. But like, it helps break that relationship restriction if you do need to change those values and independent templates. So couple of ways to handle that depends on what works for your use case. Yeah, kind of follow up to that. When you have multi division stacks, you have a resource that's only

**Speaker 2 (18:36):**  
in one region, like us each one, because that's where you can create the resources. And then you're in Ireland, any higher

**Speaker 3 (18:44):**  
than any good solution for cross region references, not yet. I'll leave it at that, because I can't say more, but yeah, tonight, definitely something. We've heard a lot of feedback on something we want to help make better. I it

**Speaker 1 (19:06):**  
because we have lots of applications which are forming across

**Speaker 1 (19:15):**  
multiple even mental.

**Speaker 3 (19:40):**  
To transform. So you're saying, I make sure I get the question, but you're saying, like, reading values from DynamoDB, yeah, yeah, okay, yeah. That is a good that's a good request. I guess I haven't had that one yet. There are a few ways you can work around it. I'm sure you maybe already figured out custom resources, right? There is a, I think, a third party registry resource, which is a, it's almost like a CLI runner, because make SB code APK calls and then returns the values back to you so you can get at the values. It's something that you felt that you can use, but, like, there are a few ways in

**Unknown Speaker (20:17):**  
which you can kind of work around that a little bit. But,

**Unknown Speaker (20:22):**  
yeah, good request. I guess I haven't

**Unknown Speaker (20:28):**  
had another one yet. Hi, I've got way I'm currently using is I use a lot of message stacks, and

**Speaker 4 (20:36):**  
I was just wondering what would be like a strategy for maybe pivoting away from that type

**Unknown Speaker (20:43):**  
a pattern, yeah.

**Unknown Speaker (20:47):**  
How are you? How do you feel about your message back

**Speaker 4 (20:49):**  
experience so far, it's great, up until something doesn't work in the

**Speaker 3 (20:58):**  
entire thing has to pull back something up perfectly. Yeah, so, like, that's one of the things. Like, when we talk about this, I think about it as layering, right, like a layer cake, right? It's laying one level and the next level and the next level. The other approach that people have done is message stacks, right, like this, then and then it goes and deploys the levels. It's great for sharing information between stacks, right? It coordinates the stack deployments. It organizes them, it does the right ones, the right order, all. That's great. And then sometimes there's an issue, and then you have all these, you know, your parents stacks messed up because one nested stack is messed up. And then you have to, like, figure out how to decouple it and fix it moving away. So the best probably would be looking at stack refactoring and those capabilities we have there. And I will, I don't demo it, but I'll definitely click through it, and there's a few experiences with it that we've done. So it was released last year. I wrote the blog post on it, so you can make fun of me later if you go and read it. The idea on it is just, it's a bunch of CLI commands. So we can provide stack one step two, and you can manage moving the resources between those steps. It's a little bit better than the current call. Like way of doing this. So it used to be, you have to set a deletion policy and retain and then you remove, you know, you update the template, then you delete the resource. And then when you do that, the resource stays existing, and then you can go and import it into a new stack, right? This is a multitude of steps. It's hard to orchestrate and organize the stack. Refactoring is supposed to just kind of make that process a little easier. The CLI experience, even making it easier was still kind of like two or three steps of things, because there's always things we have to do to make it work, right? And then if you look and if you've been the console in the last like three days, they just open up a new console experience to walk you through statute factory. It's much better, much cleaner, it's much easier. I would definitely suggest it in the console experience, and it's the same API that you do from the CLI. I just find that experience better for those that are in the CDK world stack refactoring. So I think sometimes we do that CDK world, right, like sometimes we have a stack and you recreate a logical ID, because you move it into a different file, right? Like this helps in that world too, as well, because now you can kind of move those resources around. A little easier, yeah, my second question here, and then how would I Oh, okay, that is a little trickier. There is a way, right? There is an import operation you can do in the CDK. One of the cool benefits of CDK is our constructs, right? Our idea that you can use a construct for those who don't know, are sorry, who doesn't know about constructs and CDK, maybe before I explain the basics of it all. Okay, so constructs are, for lack of a better term, we'll just call them abstractions, right? So when I do my template, my demo, I'm going to create a VPC, and I'm going to create a couple subnets. And you know, if you do this the right way, you have nag gateways, you have run tables, you have a bunch of resources, right? Well, we create a construct that is deploy a VPC, and then tell me how many subnets you want to have, or how many ads you want to have. And then it will go through and just create all the things for you, like on private subnets, I'm on public subnets. And then it does all the work that expands into like, whatever 2025 resources. But for me, it was like four lines of code, right? Those constructs are really handy. So doing this conversion of CloudFormation into CDK, into those constructs is difficult because they are abstractions. So there is a version of an l1 idea, which is basically equivalent to a cloud formation resource. So you can convert into, you know, CDK. Start using CDK, then maybe getting to some of those benefits at the l2 level is a little trickier. We continue to work to try to make that experience better and better. But it's a tricky thing, going from like arbitrary resources into a managed construct that has a bunch

**Speaker 1 (25:10):**  
of resources. So yeah, thank you. All right. Cool. Ready? Yeah,

**Speaker 3 (25:21):**  
yeah. All right, I'm going to do a little demo, talk about some of the things we released recently, this year and last year, and kind of hope to you know, show you some of the benefits of using these things and where they can come in handy for you. So the first thing, I don't know, if I got a show handed this earlier, how much people are just doing straight cloud formation development like Yan will JSON, okay, a good number of YouTube All right, cool. So I'm just going to talk about some of the stuff we did to try to make that development experience a lot better, a lot easier for you. One of our goals in this area was just to try to reduce context flipping, like, for me, being a customer, right? It's like, you have the docs page open I'm like, flip flopping between the two experiences of my IDE, my website. I get the template done, and then I log into my console, and I have to go through all this stuff, you know, to deploy it, see if it works right, all those types of things. And we're trying to work to make that experience a lot easier and just quicker for you all. So first thing I'm going to do is we're just, I just installed AWS toolkit, right? It's a car standard toolkit. Actually, I should ask at this point too, because it's good information for me, how many people are using VS code?

**Unknown Speaker (26:31):**  
Number of you IntelliJ or other editors?

**Speaker 3 (26:36):**  
Okay, all right, cool. So right now this isn't just working VS code. We're working to try to bring it into intelligent but this is intelligence, but this is a VS code experience, and hopefully what we'll get into the other editors as well. So what I'm going to do is just kind of start with just a bare template, and I just kind of want to go through this authoring experience and kind of show you what we've done here. And a lot of these are just typical experiences you get from IDE. So like, I'll try to go somewhat quick in them, but I just want to show you some of the benefits we've had in this world. So I'm just kind of starting from creating resources, right? We have some snippets. We have some things in here to help make this experience a little better. And then what I'm going to do is I just want to create a VPC resource. And one of the things, like, first and VPC is easy. I remember this one. But, you know, sometimes you don't always remember the service name or the full name of the thing, right? If you're doing API gateway stuff, some of those other things, right? So we did some stuff with funding searching in this so I can just type in VPC. I get all the resources that have VPC in it. I'm going to pick easy to VPC, and then I'm going to do some properties. What I want to call out here, right now, right, is it gave me nothing. That's because the property, or the BBC has no required properties. So we do have a hover down here with the like documentation. So in the weirdness of the back end, right, for the most part, we're trying to get people to put their metadata or their documentation of the schema so it will map and match the docs pages. This is what we're showing in this regard. So this is what's generated. Here we went with a TypeScript kind of layout. So you know, if the question mark means all these things are optional, and then you have all the dots here. Additionally, you can hop into the source documentation from hovering over the resource, right? So there's some things here to help, kind of just make this a little easier. And I don't want to context with the documentation. I'm going to fill in the cider block, and then what I want to do is do ace. Just want to show the experience here related to that I'm so this time, right? We have acquired properties, so we're just gonna get the DPC ID. So up until this point, this is pretty common, right? There's some things you could have done with JSON Yan completion that are pretty close, but one of the things we worked at to add on top of this is support for intrinsic functions. So, you know, especially as you start working in a large template, right, like you start doing GitHub or rep, you have to remember, what are all my parameters, what are all my, you know, resources that are out there, right, that type of thing. So, like in this case, we just want to do a get at the VPC, and then we actually have the read only properties here. So again, when these things that I open, the context flip through is back the documentation, look at the return values, find the one I wanted, and then put it in right and we just kind of bring all this information to you inside that IDE experience. So I'm going to go ahead and do that in here. All

**Speaker 3 (29:42):**  
right, so you notice, in this case, when we hover too like you'll see the required properties towards the top of the list, so VPC ID is required, doesn't have the question mark,

**Unknown Speaker (29:53):**  
those types of things. So we're going to do something here,

**Unknown Speaker (29:57):**  
and I want to do a few other little things here. Just

**Speaker 5 (30:02):**  
kind of draws. Examples. I

**Speaker 3 (30:10):**  
just want to show you some of the things we're doing here. All right, so and so now we get into the static validation I kind of been thinking about errors in our world is like three types of errors that exist, right? I have, like, static validation errors. Things are just easily checkable locally, right? Runtime errors. So things about the actual deployment that I'm going to do, we're going to go through some of those in a little bit, and then maybe just, hey, my template works, but my app doesn't work. Maybe my security group rules aren't right, allows this to talk to that right? Technically, from a cloud formation side, everything's deployable. It's just not configured correctly. So like right now, we're looking at what I would call these static validation rules, and we integrated in with CFM lint for validation and confirmation guard. So when I do this, hover over on this now you'll notice that I get this error that just says my subnets overlap, right? So this is CFM link going you can deploying two subnets into the same VPC, and you're using the same cider ranges. When you actually go to deploy this, it's going to fail because these, you know, the cider range is already allocated. And so, you know, having that feedback here, right? Quick Fix and let it go on my bucket. This is a bunch of guard rules, right? I didn't create a bucket with the encryption or any other typical standard things we see nowadays. In this regard, bucket, I use this as a very extreme example, because buckets have a lot of things to make them appear. So this has got a lot of different things under there. The other thing, so the other thing we kind of integrated in to make this experience better. Maybe I said, Okay, I said, Okay, I don't want I don't want to remember all those properties, all those attributes, but I do know I have a bucket under my account that has what I need. It's already configured the right way. So you'll notice also, in this AWS side, we have a CloudFormation panel, and in here we have integrations into Cloud Control API. How many people know about the Cloud Control API? Okay, all right, we're going to explain a big, quick so Cloud Control API. So the best way to think about this is when CloudFormation or when service teams create resources for CloudFormation, the credit are based on the operation. So create, read, update, delete, that yields itself to a RESTful API very well, right? We can actually just create an API from the same calls you would use from the confirmation engine. That's what we did. It's called the CC API. So you can actually go and look at resources based on their resource name, like s3 bucket. And you can go list, and it will list all the s3 buckets in your account. You know, account regions buckets, a little weird because it's global, but you get the idea, right? It's going to list them all for your account in that area. So it's a great way to inventory your accounts. There's some other things we'll show later that we've done with IAC generator, we have time that uses as well for those that are using things like TerraForm. TerraForm also has a cc API provider, which is different than the other one, and it's an auto generated from the schema to define CC API so it allows them to get pretty quick coverage when we have our day one releases and we have that resource support. So this is what I did, looking at the CC API. I have this three bucket, and I can see this one here. This is a bucket I just wanted to copy. We have a couple of ways we can do that in here. We can just clone it, or we can import it. I'm going to import it because I want to do something with a demo. And there went through and imported it, right? So all these properties that I have to remember how to set, they just gave it to me because I knew I had something there that I could just take and getting copy of that process a little bit. You want to show

**Speaker 6 (33:58):**  
another little thing here. So let me create A quick somebody prayed us.

**Speaker 3 (34:40):**  
All right, I just want to use this or show some value here of some of the things we've done, so just kind

**Unknown Speaker (34:53):**  
of demo the little value. All

**Speaker 6 (35:02):**  
right, that and all

**Speaker 3 (35:21):**  
right, that and then, all right, so, now I got a template, you know, created, right? All my lines are, problems are gone, and now we're kind of getting this deployment set like, what can I do to actually do a deployment of this template and not have to flip around? We do have some options in here, right? I can just click on the top here and do the validated deploy. I'm just going to walk through this experience, show what it looks like, it's asking you a lot of the questions you'll get from the console. I'm actually going to type something that's going to fail here.

**Speaker 7 (35:53):**  
So I know it is to be what it is, and I want to show you the piece of validation we're doing as well. I bit.

**Speaker 3 (36:06):**  
So now we're going to go out and we're actually creating a change set, and if you were getting around this time of the year watching, we also enabled early validation on change sets. So we go out and create a change that and we do some runtime validation. Back to that second set of errors. I was talking about things that can go wrong when you're actually going to deploy that template. And there's three types of checks that we have are out there right now. One is this resource of this Id already exists. So my case, you'll actually see this name conflict validation error right here. And this is basically saying you already have a three bucket with this name. You can't like, this is going to conflict. This is going to fail, right? So this is just, you know, again, kind of invalidates that change set. So I know now I have to go back and correct my bucket name before I do deployment, that type of thing. The second one is because it's on the operation. If you're deleting the bucket and the bucket is not empty, we will show that as a warning, so you can also see that one. So anybody that's gone through that process of like, you know, you change that, maybe delete the bucket, and it's going through a bunch of operations, and then they hit fit, and they can't do the Delete, and it rolls back. Like this will help just kind of like that for you. So you know that that's going to be a problem, and you can correct it before you go through and execute it. And the last one is property validation. So this is similar to CFM lint, but it's happening on the server side. It has some benefits for things like Sam transforms, language extension transforms, or any other custom transforms you're doing. Also allows us to do parameter value type checks right, because it's actually something in the parameter value at that time. So even though my template was valid there, right, because I've typed the wrong value into the parameter back up to me as well. So you'll see that that's the property validation here.

**Unknown Speaker (37:56):**  
All right, so we

**Unknown Speaker (37:58):**  
have a question at the back. Oh, yeah. Them.

**Speaker 3 (38:06):**  
So the validation stuff that we just showed, so this will work on any change that you create right now by default. So it'll happen inside your pipeline as well. Happens inside this experience. But yeah, all we did was create a change set. And this just happened. Yeah, the team worked hard not to hopefully break anything you know that make a bad change set, right from this so it's all validation based. It's all things that shouldn't fail when you actually get executed. So, like, that's what we're trying to bubble up to you at this point. Yeah, what's that?

**Unknown Speaker (38:42):**  
Ah, numbers should be in production,

**Unknown Speaker (38:48):**  
the 19th, 18th, technically. So

**Unknown Speaker (38:51):**  
really do, Yep, alright,

**Unknown Speaker (38:54):**  
yeah, sorry, go ahead.

**Speaker 4 (38:56):**  
So I thought it was really cool how you were able to use the ES three bucket and just bring the whole, here's all the properties of it into the stack that make a different one. Yup. But as you showed it, kind of included properties that, if you just tried to run it straight away you got the name conflict. So is there an upcoming feature where it will bring in, you know, the whole resource

**Unknown Speaker (39:21):**  
block with all of the primary

**Speaker 4 (39:24):**  
maybe, like, leave a comment on the ones that are known to cause a conflict of, like, this whole conflict, if you don't change.

**Speaker 3 (39:31):**  
So when we were here, this is why we had different buttons here. So this one is clone, the second one, and the clone is supposed to strip out the supposed to strip out the primary identifiers. So the idea there was just remove them so that they're, you know, you have to put them in I guess basically there's a weird balance. I think sometimes we leave a note in there that, like, Hey, this is not, you know, like you have to change this. But like on this one, we can just remove the bucket name, for instance, and then you can manually put it in there. The other thing to note too is there's another button here that says, Get stack management info. So, like, you can actually, if this was resource managed by another stack, you can't have it in two stacks. So you can actually click this button, and I'll tell you,

**Unknown Speaker (40:12):**  
managed by another stack as well. Yeah, if they're ready, if

**Unknown Speaker (40:20):**  
they're in the register, yes, you

**Speaker 3 (40:22):**  
can, all we do is a list type and we pull in all your private registry resource types so they all come in with all the documentation

**Speaker 3 (40:36):**  
to Your this resource, this thing that, this thing right here is a Cloud Control API, okay, yeah, it's been out for a few years, but, yeah, those are, like, not a lot of people know about. That's always why I ask the question, yeah, exactly like the CFN, if you're doing things with CDK, is

**Unknown Speaker (40:58):**  
it account for those best practices? Already?

**Speaker 3 (41:02):**  
Account for those best practices already? It should. There's, it's independent. I know I have a lot of people that still use it after they do CDK to generate the template like CDK should generally gear you towards the right choices, but there's always ways to break out right. You have escape hatches. There's sometimes just really weird things. Sometimes the things between resources can get a little tricky, right? Like, and so depending on how you did the l1 or l2 comes drop, it may or may not have guided you down the right path. So some of it's there, some of it's not there, yeah, can I use my custom guard rules for the integration of the guard thing. Yes, you can specify guard rule file and it will use that guard rule file, I should say, like what we did by default was there's a guard rule registry. How many people are familiar with guard? The guard is just a DSL language to validate any Yan or J com payload. It's used a lot just for CloudFormation templates, but it can validate any JSON Yan template. And so we also have out there the guardable registry that has a bunch of rules tied into management paths. And what will be just enabled by default and you can turn it off, of course, is just the AWS best practice security pillar, but you can also just remove that and add in your own light path to your own guard file. So, yeah, that'll work as well

**Unknown Speaker (42:31):**  
for what part. Sorry,

**Speaker 3 (42:36):**  
yeah, so we did import the SAM team created schemas for those types of resources. So, yes, you can still do the typing and get the SAM auto complete and stuff. Documentation still a little wonky just because of how they design the schemas, but it will help with the auto complete and what they have we do make available resources.

**Unknown Speaker (43:01):**  
Information section, right there only because you declared

**Speaker 3 (43:13):**  
it, nope, it will take anything. So you can actually go and pick different all the different resource types you have, right? So I could take an IO role. It doesn't matter if it's managed or not managed. We'll just get all the things right. So yeah, 43

**Speaker 3 (43:41):**  
roles here, correct? Um, because the list is just listed like, when you call that handler, it just calls like list buckets, and so it doesn't matter if it was CloudFormation controlled or not. Is this going to put it all into the list? And the response this tool, the CC API, has been great, even for our software creators like think of some of those security can't scanning software companies because they can easily, just now add resource support, despite supporting the list and get on these resources.

**Unknown Speaker (44:11):**  
There's a really cool things you can do with this. Yeah. Back. Kayla, I have a

**Speaker 3 (44:26):**  
demo of that I might run out of time for. So hero, if you haven't noticed, also, I'm probably not gonna have time for it. So I'll just say what it is, right?

**Unknown Speaker (44:35):**  
So for those, how many are using Gen AI in their daily use?

**Speaker 3 (44:42):**  
So for those that are right, my demos are here because, you know, AWS, right, it will work no matter you know how the ID setup probably is. But my demo is basically telling it to create a template I know it's going to make a bad template that's going to not be correct, really a zero issue. I know enough now to trick it into making something that won't work. And you can actually tell them go, like, hey, there's some diagnostic information here. Like, can you go and fix it? And they can read the diagnostics. It can go resolve that. So, like, in the case of, like, the bucket one, for instance, it does the same thing. It creates a pretty generic bucket, and then it goes, Oh yeah, but there's a bunch of issues here. Like, I'll go make a compliant bucket. So it is kind of nice to have that kind of interaction and that capabilities integrated in for me, you know, initially, like, hover right? Like, hey, you can generate a template. You're probably still reviewing that code, right? So me, it'll look at it, hover over things, see things. It helps a lot, I think, in that regard. So, yeah, I do want to get to a few more things, so I'm going to jump right back into this really quick. We're going to redo

**Speaker 5 (45:49):**  
this deployment, but I'm not going to make it fail this time. So get rid of this bucket name. We'll just have a creative, dynamic name. And

**Speaker 3 (46:01):**  
this is the failure from validation. So we're just going to do validate,

**Speaker 8 (46:19):**  
deploy again. Does anybody use rollback of necessity. Out of necessity, alright,

**Speaker 3 (46:29):**  
for those that don't know, do nothing on the rollback. Kind of a newer thing that existed, I think, in the last few years, maybe two years, two years and a half. And what it does is typically, and I find it more beneficial in my development cycle. That's why it's considered more of a dev type of flight. Is if you're doing a great stack, versus like I'm developing a template, I have 30 resources in there, you hit the deploy and on the 30th time, right? Something fails the previous resource, it rolls it all back to nothing, right? Do nothing. Just stops it at the last time did state. So you can make an update, you can do an update stack from there. It just helps, if you're doing that development cycle, to kind of stop that rollback from happening. So you can make those improvements and fix it. So we have some stuff here. I'll show this a little bit later. So that time, we passed our early validation because we didn't have any conflicts or issues. And we're going to go through the deployment. One of the things I want to note here right is we try to bring all that information from the stack into the IDE so I'm getting a scroll of the events that are happening. But I also want to show something else here that's kind of cool. If you go into your actual console, you will notice a few things that changed in this view, one of the things is we now have an operation ID. Operation IDs are not necessarily like in this case, right? I'm doing an execute, change set. It doesn't always just include that, but in this case, it will think of it if we do hit a rollback scenario, those are actually two separate operations. So you can actually break down what happened during the rollback phase, separate from the actual implementation phase. And so now those are broken up by Operation IDs. Additionally, we have this timeline view for those that don't know right way to visualize a template resources. It takes a long time. You can break it down by resources. See how long each one's taking. You kind of get an idea of the dependencies right. Next up, that's dependent on my VPC. That's where they started. Later, those types of things, all right. The next thing I want to do is show you a little bit we're doing with drift remediation as well. So what we're actually going to do is we're going to make some drift so I'm going to pretend that I am fixing a bug, right? I'm going to go in and set that time out, I'm going to change it to two minutes, and I got to whatever set one issue, and I'm just doing things to fix it at this point. If

**Unknown Speaker (48:57):**  
you want to go that way, all

**Speaker 3 (49:20):**  
hand idea, alright, so I'm going to change so we'll come back. I'm going to change this visibility of time off 90, right? My template is local. Somebody's changed some stuff in my account. It's now thrifted technically, but I made an update. It was like, Oh yeah, right. We were supposed to update our visibility timeout, and we want to be 90 now, right? And we go through and do this execution and deployment. So I'm actually going to go through again and do this as Well. Yan, oh, man.

**Unknown Speaker (50:22):**  
We more time,

**Unknown Speaker (50:27):**  
if I don't get it to

**Speaker 6 (50:42):**  
work, You while

**Unknown Speaker (50:56):**  
having doing

**Speaker 1 (51:02):**  
that, I put in a summary of some of the things that you can't try out after today talk about statin factoring, software experience, the ID experience, download the plugin for VS code, API operations, really valuable.

**Speaker 1 (51:20):**  
IAC generator. We won't have time to get to the demo today, but really good way to inventory your account. And if you have some of you have manual or creative resources. So to bring those under the management of CloudFormation, stack or CDK, trial the ISP generator, and then rollback, do nothing, which we just talked about, and

**Speaker 3 (51:49):**  
my credentials expired because I have a second sign on thing or whatever. So anyway, so there's an option now when I can do a free chase that called revert grip. Oh yeah, it's great. Up. Okay, so you'll see this revert driven standard. So now there is an option, when we create a change set where it will actually go and analyze the drift. What's cool about this is, when we go to execute this, it will actually reverse the drift. So for those TerraForm users, you're probably used to this from your TerraForm plan and apply, you know, world, right? But now it's in cloud formation, so it's a great way for us to set things back in to the temper, back to what we expected them to be from our template. And so what I'm going to do is actually go through and hit this, and I want to show this real quick.

**Speaker 3 (52:35):**  
Takes a little longer because we have to go run the drift analysis against all the resources, so it's a few extra seconds. But I use this view, right? So what's kind of cool from here is now those things that I just changed in the console, right? I changed my queue timeout, what I want to call it here, right? We have that before value and that after value, right? And the good value, and what that said at So before, it's 120 that's what I changed it to. Two Minutes after, because I have it in my template, it'll be 90, and you'll know that it was you. It was meant to be 60, right? That's what it was defined in the template before. Additionally, even though I didn't update Yes, three bucket, I can also get this drift detection here. So we're actually going to revert that drift and reset those properties as well in this case. So this is a great way for us to kind

**Unknown Speaker (53:28):**  
of go through and do that,

**Speaker 3 (53:35):**  
yeah, setting it to what the template had somebody fixed something wrong? Yes, correct. And that's why we show it. And so you get all the options that I haven't hit the full yet, so I could obviously correct it or fix it. We do do this in a dip view as well, so you kind of see this

**Unknown Speaker (53:50):**  
as well. In this regard, what

**Speaker 2 (53:51):**  
was the smartest way to fix the right value?

**Speaker 3 (53:55):**  
But then I would go change my template to 120 if that was meant to be the right one, and then recreate the change that, yep, and then deploy here in this

**Unknown Speaker (54:06):**  
Oh, yeah, okay, sorry.

**Speaker 4 (54:09):**  
So let's say we do, we do our cooperation development in our dev account, but someone has made a change in the production account, a controlled change in the production account, but it's not communicated back to the template. Is there a way to do a dip, cross account, cross

**Unknown Speaker (54:27):**  
account? No. So with the

**Unknown Speaker (54:32):**  
there isn't that mechanism yet. I guess I should say

**Speaker 3 (54:36):**  
so you would have, I could, of course, log into all my accounts and do that div for that check myself, but you have to do that check kind of manually, or build a system to kind of do that for yourself.

**Unknown Speaker (54:49):**  
Sorry, across the board, annoying,

**Speaker 3 (54:55):**  
yes, the drift aware change. That's also the console. So you can get that same experience there. We try to match that visualization as close as the face we could with the annual constraints and stuff. So that also happens there. You can create it. There you can visualize. There. You can see it along with all those pre deployment books as well, holding your release pipeline the moment you release your first check. So your release pipeline is still wrong in drift, aware change that, and then it says how you're reviewing it, right? Are you just, are you getting a comment back on something and then hit and approve? Or however the pipeline builds up to handle that? So you ideally, that's what we like people to use change. That's right, they can see the changes that are going to happen in that world. Oh, man, I got three seconds. So the other thing too, just to be quick, on hooks, for those that don't know all the validation. We can also run server side. We can do it on a change set. So think of things like making sure my ASGs haven't changed. Instance sizes from like for instance numbers from like 1000 to 10, right? Like that might represent the bad change. Or my DynamoDB instance is going to get recreated, right? Bad changes in that world. There is a way to do these in critical guard rules. Implement those guard rules with lambda hooks, and then additionally, control tower has released the control catalog, which has a bunch of managed rules for you. Great way to implement a bunch of things that happen on the server side. So you can do that trust will verify, right? We provide that information the IDE, but you also get it on the side. So I know I'm at time. They're going to pick me up quick. We'll be on the hallway if anybody has any questions

**Unknown Speaker (56:29):**  
or anything else. I Appreciate it. Thank you.

**Unknown Speaker (57:00):**  
I everybody Got everything. Yan, one.

