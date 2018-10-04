# EdmundsCommentScraper
A script that scrapes comment data from a car forum website and outputs a json file.

For reference:  
  This is an index page - https://forums.edmunds.com/discussions/tagged/x/tires-wheels/p1  
  This is a page in a forum - https://forums.edmunds.com/discussion/2219/chrysler/sebring/chrysler-sebring-accessories-and-modifications


The resultant json file is in the following format:
<pre>
{
	"indexpage1": {
		"forum1": {
			"page1": {
				"comment1": "first comment",
				"comment2": "second comment"
			},
			"page2": {
				"comment1": "first comment",
				"comment2": "second comment"
			}
		},
		"forum2": {
			"page1": {
				"comment1": "first comment",
				"comment2": "second comment"
			},
			"page2": {
				"comment1": "first comment",
				"comment2": "second comment"
			}
		}
	},
	"indexpage2": {
		"forum1": {
			"page1": {
				"comment1": "first comment",
				"comment2": "second comment"
			},
			"page2": {
				"comment1": "first comment",
				"comment2": "second comment"
			}
		},
		"forum2": {
			"page1": {
				"comment1": "first comment",
				"comment2": "second comment"
			},
			"page2": {
				"comment1": "first comment",
				"comment2": "second comment"
			}
		}
	}
}
</pre>
