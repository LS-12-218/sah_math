<head>
    <meta content="charset=utf8" />
    <style>
        p {font-size: 50px; margin: 0px;}
        p.brez {color: 000000;}
        p.beli {color: E0E0E0;}
        p.crni {color: 202020;}
        table {border-collapse: collapse; table-layout: fixed;}
        th, td {height: 70px; width: 70px; text-align: center; padding: 0px;}
        td.polje_svetlo {background-color: C09048;}
        td.polje_temno {background-color: 806030;}
        button {height: 70px; width: 70px; text-align: center; border: none; padding: 0px;}
        button.polje {background-color: 60C040;}
        button.polje:hover {background-color: 20C018;}
        button.figura {background-color: C0C040;}
        button.figura:hover {background-color: C0C000;}
    </style>
</head>
%veljavni = sah.mozni_premiki(i, j)
<table>
%for k in range(8):
    <tr>
    %for l in range(8):
    %if (k + l) % 2 == 0:
    %polje = "svetlo"
    %elif (k + l) % 2 == 1:
    %polje = "temno"
    %end
    %if (k, l) == (i, j):
        <form action="/", method="get">
            <td>
                <button type="submit", class="figura">
                <p class="{{sah.barva_igra(k, l)}}">{{sah.figura_igra(k, l)}}</p>
                </button>
            </td>
        </form>
    %elif (k, l) in veljavni:
        <form action="/premakni/", method="post">
        <input type="hidden", name="premiki", value="{{i}}{{j}}{{k}}{{l}}">
            <td>
                <button type="submit", class="polje">
                <p class="{{sah.barva_igra(k, l)}}">{{sah.figura_igra(k, l)}}</p>
                </button>
            </td>
        </form>
    %else:
        <td class="polje_{{polje}}">
            <p class="{{sah.barva_igra(k, l)}}">{{sah.figura_igra(k, l)}}</p>
        </td>
    %end
    %end
    </tr>
%end
</table>