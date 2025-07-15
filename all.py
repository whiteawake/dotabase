#!/usr/bin/env python
print("Content-Type: text/html")

import sqlite3, sys, cgi, csv, random
import cgitb; cgitb.enable()
from db_functions import *

print("""
<!DOCTYPE html>
<html ng-app="heroViewer" style="overflow: hidden;">
    <head>
        <meta charset="UTF-8">
        <title>All - Dotabase</title>
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
                <li class="current"><a class="menu" href="#">All Heroes <font color="red">&#9557;</font></a></li>
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
        </nav>
        <div id="App">
            <canvas id="ViewPort" class="fs"></canvas>
            <div ng-view></div>
        </div>
        <article id="boxedheroes">
            <table class="dota" data-table-sortable="yes" width="100%">
                <thead>
                    <tr>
                        <th class="header" id="hero_header" style="color: darkgoldenrod; padding-bottom: 31px;" title="All statistics are without item benefits."><br />Hero</th>
                        <th class="header">Primary Trait</th>
                        <th class="header">Allegiance</th>
                        <th class="header">Base Strength</th>
                        <th class="header">Base Agility</th>
                        <th class="header">Base Intelligence</th>
                        <th class="header">Movement Speed</th>
                        <th class="header">Starting Armour</th>
                        <th class="header" title="Damage dealt by your hero at level 1.">Damage (min)</th>
                        <th class="header" title="Damage dealt by your hero at level 25.">Damage (max)</th>
                        <th class="header">Attack Range</th>
                        <th class="header" title="Global Win Rate (%)">Win Rate (%)</th>
                        <th class="header" title="Items recommended to suit your hero.">Recommended Items</th>
                    </tr>
                </thead>
                <tbody>
    """)

dotabase = sqlite3.connect("dotabase.db")
dotabase.row_factory = sqlite3.Row

hero_data = dotabase.execute('SELECT * FROM Hero ORDER BY hero_name')

for row in hero_data:
    
    print("""
                <tr>
                    <td class="cell-icon">
                        <strong>
                            <a href="view/#/hero/""" + row[15] + """" title='""" + row[1] + """'>
                                <img width="128" height="72" src="resources/images/portraits/""" + row[16] +"""_full.png" />
                            </a>
                        </strong>
                    </td>
                    <td><em>""" + row[2] + """</em></td>
                    <td><em>""" + row[17] + """</em></td>
                    <td>""" + str(row[3]) + """</td>
                    <td>""" + str(row[5]) + """</td>
                    <td>""" + str(row[7]) + """</td>
                    <td>""" + str(row[9]) + """</td>
                    <td>""" + str(row[10]) + """</td>
                    <td>""" + str(row[11]) + """</td>
                    <td>""" + str(row[12]) + """</td>
                    <td>""" + str(row[13]) + """</td>
                    <td>""" + str(row[14]) + """</td>
                    <td>
                         <img width="128" height="72" src="resources/images/items/""" + str(row[0]) +"""_full.png" />
                    </td>
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