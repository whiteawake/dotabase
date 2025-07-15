#!/usr/bin/env python
print("Content-Type: text/html")

import sqlite3, sys, cgi, csv
import cgitb; cgitb.enable()
from db_functions import *

print("""
<!DOCTYPE html>
<html ng-app="heroViewer" style="overflow: hidden;">
    <head>
        <meta charset="UTF-8">
        <title>By Cost - Dotabase</title>
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
        </style>
    </head>
    <body style="margin: 0px">
        <nav>
            <ul>
                <li><a class="menu" href="index.py#/heroes">Home</a></li>
                <li><a class="menu" href="create.py#/heroes">Create New</a></li>
                <li><a class="menu" href="insert.py#/heroes">Insert Data</a></li>
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
                <li class="current"><a class="menu" href="#/heroes">by Cost <font color="green">|</font></a></li>
                <li><a class="menu" href="by_damage_items.py#/heroes">by Damage <font color="green">|</font></a></li>
                <li><a class="menu" href="win_rate_items.py#/heroes">by Win Rate <font color="green">|</font></a></li>
                <li><a class="menu" href="usage.py#/heroes">by Usage <font color="green">&#9563;</font></a></li>
                <li><a class="menu" href="https://github.com/whiteawake/dotabase" target="_blank"><img src="resources/images/github.png" width="30px" height="30px" style="margin-top: 5px;" /></a></li>
            </ul>
        </nav>
        <div id="App">
            <canvas id="ViewPort" class="fs"></canvas>
            <div ng-view></div>
        </div>
        <article id="boxeditems">
            <table class="dota" data-table-sortable="yes">
                <thead>
                    <tr>
                        <th class="header" id="hero_header" style="padding-bottom: 31px;"><br />Item</th>
                        <th class="header">Type</th>
                        <th class="header" style="color: aqua;">Cost</th>
                        <th class="header" title="How much damage is dealt by the item (if applicable).">Damage</th>
                        <th class="header" title="How many times this item has been used on a winning team this month.">Global Win Rate</th>
                        <th class="header" title="How many times this item has been used this month.">Global Usage</th>
                        <th class="header" title="Breif information on the item.">Description</th>
                    </tr>
                </thead>
                <tbody>
    """)

dotabase = sqlite3.connect("dotabase.db")
dotabase.row_factory = sqlite3.Row

my_data = dotabase.execute('SELECT * FROM Items ORDER BY item_price DESC')

for row in my_data:
    print("""
                <tr>
                    <td class="cell-icon">
                        <strong>
                            <img width="128" height="72" src="resources/images/items/""" + str(row[0]) +"""_full.png" title='""" + str(row[1]) + """' />
                        </strong>
                    </td>
                    <td><em>""" + str(row[2]) + """</em></td>
                    <td>""" + str(row[4]) + """</td>
                    <td><em>""" + str(row[3]) + """</em></td>
                    <td>""" + str(row[5]) + """</td>
                    <td><em>""" + str(row[6]) + """</em></td>
                    <td>""" + str(row[7]) + """</td>
                </tr>
        """)

print("""
                </tbody>
            </table>
        </article>
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
    </body>
</html>
	""")