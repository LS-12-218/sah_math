<head>
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  <style>
    h1.text-primary.sah {font-size: 11vmin; margin: 4vmin;}
    button.btn.btn-primary.sah {font-size: 8vmin; align-self: center; margin: 2vmin; padding: 1vmin;}
    body {background-position: center center;}
  </style>
</head>
<body>
  <title>Šah Math</title>
  <table align = "center">
    <tr>
      <td>
        <h1 class="text-primary sah", align="center">Šah</h1>
      </td>
    </tr>
    <tr>
      <td>
        <form action="/igra/nova/", method="post", align="center">
          <input type="hidden", name="ai", value="1">
          <button class="btn btn-primary sah", type="submit">1 Igralec</button>
        </form>
      </td>
    </tr>
    <tr>
      <td>
        <form action="/igra/nova/", method="post", align="center">
          <input type="hidden", name="ai", value="0">
          <button class="btn btn-primary sah", type="submit">2 Igralca</button>
      </form>
      </td>
    </tr>
  </table>
</body>