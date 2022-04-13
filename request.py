#########################################################################
##### SCRAPING contra WEBL0G0S. Devuelve un json con ppal, bck, 2nivel 
#########################################################################

import requests, json, urllib3, re
urllib3.disable_warnings()
cookie=''


def sesionLogosPT():
    global cookie
    data = {
        'USER': '',
        'PASSWORD': '',
        'SMENC': 'utf-8',
        'SMLOCALE': 'US-EN',
        'target': 'https://tuweb.Scraping/',
        'smquerydata': '',
        'smauthreason': '0',
        'postpreservationdata': '',
    }
    response = requests.post('https://tuweb.Scraping/siteminderagent/login.fcc', data=data, verify=False,allow_redirects=False)
    if response.status_code == 500:
        print('L0g0s esta caido')
        exit
    else:
        cookie = response.cookies['SMSESSION']

def requestLogosPT(parametro,tipo,parametroOpcional=''): #las consulta.
    global cookie
    parametro = str(parametro)
  
    if cookie == '':
        sesionLogosPT()
    headers = {
            'Connection': 'keep-alive',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="99", "Microsoft Edge";v="99"',
            'Accept': 'application/json, text/plain, */*',
            'sec-ch-ua-mobile': '?0',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36 Edg/99.0.1150.46',
            'sec-ch-ua-platform': '"Windows"',
            'Origin': 'https://tuweb.Scraping',
            'Sec-Fetch-Site': 'same-origin',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Dest': 'empty',
            'Referer': 'https://tuweb.Scraping/planta',
            'Accept-Language': 'es,es-ES;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        }
    url_get = {
        'EquiposAccesosSede' : 'https://tuweb.Scraping/api/EquiposAccesosSede?sede=' +  parametro,
        'Servicios' :  'https://tuweb.Scraping/api/Equipos/' + parametro + '/CentrosGestion',
        'Acceso' :  'https://tuweb.Scraping/api/Accesos/' + parametro,
        'DatosRed' :  'https://tuweb.Scraping/api/Accesos/' + parametro + '/DatosRed',
        'Equipo' : 'https://tuweb.Scraping/api/Equipos/' + parametro,
        'SGC': 'https://tuweb.Scraping/api//Accesos/CalidadesSgc/' + parametro,
        'dirPublico': 'https://tuweb.Scraping/api/Accesos/' + parametro + '/DatosRed/DirPublico/' + parametroOpcional,
        'IpGestion': 'https://tuweb.Scraping/api/Equipos/' + parametro + '/Ips',
        'AccesosSede' : 'https://tuweb.Scraping/api/AccesosSede?coSede=' + parametro ,
        'EquiposSede' : 'https://tuweb.Scraping/api/EquiposSede?sede=' + parametro 
    }
    url_post = {'Sedes' : 'https://tuweb.Scraping/api/Sedes',
                'SedesVrf': 'https://tuweb.Scraping/api/Sedes',
                'PedidoVuelo' : 'https://lb.es.telefonica/lb/JSON?accion=obtieneIdsPedidos&opcion=provision&historico=false'}

    json_data = {
        'Sedes' : {"cliente":{"nombre":[],"cif":[],"cuc":[],"nombreATC":[],"matriculaATC":[],"nombreContacto":[],"telefonoContacto":[]},
                "sede":{"nombre":[],"codComercio":[],"alojamientoTIC":"","pais":[],"region":[],"poblacion":[],"direccion":[],"numero":[],"internacional":"","indIPV6":"","administrativoAcceso":[],"idSedeFlexWAN":[],"cifFlexWAN":[],"clienteFlexWAN":[]},
                "equipo":{"mnemonico":[],"tipo":[],"fabricante":[],"codModelo":[],"nomModelo":[],"numSerie":[],"ip":[],"mac":[],"criticidad":[],"proveedorMante":[],"tipoLAN":[],"dedalo":[],"autentUsuarios":[],"idVPNGCU":[],"configuracionEsp":"","workaround":"","desFuncional":[]},
                "canal":{"adminVLANFusion":[],"tipoVLAN":[],"idVPN":[],"indIPv6":"","idCanal":[],"topologia":[]},
                "centroGestion":{"nombre":[],"jefatura":[],"gerencia":[]},
                "circuito":{"tipo":[],"tecnologia":[],"administrativo":[ parametro ],"telefono":[],"nri":[],"msisdn":[],"admServicio":[],"nodo":[],"velocidad":[],"planProtege":"","indIPv6DualStack":"","indMultiVRF":"","indMigradoFusion":"","tipoDiversifica":[],"radioEnlace":"","indICC":"","indPrebaja":"","ipPublica":[],"topologia":[],"topologiaCloud":[],"tipoTraficoMovil":[],"solucion":[]},
                "rpv":{"administrativo":[],"idVPN":[],"idVLAN":[],"tipo":[],"indIPv6":"","administrativoVLAN":[]},
                "servicio":{"tipo":[],"codigo":[],"estadoAITR":[],"facilidad":[],"idVPN":[]},
                "serviciovoz":{"nombreRAI":[],"codigoRAI":[],"tipoRAI":[],"cabeceraRAI":[],"numero":[]},
                "facilidad":{"facilidad":[],"ambFunc":[],"fabricante":[],"capacidad":[],"administrativoRRLL":[]}},
        'SedesVrf' : {"cliente":{"nombre":[],"cif":[],"cuc":[],"nombreATC":[],"matriculaATC":[],"nombreContacto":[],"telefonoContacto":[]},
                "sede":{"nombre":[],"codComercio":[],"alojamientoTIC":"","pais":[],"region":[],"poblacion":[],"direccion":[],"numero":[],"internacional":"","indIPV6":"","administrativoAcceso":[],"idSedeFlexWAN":[],"cifFlexWAN":[],"clienteFlexWAN":[]},
                "equipo":{"mnemonico":[],"tipo":[],"fabricante":[],"codModelo":[],"nomModelo":[],"numSerie":[],"ip":[],"mac":[],"criticidad":[],"proveedorMante":[],"tipoLAN":[],"dedalo":[],"autentUsuarios":[],"idVPNGCU":[],"configuracionEsp":"","workaround":"","desFuncional":[]},
                "canal":{"adminVLANFusion":[],"tipoVLAN":[],"idVPN":[],"indIPv6":"","idCanal":[],"topologia":[]},
                "centroGestion":{"nombre":[],"jefatura":[],"gerencia":[]},
                "circuito":{"tipo":[],"tecnologia":[],"administrativo":[],"telefono":[],"nri":[],"msisdn":[],"admServicio":[],"nodo":[],"velocidad":[],"planProtege":"","indIPv6DualStack":"","indMultiVRF":"","indMigradoFusion":"","tipoDiversifica":[],"radioEnlace":"","indICC":"","indPrebaja":"","ipPublica":[],"topologia":[],"topologiaCloud":[],"tipoTraficoMovil":[],"solucion":[]},
                "rpv":{"administrativo":[ parametro ],"idVPN":[],"idVLAN":[],"tipo":[],"indIPv6":"","administrativoVLAN":[]},
                "servicio":{"tipo":[],"codigo":[],"estadoAITR":[],"facilidad":[],"idVPN":[]},
                "serviciovoz":{"nombreRAI":[],"codigoRAI":[],"tipoRAI":[],"cabeceraRAI":[],"numero":[]},
                "facilidad":{"facilidad":[],"ambFunc":[],"fabricante":[],"capacidad":[],"administrativoRRLL":[]}},
        'PedidoVuelo' : [{"historico":"false","admCircuito":"","nri":"","pedido":"","telefono":"","nemonico": parametro ,"solicitudAtlas":"","odin":"","pfa":"","admServicio":"","actuacionSac":"","macEquipo":"","actuacion":"","proyectoSede":"",
                 "agsi":"","dtme_codConectividad":"","sg3g_codServicio":"","solicitudGMC":"","pedidoADSL":"","vpn":"","admRPV":"","nemonicoRPV":"","admAccMul":"","sectores":[],"clientes":[],"clientesFw":[],"movimientos":[],
                 "tiposModificacion":[],"servicios":[],"provincias":[],"poblaciones":[],"territorios":[],"tareasPrimeraTarea":[],"estadosPrimeraTarea":[],"tareasSegundaTarea":[],"estadosSegundaTarea":[],"tiposIncidencias":[],
                 "incidenciaGeneraCod":"false","gruposTareas":[],"tipoFechaBusqueda":{},"fechaInicio":"","fechaFin":"","informada":"false","sinInformar":"false","modalidades":[],"gruposActuacion":[],"actuacionNoTratada":"false","consultaAbierta":"false","validadores":[],
                 "proyectos":[],"soluciones":[],"carterizados":[],"rtc":[],"centrosGestion":[],"gruposGestion":[],"fabricante":[],"modelosEquipos":[],"serviciosSecundariosEquipos":[],"tiposLAN":[],"velocidades":[],"tiposAccesos":[],"concentradores":[],"tecnologiasADSL":[],
                 "tecnologiasMovil":[],"topologias":[],"indDualstack":"","indMultiVRF":"","internacionales":[],"estadosEquipo":[],"estadosInstalacion":[],"trabajos":[],"proveedoresInstalacion":[],"descFuncional":"","coFlexwan":"","modalidadesFlexWan":[],"solIPHosted":"",
                 "paises":[],"indFwInt":"","indLiResFwInt":"","liVirFwInt":"","indWorkaround":"","nemSedeFlexwan":"","tiposRedundancia":[],"solVozDatos":[],"indRadioenlace":"","tiposDiversifica":[]}]
    }

    if tipo in url_get.keys(): #es get
        r = requests.get(url_get[tipo], cookies={'SMSESSION':cookie}, verify=False)
    else:
        r = requests.post(url_post[tipo], headers=headers, cookies={'SMSESSION':cookie}, json=json_data[tipo], verify=False)

    if r.status_code != 200 or re.search('Error 500',r.text):
        print('Error al conectar con LOGOS' + r.text)
        exit
    else:
        return json.loads(r.text)


def Caudal(Secuencia): #devuelve {'Plata':10Mb,'Oro':1Mb..}
    caudales = {}
    for i in requestLogosPT(Secuencia,'SGC'):
       caudales[i['tipoCalidad']] = i['dsCalidad']
    return caudales
def SedesVrf(nadVLAN): 
    sedes = requestLogosPT(nadVLAN, 'SedesVrf') #devuelve sedes q tienen las misma NADVLAN
    vrf = { 'nadVLAN' : nadVLAN,
            'labels':[],
            'accesos':[],
        }   

    for sede in sedes:
        accesos = requestLogosPT(sede['codSede'],'EquiposAccesosSede') #devuelve el listado de accesos y equipos q hay en la sede
      
        ML = list(filter(lambda acceso: acceso['servicio']['id'] == "E20", accesos))
        for a in ML:
            a = requestLogosPT(str(a['acceso']['coAcceso']),'Acceso')
            caudal = Caudal(str(a['secuencial']))
            
            vrf['labels'] = list(caudal.keys())
            vrf['accesos'].append( {'NAD':a['nuAdministrativo'],
                                    'cols':list(caudal.values())})
                        
    return vrf


def pedidoVuelo(nemonico): #OK
    PedidoVuelo = requestLogosPT(nemonico,'PedidoVuelo')
    if len(PedidoVuelo['listMessages']) > 0 : 
        return PedidoVuelo['listMessages'][0]['sMensaje']
    else:
        return json.dumps(PedidoVuelo ['oData']['listIdsPedidos'])


def Logos(nadEstudio):
    def Homologado(modelo): #OK
        #Verfica en el csv si el equipo esta homologado para la migración
        lines = [line.strip() for line in open('d:/User/Desktop/AVTPython/equipos_homologados.csv')]
        for x in lines:
            if re.search(modelo,x): return 'Si' 
        return 'No'

    def Servicios(coEquipo):
        servicios = requestLogosPT(coEquipo,'Servicios')
        catServicio = {'P28':'SILAN', 'P16':'IbercomIP','E20':'ML','E08':'Datainternet'}
        return list(map(lambda n: catServicio.get(n['coServicio']), servicios))

    def Acceso(coAcceso):
        keys = dict.fromkeys(['nuAdminitrativoRedundancia','tipoAcceso','coAccesoBackup','coAcceso','coEquipo','coSede','caudalMultimedia','circuitoBackup','concentrador','indMultiVrf','nuAdministrativo','secuencial','topologia','velocidad'])
        respuesta = requestLogosPT(coAcceso,'Acceso') 
        return dict({(n, respuesta[n]) for n in keys})
     
    def Equipo(coEquipo):
        keys = ['fabricante','marca','mnemonico','tipoRouting','modelo']
        respuesta = requestLogosPT(coEquipo,'Equipo')
        return dict({(n, respuesta[n]) for n in keys})
    
    def IpGestion(coEquipo):
        for i in requestLogosPT(coEquipo,'IpGestion'):
            if i['tipoIp'] == 'IP Gestion': return i['ip']

    def DirPublicas(coAcceso,coCanal):
        pool = requestLogosPT(coAcceso,'dirPublico',coCanal)
        aux = []
        for n in pool:
            asPublico = n['asPublico']
            aux.append(n['ipInicio'] + '/' + n['longitudPrefijo'])
        return {'ips': aux, 'as' : asPublico}

    def Vrfs(coAcceso):
        #rellena vrf y vpls
        vrfs=[]; vpls=[]; iPPublicas = {}
        for v in requestLogosPT(coAcceso,'DatosRed'): 
            tipoVlan = v['tipoVlan']
            if tipoVlan == "VPLS DataInternet":
                ### NADVLAN | tipoPe (PPAL BCK) | mneumonicoPE | interfazPe | IPWan | Caudal |
                aux= {  'NADVLAN' : v['coCanal'],
                        'tipoPe': v['tipoPe'],
                        'mneumonico': v['peSecundario'] if v['pe'] == None else v['pe'],
                        'interfaz': v['interfaz'] + "." + str(int(v['subinterfaz'])),
                        'ipWan':v['ipWan'],
                        'caudal': json.dumps(Caudal(v['nuSecuencialCanal']))
                    }
                vpls.append({'cols': list(aux.values())})
                iPPublicas = DirPublicas(coAcceso, v['coCanal'])
            if tipoVlan in ["VLAN Nacional", "VLAN Exclusiva Nacional"]:
                caudalesPE = Caudal(v['nuSecuencialCanal'])
                vrfs.append({   'NADVLAN' : v['coCanal'],
                                'ipWan' : v['ipWan'],
                                'pe': [v['pe'],v['peSecundario']],
                                'caudales': {'label': list(caudalesPE.keys()) , 'cols': list(caudalesPE.values())},
                                'sedesVRF' : SedesVrf(v['coCanal'])
                            })
        return {'vrfs' : vrfs , 'vpls' : vpls } | iPPublicas
        
    def DatosEquipo(NAD):
        sede = (requestLogosPT(NAD,'Sedes'))[0]
        AccesosSede = requestLogosPT(sede['codSede'],'AccesosSede')  
        for n in filter(lambda x: NAD in [x['nuAdministrativo'],x['nuTelefono']], AccesosSede): #buscamos de estudio

            coAcceso = n['coAcceso']
            a = Acceso(coAcceso)
            e = Equipo(a['coEquipo'])
            r = {'ipGestion' : IpGestion(a['coEquipo']),
                'servicios' : Servicios(n['coEquipo']),
                'pedidoVuelo' : pedidoVuelo(e['mnemonico']),
                'homologado' : Homologado(e['modelo']),
                'cif' : sede['cifCliente']
                }
            
        return  a | e | r

    #main
    data = {'hijos':{}, 'diba':{}}
    data["ppal"] = DatosEquipo(nadEstudio)
    if data["ppal"]['nuAdminitrativoRedundancia'] != None:
        data['bck'] = DatosEquipo(data["ppal"]['nuAdminitrativoRedundancia'])
    else:
        data['bck'] = {
            'nuAdministrativo': 'No aplica',
            'pedidoVuelo' : 'No aplica',
            'mnemonico' : 'No aplica',
            'modelo' : 'No aplica',
            'concentrador' : 'No aplica',
            'tipoRouting' : 'No aplica',
            'Servicio' : '',
            'indMultiVrf' : 'No aplica',
            'ipGestion' : 'No aplica',
            'descripcion' :'NO',
            'rol' : 'No aplica',
            'homologado': 'No aplica'
            }

    vrfsVpls = Vrfs(data['ppal']['coAcceso'])
    data['ppal']['vrfs'] = vrfsVpls['vrfs']
    data['ppal']['indMultiVrf'] = 'Si' if len(vrfsVpls['vrfs']) > 1 else 'No'

    if len(vrfsVpls['vpls']) >0: # si es un diba
        data['diba'] = data['ppal']
        data['diba']['vpls'] = vrfsVpls['vpls']
        data['diba']['dirPublicas'] = vrfsVpls['ips']
        data['diba']['asPublico'] = vrfsVpls['as']

   
    mnemonicoPadre = data['ppal']['mnemonico'];   
    aux = []                        
    EquiposSede = requestLogosPT(data['ppal']['coSede'],'EquiposSede') #buscamos equipos de segundo nivel
    for n in filter(lambda x: x['equipoPrimerNivel'] == mnemonicoPadre, EquiposSede):

        coEquipo = n['coEquipo']
        servicios = Servicios(coEquipo)
        if 'Datainternet' in servicios: #si es un diba 2 nivel
            data['diba'] =  data['diba'] | Equipo(coEquipo)
            data['diba']['pedidoVuelo'] = pedidoVuelo(data['diba']['mnemonico'])
            data['diba']['servicios'] = servicios
            data['diba']['ipGestion'] = IpGestion(coEquipo)
            
        aux.append({'cols': [n['mnemonico'], #mnemonico
                            json.dumps(servicios), #servicio
                            n['tipoEquipo'], #tipoEquipo
                            n['modelo']]
                    })
    data['hijos']['content'] = aux
    data['hijos']['labels'] = ['mnemonico','servicios','tipoEquipo','modelo']
    return data
