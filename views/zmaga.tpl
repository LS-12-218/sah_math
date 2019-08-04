<head>
  <title>Šah Math</title>
  <meta content="charset=utf8" />
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
  <style>
    p {font-size: 8vmin; font-family: initial; margin: 0px;}
    p.brez {color: 000000;}
    p.beli {color: E0E0E0;}
    p.crni {color: 202020;}
    p.zmaga {font-size: 5vmin; color: FFFFFF;}
    table {border-collapse: collapse; table-layout: fixed; position: relative; top: 6vmin;}
    table.zmaga {position: absolute; top: 30vmin;}
    th, td {height: 11vmin; width: 11vmin; text-align: center; padding: 0px;}
    td.polje_svetlo {background-color: C09048;}
    td.polje_temno {background-color: 806030;}
    td.zmaga {background-color: A0A0F0; opacity: 0.66; height: 40vmin; width: 100vw; font-size: 6vmin;}
    a.btn.btn-primary.nazaj {font-size: 4vmin; align-self: center; padding: 1vmin;}
  </style>
</head>
<body>
  <table align = "center">
  %for k in range(8):
    <tr>
    %for l in range(8):
    %if (k + l) % 2 == 0:
    %polje = "svetlo"
    %elif (k + l) % 2 == 1:
    %polje = "temno"
    %end
      <td class="polje_{{polje}}">
        <p class="{{sah.barva_igra(k, l)}}">{{sah.figura_igra(k, l)}}</p>
      </td>
    %end
    </tr>
  %end
  </table>
  <table class="zmaga">
    <tr>
      <td class="zmaga">
        Šah Mat<br>
        <p><b>{{igralec}} je zmagal!</b></p><br>
        <a href="/", type="button", class="btn btn-primary nazaj", type="submit">V redu</a>
      </td>
    </tr>
  </table>
</body>