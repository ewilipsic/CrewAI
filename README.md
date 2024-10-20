#### This a crew Ai implementation

### It's a 991 Dispatcher that takes a distress message(String)

Notifies the appropriate services like(police,EMS,firefighters),currently it drafts emails to them "obviously doesn't send them anywhere right now"<br />
and gives instructions to the caller to follow till help arrives<br />
it only takes the distress call as input and outputs everything in terminal<br />

distress call can be something like - "There is a crocodile loose in the walmart on 5th avenue,it has attacked 2 people,please advice on what to do, there are a lot of people here"<br />

It consists of 4 agents :
Agent 1 -> extracts important info from the message<br />
Agent 2 -> decides which departments need to be called<br />
Agent 3 -> drafts mails to those departments containing relavant information<br />
Agent 4 -> Responds to the caller giving them instructions on what to do and tries to calm them<br />

### To run

#### 1) clone repository
#### 2) use poetry to install packages
#### 3) add .env with GOOGLE_API_KEY
