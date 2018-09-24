# EdmundsCommentScraper
A script that scrapes comment data from a car forum website and outputs a json file.

For reference:
  This is an index page - https://forums.edmunds.com/discussions/tagged/x/tires-wheels/p1
  This is a page in a forum - https://forums.edmunds.com/discussion/2219/chrysler/sebring/chrysler-sebring-accessories-and-modifications

The resultant json file is in the following format:
<pre>
[  
  [  
    [  
      [ comment1 on page1 of forum1 on indexpage1, comment2 on page1 of forum1 on indexpage1, ... ],  
      [ comment1 on page2 of forum1 on indexpage1, comment2 on page2 of forum1 on indexpage1, ... ],  
      [ comment1 on page3 of forum1 on indexpage1, comment2 on page3 of forum1 on indexpage1, ... ]  
    ]  
    [  
      [ comment1 on page1 of forum2 on indexpage1, comment2 on page1 of forum2 on indexpage1, ... ],  
      [ comment1 on page2 of forum2 on indexpage1, comment2 on page2 of forum2 on indexpage1, ... ],  
      [ comment1 on page3 of forum2 on indexpage1, comment2 on page3 of forum2 on indexpage1, ... ]  
    ]  
  ]  
  [  
    [  
      [ comment1 on page1 of forum1 on indexpage2, comment2 on page1 of forum1 on indexpage2, ... ],  
      [ comment1 on page2 of forum1 on indexpage2, comment2 on page2 of forum1 on indexpage2, ... ],  
      [ comment1 on page3 of forum1 on indexpage2, comment2 on page3 of forum1 on indexpage2, ... ]  
    ]  
    [  
      [ comment1 on page1 of forum2 on indexpage2, comment2 on page1 of forum2 on indexpage2, ... ],  
      [ comment1 on page2 of forum2 on indexpage2, comment2 on page2 of forum2 on indexpage2, ... ],  
      [ comment1 on page3 of forum2 on indexpage2, comment2 on page3 of forum2 on indexpage2, ... ]  
    ]  
  ]  
]  
</pre>
