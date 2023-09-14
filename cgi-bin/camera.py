#!/usr/bin/env python3

print("""

<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <title>Camera</title>
  <style type="text/css">
  html
  {
    width: 100%;
  }
  img { 
    position: absolute;
    top: 50%;
    left: 50%;
    margin-right: -50%;
    transform: translate(-50%, -50%)
  }
  </style>
</head>
<body>
  <script src="../script.js"></script>
</body>
</html>

""")