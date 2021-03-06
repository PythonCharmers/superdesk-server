Feature: News Items Archive Comments

    @auth
    Scenario: Create comment for item
        Given "archive"
        """
        [{"_id": "xyz", "guid": "testid", "headline": "test"}]
        """
        Given empty "item_comments"
        When we post to "/item_comments"
        """
        [{"text": "test comment", "item": "xyz"}]
        """
        And we get "/item_comments"
        Then we get list with 1 items
        """
        {"text": "test comment", "item": "xyz"}
        """

    @auth
    Scenario: Create comments for item
        Given "archive"
        """
        [{"_id": "xyz", "guid": "testid", "headline": "test"}]
        """
        Given empty "item_comments"
        When we post to "/item_comments"
        """
        [{"text": "test comment", "item": "xyz"}]
        """
        When we post to "/item_comments"
        """
        [{"text": "test comment 1", "item": "xyz"}]
        """
        And we get "/item_comments"
        Then we get list with 2 items


    @auth
    Scenario: Create comment for item - get from /archive/_id/comments
        Given "archive"
        """
        [{"_id": "xyz", "guid": "testid", "headline": "test"}]
        """
        Given empty "item_comments"
        When we post to "/item_comments"
        """
        [{"text": "test comment", "item": "xyz"}]
        """
        And we get "/archive/xyz/comments"
        Then we get list with 1 items
        """
        {"text": "test comment", "item": "xyz"}
        """

    @auth
    Scenario: Create comment for item(Fail) - wrong user supplied
        Given "archive"
        """
        [{"_id": "xyz", "guid": "testid", "headline": "test"}]
        """
        Given empty "item_comments"
        When we post to "users"
        """
        {"username": "foo", "email": "foo@bar.com"}
        """
        When we post to "/item_comments"
        """
        [{"text": "test comment", "item": "xyz", "user": "#USERS_ID#"}]
        """
        Then we get error 400
        """
        {"_status": "ERR", "_issues": "Commenting on behalf of someone else is prohibited.", "_message": ""}
        """

    @auth
    Scenario: Create comment for item(Fail) - get from /archive/wrong_id/comments
        Given "archive"
        """
        [{"_id": "xyz", "guid": "testid", "headline": "test"}]
        """
        Given empty "item_comments"
        When we post to "/item_comments"
        """
        [{"text": "test comment", "item": "xyz"}]
        """
        And we get "/archive/wrong_id/comments"
        Then we get error 400
        """
        {"_message": "", "_issues": "Invalid content item ID provided: wrong_id", "_status": "ERR"}
        """


    @auth
    Scenario: Create comment for item(Fail) - wrong archive item supplied
        Given empty "archive"
        Given empty "item_comments"
        When we post to "/item_comments"
        """
        [{"text": "test comment", "item": "xyz"}]
        """
        Then we get error 400
        """
        {"_message": "", "_issues": "Invalid content item ID provided: xyz", "_status": "ERR"}
        """
