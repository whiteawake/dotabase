#!/usr/bin/python
print('Content-Type: text/html')

import sqlite3, sys, cgi, csv
import cgitb; cgitb.enable()
from db_functions import *

print("""
<!DOCTYPE html>
<html ng-app="heroViewer">
    <head>
        <meta charset="UTF-8">
        <title>Insert - Dotabase</title>
        <meta name="Author" content="Asha" />
        <link rel="icon" href="resources/images/favicon.ico" type="image/x-icon">
        <link type="text/css" rel="stylesheet" href="resources/css/pace.css" />
        <link type="text/css" rel="stylesheet" href="resources/css/menu.css" />
        <script type="text/javascript" src="resources/javascript/browsercheck.js"></script>
        <script type="text/javascript" src="resources/javascript/pace.js"></script>
        <script type="text/javascript" src="resources/javascript/less.js"></script>
        <script type="text/javascript" src="resources/javascript/qtek.js"></script>
        <script type="text/javascript" src="resources/javascript/angular.js"></script>
        <script type="text/javascript" src="resources/javascript/jquery.js"></script>
        <script type="text/javascript" src="resources/javascript/semantic.min.js"></script>
        <style type="text/css">
            body {
                overflow: hidden;
            }
            .fs {
                position: fixed; 
                right: 0; 
                bottom: 0;
                min-width: 100%; 
                min-height: 100%;
                width: auto; 
                height: auto; 
                z-index: -100;
                background: url('resources/images/wallpaper.png') no-repeat;
                background-size: cover;
                filter: alpha(opacity = 80); 
                opacity: .95;
            }
            h1.message {
                margin-top: -622px;
                margin-left: 300px;
                margin-bottom: 200px;
                color: aquamarine;
                letter-spacing: .1em;
                text-shadow: -1px -1px 1px #111111, 2px 2px 1px #363636;
                font-size: 2em;
                box-shadow: 0 0 20px red;
                background-color: #111;
                width: 525px;
                height: 220px;
                padding-left: 7px;
            }
        </style>
    </head>
    <body style="margin: 0px">
        <nav>
            <ul>
                <li><a class="menu" href="index.py#/heroes">Home</a></li>
                <li><a class="menu" href="create.py#/heroes">Create New</a></li>
                <li class="current"><a class="menu" href="insert.py#/heroes">Insert Data</a></li>
                <li><a class="menu" href="all.py#/heroes">All Heroes <font color="red">&#9557;</font></a></li>
                <li><a class="menu" href="by_trait.py#/heroes">by Trait <font color="red">|</font></a></li>
                <li><a class="menu" href="by_speed.py#/heroes">by Speed <font color="red">|</font></a></li>
                <li><a class="menu" href="by_damage.py#/heroes">by Damage <font color="red">|</font></a></li>
                <li><a class="menu" href="by_range.py#/heroes">by Range <font color="red">|</font></a></li>
                <li><a class="menu" href="win_rate.py#/heroes">by Win Rate <font color="red">&#9563;</font></a></li>
                <li><a class="menu" href="first_10.py#/heroes">First 10</a></li>
                <li><a class="menu" href="query.py#/heroes">Letter Query</a></li>
                <li><a class="menu" href="new.py#/heroes">Create Hero</a></li>
                <li><a class="menu" href="items.py#/heroes">All Items <font color="green">&#9557;</font></a></li>
                <li><a class="menu" href="by_type.py#/heroes">by Type <font color="green">|</font></a></li>
                <li><a class="menu" href="by_price.py#/heroes">by Cost <font color="green">|</font></a></li>
                <li><a class="menu" href="by_damage_items.py#/heroes">by Damage <font color="green">|</font></a></li>
                <li><a class="menu" href="win_rate_items.py#/heroes">by Win Rate <font color="green">|</font></a></li>
                <li><a class="menu" href="usage.py#/heroes">by Usage <font color="green">&#9563;</font></a></li>
                <li><a class="menu" href="https://github.com/whiteawake/dotabase" target="_blank"><img src="resources/images/github.png" width="30px" height="30px" style="margin-top: 5px;" /></a></li>
            </ul>
        </nav><br />
        <div id="text-animate">
            <h1 class="message">
                Opening hero.csv.. &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <br />
                Opening items.csv... &nbsp;&nbsp;&nbsp;&nbsp; <br />
                Inserting hero data.. &nbsp; &nbsp; <br />
                Inserting item data... &nbsp; &nbsp; <br />
                Complete!
            </h1>
        </div>
        <div id="App">
            <canvas id="ViewPort" class="fs"></canvas>
            <div ng-view></div>
        </div>
        <script type="text/javascript">
            angular.module("heroViewer", []);
        </script>
        <script type="text/javascript" src="resources/javascript/SMDParser.js"></script>
        <script type="text/javascript" src="resources/javascript/config.js"></script>
        <script type="text/javascript" src="resources/javascript/background.js"></script>
        <script type="text/javascript" src="resources/javascript/sparkle.js"></script>
        <script type="text/javascript" src="resources/javascript/heroCtrl.js"></script>
        <script type="text/javascript" src="resources/javascript/heroListCtrl.js"></script>
        <script type="text/javascript" src="resources/javascript/app.js"></script>
        <script type="text/javascript" src="resources/javascript/fly_text.js"></script>
    </body>
</html>
""")

dotabase = sqlite3.connect("dotabase.db")
dotabase.row_factory = sqlite3.Row

reader = csv.reader(open("hero.csv", 'r'), delimiter = ',')
for row in reader:
    my_data = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9], row[10], row[11], row[12], row[13], row[14], row[15], row[16], row[17]]
    dotabase.execute("""INSERT INTO Hero(heroID, 
                        hero_name, 
                        trait, 
                        strength, 
                        strength_growth, 
                        agility, 
                        agility_growth, 
                        intelligence, 
                        intelligence_growth, 
                        speed, 
                        armour, 
                        min_damage, 
                        max_damage, 
                        range, 
                        win_rate, 
                        link_name, 
                        image_name,
                        allegiance) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
                    """, my_data)

reader = csv.reader(open("items.csv", 'r'), delimiter = ',')
for row in reader:
    my_data = [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7]]
    dotabase.execute("""INSERT INTO Items(itemID, 
                        item_name, 
                        type, 
                        damage, 
                        item_price, 
                        win_rate, 
                        usage, 
                        description) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?);
                    """, my_data)

dotabase.commit()