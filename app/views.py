from flask import render_template
from app import app
from _utility import *
from _api import *
from _dashboard import *


#############################
# Main pages
#############################
@app.route('/')
@app.route('/dashboard')
def index():
    return render_template('pages/dashboard.html', title="Dashboard", header="Dashboard",
                           timeutc=timeutc(),
                           countdatakillmails="{:,.0f}".format(countdatakillmails()),
                           countdatamoonminerals="{:,.0f}".format(countdatamoonminerals()),
                           countdatamoonverify="{:,.0f}".format(countdatamoonverify()),
                           countlatestjitajump="{:,.0f}".format(countlatestjitajump()),
                           countdatamarkethistory="{:,.0f}".format(countdatamarkethistory()),
                           countdatawallet="{:,.0f}".format(countdatawallet()),
                           latestjumpdatatime=latestjumpdatatime().strftime('%Y-%m-%d %H:%M:%S'),
                           latestsovdatatime=latestsovdatatime().strftime('%Y-%m-%d %H:%M:%S'),
                           psutil_getmemory=psutil_getmemory(),
                           plexgetlatestprice="{:,.2f}".format(getlatestprice(29668, 10000002)),
                           plexgetlatestpricechange="{:,.2f}".format(getpricepercentchange(29668, 10000002)),
                           psutil_crestconnections=psutil_crestconnections(),
                           psutil_zkillboardconnections=psutil_zkillboardconnections(),
                           getwallettransactions=getwallettransactions(10),
                           getwalletbalances=getwalletbalances(),
                           getwalletbalancestotal=getwalletbalancestotal(),
                           getskillqueues=getskillqueues())

@app.route('/system/logs')
def system():
    return render_template('pages/logs.html',
                           title="Logs",
                           header="Logs",
                           timeutc=timeutc())

@app.route('/system/settings')
def settings():
    return render_template('pages/settings.html',
                           title="Settings",
                           header="Settings",
                           timeutc=timeutc())


@app.route('/blank.html')
def blank():
    return render_template('pages/blank.html', title="Blank", header="Blank", nav="Blank Page")

@app.route('/panels-wells.html')
def panels_wells():
    return render_template('pages/panels-wells.html', title="Panels and Wells", header="Panels and Wells", nav="Panels and Wells Page")

@app.route('/buttons.html')
def buttons():
    return render_template('pages/buttons.html', title="Buttons", header="Buttons", nav="Buttons Page")

@app.route('/notifications.html')
def notifications():
    return render_template('pages/notifications.html', title="Notifications", header="Notifications", nav="Notifications Page")

@app.route('/typography.html')
def typography():
    return render_template('pages/typography.html', title="Typography", header="Typography", nav="Typography Page")

@app.route('/icons.html')
def icons():
    return render_template('pages/icons.html', title="Icons", header="Icons", nav="Icons Page")

@app.route('/grid.html')
def grid():
    return render_template('pages/grid.html', title="Grid", header="Grid", nav="Grid Page")

@app.route('/forms.html')
def forms():
    return render_template('pages/forms.html', title="Forms", header="Forms", nav="Forms Page")

@app.route('/tables.html')
def tables():
    return render_template('pages/tables.html', title="Tables", header="Tables", nav="Tables Page")


#############################
# Error Handling
#############################
@app.errorhandler(404)
def page_not_found(e):
    return render_template('pages/404.html'), 404


#############################
#   factionReport
#############################
@app.route('/report/faction/overview')
def faction_report_overview():
    return render_template('pages/factionReports/overview.html',
                           title="Overview",
                           header="Overview",
                           nav="Overview",
                           timeutc=timeutc())

@app.route('/report/faction/angel')
def faction_report_angel():
    return render_template('pages/factionReports/angel.html',
                           title="Angel Cartel",
                           header="Angel Cartel",
                           nav="Angel Cartel",
                           timeutc=timeutc())

@app.route('/report/faction/blood')
def faction_report_blood():
    return render_template('pages/factionReports/blood.html',
                           title="Blood Raiders",
                           header="Blood Raiders",
                           nav="Blood Raiders",
                           timeutc=timeutc())

@app.route('/report/faction/guristas')
def faction_report_guristas():
    return render_template('pages/factionReports/guristas.html',
                           title="Guristas",
                           header="Guristas",
                           nav="Guristas",
                           timeutc=timeutc())

@app.route('/report/faction/sansha')
def faction_report_sansha():
    return render_template('pages/factionReports/sansha.html',
                           title="Sansha's Nation",
                           header="Sansha's Nation",
                           nav="Sansha's Nation",
                           timeutc=timeutc())

@app.route('/report/faction/serpentis')
def faction_report_serpentis():
    return render_template('pages/factionReports/serpentis.html',
                           title="Serpentis",
                           header="Serpentis",
                           nav="Serpentis",
                           timeutc=timeutc())

@app.route('/report/faction/mordu')
def faction_report_mordu():
    return render_template('pages/factionReports/mordu.html',
                           title="Mordu's Legion Command",
                           header="Mordu's Legion Command",
                           nav="Mordu's Legion Command",
                           timeutc=timeutc())

@app.route('/report/faction/sisters')
def faction_report_sisters():
    return render_template('pages/factionReports/sisters.html',
                           title="Servant Sisters of EVE",
                           header="Servant Sisters of EVE",
                           nav="Servant Sisters of EVE",
                           timeutc=timeutc())


#############################
#   securityReport
#############################
@app.route('/report/security/highsec')
def securityreporthighsec():
    return render_template('pages/securityReports/highsec.html',
                           title="Highsec",
                           header="Highsec",
                           nav="Highsec",
                           timeutc=timeutc())

@app.route('/report/security/lowsec')
def securityreportlowsec():
    return render_template('pages/securityReports/lowsec.html',
                           title="Lowsec",
                           header="Lowsec",
                           nav="Lowsec",
                           timeutc=timeutc())

@app.route('/report/security/nullsec')
def securityreportnullsec():
    return render_template('pages/securityReports/nullsec.html',
                           title="Nullsec",
                           header="Nullsec",
                           nav="Nullsec",
                           timeutc=timeutc())

#############################
#   characterReport
#############################
@app.route('/report/character/blueprints')
def characterreport_blueprints():
    return render_template('pages/characterReports/blueprints.html',
                           title="Blueprints",
                           header="Blueprints",
                           nav="Blueprints",
                           timeutc=timeutc())


@app.route('/report/character/wallet')
def wallet():
    return render_template('pages/characterReports/wallet.html',
                           title="Wallet",
                           header="Wallet",
                           timeutc=timeutc())


#############################
# indexReports
#############################
@app.route('/report/index/universe')
def indexreport_universe():
    return render_template('pages/indexReports/universe.html', title="Universe", header="Universe", nav="Universe")

@app.route('/report/index/deadend')
def indexreport_deadend():
    return render_template('pages/indexReports/deadend.html',
                           title="Dead End Systems",
                           header="Dead End Systems",
                           nav="Dead End Systems",
                           timeutc=timeutc(),
                           systemList=json.loads(getdeadendsystems(1)))

@app.route('/report/index/pirateships')
def indexreport_pirateships():
    return render_template('pages/indexReports/pirateships.html',
                           title="Pirate Ships",
                           header="Pirate Ships",
                           nav="Pirate Ships",
                           timeutc=timeutc())

@app.route('/report/index/boosters')
def indexreport_boosters():
    return render_template('pages/indexReports/boosters.html',
                           title="Boosters",
                           header="Boosters",
                           nav="Boosters",
                           timeutc=timeutc())

@app.route('/report/index/pilotservices')
def indexreport_pilotservices():
    return render_template('pages/indexReports/pilotservices.html',
                           title="Pilot Services",
                           header="Pilot Services",
                           nav="Pilot Services",
                           timeutc=timeutc())

@app.route('/report/index/capitalships')
def indexreport_capitalships():
    return render_template('pages/indexReports/capitalships.html',
                           title="Capital Ships",
                           header="Capital Ships",
                           nav="Capital Ships",
                           timeutc=timeutc())

@app.route('/report/index/goldenroute')
def indexreport_goldenroute():
    return render_template('pages/indexReports/goldenroute.html',
                           title="Golden Route",
                           header="Golden Route",
                           nav="Golden Route",
                           timeutc=timeutc())


#############################
# regionReports
#############################
@app.route('/report/region/<regionID>')
def regionreport(regionID):
    regionName = getregionName(regionID)
    return render_template('pages/regionReports/regionReport.html',
                           regionID=regionID,
                           regionName=regionName,
                           timeutc=timeutc())


#############################
# jumpReports
#############################
@app.route('/report/jump/tradehubs')
def jumpreport_tradehubs():
    return render_template('pages/jumpReports/tradehubs.html',
                           title="Trade Hubs",
                           header="Trade Hubs",
                           nav="Trade Hubs",
                           timeutc=timeutc())


#############################
# marketReports
#############################
@app.route('/report/market/pilotservices/')
def marketreport_pilotservices():
    return render_template('pages/marketReports/pilotservices.html',
                           title="Pilot Services",
                           header="Pilot Services",
                           nav="Pilot Services",
                           timeutc=timeutc())

#############################
# moonReports
#############################
@app.route('/report/moon/sov')
def moonreport_sov():
    return render_template('pages/moonReports/sov.html',
                           title="Sovereignty",
                           header="Sovereignty",
                           nav="Sovereignty",
                           timeutc=timeutc())

@app.route('/report/moon/gases')
def moonreport_gases():
    return render_template('pages/moonReports/gases.html',
                           title="Gasses",
                           header="Gasses",
                           nav="Gasses",
                           timeutc=timeutc())

@app.route('/report/moon/r8')
def moonreport_r8():
    return render_template('pages/moonReports/r8.html',
                           title="Rarity 8",
                           header="Rarity 8",
                           nav="Rarity 8",
                           timeutc=timeutc())

@app.route('/report/moon/r16')
def moonreport_r16():
    return render_template('pages/moonReports/r16.html',
                           title="Rarity 16",
                           header="Rarity 16",
                           nav="Rarity 16",
                           timeutc=timeutc())

@app.route('/report/moon/r32')
def moonreport_r32():
    return render_template('pages/moonReports/r32.html',
                           title="Rarity 32",
                           header="Rarity 32",
                           nav="Rarity 32",
                           timeutc=timeutc())

@app.route('/report/moon/r64')
def moonreport_r64():
    return render_template('pages/moonReports/r64.html',
                           title="Rarity 64",
                           header="Rarity 64",
                           nav="Rarity 64",
                           timeutc=timeutc())


#############################
# mapReports
#############################
@app.route('/map/sovereignty')
def map_sovereignty():
    return render_template('pages/mapReports/sovereignty.html',
                           title="Sovereignty",
                           header="Sovereignty",
                           timeutc=timeutc())

@app.route('/map/conquerablestations')
def map_conquerablestations():
    return render_template('pages/mapReports/conquerablestations.html',
                           title="Conquerable Stations",
                           header="Conquerable Stations",
                           timeutc=timeutc())


#############################
# warReports
#############################
@app.route('/report/war/worldwarbee')
def warreport_worldwarbee():
    return render_template('pages/warReports/worldwarbee.html',
                           title="World War Bee",
                           header="World War Bee",
                           timeutc=timeutc())



#############################
# API
#############################
@app.route('/api/toprattingevents')
def api_toprattingevents():
    return toprattingevents()

@app.route('/api/topnullrattingsystems')
def api_topnullrattingsystems():
    return topnullrattingsystems()

# Highsec
@app.route('/api/gettoprattingregions_nullsec')
def api_gettoprattingregions_nullsec():
    df = gettoprattingregions_nullsec()
    df = addkillsperday(df)
    return df.reset_index().to_json(orient='records')


@app.route('/api/gettoprattingsystems_nullsec')
def api_gettoprattingsystemss_nullsec():
    df = gettoprattingsystems_nullsec()
    df = addkillsperday(df)
    return df.reset_index().to_json(orient='records')


# Lowsec
@app.route('/api/gettoprattingregions_lowsec')
def api_gettoprattingregions_lowsec():
    df = gettoprattingregions_lowsec()
    df = addkillsperday(df)
    return df.reset_index().to_json(orient='records')


@app.route('/api/gettoprattingsystems_lowsec')
def api_gettoprattingsystemss_lowsec():
    df = gettoprattingsystems_lowsec()
    df = addkillsperday(df)
    return df.reset_index().to_json(orient='records')


# Highsec
@app.route('/api/gettoprattingregions_highsec')
def api_gettoprattingregions_highsec():
    df = gettoprattingregions_highsec()
    df = addkillsperday(df)
    return df.reset_index().to_json(orient='records')


@app.route('/api/gettoprattingsystems_highsec')
def api_gettoprattingsystemss_highsec():
    df = gettoprattingsystems_highsec()
    df = addkillsperday(df)
    return df.reset_index().to_json(orient='records')

# System
@app.route('/api/system/log')
def api_systemlog():
    return getsystemlogs()

@app.route('/api/system/countmapkills')
def api_systemcountmapkills():
    return databasecountmapkills()

@app.route('/api/system/countmapjumps')
def api_systemcountmapjumps():
    return databasecountmapjumps()

@app.route('/api/system/countmapsov')
def api_systemcountmapsov():
    return databasecountmapsov()

@app.route('/api/system/countmarkethistory')
def api_systemcountmarkethistory():
    return databasecountmarkethistory()


# Settings
@app.route('/api/marketitems')
def api_getmarketitems():
    return getmarketitems()

@app.route('/api/characters')
def api_getcharacters():
    return getcharacters()

@app.route('/api/zkillboarditems')
def api_getzkillboarditems():
    return getzkillboarditems()


# Wallet
@app.route('/api/wallet/transactions')
def api_wallettransactions():
    return getwallettransactions()


# Sovereignty
@app.route('/api/sov/events')
def api_getsovevents():
    return getsovevents()


# Simple Lookups
@app.route('/api/regionName/<regionID>')
def api_regionID(regionID):
    return getregionName(regionID)

# Market
@app.route('/api/typeName/<typeID>')
def api_typeID(typeID):
    return getmarkethistory_typeID(typeID)

@app.route('/api/market/avgprice/<typeID>')
def api_marketavgprice(typeID):
    return getmarkethistory_avgprice(typeID)


# Region
@app.route('/api/region/sovereignty/<regionID>')
def api_regionsovereignty(regionID):
    return getsovbyregion(regionID)

@app.route('/api/gettoprattingbyregion/<regionID>')
def api_gettoprattingbyregion(regionID):
    df = gettoprattingbyregion(regionID)
    return df.reset_index().to_json(orient='records')

@app.route('/api/killmails/region/<regionID>')
def api_getkillmailsbyregion(regionID):
    return getkillmailsbyregion(regionID)

# Moons
@app.route('/api/moonminerals/regionid/<regionID>')
def api_moonmineralsbyregion(regionID):
    return getmoonmineralsbyregion(regionID)

@app.route('/api/moonminerals/typeid/<typeID>')
def api_moonmineralsbytype(typeID):
    return getmoonmineralsbytypeid(typeID)

@app.route('/api/moonminerals/alliance/<typeID>')
def api_moonmineralsbyalliance(typeID):
    return getmoonmineralsbyalliance(typeID)

@app.route('/api/moonminerals/alliance/')
def api_moonmineralsbyallalliance():
    return getmoonmineralsbysov()

# Index
@app.route('/api/report/index/deadend/<gateCountLimit>')
def api_getdeadendsystems(gateCountLimit):
    return getdeadendsystems(gateCountLimit)

@app.route('/api/report/index/sovchanges')
def indexreport_sovchanges():
    return getsoveventsumbyday()

@app.route('/api/report/index/typeids/<typenames>')
def indexreport_indexitems(typenames):
    if typenames == "battleship":
        return getindextypeids((17918, 17740, 17736, 17738, 17920), 30000000000)
    if typenames == "cruiser":
        return getindextypeids((17720, 17922, 17715, 17718, 17722), 30000000000)
    if typenames == "frigate":
        return getindextypeids((17932, 17926, 17930, 17924, 17928), 30000000000)
    if typenames == "sisters":
        return getindextypeids((33468, 33470, 33472), 30000000000)
    if typenames == "mordu":
        return getindextypeids((33816, 33818, 33820), 30000000000)
    if typenames == "antipharmakon":
        return getindextypeids((36908, 36909, 36910, 36911, 36912), 30000)
    if typenames == "quafezero":
        return getindextypeids((3898,), 100000000000)
    if typenames == "plex":
        return getindextypeids((29668,), 50000000000000)
    if typenames == "carriers":
        return getindextypeids((23757, 23915, 23911, 22852), 100000000)
    if typenames == "faux":
        return getindextypeids((23757, 23915, 23911, 22852), 100000000)
        #return getindextypeids((37604, 37605, 37606, 37607), 30000000000)  # Placeholder
    if typenames == "dreadnoughts":
        return getindextypeids((19720, 19726, 19724, 19722), 300000000)
    if typenames == "freighters":
        return getindextypeids((20183, 20189, 20187, 20183, ), 5000000000)
    if typenames == "jumpfreighters":
        return getindextypeids(jumpFreighters, 5000000000)
    if typenames == "ore":
        return getindextypeids((34328, 28606), 300000000)

@app.route('/api/report/index/goldenroute/<typenames>')
def api_goldenroute(typenames):
    if typenames == "freighters":
        return getkillmails_typeid_solarsystem(freighters, golden_route)
    if typenames == "jumpfreighters":
        return getkillmails_typeid_solarsystem(jumpFreighters, golden_route)
    if typenames == "allfreighters":
        return getkillmails_typeid_solarsystem(allFreighters, golden_route)
    if typenames == "ore":
        return getkillmails_typeid_solarsystem(oreFreighters, golden_route)

@app.route('/api/npckills/universe')
def api_npckillsuniverse():
    return getnpckills_byuniverse()

@app.route('/api/npckills/security')
def api_npckillssecurity():
    return getnpckills_byallsecurity()

@app.route('/api/npckills/faction/totals/<factionName>')
def api_getnpckills_totalbyregions(factionName):
    if factionName == "all":
        return getnpckills_byallfactions()
    if factionName == "angel":
        df = getnpckills_byregions(regions_angel, "Angel Cartel")
        return df.reset_index().to_json(orient='records',date_format='iso')
    if factionName == "blood":
        df = getnpckills_byregions(regions_blood, "Blood Raiders")
        return df.reset_index().to_json(orient='records',date_format='iso')
    if factionName == "guristas":
        df = getnpckills_byregions(regions_guristas, "Guristas")
        return df.reset_index().to_json(orient='records', date_format='iso')
    if factionName == "sansha":
        df = getnpckills_byregions(regions_sanshas, "Sansha's Nation")
        return df.reset_index().to_json(orient='records', date_format='iso')
    if factionName == "serpentis":
        df = getnpckills_byregions(regions_serpentis, "Serpentis")
        return df.reset_index().to_json(orient='records', date_format='iso')

@app.route('/api/npckills/faction/<factionName>')
def api_getnpckills_byregions(factionName):
    if factionName == "angel":
        return getnpckills_byfaction(regions_angel)
    if factionName == "blood":
        return getnpckills_byfaction(regions_blood)
    if factionName == "guristas":
        return getnpckills_byfaction(regions_guristas)
    if factionName == "sansha":
        return getnpckills_byfaction(regions_sanshas)
    if factionName == "serpentis":
        return getnpckills_byfaction(regions_serpentis)

@app.route('/api/npckills/war/<warName>')
def api_getnpckills_bywar(warName):
    if warName == "worldwarbee":
        return getnpckills_bywar(warName)


# Map
@app.route('/api/map/conquerablestations')
def api_conquerablestations():
    return getconquerablestationslist()

@app.route('/api/map/jumps/<solarSystemID>')
def api_mapjumps_solarsystemID(solarSystemID):
    return mapjumps_solarsystemID(solarSystemID)

@app.route('/api/map/jumps/tradehubs')
def api_mapjumps_tradehubs():
    return mapjumps_tradehubs()

@app.route('/api/map/npckills/region/<regionID>')
def api_mapkills_npckillsbyregion(regionID):
    return mapkills_npckillsbyregion(regionID)

@app.route('/api/map/shipkills/region/<regionID>')
def api_mapkills_shipkillsbyregion(regionID):
    return mapkills_shipkillsbyregion(regionID)

@app.route('/api/map/podkills/region/<regionID>')
def api_mapkills_podkillsbyregion(regionID):
    return mapkills_podkillsbyregion(regionID)

@app.route('/api/map/jumps/region/<regionID>')
def api_mapkills_jumpsbyregion(regionID):
    return mapkills_jumpsbyregion(regionID)

@app.route('/api/character/blueprints')
def api_characterblueprints():
    return getcharacterblueprints()
