# REQUESTS

## Example
GET to 'http://google.com'

```
GET / HTTP/1.1
Host: www.google.com
```
Explanation:
* `GET` - verb
* `/` - path
* `HTTP/1.1` - protocol


## GENERAL
Going to a page will always do a GET.
Other things: POST, DELETE, PUT, OPTIONS, HEAD, and more.
Same response to each type
<table>
  <thead>
    <tr>
      <th>Verb</th>
      <th>Meaning</th>
      <th>Example</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>GET</th>
      <th>Retrieve smth</th>
      <th>GET /item/1</th>
    </tr>
    <tr>
      <th>POST</th>
      <th>Receive data, and use input</th>
      <!-- Also should send some data: {'name': 'chair', 'price': 152.0} -->
      <th>POST /item</th>
    </tr>
    <tr>
      <th>PUT</th>
      <th>Make sure something is there</th>
      <!-- May update, or may create {'name': 'chair', 'price': 199.95} -->
      <th>PUT /item</th>
    </tr>
    <tr>
      <th>DELETE</th>
      <th>Remove something</th>
      <th>DELETE /item/1</th>
    </tr>
  </tbody>
</table>



## RESULTS
May give:
* an error, if page not found
* an error, if HTTP not supported
* an error, if the server is unavailable
* some HTML code (normal)
* some text
* nothing at all

## EX 2+
https://twitter.com/login
```
GET /login HTTP/1.1
Host: https://twitter.com
```
https://git-scm.com/download/mac
```
GET /download/mac HTTP/1.1
Host: https//git-scm.com
```
Difference: the response - page
