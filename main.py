#!/usr/bin/env python
#create by Mike Edwards
# Em desenvolvimento #
 
#lib 
import os
import platform
import webbrowser
import time
import datetime
import random
try:
    import requests
except:
    os.system('pip install requests')
    import requests


# Variaveis, Lista e dicionarios
banda = {'11980':'Oi', '11981':'Tim', '11982':'Tim', '11983':'Tim', '11984':'Tim', '11985':'Tim', '11986':'Tim', '11987':'Tim', '11988':'Claro', '11989':'Claro', '11990':'None', '11991':'Claro', '11992':'Claro', '11993':'Claro', '11994':'Claro', '11995':'Claro', '11996':'Vivo', '11997':'Vivo', '11998':'Vivo', '11999':'Vivo', '12980':'Oi', '12981':'Tim', '12982':'Tim', '12983':'Tim', '12984':'Tim', '12985':'Tim', '12986':'Tim', '12987':'Tim', '12988':'Claro', '12989':'Claro', '12990':'None', '12991':'Claro', '12992':'Claro', '12993':'Claro', '12994':'Claro', '12995':'Claro', '12996':'Vivo', '12997':'Vivo', '12998':'Vivo', '12999':'Vivo', '13980':'Oi', '13981':'Tim', '13982':'Tim', '13983':'Tim', '13984':'Tim', '13985':'Tim', '13986':'Tim', '13987':'Tim', '13988':'Claro', '13989':'Claro', '13990':'None', '13991':'Claro', '13992':'Claro', '13993':'Claro', '13994':'Claro', '13995':'Claro', '13996':'Vivo', '13997':'Vivo', '13998':'Vivo', '13999':'Vivo', '14980':'Oi', '14981':'Tim', '14982':'Tim', '14983':'Tim', '14984':'Tim', '14985':'Tim', '14986':'Tim', '14987':'Tim', '14988':'Claro', '14989':'Claro', '14990':'None', '14991':'Claro', '14992':'Claro', '14993':'Claro', '14994':'Claro', '14995':'Claro', '14996':'Vivo', '14997':'Vivo', '14998':'Vivo', '14999':'Vivo', '15980':'Oi', '15981':'Tim', '15982':'Tim', '15983':'Tim', '15984':'Tim', '15985':'Tim', '15986':'Tim', '15987':'Tim', '15988':'Claro', '15989':'Claro', '15990':'None', '15991':'Claro', '15992':'Claro', '15993':'Claro', '15994':'Claro', '15995':'Claro', '15996':'Vivo', '15997':'Vivo', '15998':'Vivo', '15999':'Vivo', '16980':'Oi', '16981':'Tim', '16982':'Tim', '16983':'Tim', '16984':'Tim', '16985':'Tim', '16986':'Tim', '16987':'Tim', '16988':'Claro', '16989':'Claro', '16990':'None', '16991':'Claro', '16992':'Claro', '16993':'Claro', '16994':'Claro', '16995':'Claro', '16996':'Vivo', '16997':'Vivo', '16998':'Vivo', '16999':'Vivo', '17980':'Oi', '17981':'Tim', '17982':'Tim', '17983':'Tim', '17984':'Tim', '17985':'Tim', '17986':'Tim', '17987':'Tim', '17988':'Claro', '17989':'Claro', '17990':'None', '17991':'Claro', '17992':'Claro', '17993':'Claro', '17994':'Claro', '17995':'Claro', '17996':'Vivo', '17997':'Vivo', '17998':'Vivo', '17999':'Vivo', '18980':'Oi', '18981':'Tim', '18982':'Tim', '18983':'Tim', '18984':'Tim', '18985':'Tim', '18986':'Tim', '18987':'Tim', '18988':'Claro', '18989':'Claro', '18990':'None', '18991':'Claro', '18992':'Claro', '18993':'Claro', '18994':'Claro', '18995':'Claro', '18996':'Vivo', '18997':'Vivo', '18998':'Vivo', '18999':'Vivo', '19980':'Oi', '19981':'Tim', '19982':'Tim', '19983':'Tim', '19984':'Tim', '19985':'Tim', '19986':'Tim', '19987':'Tim', '19988':'Claro', '19989':'Claro', '19990':'None', '19991':'Claro', '19992':'Claro', '19993':'Claro', '19994':'Claro', '19995':'Claro', '19996':'Vivo', '19997':'Vivo', '19998':'Vivo', '19999':'Vivo', '21980':'Tim', '21981':'Tim', '21982':'Tim', '21983':'Tim', '21984':'', '21985':'', '21986':'', '21987':'Oi', '21988':'Oi', '21989':'', '21990':'', '21991':'Claro', '21992':'Claro', '21993':'Claro', '21994':'Claro', '21995':'', '21996':'Vivo', '21997':'Vivo', '21998':'Vivo', '21999':'Vivo', '22980':'Tim', '22981':'Tim', '22982':'Tim', '22983':'Tim', '22984':'', '22985':'', '22986':'', '22987':'Oi', '22988':'Oi', '22989':'', '22990':'', '22991':'Claro', '22992':'Claro', '22993':'Claro', '22994':'Claro', '22995':'', '22996':'Vivo', '22997':'Vivo', '22998':'Vivo', '22999':'Vivo', '24980':'Tim', '24981':'Tim', '24982':'Tim', '24983':'Tim', '24984':'', '24985':'', '24986':'', '24987':'Oi', '24988':'Oi', '24989':'', '24990':'', '24991':'Claro', '24992':'Claro', '24993':'Claro', '24994':'Claro', '24995':'', '24996':'Vivo', '24997':'Vivo', '24998':'Vivo', '24999':'Vivo', '27980':'Tim', '27981':'Tim', '27982':'Tim', '27983':'Tim', '27984':'', '27985':'', '27986':'', '27987':'Oi', '27988':'Oi', '27989':'', '27990':'', '27991':'Claro', '27992':'Claro', '27993':'Claro', '27994':'Claro', '27995':'', '27996':'Vivo', '27997':'Vivo', '27998':'Vivo', '27999':'Vivo', '28980':'Tim', '28981':'Tim', '28982':'Tim', '28983':'Tim', '28984':'', '28985':'', '28986':'', '28987':'Oi', '28988':'Oi', '28989':'', '28990':'', '28991':'Claro', '28992':'Claro', '28993':'Claro', '28994':'Claro', '28995':'', '28996':'Vivo', '28997':'Vivo', '28998':'Vivo', '28999':'Vivo', '31980':'none', '31981':'Claro', '31982':'Claro', '31983':'Claro', '31984':'Claro', '31985':'Oi', '31986':'Oi', '31987':'Oi', '31988':'Oi', '31989':'Oi', '31990':'Vivo', '31991':'Tim', '31992':'Tim', '31993':'Tim', '31994':'Tim', '31995':'Telemig Celular', '31996':'Telemig Celular', '31997':'Telemig Celular', '31998':'Telemig Celular', '31999':'Telemig Celular', '32980':'none', '32981':'Claro', '32982':'Claro', '32983':'Claro', '32984':'Claro', '32985':'Oi', '32986':'Oi', '32987':'Oi', '32988':'Oi', '32989':'Oi', '32990':'Vivo', '32991':'Tim', '32992':'Tim', '32993':'Tim', '32994':'Tim', '32995':'Telemig Celular', '32996':'Telemig Celular', '32997':'Telemig Celular', '32998':'Telemig Celular', '32999':'Telemig Celular', '33980':'none', '33981':'Claro', '33982':'Claro', '33983':'Claro', '33984':'Claro', '33985':'Oi', '33986':'Oi', '33987':'Oi', '33988':'Oi', '33989':'Oi', '33990':'Vivo', '33991':'Tim', '33992':'Tim', '33993':'Tim', '33994':'Tim', '33995':'Telemig Celular', '33996':'Telemig Celular', '33997':'Telemig Celular', '33998':'Telemig Celular', '33999':'Telemig Celular', '34980':'none', '34981':'Claro', '34982':'Claro', '34983':'Claro', '34984':'Claro', '34985':'Oi', '34986':'Oi', '34987':'Oi', '34988':'Oi', '34989':'Oi', '34990':'Vivo', '34991':'Tim', '34992':'Tim', '34993':'Tim', '34994':'Tim', '34995':'Telemig Celular', '34996':'Telemig Celular', '34997':'Telemig Celular', '34998':'Telemig Celular', '34999':'Telemig Celular', '35980':'none', '35981':'Claro', '35982':'Claro', '35983':'Claro', '35984':'Claro', '35985':'Oi', '35986':'Oi', '35987':'Oi', '35988':'Oi', '35989':'Oi', '35990':'Vivo', '35991':'Tim', '35992':'Tim', '35993':'Tim', '35994':'Tim', '35995':'Telemig Celular', '35996':'Telemig Celular', '35997':'Telemig Celular', '35998':'Telemig Celular', '35999':'Telemig Celular', '36980':'none', '36981':'Claro', '36982':'Claro', '36983':'Claro', '36984':'Claro', '36985':'Oi', '36986':'Oi', '36987':'Oi', '36988':'Oi', '36989':'Oi', '36990':'Vivo', '36991':'Tim', '36992':'Tim', '36993':'Tim', '36994':'Tim', '36995':'Telemig Celular', '36996':'Telemig Celular', '36997':'Telemig Celular', '36998':'Telemig Celular', '36999':'Telemig Celular', '37980':'none', '37981':'Claro', '37982':'Claro', '37983':'Claro', '37984':'Claro', '37985':'Oi', '37986':'Oi', '37987':'Oi', '37988':'Oi', '37989':'Oi', '37990':'Vivo', '37991':'Tim', '37992':'Tim', '37993':'Tim', '37994':'Tim', '37995':'Telemig Celular', '37996':'Telemig Celular', '37997':'Telemig Celular', '37998':'Telemig Celular', '37999':'Telemig Celular', '38980':'none', '38981':'Claro', '38982':'Claro', '38983':'Claro', '38984':'Claro', '38985':'Oi', '38986':'Oi', '38987':'Oi', '38988':'Oi', '38989':'Oi', '38990':'Vivo', '38991':'Tim', '38992':'Tim', '38993':'Tim', '38994':'Tim', '38995':'Telemig Celular', '38996':'Telemig Celular', '38997':'Telemig Celular', '38998':'Telemig Celular', '38999':'Telemig Celular', '41980':'none', '41981':'Telefonica Brazil', '41982':'Telefonica Brazil', '41983':'', '41984':'Brasil Telecom', '41985':'Brasil Telecom', '41986':'', '41987':'Claro', '41988':'Claro', '41989':'', '41990':'', '41991':'Vivo', '41992':'Vivo', '41993':'Vivo', '41994':'Vivo', '41995':'', '41996':'Tim', '41997':'Tim', '41998':'Tim', '41999':'Tim', '42980':'none', '42981':'Telefonica Brazil', '42982':'Telefonica Brazil', '42983':'', '42984':'Brasil Telecom', '42985':'Brasil Telecom', '42986':'', '42987':'Claro', '42988':'Claro', '42989':'', '42990':'', '42991':'Vivo', '42992':'Vivo', '42993':'Vivo', '42994':'Vivo', '42995':'', '42996':'Tim', '42997':'Tim', '42998':'Tim', '42999':'Tim', '43980':'none', '43981':'Telefonica Brazil', '43982':'Telefonica Brazil', '43983':'', '43984':'Brasil Telecom', '43985':'Brasil Telecom', '43986':'', '43987':'Claro', '43988':'Claro', '43989':'', '43990':'', '43991':'Vivo', '43992':'Vivo', '43993':'Vivo', '43994':'Vivo', '43995':'', '43996':'Tim', '43997':'Tim', '43998':'Tim', '43999':'Tim', '44980':'none', '44981':'Telefonica Brazil', '44982':'Telefonica Brazil', '44983':'', '44984':'Brasil Telecom', '44985':'Brasil Telecom', '44986':'', '44987':'Claro', '44988':'Claro', '44989':'', '44990':'', '44991':'Vivo', '44992':'Vivo', '44993':'Vivo', '44994':'Vivo', '44995':'', '44996':'Tim', '44997':'Tim', '44998':'Tim', '44999':'Tim', '45980':'none', '45981':'Telefonica Brazil', '45982':'Telefonica Brazil', '45983':'', '45984':'Brasil Telecom', '45985':'Brasil Telecom', '45986':'', '45987':'Claro', '45988':'Claro', '45989':'', '45990':'', '45991':'Vivo', '45992':'Vivo', '45993':'Vivo', '45994':'Vivo', '45995':'', '45996':'Tim', '45997':'Tim', '45998':'Tim', '45999':'Tim', '46980':'none', '46981':'Telefonica Brazil', '46982':'Telefonica Brazil', '46983':'', '46984':'Brasil Telecom', '46985':'Brasil Telecom', '46986':'', '46987':'Claro', '46988':'Claro', '46989':'', '46990':'', '46991':'Vivo', '46992':'Vivo', '46993':'Vivo', '46994':'Vivo', '46995':'', '46996':'Tim', '46997':'Tim', '46998':'Tim', '46999':'Tim', '47980':'none', '47981':'Telefonica Brazil', '47982':'Telefonica Brazil', '47983':'', '47984':'Brasil Telecom', '47985':'Brasil Telecom', '47986':'', '47987':'Claro', '47988':'Claro', '47989':'', '47990':'', '47991':'Vivo', '47992':'Vivo', '47993':'Vivo', '47994':'Vivo', '47995':'', '47996':'Tim', '47997':'Tim', '47998':'Tim', '47999':'Tim', '48980':'none', '48981':'Telefonica Brazil', '48982':'Telefonica Brazil', '48983':'', '48984':'Brasil Telecom', '48985':'Brasil Telecom', '48986':'', '48987':'Claro', '48988':'Claro', '48989':'', '48990':'', '48991':'Vivo', '48992':'Vivo', '48993':'Vivo', '48994':'Vivo', '48995':'', '48996':'Tim', '48997':'Tim', '48998':'Tim', '48999':'Tim', '49980':'none', '49981':'Telefonica Brazil', '49982':'Telefonica Brazil', '49983':'', '49984':'Brasil Telecom', '49985':'Brasil Telecom', '49986':'', '49987':'Claro', '49988':'Claro', '49989':'', '49990':'', '49991':'Vivo', '49992':'Vivo', '49993':'Vivo', '49994':'Vivo', '49995':'', '49996':'Tim', '49997':'Tim', '49998':'Tim', '49999':'Tim', '51980':'none', '51981':'Tim', '51982':'Tim', '51983':'', '51984':'Brasil Telecom', '51985':'Brasil Telecom', '51986':'', '51987':'', '51988':'', '51989':'', '51990':'', '51991':'Claro', '51992':'Claro', '51993':'Claro', '51994':'Claro', '51995':'', '51996':'Vivo', '51997':'Vivo', '51998':'Vivo', '51999':'Vivo', '53980':'none', '53981':'Tim', '53982':'Tim', '53983':'', '53984':'Brasil Telecom', '53985':'Brasil Telecom', '53986':'', '53987':'', '53988':'', '53989':'', '53990':'', '53991':'Claro', '53992':'Claro', '53993':'Claro', '53994':'Claro', '53995':'', '53996':'Vivo', '53997':'Vivo', '53998':'Vivo', '53999':'Vivo', '54980':'none', '54981':'Tim', '54982':'Tim', '54983':'', '54984':'Brasil Telecom', '54985':'Brasil Telecom', '54986':'', '54987':'', '54988':'', '54989':'', '54990':'', '54991':'Claro', '54992':'Claro', '54993':'Claro', '54994':'Claro', '54995':'', '54996':'Vivo', '54997':'Vivo', '54998':'Vivo', '54999':'Vivo', '55980':'none', '55981':'Tim', '55982':'Tim', '55983':'', '55984':'Brasil Telecom', '55985':'Brasil Telecom', '55986':'', '55987':'', '55988':'', '55989':'', '55990':'', '55991':'Claro', '55992':'Claro', '55993':'Claro', '55994':'Claro', '55995':'', '55996':'Vivo', '55997':'Vivo', '55998':'Vivo', '55999':'Vivo', '61980':'none', '61981':'Tim', '61982':'Tim', '61983':'', '61984':'Brasil Telecom', '61985':'Brasil Telecom', '61986':'', '61987':'', '61988':'', '61989':'', '61990':'', '61991':'Claro', '61992':'Claro', '61993':'Claro', '61994':'Claro', '61995':'', '61996':'Vivo', '61997':'Vivo', '61998':'Vivo', '61999':'Vivo', '62980':'none', '62981':'Tim', '62982':'Tim', '62983':'', '62984':'Brasil Telecom', '62985':'Brasil Telecom', '62986':'', '62987':'', '62988':'', '62989':'', '62990':'', '62991':'Claro', '62992':'Claro', '62993':'Claro', '62994':'Claro', '62995':'', '62996':'Vivo', '62997':'Vivo', '62998':'Vivo', '62999':'Vivo', '69980':'none', '63980':'none', '63981':'Tim', '63982':'Tim', '63983':'', '63984':'Brasil Telecom', '63985':'Brasil Telecom', '63986':'', '63987':'', '63988':'', '63989':'', '63990':'', '63991':'Claro', '63992':'Claro', '63993':'Claro', '63994':'Claro', '63995':'', '63996':'Vivo', '63997':'Vivo', '63998':'Vivo', '63999':'Vivo', '69980':'none', '64981':'Tim', '64982':'Tim', '64983':'', '64984':'Brasil Telecom', '64985':'Brasil Telecom', '64986':'', '64987':'', '64988':'', '64989':'', '64990':'', '64991':'Claro', '64992':'Claro', '64993':'Claro', '64994':'Claro', '64995':'', '64996':'Vivo', '64997':'Vivo', '64998':'Vivo', '64999':'Vivo', '69980':'none', '65981':'Tim', '65982':'Tim', '65983':'', '65984':'Brasil Telecom', '65985':'Brasil Telecom', '65986':'', '65987':'', '65988':'', '65989':'', '65990':'', '65991':'Claro', '65992':'Claro', '65993':'Claro', '65994':'Claro', '65995':'', '65996':'Vivo', '65997':'Vivo', '65998':'Vivo', '65999':'Vivo', '69980':'none', '66981':'Tim', '66982':'Tim', '63983':'', '66984':'Brasil Telecom', '66985':'Brasil Telecom', '66986':'', '66987':'', '66988':'', '66989':'', '66990':'', '66991':'Claro', '66992':'Claro', '66993':'Claro', '66994':'Claro', '66995':'', '66996':'Vivo', '66997':'Vivo', '66998':'Vivo', '66999':'Vivo', '69980':'none', '67981':'Tim', '67982':'Tim', '67983':'', '67984':'Brasil Telecom', '67985':'Brasil Telecom', '67986':'', '67987':'', '67988':'', '67989':'', '67990':'', '67991':'Claro', '67992':'Claro', '67993':'Claro', '67994':'Claro', '67995':'', '67996':'Vivo', '67997':'Vivo', '67998':'Vivo', '67999':'Vivo', '69980':'none', '68981':'Tim', '68982':'Tim', '68983':'', '68984':'Brasil Telecom', '68985':'Brasil Telecom', '68986':'', '68987':'', '68988':'', '68989':'', '68990':'', '68991':'Claro', '68992':'Claro', '68993':'Claro', '68994':'Claro', '68995':'', '68996':'Vivo', '68997':'Vivo', '68998':'Vivo', '68999':'Vivo', '69980':'none', '69981':'Tim', '69982':'Tim', '69983':'', '69984':'Brasil Telecom', '69985':'Brasil Telecom', '69986':'', '69987':'', '69988':'', '69989':'', '69990':'', '69991':'Claro', '69992':'Claro', '69993':'Claro', '69994':'Claro', '69995':'', '69996':'Vivo', '69997':'Vivo', '69998':'Vivo', '69999':'Vivo', '71980':'none', '71981':'Claro', '71982':'Claro', '71983':'Claro', '71984':'', '71985':'', '71986':'', '71987':'Oi', '71988':'Oi', '71989':'', '71990':'', '71991':'Tim', '71992':'Tim', '71993':'Tim', '71994':'Tim', '71995':'', '71996':'Vivo', '71997':'Vivo', '71998':'Vivo', '71999':'Vivo', '73980':'none', '73981':'Claro', '73982':'Claro', '73983':'Claro', '73984':'', '73985':'', '73986':'', '73987':'Oi', '73988':'Oi', '73989':'', '73990':'', '73991':'Tim', '73992':'Tim', '73993':'Tim', '73994':'Tim', '73995':'', '73996':'Vivo', '73997':'Vivo', '73998':'Vivo', '73999':'Vivo', '74980':'none', '74981':'Claro', '74982':'Claro', '74983':'Claro', '74984':'', '74985':'', '74986':'', '74987':'Oi', '74988':'Oi', '74989':'', '74990':'', '74991':'Tim', '74992':'Tim', '74993':'Tim', '74994':'Tim', '74995':'', '74996':'Vivo', '74997':'Vivo', '74998':'Vivo', '74999':'Vivo', '75980':'none', '75981':'Claro', '75982':'Claro', '75983':'Claro', '75984':'', '75985':'', '75986':'', '75987':'Oi', '75988':'Oi', '75989':'', '75990':'', '75991':'Tim', '75992':'Tim', '75993':'Tim', '75994':'Tim', '75995':'', '75996':'Vivo', '75997':'Vivo', '75998':'Vivo', '75999':'Vivo', '77980':'none', '77981':'Claro', '77982':'Claro', '77983':'Claro', '77984':'', '77985':'', '77986':'', '77987':'Oi', '77988':'Oi', '77989':'', '77990':'', '77991':'Tim', '77992':'Tim', '77993':'Tim', '77994':'Tim', '77995':'', '77996':'Vivo', '77997':'Vivo', '77998':'Vivo', '77999':'Vivo', '79980':'none', '79981':'Claro', '79982':'Claro', '79983':'Claro', '79984':'', '79985':'', '79986':'', '79987':'Oi', '79988':'Oi', '79989':'', '79990':'', '79991':'Tim', '79992':'Tim', '79993':'Tim', '79994':'Tim', '79995':'', '79996':'Vivo', '79997':'Vivo', '79998':'Vivo', '79999':'Vivo', '81980':'none', '81981':'Vivo', '81982':'Vivo', '81983':'', '81984':'', '81985':'', '81986':'', '81987':'Oi', '81988':'Oi', '81989':'', '81990':'', '81991':'Claro', '81992':'Claro', '81993':'Claro', '81994':'Claro', '81995':'', '81996':'Tim', '81997':'Tim', '81998':'Tim', '81999':'Tim', '82980':'none', '82981':'Vivo', '82982':'Vivo', '82983':'', '82984':'', '82985':'', '82986':'', '82987':'Oi', '82988':'Oi', '82989':'', '82990':'', '82991':'Claro', '82992':'Claro', '82993':'Claro', '82994':'Claro', '82995':'', '82996':'Tim', '82997':'Tim', '82998':'Tim', '82999':'Tim', '83980':'none', '83981':'Vivo', '83982':'Vivo', '83983':'', '83984':'', '83985':'', '83986':'', '83987':'Oi', '83988':'Oi', '83989':'', '83990':'', '83991':'Claro', '83992':'Claro', '83993':'Claro', '83994':'Claro', '83995':'', '83996':'Tim', '83997':'Tim', '83998':'Tim', '83999':'Tim', '84980':'none', '84981':'Vivo', '84982':'Vivo', '84983':'', '84984':'', '84985':'', '84986':'', '84987':'Oi', '84988':'Oi', '84989':'', '84990':'', '84991':'Claro', '84992':'Claro', '84993':'Claro', '84994':'Claro', '84995':'', '84996':'Tim', '84997':'Tim', '84998':'Tim', '84999':'Tim', '85980':'none', '85981':'Vivo', '85982':'Vivo', '85983':'', '85984':'', '85985':'', '85986':'', '85987':'Oi', '85988':'Oi', '85989':'', '85990':'', '85991':'Claro', '85992':'Claro', '85993':'Claro', '85994':'Claro', '85995':'', '85996':'Tim', '85997':'Tim', '85998':'Tim', '85999':'Tim', '86980':'none', '86981':'Vivo', '86982':'Vivo', '86983':'', '86984':'', '86985':'', '86986':'', '86987':'Oi', '86988':'Oi', '86989':'', '86990':'', '86991':'Claro', '86992':'Claro', '86993':'Claro', '86994':'Claro', '86995':'', '86996':'Tim', '86997':'Tim', '86998':'Tim', '86999':'Tim', '87980':'none', '87981':'Vivo', '87982':'Vivo', '87983':'', '87984':'', '87985':'', '87986':'', '87987':'Oi', '87988':'Oi', '87989':'', '87990':'', '87991':'Claro', '81992':'Claro', '87993':'Claro', '87994':'Claro', '87995':'', '87996':'Tim', '87997':'Tim', '87998':'Tim', '87999':'Tim', '88980':'none', '88981':'Vivo', '88982':'Vivo', '88983':'', '88984':'', '88985':'', '88986':'', '88987':'Oi', '88988':'Oi', '88989':'', '88990':'', '88991':'Claro', '88992':'Claro', '88993':'Claro', '88994':'Claro', '88995':'', '88996':'Tim', '88997':'Tim', '88998':'Tim', '88999':'Tim', '89980':'none', '89981':'Vivo', '89982':'Vivo', '89983':'', '89984':'', '89985':'', '89986':'', '89987':'Oi', '89988':'Oi', '89989':'', '89990':'', '89991':'Claro', '89992':'Claro', '89993':'Claro', '89994':'Claro', '89995':'', '89996':'Tim', '89997':'Tim', '89998':'Tim', '89999':'Tim', '91980':'Tim', '91981':'Tim', '91982':'Tim', '91983':'Tim', '91984':'', '91985':'', '91986':'', '91987':'Oi', '91988':'Oi', '91989':'', '91990':'', '91991':'Vivo', '91992':'Vivo', '91993':'Vivo', '91994':'Vivo', '91995':'', '91996':'Amazônia Celular', '91997':'Amazônia Celular', '91998':'Amazônia Celular', '91999':'Amazônia Celular', '92980':'Tim', '92981':'Tim', '92982':'Tim', '92983':'Tim', '92984':'', '92985':'', '92986':'', '92987':'Oi', '92988':'Oi', '92989':'', '92990':'', '92991':'Vivo', '92992':'Vivo', '92993':'Vivo', '92994':'Vivo', '92995':'', '92996':'Amazônia Celular', '92997':'Amazônia Celular', '92998':'Amazônia Celular', '92999':'Amazônia Celular', '93980':'Tim', '93981':'Tim', '93982':'Tim', '93983':'Tim', '93984':'', '93985':'', '93986':'', '93987':'Oi', '93988':'Oi', '93989':'', '93990':'', '93991':'Vivo', '93992':'Vivo', '93993':'Vivo', '93994':'Vivo', '93995':'', '93996':'Amazônia Celular', '93997':'Amazônia Celular', '93998':'Amazônia Celular', '93999':'Amazônia Celular', '94980':'Tim', '94981':'Tim', '94982':'Tim', '94983':'Tim', '94984':'', '94985':'', '94986':'', '94987':'Oi', '94988':'Oi', '94989':'', '94990':'', '94991':'Vivo', '94992':'Vivo', '94993':'Vivo', '94994':'Vivo', '94995':'', '94996':'Amazônia Celular', '94997':'Amazônia Celular', '94998':'Amazônia Celular', '94999':'Amazônia Celular', '95980':'Tim', '95981':'Tim', '96982':'Tim', '95983':'Tim', '95984':'', '95985':'', '95986':'', '95987':'Oi', '95988':'Oi', '95989':'', '95990':'', '95991':'Vivo', '95992':'Vivo', '95993':'Vivo', '95994':'Vivo', '95995':'', '95996':'Amazônia Celular', '95997':'Amazônia Celular', '95998':'Amazônia Celular', '95999':'Amazônia Celular', '96980':'Tim', '96981':'Tim', '96982':'Tim', '96983':'Tim', '96984':'', '96985':'', '96986':'', '96987':'Oi', '96988':'Oi', '96989':'', '96990':'', '96991':'Vivo', '96992':'Vivo', '96993':'Vivo', '96994':'Vivo', '96995':'', '96996':'Amazônia Celular', '96997':'Amazônia Celular', '96998':'Amazônia Celular', '96999':'Amazônia Celular', '97980':'Tim', '97981':'Tim', '97982':'Tim', '97983':'Tim', '97984':'', '97985':'', '97986':'', '97987':'Oi', '97988':'Oi', '97989':'', '97990':'', '97991':'Vivo', '97992':'Vivo', '97993':'Vivo', '97994':'Vivo', '97995':'', '97996':'Amazônia Celular', '97997':'Amazônia Celular', '97998':'Amazônia Celular', '97999':'Amazônia Celular', '98980':'Tim', '98981':'Tim', '98982':'Tim', '98983':'Tim', '98984':'', '98985':'', '98986':'', '98987':'Oi', '98988':'Oi', '98989':'', '98990':'', '98991':'Vivo', '98992':'Vivo', '98993':'Vivo', '98994':'Vivo', '98995':'', '98996':'Amazônia Celular', '98997':'Amazônia Celular', '98998':'Amazônia Celular', '98999':'Amazônia Celular', '99980':'Tim', '99981':'Tim', '99982':'Tim', '99983':'Tim', '99984':'', '99985':'', '99986':'', '99987':'Oi', '99988':'Oi', '99989':'', '99990':'', '99991':'Vivo', '99992':'Vivo', '99993':'Vivo', '99994':'Vivo', '99995':'', '99996':'Amazônia Celular', '99997':'Amazônia Celular', '99998':'Amazônia Celular', '99999':'Amazônia Celular'}

ddi_d = {'001':'Anguila, Antígua e Barbuda, Bahamas, Barbados, Bermudas, Canadá, Dominica, Estados Unidos, Granada, Ilhas Caimão, Ilhas Marianas do Norte, Ilhas Virgens Americanas, Ilhas Virgens Britânicas, Jamaica, Montserrat, Porto Rico, República Dominicana, Samoa Americana, Santa Lúcia, São Cristóvão e Neves, São Vicente e Granadinas, Trinidad e Tobago, Turcas e Caicos', '002':'Sem informações', '003':'Sem informações', '004':'Sem informações', '005':'Sem informações', '006':'Sem informações', '007':'Casaquistão, Rússia', '008':'Sem informações', '009':'Sem informações', '010':'Sem informações', '011':'Sem informações', '012':'Sem informações', '013':'Sem informações', '014':'Sem informações', '015':'Sem informações', '016':'Sem informações', '017':'Sem informações', '018':'Sem informações', '019':'Sem informações', '020':'Egito', '021':'Sem informações', '022':'Sem informações', '023':'Sem informações', '024':'Sem informações', '025':'Sem informações', '026':'Sem informações', '027':'África Do Sul', '028':'Sem informações', '029':'Sem informações', '030':'Grécia', '031':'Holanda', '032':'Bélgica', '033':'França', '034':'Espanha', '035':'Sem informações', '036':'Hungria', '037':'Sem informações', '038':'Sem informações', '039':'Itália', '040':'Romênia', '041':'Suíça', '042':'Sem informações', '043':'Áustria', '044':'Reino Unido', '045':'Dinamarca', '046':'Suécia', '047':'Noruega', '048':'Polônia', '049':'Alemanha', '050':'Sem informações', '051':'Peru', '052':'México', '053':'Cuba', '054':'Argentina', '055':'Brasil', '056':'Chile', '057':'Colômbia', '058':'Venezuela', '059':'Sem informações', '060':'Malásia', '061':'Austrália', '062':'Indonésia', '063':'Filipinas', '064':'Nova Zelândia', '065':'Cingapura', '066':'Tailândia', '067':'Sem informações', '068':'Sem informações', '069':'Sem informações', '070':'Sem informações', '071':'Sem informações', '072':'Sem informações', '073':'Sem informações', '074':'Sem informações', '075':'Sem informações', '076':'Sem informações', '077':'Sem informações', '078':'Sem informações', '079':'Sem informações', '080':'Sem informações', '081':'Japão', '082':'Coréia do Sul', '083':'Sem informações', '084':'Vietnã', '085':'Sem informações', '086':'China', '087':'Sem informações', '088':'Sem informações', '089':'Sem informações', '090':'Turquia', '091':'Índia', '092':'Paquistão', '093':'Afeganistão', '094':'Sri Lanka', '095':'Myanmar', '096':'Sem informações', '097':'Sem informações', '098':'Irã', '099':'Sem informações', '100':'Sem informações', '101':'Sem informações', '102':'Sem informações', '103':'Sem informações', '104':'Sem informações', '105':'Sem informações', '106':'Sem informações', '107':'Sem informações', '108':'Sem informações', '109':'Sem informações', '110':'Sem informações', '111':'Sem informações', '112':'Sem informações', '113':'Sem informações', '114':'Sem informações', '115':'Sem informações', '116':'Sem informações', '117':'Sem informações', '118':'Sem informações', '119':'Sem informações', '120':'Sem informações', '121':'Sem informações', '122':'Sem informações', '123':'Sem informações', '124':'Sem informações', '125':'Sem informações', '126':'Sem informações', '127':'Sem informações', '128':'Sem informações', '129':'Sem informações', '130':'Sem informações', '131':'Sem informações', '132':'Sem informações', '133':'Sem informações', '134':'Sem informações', '135':'Sem informações', '136':'Sem informações', '137':'Sem informações', '138':'Sem informações', '139':'Sem informações', '140':'Sem informações', '141':'Sem informações', '142':'Sem informações', '143':'Sem informações', '144':'Sem informações', '145':'Sem informações', '146':'Sem informações', '147':'Sem informações', '148':'Sem informações', '149':'Sem informações', '150':'Sem informações', '151':'Sem informações', '152':'Sem informações', '153':'Sem informações', '154':'Sem informações', '155':'Sem informações', '156':'Sem informações', '157':'Sem informações', '158':'Sem informações', '159':'Sem informações', '160':'Sem informações', '161':'Sem informações', '162':'Sem informações', '163':'Sem informações', '164':'Sem informações', '165':'Sem informações', '166':'Sem informações', '167':'Sem informações', '168':'Sem informações', '169':'Sem informações', '170':'Sem informações', '171':'Sem informações', '172':'Sem informações', '173':'Sem informações', '174':'Sem informações', '175':'Sem informações', '176':'Sem informações', '177':'Sem informações', '178':'Sem informações', '179':'Sem informações', '180':'Sem informações', '181':'Sem informações', '182':'Sem informações', '183':'Sem informações', '184':'Sem informações', '185':'Sem informações', '186':'Sem informações', '187':'Sem informações', '188':'Sem informações', '189':'Sem informações', '190':'Sem informações', '191':'Sem informações', '192':'Sem informações', '193':'Sem informações', '194':'Sem informações', '195':'Sem informações', '196':'Sem informações', '197':'Sem informações', '198':'Sem informações', '199':'Sem informações', '200':'Sem informações', '201':'Sem informações', '202':'Sem informações', '203':'Sem informações', '204':'Sem informações', '205':'Sem informações', '206':'Sem informações', '207':'Sem informações', '208':'Sem informações', '209':'Sem informações', '210':'Sem informações', '211':'Sem informações', '212':'Marrocos', '213':'Argélia', '214':'Sem informações', '215':'Sem informações', '216':'Tunísia', '217':'Sem informações', '218':'Líbia', '219':'Sem informações', '220':'Gâmbia', '221':'Senegal', '222':'Mauritânia', '223':'Mali', '224':'Guiné', '225':'Costa do Marfim', '226':'Burkina Faso', '227':'Níger', '228':'Togo', '229':'Benim', '230':'Maurício', '231':'Libéria', '232':'Serra Leoa', '233':'Gana', '234':'Nigéria', '235':'Chade', '236':'República Centro-Africana', '237':'Camarões', '238':'Cabo Verde', '239':'São Tomé e Príncipe', '240':'Guiné Equatorial', '241':'Gabão', '242':'Congo-Brazzaville', '243':'Congo-Kinshasa', '244':'Angola', '245':'Guiné-Bissau', '246':'Território Britânico do Oceano Índico', '247':'Ascensão', '248':'Seicheles', '249':'Sudão', '250':'Ruanda', '251':'Etiópia', '252':'Somália', '253':'Djibuti', '254':'Quênia', '255':'Tanzânia', '256':'Uganda', '257':'Burundi', '258':'Moçambique', '259':'Sem informações', '260':'Zâmbia', '261':'Madagascar', '262':'Reunião', '263':'Zimbábue', '264':'Namíbia', '265':'Malawi', '266':'Lesoto', '267':'Botsuana', '268':'Suazilândia', '269':'Comores, Mayotte', '270':'Sem informações', '271':'Sem informações', '272':'Sem informações', '273':'Sem informações', '274':'Sem informações', '275':'Sem informações', '276':'Sem informações', '277':'Sem informações', '278':'Sem informações', '279':'Sem informações', '280':'Sem informações', '281':'Sem informações', '282':'Sem informações', '283':'Sem informações', '284':'Sem informações', '285':'Sem informações', '286':'Sem informações', '287':'Sem informações', '288':'Sem informações', '289':'Sem informações', '290':'Santa Helena', '291':'Eritréia', '292':'Sem informações', '293':'Sem informações', '294':'Sem informações', '295':'Sem informações', '296':'Sem informações', '297':'Aruba', '298':'Ilhas Faroé', '299':'Groenlândia', '300':'Sem informações', '301':'Sem informações', '302':'Sem informações', '303':'Sem informações', '304':'Sem informações', '305':'Sem informações', '306':'Sem informações', '307':'Sem informações', '308':'Sem informações', '309':'Sem informações', '310':'Sem informações', '311':'Sem informações', '312':'Sem informações', '313':'Sem informações', '314':'Sem informações', '315':'Sem informações', '316':'Sem informações', '317':'Sem informações', '318':'Sem informações', '319':'Sem informações', '320':'Sem informações', '321':'Sem informações', '322':'Sem informações', '323':'Sem informações', '324':'Sem informações', '325':'Sem informações', '326':'Sem informações', '327':'Sem informações', '328':'Sem informações', '329':'Sem informações', '330':'Sem informações', '331':'Sem informações', '332':'Sem informações', '333':'Sem informações', '334':'Sem informações', '335':'Sem informações', '336':'Sem informações', '337':'Sem informações', '338':'Sem informações', '339':'Sem informações', '340':'Sem informações', '341':'Sem informações', '342':'Sem informações', '343':'Sem informações', '344':'Sem informações', '345':'Sem informações', '346':'Sem informações', '347':'Sem informações', '348':'Sem informações', '349':'Sem informações', '350':'Gibraltar', '351':'Portugal', '352':'Luxemburgo', '353':'Irlanda', '354':'Islândia', '355':'Albânia', '356':'Malta', '357':'Chipre', '358':'Finlândia', '359':'Bulgária', '360':'Sem informações', '361':'Sem informações', '362':'Sem informações', '363':'Sem informações', '364':'Sem informações', '365':'Sem informações', '366':'Sem informações', '367':'Sem informações', '368':'Sem informações', '369':'Sem informações', '370':'Lituânia', '371':'Letônia', '372':'Estônia', '373':'Moldávia', '374':'Armênia', '375':'Bielorrússia', '376':'Andorra', '377':'Mônaco', '378':'São Marinho', '379':'Vaticano', '380':'Ucrânia', '381':'Sérvia e Montenegro', '382':'Sem informações', '383':'Sem informações', '384':'Sem informações', '385':'Croácia', '386':'Eslovénia', '387':'Bósnia e Herzegovina', '388':'Sem informações', '389':'Macedônia', '390':'Sem informações', '391':'Sem informações', '392':'Sem informações', '393':'Sem informações', '394':'Sem informações', '395':'Sem informações', '396':'Sem informações', '397':'Sem informações', '398':'Sem informações', '399':'Sem informações', '400':'Sem informações', '401':'Sem informações', '402':'Sem informações', '403':'Sem informações', '404':'Sem informações', '405':'Sem informações', '406':'Sem informações', '407':'Sem informações', '408':'Sem informações', '409':'Sem informações', '410':'Sem informações', '411':'Sem informações', '412':'Sem informações', '413':'Sem informações', '414':'Sem informações', '415':'Sem informações', '416':'Sem informações', '417':'Sem informações', '418':'Sem informações', '419':'Sem informações', '420':'República Tcheca', '421':'Eslováquia', '422':'Sem informações', '423':'Liechtenstein', '424':'Sem informações', '425':'Sem informações', '426':'Sem informações', '427':'Sem informações', '428':'Sem informações', '429':'Sem informações', '430':'Sem informações', '431':'Sem informações', '432':'Sem informações', '433':'Sem informações', '434':'Sem informações', '435':'Sem informações', '436':'Sem informações', '437':'Sem informações', '438':'Sem informações', '439':'Sem informações', '440':'Sem informações', '441':'Sem informações', '442':'Sem informações', '443':'Sem informações', '444':'Sem informações', '445':'Sem informações', '446':'Sem informações', '447':'Sem informações', '448':'Sem informações', '449':'Sem informações', '450':'Sem informações', '451':'Sem informações', '452':'Sem informações', '453':'Sem informações', '454':'Sem informações', '455':'Sem informações', '456':'Sem informações', '457':'Sem informações', '458':'Sem informações', '459':'Sem informações', '460':'Sem informações', '461':'Sem informações', '462':'Sem informações', '463':'Sem informações', '464':'Sem informações', '465':'Sem informações', '466':'Sem informações', '467':'Sem informações', '468':'Sem informações', '469':'Sem informações', '470':'Sem informações', '471':'Sem informações', '472':'Sem informações', '473':'Grenada', '474':'Sem informações', '475':'Sem informações', '476':'Sem informações', '477':'Sem informações', '478':'Sem informações', '479':'Sem informações', '480':'Sem informações', '481':'Sem informações', '482':'Sem informações', '483':'Sem informações', '484':'Sem informações', '485':'Sem informações', '486':'Sem informações', '487':'Sem informações', '488':'Sem informações', '489':'Sem informações', '490':'Sem informações', '491':'Sem informações', '492':'Sem informações', '493':'Sem informações', '494':'Sem informações', '495':'Sem informações', '496':'Sem informações', '497':'Sem informações', '498':'Sem informações', '499':'Sem informações', '500':'Ilhas Malvinas', '501':'Belize', '502':'Guatemala', '503':'El Salvador', '504':'Honduras', '505':'Nicarágua', '506':'Costa Rica', '507':'Panamá', '508':'São Pedro e Miquelon', '509':'Haiti', '510':'Sem informações', '511':'Sem informações', '512':'Sem informações', '513':'Sem informações', '514':'Sem informações', '515':'Sem informações', '516':'Sem informações', '517':'Sem informações', '518':'Sem informações', '519':'Sem informações', '520':'Sem informações', '521':'Sem informações', '522':'Sem informações', '523':'Sem informações', '524':'Sem informações', '525':'Sem informações', '526':'Sem informações', '527':'Sem informações', '528':'Sem informações', '529':'Sem informações', '530':'Sem informações', '531':'Sem informações', '532':'Sem informações', '533':'Sem informações', '534':'Sem informações', '535':'Sem informações', '536':'Sem informações', '537':'Sem informações', '538':'Sem informações', '539':'Sem informações', '540':'Sem informações', '541':'Sem informações', '542':'Sem informações', '543':'Sem informações', '544':'Sem informações', '545':'Sem informações', '546':'Sem informações', '547':'Sem informações', '548':'Sem informações', '549':'Sem informações', '550':'Sem informações', '551':'Sem informações', '552':'Sem informações', '553':'Sem informações', '554':'Sem informações', '555':'Sem informações', '556':'Sem informações', '557':'Sem informações', '558':'Sem informações', '559':'Sem informações', '560':'Sem informações', '561':'Sem informações', '562':'Sem informações', '563':'Sem informações', '564':'Sem informações', '565':'Sem informações', '566':'Sem informações', '567':'Sem informações', '568':'Sem informações', '569':'Sem informações', '570':'Sem informações', '571':'Sem informações', '572':'Sem informações', '573':'Sem informações', '574':'Sem informações', '575':'Sem informações', '576':'Sem informações', '577':'Sem informações', '578':'Sem informações', '579':'Sem informações', '580':'Sem informações', '581':'Sem informações', '582':'Sem informações', '583':'Sem informações', '584':'Sem informações', '585':'Sem informações', '586':'Sem informações', '587':'Sem informações', '588':'Sem informações', '589':'Sem informações', '590':'Guadalupe, Saint-Martin (French West Indies)', '591':'Bolívia', '592':'Guiana', '593':'Equador', '594':'Guiana Francesa', '595':'Paraguai', '596':'Martinica', '597':'Suriname', '598':'Uruguai', '599':'Sint Maarten (Antilhas Holandesas)', '600':'Sem informações', '601':'Sem informações', '602':'Sem informações', '603':'Sem informações', '604':'Sem informações', '605':'Sem informações', '606':'Sem informações', '607':'Sem informações', '608':'Sem informações', '609':'Sem informações', '610':'Sem informações', '611':'Sem informações', '612':'Sem informações', '613':'Sem informações', '614':'Sem informações', '615':'Sem informações', '616':'Sem informações', '617':'Sem informações', '618':'Sem informações', '619':'Sem informações', '620':'Sem informações', '621':'Sem informações', '622':'Sem informações', '623':'Sem informações', '624':'Sem informações', '625':'Sem informações', '626':'Sem informações', '627':'Sem informações', '628':'Sem informações', '629':'Sem informações', '630':'Sem informações', '631':'Sem informações', '632':'Sem informações', '633':'Sem informações', '634':'Sem informações', '635':'Sem informações', '636':'Sem informações', '637':'Sem informações', '638':'Sem informações', '639':'Sem informações', '640':'Sem informações', '641':'Sem informações', '642':'Sem informações', '643':'Sem informações', '644':'Sem informações', '645':'Sem informações', '646':'Sem informações', '647':'Sem informações', '648':'Sem informações', '649':'Sem informações', '650':'Sem informações', '651':'Sem informações', '652':'Sem informações', '653':'Sem informações', '654':'Sem informações', '655':'Sem informações', '656':'Sem informações', '657':'Sem informações', '658':'Sem informações', '659':'Sem informações', '660':'Sem informações', '661':'Sem informações', '662':'Sem informações', '663':'Sem informações', '664':'Sem informações', '665':'Sem informações', '666':'This forgotten throne (My dark journal)', '667':'Sem informações', '668':'Sem informações', '669':'Sem informações', '670':'Timor-Leste', '671':'Guam', '672':'Territórios Externos Australianos', '673':'Brunei', '674':'Nauru', '675':'Papua-Nova Guiné', '676':'Tonga', '677':'Ilhas Salomão', '678':'Vanuatu', '679':'Fiji', '680':'Palau', '681':'Wallis e Futuna', '682':'Ilhas Cook', '683':'Ilha Niue', '684':'Sem informações', '685':'Samoa', '686':'Kiribati', '687':'Nova Caledônia', '688':'Tuvalu', '689':'Polinésia Francesa', '690':'Tokelau', '691':'Micronésia', '692':'Ilhas Marshall', '693':'Sem informações', '694':'Sem informações', '695':'Sem informações', '696':'Sem informações', '697':'Sem informações', '698':'Sem informações', '699':'Sem informações', '700':'Sem informações', '701':'Sem informações', '702':'Sem informações', '703':'Sem informações', '704':'Sem informações', '705':'Sem informações', '706':'Sem informações', '707':'Sem informações', '708':'Sem informações', '709':'Sem informações', '710':'Sem informações', '711':'Sem informações', '712':'Sem informações', '713':'Sem informações', '714':'Sem informações', '715':'Sem informações', '716':'Sem informações', '717':'Sem informações', '718':'Sem informações', '719':'Sem informações', '720':'Sem informações', '721':'Sem informações', '722':'Sem informações', '723':'Sem informações', '724':'Sem informações', '725':'Sem informações', '726':'Sem informações', '727':'Sem informações', '728':'Sem informações', '729':'Sem informações', '730':'Sem informações', '731':'Sem informações', '732':'Sem informações', '733':'Sem informações', '734':'Sem informações', '735':'Sem informações', '736':'Sem informações', '737':'Sem informações', '738':'Sem informações', '739':'Sem informações', '740':'Sem informações', '741':'Sem informações', '742':'Sem informações', '743':'Sem informações', '744':'Sem informações', '745':'Sem informações', '746':'Sem informações', '747':'Sem informações', '748':'Sem informações', '749':'Sem informações', '750':'Sem informações', '751':'Sem informações', '752':'Sem informações', '753':'Sem informações', '754':'Sem informações', '755':'Sem informações', '756':'Sem informações', '757':'Sem informações', '758':'Sem informações', '759':'Sem informações', '760':'Sem informações', '761':'Sem informações', '762':'Sem informações', '763':'Sem informações', '764':'Sem informações', '765':'Sem informações', '766':'Sem informações', '767':'Sem informações', '768':'Sem informações', '769':'Sem informações', '770':'Sem informações', '771':'Sem informações', '772':'Sem informações', '773':'Sem informações', '774':'Sem informações', '775':'Sem informações', '776':'Sem informações', '777':'Sem informações', '778':'Sem informações', '779':'Sem informações', '780':'Sem informações', '781':'Sem informações', '782':'Sem informações', '783':'Sem informações', '784':'Sem informações', '785':'Sem informações', '786':'Sem informações', '787':'Sem informações', '788':'Sem informações', '789':'Sem informações', '790':'Sem informações', '791':'Sem informações', '792':'Sem informações', '793':'Sem informações', '794':'Sem informações', '795':'Sem informações', '796':'Sem informações', '797':'Sem informações', '798':'Sem informações', '799':'Sem informações', '800':'Sem informações', '801':'Sem informações', '802':'Sem informações', '803':'Sem informações', '804':'Sem informações', '805':'Sem informações', '806':'Sem informações', '807':'Sem informações', '808':'Sem informações', '809':'Sem informações', '810':'Sem informações', '811':'Sem informações', '812':'Sem informações', '813':'Sem informações', '814':'Sem informações', '815':'Sem informações', '816':'Sem informações', '817':'Sem informações', '818':'Sem informações', '819':'Sem informações', '820':'Sem informações', '821':'Sem informações', '822':'Sem informações', '823':'Sem informações', '824':'Sem informações', '825':'Sem informações', '826':'Sem informações', '827':'Sem informações', '828':'Sem informações', '829':'Sem informações', '830':'Sem informações', '831':'Sem informações', '832':'Sem informações', '833':'Sem informações', '834':'Sem informações', '835':'Sem informações', '836':'Sem informações', '837':'Sem informações', '838':'Sem informações', '839':'Sem informações', '840':'Sem informações', '841':'Sem informações', '842':'Sem informações', '843':'Sem informações', '844':'Sem informações', '845':'Sem informações', '846':'Sem informações', '847':'Sem informações', '848':'Sem informações', '849':'Sem informações', '850':'Coréia do Norte', '851':'Sem informações', '852':'Hong Kong', '853':'Macau', '854':'Sem informações', '855':'Camboja', '856':'Laos', '857':'Sem informações', '858':'Sem informações', '859':'Sem informações', '860':'Sem informações', '861':'Sem informações', '862':'Sem informações', '863':'Sem informações', '864':'Sem informações', '865':'Sem informações', '866':'Sem informações', '867':'Sem informações', '868':'Sem informações', '869':'Sem informações', '870':'Sem informações', '871':'Sem informações', '872':'Sem informações', '873':'Sem informações', '874':'Sem informações', '875':'Sem informações', '876':'Sem informações', '877':'Sem informações', '878':'Sem informações', '879':'Sem informações', '880':'Bangladesh', '881':'Sem informações', '882':'Sem informações', '883':'Sem informações', '884':'Sem informações', '885':'Sem informações', '886':'Taiwan', '887':'Sem informações', '888':'Sem informações', '889':'Sem informações', '890':'Sem informações', '891':'Sem informações', '892':'Sem informações', '893':'Sem informações', '894':'Sem informações', '895':'Sem informações', '896':'Sem informações', '897':'Sem informações', '898':'Sem informações', '899':'Sem informações', '900':'Sem informações', '901':'Sem informações', '902':'Sem informações', '903':'Sem informações', '904':'Sem informações', '905':'Sem informações', '906':'Sem informações', '907':'Sem informações', '908':'Sem informações', '909':'Sem informações', '910':'Sem informações', '911':'Sem informações', '912':'Sem informações', '913':'Sem informações', '914':'Sem informações', '915':'Sem informações', '916':'Sem informações', '917':'Sem informações', '918':'Sem informações', '919':'Sem informações', '920':'Sem informações', '921':'Sem informações', '922':'Sem informações', '923':'Sem informações', '924':'Sem informações', '925':'Sem informações', '926':'Sem informações', '927':'Sem informações', '928':'Sem informações', '929':'Sem informações', '930':'Sem informações', '931':'Sem informações', '932':'Sem informações', '933':'Sem informações', '934':'Sem informações', '935':'Sem informações', '936':'Sem informações', '937':'Sem informações', '938':'Sem informações', '939':'Sem informações', '940':'Sem informações', '941':'Sem informações', '942':'Sem informações', '943':'Sem informações', '944':'Sem informações', '945':'Sem informações', '946':'Sem informações', '947':'Sem informações', '948':'Sem informações', '949':'Sem informações', '950':'Sem informações', '951':'Sem informações', '952':'Sem informações', '953':'Sem informações', '954':'Sem informações', '955':'Sem informações', '956':'Sem informações', '957':'Sem informações', '958':'Sem informações', '959':'Sem informações', '960':'Ilhas Maldivas', '961':'Líbano', '962':'Jordânia', '963':'Síria', '964':'Iraque', '965':'Kuwait', '966':'Arábia Saudita', '967':'Iêmen', '968':'Omã', '969':'Sem informações', '970':'Palestina', '971':'Emirados Árabes Unidos', '972':'Israel', '973':'Bahrein', '974':'Qatar', '975':'Butão', '976':'Mongólia', '977':'Nepal', '978':'Sem informações', '979':'Sem informações', '980':'Sem informações', '981':'Sem informações', '982':'Sem informações', '983':'Sem informações', '984':'Sem informações', '985':'Sem informações', '986':'Sem informações', '987':'Sem informações', '988':'Sem informações', '989':'Sem informações', '990':'Sem informações', '991':'Sem informações', '992':'Tadjiquistão', '993':'Turquemenistão', '994':'Azerbaijão', '995':'Geórgia', '996':'Quirguistão', '997':'Sem informações', '998':'Uzbequistão', '999':'Sem informações'}

ddd_siglas = {'11':'SP', '12':'SP', '13':'SP', '14':'SP', '15':'SP', '16':'SP', '17':'SP', '18':'SP', '19':'SP', '21':'RJ', '22':'RJ', '24':'RJ', '27':'ES', '28':'ES', '31':'MG', '32':'MG', '33':'MG', '34':'MG', '35':'MG', '37':'MG', '38':'MG', '41':'PR', '42':'PR', '43':'PR', '44':'PR', '45':'PR', '46':'PR', '47':'SC', '48':'SC', '49':'SC', '51':'RS', '53':'RS', '54':'RS', '55':'RS', '61':'DF', '62':'GO', '63':'TO', '64':'GO', '65':'MT', '66':'MT', '67':'MS', '68':'AC', '69':'RO', '71':'BA', '73':'BA', '74':'BA', '75':'BA', '77':'BA', '79':'SE', '81':'PE', '82':'AL', '83':'PB', '84':'RN', '85':'CE', '86':'PI', '87':'PE', '88':'CE', '89':'PI', '91':'PA', '92':'AM', '93':'PA', '94':'PA', '95':'RR', '96':'AP', '97':'AM', '98':'MA', '99':'MA'}

siglas_estados = {'AC':'Acre', 'AL':'Alagoas', 'AP':'Amapá', 'AM':'Amazonas', 'BA':'Bahia', 'CE':'Ceará', 'DF':'Distrito Federal', 'ES':'Espírito Santo', 'GO':'Goiás', 'MA':'Maranhão', 'MT':'Mato Grosso', 'MS':'Mato Grosso Do Sul', 'MG':'Minas Gerais', 'PA':'Pará', 'PB':'Paraíba', 'PR':'Paraná', 'PE':'Pernambuco', 'PI':'Piauí', 'RJ':'Rio de Janeiro', 'RN':'Rio Grande Do Norte', 'RS':'Rio Grande Do Sul', 'RO':'Rondônia', 'RR':'Roraima', 'SC':'Santa Catarina', 'SP':'São Paulo', 'SE':'Sergipe', 'TO':'Tocantins'}


def main():
    clear()
    links()
    clear()
    func = {1:banco, 2:bin, 3:cep, 4:cnpj, 5:covid19, 6:ddd, 7:ddi, 8:ip, 9:geradorCnpj, 10:geradorCpf, 11:geradorPessoas, 12:validadorCnpj, 13:validadorCpf, 14:validadorRg}
    while True:
        bannerMenu()
        option = input('\n\033[1;34m ===> \033[1;36m').strip()
        if readInput(option, 'empty'): continue
        if option.lower() == 'q': return 0
        if readInput(option, 'numeric') != True: continue
        if int(option) == 99 or int(option) == 0: return 0
        if int(option) > 13:
            print(' option invalida!')
            time.sleep(1)
            continue
        str(func[int(option)]())


def sair():
    banner()
    print('\033[1;34m Obrigado por usar o painel Clownters\n Telegram: @Clownters\n YouTube: @Clownters1')
    exit()


def clear():
    if platform.system() == 'Windows': os.system('cls')
    else: os.system('clear')


def links():
    if platform.system() == 'Linux':
        os.system  ('xdg-open https://instagram.com/mike90s15 &>/dev/null; clear')
        time.sleep(5)
        os.system('xdg-open https://twitter.com/mike90s15 &>/dev/null; clear')
        time.sleep(5)
        os.system('xdg-open https://github.com/mike90s15 &>/dev/null; clear')
        time.sleep(5)
    else:
        webbrowser.open('https://instagram.com/mike90s15')
        time.sleep(5)
        webbrowser.open('https://twitter.com/mike90s15')
        time.sleep(5)
        webbrowser.open('https://github.com/mike90s15')


def banner():
    clear()
    banner = ["\n \033[1;33m" ".--------.____________", "|| ° ° ° °     .2021.|| \033[1;32m®\033[1;33m", "||                    | \033[1;32m©\033[1;33m", "||\     ______________________", "|| \   // ° ° ° ° ° ° ° ° ° °/", "||\ \ //                    /", "|| \ //                    /", "||\ //                    /", "|| //                    /", "||//                    /", "||/                    /", "|/____________________/", "\033[1;31mArquivo Clownters \033[m\n", "\033[1;35m<<<   PAINEL CLOWNTERS " + str(datetime.date.today()) + "   >>>", "\033[1;32m=======================================\n"]
    for i in banner:
        print('', i)
        time.sleep(0.01)


def bannerMenu():
    banner()
    #banner_menu = ['Buscas', 'Geradores', 'Moedas', 'Validadores', 'Calculos', 'cep']
    banner_menu = ['Consulta de Banco', 'Consulta de Bin', 'Consulta de CEP', 'Consulta de CNPJ', 'Consulta de Covid19', 'Consulta de IP', 'Consulta de DDD', 'Consulta de DDI']
    geradores = ['Gerador de CPF', 'Gerador de CNPJ', 'Gerador de Pessoas']
    validadores = ['Validador de CNPJ', 'Validador de CPF', 'Validador de RG']
    banner_menu = banner_menu + geradores + validadores
    a = 0
    for i in sorted(banner_menu):
        a += 1
        if a < 10: b = '0' + str(a)
        else: b = a
        print(f' \033[1;32m[\033[m\033[1;36m{b}\033[1;32m]\033[m \033[1;36m{str(i): <19}   \033[1;32m]\033[m\033[1;32m      (+_+)')
    print('\n \033[1;32m[\033[m\033[1;31m99\033[1;32m]\033[m \033[1;36mSair\t\t    \033[1;32m]\033[m\033[1;32m      (+_+)')
    

def readInput(x, typ):
    match  typ:
        case 'numeric':
            if x.isnumeric(): return True
            else: print('\033[1;33m Digite apenas números!')
            time.sleep(2)
        case 'isalpha':
            if x.isalpha(): return True
            else: print('\033[1;33m Digite apenas letras!')
            time.sleep(2)
        case 'isalnum':
            if x.isalnum(): return True
            else: print('\033[1;33m Digite apenas números e letras!')
            time.sleep(2)
        case 'empty':
            if len(x) == 0 or x.isspace():
                print('\033[1;33m Digite alguma coisa!')
                time.sleep(2)
                return True
        case other: return False


def retorneMenu():
    lst = ['Continue', 'Retorne para o menu', 'Sair do menu']
    print('\n\033[1;32m', '=' * 39, '\n\n\033[1;34m Continue ou retornar ao menu principal?\n')
    a = 0
    for i in lst:
        a += 1
        if a == 3: a = 00
        print(f' \033[1;32m[\033[m\033[1;36m0{a}\033[1;32m]\033[m \033[1;36m{str(i): <19.19}    \033[1;32m]\033[m\033[1;32m     (+_+)')
        time.sleep(0.01)
    input_user = input('\n\033[1;34m ===> \033[1;36m').strip()
    if input_user.replace(' ', '') == '': return False
    elif input_user.lower() == 'q': return True
    elif input_user.isnumeric() == False: return False
    if int(input_user) == 0: exit()
    elif int(input_user) == 2: return True


def myReplace(x):
    var = '"\'!@#$%¨&*()_+-´`{[]}^~?/:;<>.,|\\'
    for i in var:
        x = x.replace(i, '')
    return x
        

# Funções de busca
def banco():
    while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;34m Informe o codigo para a consulta\n ===> \033[1;36m').strip()
            if input_user == '99' or input_user.lower() == 'q': return True
            if readInput(input_user, 'empty'): continue
            if readInput(input_user, 'numeric') != True: continue
            break             
        req = requests.get(f'https://brasilapi.com.br/api/banks/v1/{input_user}').json()
        print('')
        for i in req.keys():
            print(f'\033[1;34m  •{i.capitalize(): <8}:\033[0;32m {str(req[i])}')
            time.sleep(0.01)
        if retorneMenu() == True: return True
    

def bin():
    while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;34m Informe o bin para a consulta\n ===> \033[1;36m').strip()
            if input_user == '99' or input_user.lower() == 'q': return True
            if readInput(input_user, 'empty'): continue
            if readInput(input_user, 'numeric') != True: continue
            break 
        req = requests.get(f'https://lookup.binlist.net/{input_user}').json()
        print()
        for i in req.keys():
            print(f'\033[1;34m  •{i.capitalize(): <7}:\033[0;32m {str(req[i])}')
            time.sleep(0.01)
        if retorneMenu() == True: return True
 

def cep():
    while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;34m Informe o CEP para a consulta\n ===> \033[1;36m').strip().replace('-', '')
            if input_user == '99' or input_user.lower() == 'q': return True
            if readInput(input_user, 'empty'): continue
            if readInput(input_user, 'numeric') != True: continue
            if len(input_user) != 8:
                print('\033[1;33m O cep é formado por 8 digitos númerico!')
                time.sleep(2)
                continue
            break               
        req = requests.get(f'https://viacep.com.br/ws/{input_user}/json/').json()
        print('')
        for i in req.keys():
            print(f'\033[1;34m  •{i.capitalize(): <11}:\033[0;32m {str(req[i])}')
            time.sleep(0.01)
        if retorneMenu() == True: return True


def cnpj():
    while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;34m Informe o CNPJ para a consulta\n ===> \033[1;36m').strip().replace('.', '').replace('-', '').replace('/', '')
            print(input_user)
            if input_user == '99' or input_user.lower() == 'q': return True
            if readInput(input_user, 'empty'): continue
            if readInput(input_user, 'numeric') != True: continue
            if len(input_user) != 14:
                print('\033[1;33m O cep é formado por 8 digitos númerico!')
                time.sleep(2)
                continue
            break               
        req = requests.get(f'https://brasilapi.com.br/api/cnpj/v1/${input_user}').json()
        print('')
        for i in req.keys():
            print(f'\033[1;34m  •{i.capitalize(): <11}:\033[0;32m {str(req[i])}')
            time.sleep(0.01)
        if retorneMenu() == True: return True
    

def covid19():
    while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;34m Informe a sigla do estado para a consulta\n ===> \033[1;36m').strip()
            if input_user == '99' or input_user.lower() == 'q': return True
            if readInput(input_user, 'empty'): continue
            if readInput(input_user, 'isalpha') != True: continue
            break 
        req = requests.get(f'https://covid19-brazil-api.vercel.app/api/report/v1/brazil/uf/{input_user}').json()
        print()
        for i in req.keys():
            print(f'\033[1;34m  •{i.capitalize(): <8}:\033[0;32m {str(req[i])}')
            time.sleep(0.01)
        if retorneMenu() == True: return True


def ddd():
    while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;34m Informe o DDD para a consulta\n ===> \033[1;36m').strip().replace('0', '')
            if input_user == '99' or input_user.lower() == 'q': return True
            if readInput(input_user, 'empty'): continue
            if readInput(input_user, 'numeric') != True: continue
            if len(input_user) != 2:
                print('\033[1;33m O número não corresponde ao um DDD existente!')
                time.sleep(2)
                continue
            break
        req = requests.get(f'https://brasilapi.com.br/api/ddd/v1/{input_user}').json()
        print('')
        for i in req.keys():
            print(f'\033[1;34m  •{i.capitalize(): <6}:\033[0;32m {str(req[i])}')
            time.sleep(0.01)
        if retorneMenu() == True: return True


def ddi():
     while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = myReplace(input('\033[1;34m Informe o DDI para a consulta\n ===> \033[1;36m').strip())
            if input_user == '99' or input_user.lower() == 'q': return True
            if readInput(input_user, 'empty'): continue
            if readInput(input_user, 'numeric') != True: continue
            if len(input_user) > 3:
                print('\033[1;33m O número não corresponde ao um DDI existente!')
                time.sleep(2)
                continue
            elif len(input_user) == 2:
                input_user = '0' + input_user
            elif len(input_user) == 1:
                input_user = '00' + input_user
            break
        print('\n\033[1;34m  •DDI:\033[0;32m +' + input_user.replace('0', ''))
        if ',' in ddi_d[input_user]:
            print('\033[1;34m  •Países:\033[0;32m', end='')
        else:
            print('\033[1;34m  •País:\033[0;32m', end='')
        a = 1
        for i in ddi_d[input_user].split(','):
            if a == 1:
                print(f' {i}')
            else:
                print(f'   {i}')
            a = 0
            time.sleep(0.01)
        if retorneMenu() == True: return True
        # for dois nomes coloca o "e" em vez de pula a linha e definir as cores


def ip():
    while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;34m Informe o ip para a consulta\n ===> \033[1;36m').strip()
            if input_user == '99' or input_user.lower() == 'q': return True
            if readInput(input_user, 'empty'): continue
            '''
            for i in range(0, len(input_user)):
                if input_user[i] == '.':
                    if int(input_user[0:i-4]) > 255:
                        print('\033[1;33m O IP informado é falso!')
                        time.sleep(2)
            '''
            #if readInput(input_user, 'numeric') != True: continue
            break
        req = requests.get(f'http://ip-api.com/json/{input_user}').json()
        print('')
        for i in req.keys():
            print(f'\033[1;34m  •{i.capitalize(): <11}:\033[0;32m {str(req[i])}')
            time.sleep(0.01)
        if retorneMenu() == True: return True
        # verifica se o ip é valido . 255


def telefone():
    while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;34m Informe o telefone para a consulta\n ===> \033[1;36m').strip()
            if input_user == '99' or input_user.lower() == 'q': return True
            if readInput(input_user, 'empty'): continue
            break 
        #if len(input_user) == 11 or len(input_user) == 10:
        print(f'''
  •Telefone: +{input_user[0:2]} ({input_user[2:4]}) {input_user[4:9]}-{input_user[9::]}
  •DDI: {input_user[0:2]}
  •DDD: {input_user[2:4]}
  •Pais: Brasil
  •Codigo do pais: BR
  •Estado: São Paulo
  •Codigo da Estado: SP
  •Operadora: Claro
  •Região: Região Sudeste
  •CPF: 
  •RG: ××.×××.×××-×
  •Consulta By: Clownters
  •Usuario: mike
''')
        break


# Funções de geredores
def geradorCpf():
    while True:
        banner()
        soma = 0
        var = ''
        for i in range(0, 8): var = var + str(random.randint(0, 9))
        var = var + '8'
        #var = '435231910'
        num = 11
        for i in range(0, 9):
            num -= 1
            soma += int(var[i:i+1]) * num
        if (soma % 11) < 2: soma = 0
        else: soma = 11 - (soma % 11)
        var = var + str(soma)
        soma = 0
        num = 11
        for i in range(0, 10):
            soma += int(var[i:i+1]) * num
            num -= 1
        if (soma % 11) < 2: soma = 0
        else: soma = 11 - (soma % 11)
        var = var + str(soma)
        print(f'\033[1;34m CPF gerado:\033[0;32m {var}\n\033[1;34m CPF gerado:\033[0;32m {var[0:3]}.{var[3:6]}.{var[6:9]}-{var[9:]}')
        if retorneMenu() == True: return True


def geradorCnpj():
    while True:
        banner()
        var = ''
        soma = 0
        for i in range(0, 8):
            var = var + str(random.randint(0,9))
        var = var + '0001'
        num = 6
        for i in range(0, 12):
            num -= 1
            if num < 2: num = 9
            soma += int(var[i:i+1]) * num
        if (soma % 11) < 2: var = var + '0'
        else: var = var + str(11 - (soma % 11))
        soma = 0 
        num = 6
        for i in range(0, 13):
            soma += int(var[i:i+1]) * num
            num -= 1
            if num < 2: num = 9
        if (soma % 11) < 2: var = var + '0'
        else: var = var + str(11 - (soma % 11))
        print(f'\033[1;34m CNPJ gerado:\033[0;32m {var}\n\033[1;34m CNPJ gerado:\033[0;32m {var[0:2]}.{var[2:5]}.{var[5:8]}/{var[8:12]}-{var[12:]}')
        if retorneMenu() == True: return True


def geradorPessoas():
    while True:
        banner()
        req = requests.get(f'https://randomuser.me/API/?nat=BR').json()
        print(req['results'].replace('[', '')) #.replace('[', ''))
        for i in req.keys():
            print(f'\033[1;34m  •{i.capitalize(): <8}:\033[0;32m {str(req[i])}')
            time.sleep(0.01)
        break
        #if retorneMenu() == True: return True


def geradorEmail():
    nomes_f = ['Miguel', 'Arthur', 'Gael', 'Théo', 'Heitor', 'Ravi', 'Davi', 'Bernardo', 'Noah', 'Gabriel', 'Samuel', 'Pedro', 'Anthony', 'Isaac', 'Benício', 'Benjamin', 'Matheus', 'Lucas', 'Joaquim', 'Nicolas', 'Lucca', 'Lorenzo', 'Henrique', 'João', 'Miguel', 'Rafael', 'Henry', 'Murilo', 'Levi', 'Guilherme', 'Vicente', 'Felipe', 'Bryan', 'Matteo', 'Bento', 'João', 'Pedro', 'Pietro', 'Leonardo', 'Daniel', 'Gustavo', 'Pedro', 'Henrique', 'João', 'Lucas', 'Emanuel', 'João', 'Caleb', 'Davi', 'Lucca', 'Antônio', 'Eduardo', 'Enrico', 'Caio', 'José', 'Enzo', 'Gabriel', 'Augusto', 'Mathias', 'Vitor', 'Enzo', 'Cauã', 'Francisco', 'Rael', 'João', 'Guilherme', 'Thomas', 'Yuri', 'Yan', 'Anthony', 'Gabriel', 'Oliver', 'Otávio', 'João', 'Gabriel', 'Nathan', 'Davi', 'Lucas', 'Vinícius', 'Theodoro', 'Valentim', 'Ryan', 'Luiz', 'Miguel', 'Arthur', 'Miguel', 'João', 'Vitor', 'Léonovo', 'Ravi', 'Lucca', 'Apollo', 'Thiago', 'Tomás', 'Martin', 'José', 'Miguel', 'Erick', 'Liam', 'Josué', 'Luan', 'Asafe', 'Raul', 'José', 'Pedro', 'Dominic', 'Kauê', 'Kalel', 'Luiz', 'Henrique', 'Dom', 'Davi', 'Miguel', 'Estevão', 'Breno', 'Davi', 'Luiz', 'Thales', 'Israel']
    nomes_m = ['Helena', 'Alice', 'Laura', 'Manuela', 'Sophia', 'Isabella', 'Luísa', 'Heloísa', 'Cecília', 'Maitê', 'Eloá', 'Elisa', 'Liz', 'Júlia', 'Maria', 'Luísa', 'Valentina', 'Maria', 'Alice', 'Lívia', 'Antonella', 'Lorena', 'Ayla', 'Isis', 'Maria', 'Júlia', 'Maya', 'Maria', 'Clara', 'Esther', 'Giovanna', 'Lara', 'Sarah', 'Beatriz', 'Aurora', 'Mariana', 'Maria', 'Cecília', 'Olívia', 'Maria', 'Helena', 'Isadora', 'Luna', 'Catarina', 'Melissa', 'Maria', 'Eduarda', 'Lavínia', '', 'Agatha', '', 'Emanuelly', 'Maria', 'Alícia', 'Rebeca', 'Ana', 'Clara', 'Yasmin', 'Clara', 'Marina', 'Ana', 'Júlia', 'Ana', 'Luísa', 'Isabelly', 'Ana', 'Laura', 'Rafaela', 'Ana', 'Liz', 'Stella', 'Gabriela', 'Vitória', 'Allana', 'Mirella', 'Milena', 'Bella', 'Ana', 'Nicole', 'Emilly', 'Maria', 'Vitória', 'Mariah', 'Clarice', 'Letícia', 'Laís', 'Maria', 'Liz', 'Bianca', 'Melina', 'Jade', 'Ana', 'Beatriz', 'Maria', 'Fernanda', 'Betina', 'Maria', 'Valentina', 'Maria', 'Laura', 'Heloíse', 'Maria', 'Isis', 'Zoe', 'Louise', 'Malu', 'Melinda', 'Ana', 'Cecília', 'Ana', 'Lívia', 'Ana', 'Vitória', 'Maria', 'Heloísa', 'Chloe', 'Maria', 'Flor', 'Pietra', 'Pérola', 'Ana', 'Sophia', 'Maria', 'Elisa', 'Gabrielly', 'Larissa', 'Maria', 'Eloá', 'Eduarda']
    nomes_a = nomes_f + nomes_m
    print(f'Email: {random.choice(nomes_a)}@exemplo.com')

# Validadores
def validadorCartao():
    pass


def validadorCnpj():
    while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;34m Informe o CNPJ para a validação\n ===> \033[1;36m').strip().replace('-', '')
            if input_user == '99' or input_user.lower() == 'q': return True
            if readInput(input_user, 'empty'): continue
            input_user = myReplace(input_user)
            if readInput(input_user, 'numeric') != True: continue
            break
        soma = 0
        num = 6
        cnpj = input_user
        input_user = str(input_user[0:12])
        for i in range(0, 12):
            num -= 1
            if num < 2: num = 9
            soma += int(input_user[i:i+1]) * num
        if (soma % 11) < 2: input_user = input_user + '0'
        else: input_user = input_user + str(11 - (soma % 11))
        soma = 0 
        num = 6
        for i in range(0, 13):
            soma += int(input_user[i:i+1]) * num
            num -= 1
            if num < 2: num = 9
        if (soma % 11) < 2: input_user = input_user + '0'
        else: input_user = input_user + str(11 - (soma % 11))
        if input_user == cnpj:
            print(f'\n\033[1;34m  CNPJ:\033[0;32m {input_user[0:2]}.{input_user[2:5]}.{input_user[5:8]}/{input_user[8:12]}-{input_user[12::]}\033[1;32m válido')
        else:
            print(f'\n\033[1;34m  CNPJ:\033[0;32m {input_user[0:2]}.{input_user[2:5]}.{input_user[5:8]}/{input_user[8:12]}-{input_user[12::]}\033[1;31m inválido')
        if retorneMenu() == True: return True
        # printa a variavel original caso o cnpj seja falso
        # varificar tamanho para evitar erro


def validadorCpf():
      while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;34m Informe o CPF para a validação\n ===> \033[1;36m').strip().replace('-', '')
            if input_user == '99' or input_user.lower() == 'q': return True
            if readInput(input_user, 'empty'): continue
            input_user = myReplace(input_user)
            if readInput(input_user, 'numeric') != True: continue
            break
        soma = 0
        cpf = input_user
        input_user = str(input_user[0:9])
        num = 11
        for i in range(0, 9):
            num -= 1
            soma += int(input_user[i:i+1]) * num
        if (soma % 11) < 2: soma = 0
        else: soma = 11 - (soma % 11)
        input_user = input_user + str(soma)
        soma = 0
        num = 11
        for i in range(0, 10):
            soma += int(input_user[i:i+1]) * num
            num -= 1
        if (soma % 11) < 2: soma = 0
        else: soma = 11 - (soma % 11)
        input_user = input_user + str(soma)
        if input_user == cpf:
            print(f'\n\033[1;34m  CPF:\033[0;32m {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}\033[1;32m válido')
        else: 
            print(f'\n\033[1;34m  CPF:\033[0;32m {cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}\033[1;31m inválido')
        if retorneMenu() == True: return True
        # cria uma função a parte para a logica cpf e valida
        # varificar tamanho para evitar erro


def validadorRg():
    while True:
        for i in range(0, 4):
            if i == 3: return False
            banner()
            input_user = input('\033[1;34m Informe o RG para a validação\n ===> \033[1;36m').strip().replace('-', '')
            if input_user == '99' or input_user.lower() == 'q': return True
            if readInput(input_user, 'empty'): continue
            input_user = myReplace(input_user)
            if len(input_user) != 9: continue
            break
        rg = input_user
        input_user = str(input_user[0:8])
        soma = 0 
        num = 2
        for i in range(0, 8):
            soma += int(input_user[i:i+1]) * num
            num += 1
        if (soma % 11) == 0: soma = 0
        elif (soma % 11) == 1: soma = 'x'
        else: soma = 11 - (soma % 11)
        input_user = input_user + str(soma)
        if input_user == rg:
            print(f'\n\033[1;34m  RG:\033[0;32m {rg[0:2]}.{rg[2:5]}.{rg[5:8]}-{rg[8:]}\033[1;32m válido')
        else: 
            print(f'\n\033[1;34m  RG:\033[0;32m {rg[0:2]}.{rg[2:5]}.{rg[5:8]}-{rg[8:]}\033[1;31m inválido')
        if retorneMenu() == True: return True


if __name__ == '__main__':
    try: 
        main()
        time.sleep(1)
        sair()
    except KeyboardInterrupt:
        print('\n\033[1;33m Programa interrompido pelo usuário')
        time.sleep(2)
        sair()
    except EOFError: 
        print('\n\033[1;33m Programa interrompido pelo usuário')
        time.sleep(2)
        sair()
