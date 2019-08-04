<head>
  <title>Šah Math</title>
  <meta content="charset=utf8" />
  <style>
    p {font-size: 8vmin; margin: 0px;}
    p.brez {color: 000000;}
    p.beli {color: E0E0E0;}
    p.crni {color: 202020;}
    table {border-collapse: collapse; table-layout: fixed; position: relative; top: 6vmin;}
    th, td {height: 11vmin; width: 11vmin; text-align: center; padding: 0px;}
    td.polje_svetlo {background-color: C09048;}
    td.polje_temno {background-color: 806030;}
    button {height: 100%; width: 100%; text-align: center; border: none; padding: 0px;}
    button.polje_svetlo {background-color: C09048;}
    button.polje_temno {background-color: 806030;}
    button.polje_svetlo:hover {background-color: C09000;}
    button.polje_temno:hover {background-color: 906A00;}
  </style>
  </head>
<body>
  <table align="center">
  %for i in range(8):
    <tr>
    %for j in range(8):
    %if (i + j) % 2 == 0:
    %polje = "svetlo"
    %elif (i + j) % 2 == 1:
    %polje = "temno"
    %end
    %if (i, j) in veljavni:
      <form action="/igra/premik/", method="get">
      <input type="hidden", name="i", value="{{i}}">
      <input type="hidden", name="j", value="{{j}}">
        <td>
          <button type="submit", class="polje_{{polje}}">
          <p class="{{sah.barva_igra(i, j)}}">{{sah.figura_igra(i, j)}}</p>
          </button>
        </td>
      </form>
    %else:
      <td class="polje_{{polje}}">
        <p class="{{sah.barva_igra(i, j)}}">{{sah.figura_igra(i, j)}}</p>
      </td>
    %end
    %end
    </tr>
  %end
  </table>
</body>