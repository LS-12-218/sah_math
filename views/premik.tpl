<head>
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
        button {height: 100%; width: 100%; text-align: center; border: none; padding: 0px; margin: 0px;}
        button.polje_svetlo {background-color: 60C040;}
        button.polje_temno {background-color: 48A838;}
        button.polje_svetlo:hover {background-color: 40C030;}
        button.polje_temno:hover {background-color: 20A814;}
        button.figura_svetlo {background-color: C0C040;}
        button.figura_temno {background-color: A0A030;}
        button.figura_svetlo:hover {background-color: C0C000;}
        button.figura_temno:hover {background-color: A0A000;}
    </style>
</head>
<body>
    <title>Šah Math</title>
    <table align="center">
    %for k in range(8):
        <tr>
        %for l in range(8):
        %if (k + l) % 2 == 0:
        %polje = "svetlo"
        %elif (k + l) % 2 == 1:
        %polje = "temno"
        %end
        %if (k, l) == (i, j):
            <form action="/igra/", method="get">
                <td>
                    <button type="submit", class="figura_{{polje}}">
                    <p class="{{sah.barva_igra(k, l)}}">{{sah.figura_igra(k, l)}}</p>
                    </button>
                </td>
            </form>
        %elif (k, l) in veljavni:
            <form action="/igra/premakni/", method="post">
            <input type="hidden", name="premiki", value="{{i}}{{j}}{{k}}{{l}}">
                <td>
                    <button type="submit", class="polje_{{polje}}">
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
</body>