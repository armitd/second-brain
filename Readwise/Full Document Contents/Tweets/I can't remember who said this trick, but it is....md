# I can't remember who said this trick, but it is...

![rw-book-cover](https://pbs.twimg.com/profile_images/1730584907674480640/0aIGiTFL.jpg)

## Metadata
- Author: [[ani]]
- Full Title: I can't remember who said this trick, but it is...
- Category: #tweets
- Summary: I can't remember who said this trick, but it is now trivially easy to make APIs and MCP servers for websites:

1. Go to the site
2. Turn on DevTools => Network tab => "Keep Log"
3. Log out and log back in
4. Visit all the pages you want data from

(cont.)
- URL: https://twitter.com/anaisbetts/status/2084258524448665704/?rw_tt_thread=True

## Full Document
I can't remember who said this trick, but it is now trivially easy to make APIs and MCP servers for websites:

1. Go to the site
2. Turn on DevTools => Network tab => "Keep Log"
3. Log out and log back in
4. Visit all the pages you want data from

(cont.) 

---

5. In DevTools, right-click a request => "Copy all as HAR", save the clipboard output as a file
6. "Copy all as fetch" => same
7. Dump it in an empty Bun project, Plan Mode "Read these archives and make a TypeScript API and MCP server"
