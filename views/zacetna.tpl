<head>
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
</head>
<body>
    <title>Šah Math</title>
    <br><h1 class="text-primary", align="center">Šah</h1><br><br>
    <form action="/igra/nova/", method="post", align="center">
        <input type="hidden", name="ai", value="1">
        <button class="btn btn-primary btn-lg", type="submit">1 Igralec</button>
    </form><br>
    <form action="/igra/nova/", method="post", align="center">
        <input type="hidden", name="ai", value="0">
        <button class="btn btn-primary btn-lg", type="submit">2 Igralca</button>
    </form>
</body>