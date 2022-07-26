# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import json

from apps.home import blueprint
from flask import render_template
from flask_login import login_required
from jinja2 import TemplateNotFound



@blueprint.route('/index')
@blueprint.route('/index.html')

def index():
    filtered_data_all_wiso_publs = []
    filtered_data_all_wiso_publs.append(
        {'title': '100% organic? A sustainable entrepreneurship perspective on the diffusion of organic clothing',
         'keywords': 'Corporate social responsibility; Corporate sustainability; Germany; Integrated production; Organic cotton; Supply chain management; Sustainability-oriented innovation; Sustainable entrepreneurship; Textile industry; Transformation',
         'author': 'Hansen E. G., Schaltegger S.', 'language': 'None', 'publish_year': '2013',
         'URL': 'https://cris.fau.de/converis/portal/Publication/122909864?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': '10 Jahre Qualitätsmanagement im österreichischen berufsbildenden Schulwesen mit QIBB: Fragen zu Monitoring und Evaluation eines Mehrebenensystem',
                                            'keywords': 'None',
                                            'author': 'Gramlinger Franz, Jonach Michaela, Wilbers Karl',
                                            'language': 'None', 'publish_year': '2014',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/107789484?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '1913. The World before the Great War - by C. Emmerson', 'keywords': 'Great War',
         'author': 'GL Gardini', 'language': 'None', 'publish_year': '2014',
         'URL': 'https://cris.fau.de/converis/portal/Publication/113168484?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '2012 Mexico election: The return of the Partido Revolucionario Institucional (PRI)',
         'keywords': 'None', 'author': 'Gardini GL', 'language': 'None', 'publish_year': '2012',
         'URL': 'https://cris.fau.de/converis/portal/Publication/252934657?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': "2012 Venezuela elections: Will Chavez's 4th mandate bring moderation or radicalization?",
         'keywords': 'None', 'author': 'Gardini GL', 'language': 'None', 'publish_year': '2012',
         'URL': 'https://cris.fau.de/converis/portal/Publication/252934406?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': '2013-14 State of the Future, Glenn, J.C./ Gordon, T.J./ Florescu, E., The Millennium Project, April 2014 (247 pages)',
                                            'keywords': 'None', 'author': 'von der Gracht H. A.', 'language': 'None',
                                            'publish_year': '2014',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/206787687?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '20 Jahre Spruchverfahren: Empirische Ergebnisse zu Anlässen und Formen der Abfindung',
         'keywords': 'None', 'author': 'Henselmann Klaus, Munkert MichaelJ., Winkler Nadine, Schrenker Claudia',
         'language': 'None', 'publish_year': '2013',
         'URL': 'https://cris.fau.de/converis/portal/Publication/110635184?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '20 Jahre Spruchverfahren: Empirische Ergebnisse zu Anlässen und Formen der Abfindung',
         'keywords': 'None', 'author': 'Henselmann Klaus', 'language': 'None', 'publish_year': '2014',
         'URL': 'https://cris.fau.de/converis/portal/Publication/118229144?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': '20 Jahre Spruchverfahren: Empirische Ergebnisse zum gerichtlichen Verfahrensgang und zum Ausgang von Spruchverfahren',
                                            'keywords': 'None',
                                            'author': 'Henselmann Klaus, Munkert MichaelJ., Winkler Nadine, Schrenker Claudia',
                                            'language': 'None', 'publish_year': '2013',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/110638044?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': '20 Jahre Spruchverfahren: Empirische Ergebnisse zur Abfindungserhöhung in Abhängigkeit vom Antragsteller und von den Bewertungssubjekten',
                                            'keywords': 'None',
                                            'author': 'Henselmann Klaus, Munkert MichaelJ., Winkler Nadine, Schrenker Claudia',
                                            'language': 'None', 'publish_year': '2013',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/110650804?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '21 Open Labs as Islands of Reason in the Digital Age', 'keywords': 'None',
         'author': 'Albrecht Fritzsche', 'language': 'None', 'publish_year': '2020',
         'URL': 'https://cris.fau.de/converis/portal/Publication/239510774?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '2.2 Kurz vorgestellt – Bücher zum Thema E-Learning', 'keywords': 'E-Learning1; Buchbesprechung2;',
         'author': 'Jahn Dirk, Kalsperger Maria, Dr. Trager Bernhard', 'language': 'German', 'publish_year': '2013',
         'URL': 'https://cris.fau.de/converis/portal/Publication/106787604?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '5 Strategien zur Deeskalation von Commitment', 'keywords': 'None', 'author': 'None',
         'language': 'None', 'publish_year': '2021',
         'URL': 'https://cris.fau.de/converis/portal/Publication/260407515?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '6th DACH+ Conference on Energy Informatics (EnInf 2017)', 'keywords': 'None',
         'author': 'Santini S, Tiefenbeck V', 'language': 'None', 'publish_year': '2018',
         'URL': 'https://cris.fau.de/converis/portal/Publication/227859388?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '6 The Many Facets of Open Laboratories and Their Implications for Innovation Management',
         'keywords': 'None', 'author': 'Albrecht Fritzsche', 'language': 'None', 'publish_year': '2020',
         'URL': 'https://cris.fau.de/converis/portal/Publication/239627162?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abbildung der stationären allergologischen Expositionstestungen im deutschen DRG-System',
         'keywords': 'None', 'author': 'Treudler R, Meier F, Schöffski O, Simon J-C', 'language': 'German',
         'publish_year': '2012', 'URL': 'https://cris.fau.de/converis/portal/Publication/114711124?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Ab die Mail!', 'keywords': 'None', 'author': 'None', 'language': 'German', 'publish_year': '2003',
         'URL': 'https://cris.fau.de/converis/portal/Publication/108116844?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abgehängt - Unternehmenskultur und Veränderung.', 'keywords': 'Unternehmenskultur',
         'author': 'Widuckel W.', 'language': 'German', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/119458724?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abgeltungssteuer als Lösung?', 'keywords': 'Kohäsion', 'author': 'Scheffler W.', 'language': 'None',
         'publish_year': '2005', 'URL': 'https://cris.fau.de/converis/portal/Publication/107346844?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A bibliometric analysis of the German corporate governance research', 'keywords': 'None',
         'author': 'Eulerich M., Stiglbauer M., Haustein S.', 'language': 'None', 'publish_year': '2012',
         'URL': 'https://cris.fau.de/converis/portal/Publication/118817424?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A bibliometric review of scientific theory in futures and foresight: A commentary on Fergnani and Chermack 2021',
                                            'keywords': 'None', 'author': 'Münch C, von der Gracht HA',
                                            'language': 'English', 'publish_year': '2021',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/251576873?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abitur and what next? Reasons for gaining double qualifications in Germany',
         'keywords': 'Transformation; qualification; Forschungsbericht 2010; double qualification; Abitur',
         'author': 'None', 'language': 'None', 'publish_year': '2010',
         'URL': 'https://cris.fau.de/converis/portal/Publication/117482684?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Ablenkung oder Abkehr von der Politik? Mediennutzung im Geflecht politischer Orientierun\xadgen',
         'keywords': 'None', 'author': 'Holtz-Bacha C.', 'language': 'None', 'publish_year': '1990',
         'URL': 'https://cris.fau.de/converis/portal/Publication/217759061?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({'title': 'A Blueprint for Event-driven Business Activity Management',
                                         'keywords': 'Reference Architecture, Complex event processing, Business process management, Business process analytics, Business activity management',
                                         'author': 'Janiesch Christian, Matzner Matzner, Müller Oliver',
                                         'language': 'English', 'publish_year': '2011',
                                         'URL': 'https://cris.fau.de/converis/portal/Publication/112510244?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'About well-considered decisions, favorable alternatives and sudden ideas: A qualitative research to identify beliefs that influence women to study information systems in Germany',
                                            'keywords': 'None',
                                            'author': 'Oehlhorn Caroline, Laumer Sven, Maier Christian',
                                            'language': 'English', 'publish_year': '2017',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/205783058?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abschaffung der Abgeltungsteuer: Folgewirkungen auf die Unternehmensbesteuerung',
         'keywords': 'Kohäsion', 'author': 'Scheffler W., Christ R.', 'language': 'German', 'publish_year': '2016',
         'URL': 'https://cris.fau.de/converis/portal/Publication/116060164?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abschließende Bemerkungen zu den Erwiderungen von Foppa und Droz', 'keywords': 'None',
         'author': 'None', 'language': 'None', 'publish_year': '1989',
         'URL': 'https://cris.fau.de/converis/portal/Publication/119609424?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abschlussanalyse 4.0', 'keywords': 'None', 'author': 'Henselmann K', 'language': 'None',
         'publish_year': '2016', 'URL': 'https://cris.fau.de/converis/portal/Publication/200189263?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Abschlussbericht des Lehrforschungsprojekts Lebenswirklichkeit und Partizipation Jugendlicher in Nürnberg im Auftrag des Kreisjugendrings Nürnberg-Stadt',
                                            'keywords': 'None', 'author': 'Damelang A', 'language': 'None',
                                            'publish_year': '2013',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/117625244?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Abschlussprüferhonorare bei deutschen kapitalmarktorientierten Unternehmen\r\nEine Analyse der Entwicklung von Abschlussprüferhonoraren unter Berücksichtigung des IDW RS HFA 36 n. F. und der EU-Verordnung 537/2014',
                                            'keywords': 'None', 'author': 'Dimmer M', 'language': 'German',
                                            'publish_year': '2020',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/238554412?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abschreibungsfinanzierung', 'keywords': 'None', 'author': 'Fischer Thomas, Hitz J.',
         'language': 'None', 'publish_year': '2006',
         'URL': 'https://cris.fau.de/converis/portal/Publication/115230544?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abschreibungsfinanzierung', 'keywords': 'None', 'author': 'None', 'language': 'German',
         'publish_year': '2001', 'URL': 'https://cris.fau.de/converis/portal/Publication/245199850?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abschreibungsfinanzierunng', 'keywords': 'None', 'author': 'None', 'language': 'German',
         'publish_year': '2001', 'URL': 'https://cris.fau.de/converis/portal/Publication/123068264?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Absence from Work of the Self-Employed: A Comparison with Paid Employees', 'keywords': 'None',
         'author': 'Lechmann D, Schnabel C', 'language': 'None', 'publish_year': '2014',
         'URL': 'https://cris.fau.de/converis/portal/Publication/118443204?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Absenteeism and Employment Probation - A Panel Study for Germany', 'keywords': 'None',
         'author': 'None', 'language': 'English', 'publish_year': '1999',
         'URL': 'https://cris.fau.de/converis/portal/Publication/120944164?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Absenteeism and Employment Protection: 3 Case Studies', 'keywords': 'None', 'author': 'None',
         'language': 'None', 'publish_year': '2004',
         'URL': 'https://cris.fau.de/converis/portal/Publication/122969264?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Absorptive Capacity as a Prerequisite for Open Innovation', 'keywords': 'None',
         'author': 'Ixmeier Johannes, Scheiner Christian, Voigt Kai-Ingo', 'language': 'English',
         'publish_year': '2011', 'URL': 'https://cris.fau.de/converis/portal/Publication/121666864?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Abweichungen zwischen Handels- und Steuerbilanz, Übersichten über die Reichweite des Maßgeblichkeitsprinzips und die Ausnahmen von der Maßgeblichkeit der Handelsbilanz für die Steuerbilanz',
                                            'keywords': 'Kohäsion', 'author': 'Scheffler W.', 'language': 'None',
                                            'publish_year': '2004',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/111123584?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Abweichungen zwischen Handels- und Steuerbilanz, Übersichten über die Reichweite des Maßgeblichkeitsprinzips und die Ausnahmen von der Maßgeblichkeit der Handelsbilanz für die Steuerbilanz',
                                            'keywords': 'Kohäsion', 'author': 'Scheffler W.', 'language': 'None',
                                            'publish_year': '2004',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/114374524?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({'title': 'Abweichungsanalyse bei Projekten im F&E-Bereich', 'keywords': 'None',
                                         'author': 'Fischer Thomas, Coenenberg Adolf G., Raffel Andreas',
                                         'language': 'German', 'publish_year': '1992',
                                         'URL': 'https://cris.fau.de/converis/portal/Publication/122077824?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Academic Entrepreneurship - Examining Motivating and Hindering Influences Through the Gender Lense; Internationalizing Entrepreneurship Education and Training - Innovative Formats for Entrepreneurship Education Teaching',
                                            'keywords': 'None',
                                            'author': 'Laspita S., Scheiner Christian, Chlosta S., Brem Alexander, Voigt Kai-Ingo, Klandt H.',
                                            'language': 'English', 'publish_year': '2007',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/120565984?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Academic Writing – Guidelines for a Term Paper, Bachelor and Master Thesis', 'keywords': 'None',
         'author': 'None', 'language': 'None', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/234792548?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Case About the Diffusion of Co-Creation Expertise in Organizations', 'keywords': 'None',
         'author': 'Krämer K., Roth Angela, Möslein Kathrin M.', 'language': 'None', 'publish_year': '2014',
         'URL': 'https://cris.fau.de/converis/portal/Publication/118831724?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Case Mining based Recommender System for Knowledge Workers', 'keywords': 'None', 'author': 'None',
         'language': 'None', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/114537544?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Accelerating Scientific Research with Open Laboratories', 'keywords': 'None',
         'author': 'Fritzsche A, Möslein K', 'language': 'None', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/116512924?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Accepting a crowdsourced delivery - a choice-based conjoint analysis', 'keywords': 'None',
         'author': 'Bathke H, Hartmann E', 'language': 'English', 'publish_year': '2021',
         'URL': 'https://cris.fau.de/converis/portal/Publication/269365499?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Accessing complex patient data from Arden Syntax Medical Logic Modules', 'keywords': 'None',
         'author': 'Stefan Kraus, Martin Enders, Hans-Ulrich Prokosch, Ixchel Castellanos, Richard Lenz, Martin Sedlmayr',
         'language': 'None', 'publish_year': '2018',
         'URL': 'https://cris.fau.de/converis/portal/Publication/216630771?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Access to Commitment Devices Reduces Investment Incentives in Oligopoly', 'keywords': 'None',
         'author': 'Grimm Veronika, Zöttl Gregor', 'language': 'English', 'publish_year': '2005',
         'URL': 'https://cris.fau.de/converis/portal/Publication/121259204?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Accounting for Sustainable Organisations: Where is the Accountant and why it Matters',
         'keywords': 'None', 'author': 'None', 'language': 'None', 'publish_year': '2011',
         'URL': 'https://cris.fau.de/converis/portal/Publication/123255484?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Accounting fraud: Case studies and practical implications', 'keywords': 'None',
         'author': 'Henselmann Klaus, Hofmann Stefan', 'language': 'English', 'publish_year': '2010',
         'URL': 'https://cris.fau.de/converis/portal/Publication/110531124?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Accounting Rules for SMEs in Germany - General Structure and Changes over Time',
         'keywords': 'Rechungslegung; Deutschland; EU; historisch; Mittelstand; KMU; SME; Accounting; Germany; History; Europe',
         'author': 'Henselmann K', 'language': 'English', 'publish_year': '2020',
         'URL': 'https://cris.fau.de/converis/portal/Publication/243473537?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Accuracy, unbiasedness and efficiency of professional macroeconomic forecasts: An empirical comparison for the G7',
                                            'keywords': 'Evaluating forecasts\r\nMacroeconomic forecasting\r\nRationality\r\nSurvey data\r\nFixed-event forecasts',
                                            'author': 'None', 'language': 'English', 'publish_year': '2011',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/216788980?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({'title': 'Achieving and assuring high availability', 'keywords': 'Innovation',
                                         'author': 'K.S. Trivedi, Ciardo G., Dasarathy B., Grottke Michael, Matias R., Rindos A., Vashaw B.',
                                         'language': 'None', 'publish_year': '2008',
                                         'URL': 'https://cris.fau.de/converis/portal/Publication/115263544?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Achieving Competitive Advantage from Sustainable Supplier Management - Insights from the Chemical Industry',
                                            'keywords': 'Innovation',
                                            'author': 'Reuter C., Förstl K., Hartmann E., Blome C.', 'language': 'None',
                                            'publish_year': '2009',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/121689084?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Achtsamkeit im organisationalen Kontext: Der Einfluss individueller und organisationaler Achtsamkeit auf resilientes Verhalten, psychische Gesundheit und Arbeitsengagement',
                                            'keywords': 'None', 'author': 'None', 'language': 'German',
                                            'publish_year': '2018',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/107190864?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Cluster Analysis of Pediatric Cancer Incidence Rates in Florida: 2000–2010', 'keywords': 'None',
         'author': 'None', 'language': 'None', 'publish_year': '2014',
         'URL': 'https://cris.fau.de/converis/portal/Publication/114691764?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({'title': 'ACM SIGMIS CPR 2020 Introduction', 'keywords': 'None',
                                         'author': 'Sven Laumer, Jeria Quesenberry, Damien Joseph, Christian Maier, Daniel Beimborn, Shirish C. Srivastava',
                                         'language': 'None', 'publish_year': '2020',
                                         'URL': 'https://cris.fau.de/converis/portal/Publication/255637517?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A community-based toolkit for designing ride-sharing services: The case of a virtual network of ride access points in Germany',
                                            'keywords': 'Innovation',
                                            'author': 'Hansen E. G., Gomm M. L., Bullinger A.C., Möslein Kathrin M.',
                                            'language': 'None', 'publish_year': '2010',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/114151444?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A commuting-based refinement of the contiguity matrix for spatial models, and an application to local police expenditures',
                                            'keywords': 'spatial weights; contiguity matrix; commuting flows; police expenditures',
                                            'author': 'Rincke Johannes', 'language': 'English', 'publish_year': '2010',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/118021244?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Comparative Analysis of the Australian and German eHealth System', 'keywords': 'None',
         'author': 'None', 'language': 'English', 'publish_year': '2016',
         'URL': 'https://cris.fau.de/converis/portal/Publication/124065304?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Comparative Assessment of Basel II/III and Solvency II', 'keywords': 'Solvency II; Basel II/III',
         'author': 'Gatzert Nadine, Wesker Hannah', 'language': 'English', 'publish_year': '2012',
         'URL': 'https://cris.fau.de/converis/portal/Publication/114515984?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A comparative perspective on political advertising in western democracies: implications of media and political system characteristics',
                                            'keywords': 'None', 'author': 'Holtz-Bacha C, Kaid Lynda L.',
                                            'language': 'None', 'publish_year': '1995',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/219599238?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({'title': 'A comprehensive wealth index for cities in Germany',
                                         'keywords': 'Cities in Germany; Comprehensive wealth index',
                                         'author': 'Dovern J., Quaas M., Rickels W.', 'language': 'None',
                                         'publish_year': '2014',
                                         'URL': 'https://cris.fau.de/converis/portal/Publication/204170331?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Conceptual Framework of Service Innovation and Its Implications for Future Research',
         'keywords': 'Conceptual framework; Service innovation; Service science; Service-dominant logic',
         'author': 'Sven Schwarz, Carolin Durst, Freimut Bodendorf', 'language': 'None', 'publish_year': '2012',
         'URL': 'https://cris.fau.de/converis/portal/Publication/120019504?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Conceptualized Investment Model of Crowdfunding', 'keywords': 'Crowdfunding',
         'author': 'Tomczak A, Brem A', 'language': 'English', 'publish_year': '2013',
         'URL': 'https://cris.fau.de/converis/portal/Publication/108691924?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A conceptualized investment model of crowdfunding', 'keywords': 'None',
         'author': 'Tomczak Alan, Brem Alexander', 'language': 'None', 'publish_year': '2016',
         'URL': 'https://cris.fau.de/converis/portal/Publication/108692144?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A configuration of sustainable sourcing and supply management strategies', 'keywords': 'None',
         'author': 'None', 'language': 'English', 'publish_year': '2017',
         'URL': 'https://cris.fau.de/converis/portal/Publication/119561904?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Context Aware Mobile Application for Physical Activity Promotion', 'keywords': 'None',
         'author': 'Hamper Andreas', 'language': 'None', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/114567684?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Continuous Logit Hotelling Model with Endogenous Locations of Consumers',
         'keywords': 'Spatial competition; Continuous logit model; Minimum differentiation principle',
         'author': 'Matthias Wrede', 'language': 'English', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/108803244?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({'title': 'A Continuous Spatial Choice Logit Model of a Polycentric City.',
                                         'keywords': 'Urban spatial equilibrium; Polycentric city; Probabilistic location choices; Continuous logit model; Cross-commuting',
                                         'author': 'Matthias Wrede', 'language': 'English', 'publish_year': '2015',
                                         'URL': 'https://cris.fau.de/converis/portal/Publication/122098724?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Acquiring new customers by price comparison sites vs. direct marketing: Long-term effects on customer loyalty and cross-buying in a contractual setting',
                                            'keywords': 'None', 'author': 'None', 'language': 'None',
                                            'publish_year': '2020',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/240747535?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Credit Portfolio Framework under Dependent Risk Parameters PD, LGD and EAD', 'keywords': 'None',
         'author': 'Matthias Fischer, Kevin Jakob, Johanna Eckert', 'language': 'English', 'publish_year': '2016',
         'URL': 'https://cris.fau.de/converis/portal/Publication/116016164?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A cross-domain comparison of application areas for service systems based on cyber-physical systems',
         'keywords': 'service systems; service systems engineering, cyber-physical systems', 'author': 'Oks S J',
         'language': 'English', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/110252604?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A Cross-National Study of the Effects of Education on Pre-Service Teachers’ Attitudes, Intentions, Concerns, and Self-Efficacy Regarding Inclusive Education',
                                            'keywords': 'Inclusion; teacher education; Canada; Germany; attitudes; intentions; concerns; self-efficacy; Inklusion;',
                                            'author': 'Miesera Susanne, Sokal Laura, Kimmelmann Nicole',
                                            'language': 'English', 'publish_year': '2021',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/268597337?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A cross-sectional study assessing the association between online ratings and clinical quality of care measures for US hospitals: results from an observational study.',
                                            'keywords': 'None', 'author': 'Emmert M, Meszmer N, Schlesinger M',
                                            'language': 'None', 'publish_year': '2018',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/106835784?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A cross-sectional study assessing the association between online ratings and structural and quality of care measures: results from two German physician rating websites.',
                                            'keywords': 'None',
                                            'author': 'Emmert M, Adelhardt T, Sander U, Wambach V, Lindenthal J',
                                            'language': 'None', 'publish_year': '2015',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/120070324?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Active Sourcing und Social Recruiting - Ausgewählte Ergebnisse der Recruiting Trends 2016 und der Bewerbungspraxis 2016',
                                            'keywords': 'None',
                                            'author': 'Weitzel Tim, Laumer Sven, Maier Christian, Oehlhorn Caroline, Wirth Jakob, Weinert Christoph, Eckhardt Andreas',
                                            'language': 'German', 'publish_year': '2016',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/208765364?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Active Sourcing und Social Recruiting - Ausgewählte Ergebnisse der Recruiting Trends 2017 und der Bewerbungspraxis 2017',
                                            'keywords': 'None',
                                            'author': 'Weitzel Tim, Laumer Sven, Maier Christian, Oehlhorn Caroline, Wirth Jakob, Weinert Christoph, Eckhardt Andreas',
                                            'language': 'German', 'publish_year': '2017',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/206235115?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Activity-Based Costing and Performance Measurement in the Electronics Industry', 'keywords': 'None',
         'author': 'None', 'language': 'None', 'publish_year': '1995',
         'URL': 'https://cris.fau.de/converis/portal/Publication/245268155?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Activity-based working: How the use of available workplace options increases perceived autonomy in the workplace',
                                            'keywords': 'None', 'author': 'None', 'language': 'English',
                                            'publish_year': '2022',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/266062440?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Actor and Institutional Dynamics in the Development of Multi-Stakeholder Initiatives',
         'keywords': 'Business self-regulation; Club theory; Global governance; Institutional entrepreneurship; Institutional theory; Management of diverse interests; Multi-stakeholder initiatives; Political role of the firm; Soft law',
         'author': 'Zeyen Anica, Beckmann Markus, Wolters Stella', 'language': 'None', 'publish_year': '2016',
         'URL': 'https://cris.fau.de/converis/portal/Publication/122177264?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Actor integration in service systems – exploring effects on a micro level', 'keywords': 'None',
         'author': 'Jonas J, Roth A, Möslein K', 'language': 'None', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/122100924?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A Customer Perspective on Product Eliminations: How the Removal of Products Affects Customers and Business Relationships',
                                            'keywords': 'Forschungsbericht 2010; Innovation',
                                            'author': 'Homburg Ch., Fürst Andreas, Prigge J.-K.', 'language': 'None',
                                            'publish_year': '2010',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/117743604?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Adaptation to the market? Status differences between target occupations in the application process and realized training occupation of German adolescents',
                                            'keywords': 'None', 'author': 'Schels B, Abraham M', 'language': 'English',
                                            'publish_year': '2021',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/262083973?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Adaption der Berufsaspiration bei Jugendlichen - eine Befragung von Haupt- und Realschüler/innen in Nürnberg. Überblick über die Studie und Datendokumentation',
                                            'keywords': 'None', 'author': 'Abraham M, Dietrich H, Sachse H, Schels B',
                                            'language': 'German', 'publish_year': '2015',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/108913904?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Adaptive Case Management: Anwendung des Business Process Management 2.0-Konzepts auf schwach strukturierte Geschäftsprozesse',
                                            'keywords': 'None', 'author': 'Christian Herrmann, Matthias Kurz',
                                            'language': 'None', 'publish_year': '2011',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/109360284?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Adaptive Innovation Management - Concept and Tool Support', 'keywords': 'None',
         'author': 'Sebastian Huber, Christian Mühlroth, Freimut Bodendorf', 'language': 'None', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/122114564?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Adaptive Open Innovation - Solution Approach and Tool Support', 'keywords': 'None',
         'author': 'Sebastian Huber, Peter Schott, Matthias Lederer', 'language': 'English', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/109270084?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Dark Side of Telework: A Social Comparison-Based Study from the Perspective of Office Workers',
         'keywords': 'Social comparison theory; Telework; Envy; Turnover; Job performance; Empirical study; COVID-19',
         'author': 'None', 'language': 'English', 'publish_year': '2022',
         'URL': 'https://cris.fau.de/converis/portal/Publication/277654048?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Additive Fertigung für industrielle Anwendungen - Entwicklung einer Auswahlsystematik für Bauteile zur Generierung funktionalen Mehrwerts mittels additiver Fertigung',
                                            'keywords': 'None',
                                            'author': 'Thomas Papke, Dominic Bartels, Michael Schmidt, Marion Merklein, Daniel Gerhard, Jonas Baumann, Indra Pitz',
                                            'language': 'None', 'publish_year': '2020',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/245752967?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': "Addressing a product management's orphan: How to externally implement product eliminations in a B2B setting",
                                            'keywords': 'None', 'author': 'Prigge JK, Homburg C, Fürst A',
                                            'language': 'English', 'publish_year': '2018',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/119815784?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Addressing sustainability information needs along supply chains', 'keywords': 'Nachhaltigkeit;',
         'author': 'None', 'language': 'English', 'publish_year': '2019',
         'URL': 'https://cris.fau.de/converis/portal/Publication/229265156?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': '[A Decade of Online Physician-Rating Websites in Germany: an Assessment of the Current Level of Development].',
                                            'keywords': 'None', 'author': 'Emmert M, Meszmer N', 'language': 'None',
                                            'publish_year': '2017',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/106774844?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A decision support scheme for software process improvement prioritization', 'keywords': 'Innovation',
         'author': 'A. Beckhaus, L.M. Karg, C. Graf, Grottke Michael, D. Neumann', 'language': 'English',
         'publish_year': '2011', 'URL': 'https://cris.fau.de/converis/portal/Publication/111819664?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A Deep Learning Approach for Managing Medical Consumable Materials in Intensive Care Units via Convolutional Neural Networks: Technical Proof-of-Concept Study',
                                            'keywords': 'convolutional neural networks; deep learning; critical care; intensive care; image recognition; medical economics; medical consumables; artificial intelligence; machine learning',
                                            'author': 'Peine A., Hallawa A., Schöffski O., Dartmann G., Begic Fazlic L., Schmeink A., Marx G., Martin L.',
                                            'language': 'None', 'publish_year': '2019',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/229850573?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A Delphi-based risk analysis — Identifying and assessing future challenges for supply chain security in a multi-stakeholder environment',
                                            'keywords': 'Risk; Supply chain security; Terroristic attacks; Delphi; Multi-stakeholder; Future',
                                            'author': 'Markmann C, Darkow I, von der Gracht H', 'language': 'None',
                                            'publish_year': '2013',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/205750466?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A description of the operative decision-making process of a power generating company on the Nordic electricity market',
                                            'keywords': 'Bidding strategy; Decisions under uncertainty; Electricity trading; Nordic power system; Power producer; Risk management',
                                            'author': 'Scharff R., Egerer J., Söder L.', 'language': 'None',
                                            'publish_year': '2014',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/119616024?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A discussion on the General Data Protection Regulation Eine Diskussion zur Datenschutz-Grundverordnung',
                                            'keywords': 'None', 'author': 'Peter Mertens', 'language': 'None',
                                            'publish_year': '2020',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/244599733?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A dissent-based approach for multi-stakeholder scenario development — The future of electric drive vehicles',
                                            'keywords': 'Scenarios; Delphi; Multi-stakeholder; Dissent; Electric drive vehicles',
                                            'author': 'Warth J, von der Gracht HA, Darkow I', 'language': 'None',
                                            'publish_year': '2013',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/205775947?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Distortive Wage Tax and a Countervailing Commuting Subsidy', 'keywords': 'Transformation',
         'author': 'Wrede Matthias', 'language': 'English', 'publish_year': '2009',
         'URL': 'https://cris.fau.de/converis/portal/Publication/114251984?auxfun=&lang=de_DE'})

    filtered_data_all_wiso_pro = []
    filtered_data_all_wiso_pro.append({'project_leader': '105707876,101530724,105329106',
                                       'title': 'Individuell empfohlen? - Wie KI-basierte Beratungssysteme die Diversität der Studierenden beeinflussen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '28.02.2021', 'project_start': '01.03.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235228880?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'AI for Public Services', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '01.06.2024', 'project_start': '01.04.2021',
         'URL': 'https://cris.fau.de/converis/portal/Project/257929870?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '200418444', 'title': 'AI for Industry 4.0: models and technologies', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.07.2020', 'project_start': '01.07.2020',
         'URL': 'https://cris.fau.de/converis/portal/Project/237715326?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '203395223',
                                       'title': 'Künstliche Intelligenz zur Erschließung von Potentialen zur Semi-Prozessautomatisierung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2020', 'project_start': '01.01.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/221488811?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105329106',
                                       'title': 'Eine lebensverlaufssoziologische Perspektive auf das Arbeitsangebot: Zeitliche, institutionelle und soziale Einbettung als Determinanten individueller Reservationslöhne',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.01.2022', 'project_start': '01.02.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/228016423?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Alles Sprache oder was? Qualifizierung von Mentorinnen und Mentoren für ein sprachsensibles Mentoring von Geflüchteten',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': '30.09.2021',
                                       'project_start': '01.04.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/250249701?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760,104991104',
                                       'title': 'Arbeitslosigkeit und Behinderung unter Berücksichtigung der Covid-19-Pandemie und ihrer Bewältigung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.11.2024', 'project_start': '01.12.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/271088154?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760,101148916', 'title': 'Konzeption von Diagnose- und Evaluationsinstrumenten',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.10.2017',
         'project_start': '01.11.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/126433982?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101305324',
                                       'title': 'Analyse und Optimierung standardisierter Behandlungsprozesse im Krankenhaus',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2016', 'project_start': '01.05.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/203774296?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Arbeiten, Lernen und Weiterbildung in der Zeitarbeit - Eine Befragung von Erwerbstätigen in der Zeitarbeit',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2007', 'project_start': '01.01.2005',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235292385?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101494856', 'title': 'Arbeitsmarkteffekte der Reform des vorzeitigen Rentenbezugs',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.03.2020',
         'project_start': '01.09.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/205223927?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Arbeitszeugnisse in Deutschland: Der Einfluss von Geschlecht, Position und Unternehmensmerkmalen auf Inhalt und Bewertung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2012', 'project_start': '01.04.2012',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229844378?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100502116',
                                       'title': 'Eine Analyse von Reputationsrisiken und Spillover-Risiken aus Perspektive der Versicherungswirtschaft',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.11.2018', 'project_start': '01.06.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126185890?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '242689003', 'title': 'None', 'funder': 'None', 'project_type': 'Own Funds',
         'project_end': 'None', 'project_start': '01.09.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/263866704?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101975056', 'title': 'Atlantic Future - Regionalism and inter-regionalism (WP8)',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2015',
         'project_start': '01.01.2013',
         'URL': 'https://cris.fau.de/converis/portal/Project/125810879?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104386248,239219621', 'title': 'Aufkommenseffekte von Steuerrechtsänderungen',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2022',
         'project_start': '01.01.2022',
         'URL': 'https://cris.fau.de/converis/portal/Project/267037038?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101494856',
                                       'title': 'Auswirkungen der Elterngeldreform auf Haushaltsstrukturen und Familiengründung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2016', 'project_start': '01.01.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/213945993?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760,103888408',
                                       'title': 'AVENUE - Zusammenstellung von Verfahren zur Ermittlung von neuen Formen der Arbeitsverdichtung und ihren Folgen sowie von Maßnahmen zur Prävention (Arbeitstitel: AVENUE)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.05.2021', 'project_start': '01.03.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/226649511?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105108214',
                                       'title': 'Bayessche Vorhersagemodelle auf Basis von Kontextinformationen für das Monitoring von Geschäftsprozessen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2018', 'project_start': '06.03.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/201722116?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Belastungen und Beanspruchung im Kontext atypischer Karrieren und flexibler Beschäftigungsverhältnisse',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2006', 'project_start': '01.01.2004',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235292115?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101872450',
                                       'title': 'Ausweitung der Bedarfsorientierten Budgetierung auf städtische berufliche Schulen mit Schwerpunkt Heterogenität',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2024', 'project_start': '01.10.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/266476875?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101872450',
                                       'title': 'Bedarfsorientierte Budgetierung an ausgewählte städtischen Berufsschulen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2021', 'project_start': '01.01.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/226019340?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101533762', 'title': 'Berufssprache Deutsch', 'funder': 'None', 'project_type': 'Own Funds',
         'project_end': '31.12.2014', 'project_start': '01.01.2011',
         'URL': 'https://cris.fau.de/converis/portal/Project/210774505?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '103586862',
                                       'title': 'Betriebsschließungen in Deutschland: Umfang, Verlauf und Einflussfaktoren',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.03.2013', 'project_start': '01.02.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126148710?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762,101734956',
                                       'title': 'Bildungsbenachteiligung und COVID-19: Herausforderungen und Auswirkungen des pandemiebedingten Homeschoolings sowie damit verbundener digitaler Lehr-Lernformate auf junge Geflüchtete in dualer Ausbildung.',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': '31.03.2021',
                                       'project_start': '01.04.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/250249303?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101530724',
                                       'title': 'BIRD steht für kaufmännische und gewerblich-technische Angebote zu Industrie 4.0 auf der Plattform der DQR-Stufe 5 als Motor der Durchlässigkeit zwischen Berufsausbildung und schulischer Fortbildung (Fach-/Technikerschule), IHK-Fortbildung (Fachwirt/in, Fachmeister/in) und akademischer Bildung (Bachelorstudium)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '29.02.2020', 'project_start': '01.09.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/228125107?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101530724',
                                       'title': 'Attraktive, durchlässige und Bildungs- und Beratungsangebote in der schulischen und außerschulischen beruflichen Aus- und Weiterbildung sowie der akademischen Bildung im blended-learning-Design am Beispiel neuer Anforderungen durch Industrie 4.0 unter strategischer Nutzung der ersten Fortbildungsstufe',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2024', 'project_start': '01.10.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/246600157?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105108214',
                                       'title': 'Internationales Forschnungsnetzwerk für E-Government zwischen Deutschland und Brasilien',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '30.06.2009', 'project_start': '01.01.2006',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126475556?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103861360', 'title': 'Careers in transition: Karrierecoaching und Karriereerfolg',
         'funder': 'None', 'project_type': 'Own Funds', 'project_end': 'None', 'project_start': '01.04.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/229903464?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '242689003,inv,inv', 'title': 'None', 'funder': 'None', 'project_type': 'Fremdprojekt',
         'project_end': 'None', 'project_start': '01.09.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/263863669?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101309146',
                                       'title': 'Kausale Effekte von Lohnsubventionen auf Arbeitsangebot und Arbeitsnachfrage',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2017', 'project_start': '01.01.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126123867?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760,104991104',
                                       'title': 'Veränderung von Covid-19-bezogenen Sorgen und Ängsten, Risikowahrnehmungen und Präventionsverhalten im Verlauf der Pandemie: Längsschnittliche Vorhersage präventionsbezogener Variablen in einer vulnerablen Stichprobe ehemals arbeitsloser Personen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2022', 'project_start': '01.01.2022',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/271344712?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Connecting the Cooperative (CoCo)', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '30.06.2016', 'project_start': '01.07.2013',
         'URL': 'https://cris.fau.de/converis/portal/Project/211012798?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246,101487604', 'title': 'Cooperatives in the Digital Age (CoDi)', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.03.2018', 'project_start': '01.10.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/126231182?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246,101487604',
                                       'title': 'Community-basierte Dienstleistungs-Innovation für e-Mobility (CODIFeY)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.10.2017', 'project_start': '01.11.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/203640687?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105782552',
                                       'title': 'Conjoint-basierte Bedürfnisanalyse von Kreditgenossenschaftskunden im digitalen Zeitalter und Implikationen für das genossenschaftliche Geschäftsmodell',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.04.2017', 'project_start': '01.05.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126163244?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100501136,102333246',
                                       'title': 'Advanced Systems Configuration zur komplexitätsreduzierten sensorgetriebenen Entwicklung von Produktionssystemen im digitalen Zeitalter (ConSensE)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '29.02.2024', 'project_start': '01.03.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/272534948?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Corporate Social Responsibility und die Attraktivität von Arbeitgebermarken am Beispiel von Genossenschaftsbanken',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': 'None', 'project_start': '01.04.2012',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229844855?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105782552', 'title': 'Creating the bank account of the future', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '30.04.2018', 'project_start': '01.10.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/200434253?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105108214', 'title': 'Nutzerakzeptanz und Dienstleistungskonzeption', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Sub project', 'project_end': '28.02.2015',
         'project_start': '01.12.2013',
         'URL': 'https://cris.fau.de/converis/portal/Project/126338835?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Methoden der Datenerhebung in den Sozial- und Verhaltenswissenschaften',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '28.02.2022', 'project_start': '01.03.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/248524831?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '275370701',
                                       'title': 'Data-driven analysis, benchmarking, and coordination of European IS-curricula',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.05.2023', 'project_start': '01.06.2022',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/276125534?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104052166',
                                       'title': 'Entwicklung der Systematik und der Algorithmen des Umfeld-Scanning-Systems',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.07.2020', 'project_start': '01.08.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/202426626?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101975056',
                                       'title': 'Debunking Interregionalism: concepts, types, critiques. German-Portuguese strategic action fund. To train young researchers.',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': 'None', 'project_start': '01.01.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/213823018?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104991104,101146760',
                                       'title': 'Deprivierte Bedürfnisse und inkongruente Werte - Untersuchungen zu den Ursachen des seelischen Leidens Arbeitsloser',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.07.2016', 'project_start': '01.08.2013',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126112544?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101585016',
                                       'title': 'Der Algorithmus, Dein Freund und Helfer: \r\nDatenbasierte Orientierungshilfe in der Studieneingangsphase des Bachelorstudiengangs Wirtschaftswissenschaften',
                                       'funder': 'None', 'project_type': 'FAU Funds', 'project_end': '30.09.2020',
                                       'project_start': '01.10.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/246311348?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102917228,104452594',
                                       'title': 'Der Einfluss von Patient Reported Outcomes auf die Akzeptanz von Qualitätstransparenzinitiativen für die Krankenhausauswahl',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2019', 'project_start': '01.02.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/216817177?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100550528',
                                       'title': 'Der Reification Bias in der Marketing-Kommunikation: Einflussfaktoren und Auswirkungen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.03.2020', 'project_start': '01.04.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126504286?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101320710', 'title': 'Designing Innovative Pedagogy for Complex Accountancy Topics',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.08.2021',
         'project_start': '01.09.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/208528908?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Determinanten der Verkehrsmittelwahl', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2001', 'project_start': '01.01.1999',
         'URL': 'https://cris.fau.de/converis/portal/Project/235284276?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105108214',
                                       'title': 'German-Brazilian Workshop on Management and Engineering of IT-Supported Business Networks, Administration Networks and Social Networks',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '31.07.2011', 'project_start': '01.04.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126486034?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101533762', 'title': 'Deutsch am Arbeitsplatz', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': '31.12.2013', 'project_start': '01.01.2011',
         'URL': 'https://cris.fau.de/converis/portal/Project/210773338?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101597854',
                                       'title': 'Deutsch-Russische Wirtschaftskooperation im Spannungsfeld von Geschäftsinteressen und unternehmerischer Verantwortung (am Beispiel des Energie- und Finanzsektors)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2022', 'project_start': '01.02.2022',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/270550569?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774,103589606',
                                       'title': 'Dezentralität und zellulare Optimierung – Auswirkungen auf den Netzausbaubedarf',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.06.2016', 'project_start': '10.03.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126509356?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103589606', 'title': 'B09 „Strategische Buchungsentscheidungen im Entry-Exit-System“',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '30.06.2022',
         'project_start': '01.07.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/205660185?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104386248', 'title': 'Die Lebenssteuerlast von Arbeitnehmern', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2018', 'project_start': '01.01.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/126516116?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Die Opferpersönlichkeit als Determinante von Mobbing in Organisationen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2011', 'project_start': '01.06.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229844146?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100248492',
                                       'title': 'Die Regulierung von Berufen und ihr Einfluss auf die Positionierung im Arbeitsmarkt',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2019', 'project_start': '01.01.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126217155?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102330404,100248492',
                                       'title': 'Die Regulierung von Berufen und ihr Einfluss auf die Positionierung im Arbeitsmarkt',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2019', 'project_start': '01.01.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/221696747?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104056282,103342548',
                                       'title': 'Die Wirkungen der Kurzarbeit: Eine Analyse an der Schnittstelle von dynamischer Makro-Arbeitsmarkttheorie und angewandter Ökonometrie',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '01.06.2018', 'project_start': '01.06.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126018073?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '103271008',
                                       'title': 'Die Wirkung von Defaults bei sequentiellen Entscheidungen – Unterschiede zwischen Einzel- und Paarentscheidungen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '01.02.2018', 'project_start': '01.02.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/238570667?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Diffusion von Innovationen. Eine prognostische Studie',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2008',
         'project_start': '01.01.2008',
         'URL': 'https://cris.fau.de/converis/portal/Project/235549895?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'DIGItal COllaboration Platforms as enablers of organizational exchange',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2024', 'project_start': '01.01.2022',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/267037910?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101270338,104628504,100710170,102364998,100228696,101449090,104452594',
         'title': 'Integratives Konzept zur personalisierten Präzisionsmedizin in Prävention, Früh-Erkennung, Therapie und Rückfallvermeidung am Beispiel von Brustkrebs',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '30.09.2024',
         'project_start': '01.10.2020',
         'URL': 'https://cris.fau.de/converis/portal/Project/250673737?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101270338,100710170,102364998,100228696,101449090,104452594',
                                       'title': 'Integratives Konzept zur personalisierten Präzisionsmedizin in Prävention, Früh-Erkennung, Therapie undRückfallvermeidung am Beispiel von Brustkrebs - DigiOnko',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2024', 'project_start': '01.10.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/250674114?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100248492', 'title': 'Digitale Kontrolle in Arbeitsverhältnissen', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Overall project', 'project_end': '30.11.2023',
         'project_start': '01.12.2020',
         'URL': 'https://cris.fau.de/converis/portal/Project/243893068?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103586862', 'title': 'Digitalisierung und ihre Arbeitsmarktwirkungen', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': 'None', 'project_start': '01.07.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/229908870?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103861360', 'title': 'Digitaler Stress', 'funder': 'None', 'project_type': 'Own Funds',
         'project_end': 'None', 'project_start': '01.04.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/126172877?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104385954', 'title': 'Digitization in Controlling and Reporting', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': 'None', 'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/210709292?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101487604',
                                       'title': 'Digitalisierung des zentralen Überlassungsprozesses in der Zeitarbeit',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.07.2020', 'project_start': '29.07.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235835986?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105707876,105628398',
                                       'title': 'Transforming digitally: Digitale Innovationen zur erfolgreichen Gestaltung desorganisationalen Wandels',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.03.2025', 'project_start': '01.04.2022',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/270752781?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100489180', 'title': 'Diversität und Erfolg von Organisationen', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '30.05.2012', 'project_start': '01.11.2010',
         'URL': 'https://cris.fau.de/converis/portal/Project/126084828?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100489180', 'title': 'Diversität und individuelle Karrieren', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '30.11.2017', 'project_start': '01.12.2012',
         'URL': 'https://cris.fau.de/converis/portal/Project/126027537?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101533762', 'title': 'Diversity Management an beruflichen Schulen', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2015',
         'project_start': '01.01.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/210685110?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101487604',
                                       'title': 'Digitale Dienstleistungen als Erfolgsfaktor für die Wertschöpfung der Zukunft',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.03.2021', 'project_start': '01.08.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/228058372?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101320710', 'title': 'E-Bilanzen', 'funder': 'None',
                                       'project_type': 'Third Party Funds Single', 'project_end': '31.03.2016',
                                       'project_start': '01.04.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/125808851?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100088458', 'title': 'Auswirkungen der Mietpreisbremse', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': '14.01.2018', 'project_start': '15.01.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/125983766?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101494856',
                                       'title': 'Eine komparative Analyse der Ursachen und Konsequenzen von Ungleichheit: wie wirken sich frühkindliche Bedingungen auf die Entwicklung von Kindern aus?',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.10.2016', 'project_start': '01.03.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/237122562?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104452594', 'title': 'Einführung der elektronischen Gesundheitskarte', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.08.2017', 'project_start': '01.10.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/126510539?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104373606',
                                       'title': 'Einführung in die unternehmerische Zukunftsforschung - Verbesserungsprojekt',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2021', 'project_start': '01.06.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/261463580?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Einführung von Mitarbeitergesprächen', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': '31.12.2001', 'project_start': '01.01.1999',
         'URL': 'https://cris.fau.de/converis/portal/Project/235286374?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Einführung von Mitarbeitergesprächen in einer Stadtverwaltung - Längsschnittstudie',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2007', 'project_start': '01.01.2006',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235548600?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Einstellungen, Bedenken, Selbstwirksamkeit und Intentionen von Lehramtsstudierenden mit Blick auf Inklusion',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': 'None',
                                       'project_start': '01.04.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/250322029?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '103586862',
                                       'title': 'Einstellungsverhalten, Beschäftigungsperspektiven und Entlohnung in neu gegründeten Betrieben',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': 'None',
                                       'project_start': '01.01.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/211416558?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105707876', 'title': 'Electronic Human Resources Management', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.08.2020', 'project_start': '01.03.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/211149887?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101530724',
                                       'title': 'Module Distance Education System as a new product for reducing the Education Job Mismatch in European Area',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '01.02.2017', 'project_start': '01.02.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/125788571?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774', 'title': 'Economy', 'funder': 'None',
                                       'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.12.2015', 'project_start': '29.07.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126472514?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774,104082252,102089422,100329440,105358016,101433312,103589606',
         'title': 'Energiemarktdesign', 'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
         'project_end': '31.12.2021', 'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/126328188?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774,103589606', 'title': 'Speicher B - Effiziente Wasserstofflogistik',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2021',
         'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/126249941?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246,100501136,101487604',
                                       'title': 'Methodische Konzeptentwicklung für Dienstleistungsplattformen und Schnittstellen, Service Systems Engineering, Kommunikationsdesign',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.06.2020', 'project_start': '01.07.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/125918532?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246',
                                       'title': 'Kommunikationsmanagement und Organisation der Gestaltung von Dienstleistungssystemen im Rahmen pilotierender Einführungen (ExTEND)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.04.2019', 'project_start': '01.10.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126239632?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103291000', 'title': 'Enhancing European teacher education through University schools',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '30.11.2020',
         'project_start': '01.12.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/209613121?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Entering the learning landscape: teacher innovations in classroom and social spaces – a cross-institutional study of trainee teachers by the Universities of Derby and Nuremburg',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': '31.12.2013',
                                       'project_start': '01.01.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210686807?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104452594',
                                       'title': 'Entwicklung eines Befragungsinstruments zur Erfassung von Patientenpräferenzen zum Medikationsmanagement in Deutschland',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2016', 'project_start': '02.02.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/202964987?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Entwicklung eines internationalen Online-Panels', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2006', 'project_start': '01.07.2003',
         'URL': 'https://cris.fau.de/converis/portal/Project/235291497?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104373606',
                                       'title': 'Entwicklung eines Lieferantenauswahl-Prozesses hinsichtlich ausgewählter Nachhaltigkeitskriterien - Sustainable Supplier Selection Process',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2015', 'project_start': '15.01.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/213827010?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774',
                                       'title': 'EOM+: Analyse der kurz- und mittelfristige Auswirkungen von marktbasierten Engpassinstrumenten als regionale und temporäre Ergänzung zum bestehenden Energy-Only-Marktdesign',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '31.10.2022', 'project_start': '01.11.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229944472?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102215842',
                                       'title': 'Erwerbsintegration oder Maßnahmekarriere? Förder- und Erwerbsverlaufmuster von jungen Maßnahmeteilnehmer/innen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2017', 'project_start': '01.01.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/211298853?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101573844', 'title': 'Die Europawahl 2014 in den Medien', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': '31.12.2014', 'project_start': '01.03.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/231679316?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101975056', 'title': 'The Reconfiguration of the EU presence in Latin America',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.08.2022',
         'project_start': '01.09.2020',
         'URL': 'https://cris.fau.de/converis/portal/Project/252964093?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Evaluation eines Auswahlverfahrens hochbegabter Studierender für Studien- und Promotionsstipendien',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2009', 'project_start': '01.01.2009',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235561001?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774', 'title': 'Evaluation eines Smart Grid-Feldexperiments', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2015', 'project_start': '01.01.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/126331906?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Evaluation von Mitarbeitergesprächen (Stadt Fürth)', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2003', 'project_start': '01.01.2001',
         'URL': 'https://cris.fau.de/converis/portal/Project/235287512?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Evaluation von Trainings gegen Informationsüberflutung',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2003',
         'project_start': '01.01.2002',
         'URL': 'https://cris.fau.de/converis/portal/Project/235288576?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774,101582370',
                                       'title': 'Experimentelle Studien zur Auswirkung von kollektiven Lohnverhandlungen auf den Gender Wage Gap',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.12.2015', 'project_start': '01.12.2012',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126316696?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774,105006980',
                                       'title': 'Experimentelle Validierung von Indikatoren des Managerverhaltens in Betriebsbefragungen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2016', 'project_start': '02.04.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126396126?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Expertenstudie zur Reliabilität und Validität von Arbeitszeugnissen',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '30.04.2015',
         'project_start': '01.11.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/235210146?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '242689003,inv,inv', 'title': 'None', 'funder': 'None', 'project_type': 'Own Funds',
         'project_end': 'None', 'project_start': '01.08.2021',
         'URL': 'https://cris.fau.de/converis/portal/Project/263864679?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103256700', 'title': 'Schöller-Fellowship von Frau Dr. Cynthia Sende', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '19.06.2018', 'project_start': '20.06.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/201311736?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105108214', 'title': 'Föderales Informationsmanagement', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': '31.12.2012', 'project_start': '04.12.2012',
         'URL': 'https://cris.fau.de/converis/portal/Project/126487893?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102215842,inv',
                                       'title': 'Kompromissbildung und deren Konsequenzen - Pfadabhängigkeiten zwischen Berufsfindung, Bildungsentscheidungen und Ausbildungsverläufen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2021', 'project_start': '01.10.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126398323?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Flexibilisierte Beschäftigungsverhältnisse und die Beziehung zwischen Mitarbeitern und Unternehmen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2007', 'project_start': '01.01.2006',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235558885?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Integrations- und Kompetenzmanagement im Kontext von Flexibilisierungsstrategien bei KMU',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.04.2013', 'project_start': '01.07.2009',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229843182?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774,103589606', 'title': 'Flexible Verbraucher im Deutschen Strommarkt',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.01.2016',
         'project_start': '01.11.2015',
         'URL': 'https://cris.fau.de/converis/portal/Project/126460008?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105108214',
                                       'title': 'Flexible Informationssystem-Architekturen für hybride Wertschöpfungsnetzwerke',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '31.03.2010', 'project_start': '01.10.2006',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126491104?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246',
                                       'title': 'Mit Flexudy wollen wir Studierenden ein zeiteffizientes und mobiles Lernen ermöglichen. Mit Hilfe künstlicher Intelligenz generiert unsere Technologie aus jeglichen Lernmaterialien in verschiedenen Sprachen automatisiert Fragen-Antwort Karteikarten, Multiple Choice Fragen, Lückentexte und Zusammenfassungen.',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2021', 'project_start': '01.10.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/250326027?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105108214', 'title': 'FOKUS:SE - Das Forschernetzwerk Service Engineering',
         'funder': 'None', 'project_type': 'Own Funds', 'project_end': '01.01.2018', 'project_start': '01.01.2015',
         'URL': 'https://cris.fau.de/converis/portal/Project/126460853?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Förderung sprachlich-kommunikativer Fähigkeiten in der betrieblichen Ausbildung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.12.2014', 'project_start': '01.01.2013',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210685913?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760,103256700',
                                       'title': 'Forschungsvorhaben zur Untersuchung von Mediennutzung und Studienerfolg',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2019', 'project_start': '01.08.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229847147?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '103271008,100502116', 'title': 'Forum V', 'funder': 'None',
                                       'project_type': 'Third Party Funds Single', 'project_end': '31.05.2026',
                                       'project_start': '01.06.2013',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126170173?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105108214', 'title': 'Automatisiertes Content-Providing durch Smarte Steuersysteme',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2019',
         'project_start': '01.01.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/126488907?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246',
                                       'title': 'Führung und Zusammenarbeit im Kontext von Open Innovation bei der AUDI AG',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2013', 'project_start': '01.01.2012',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/125826089?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '248294705', 'title': 'Gamifizierung der Mensch-KI-Interaktion', 'funder': 'None',
         'project_type': 'FAU Funds', 'project_end': '30.06.2022', 'project_start': '01.07.2021',
         'URL': 'https://cris.fau.de/converis/portal/Project/276430350?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246,101487604',
                                       'title': 'Entwicklung von Big-Data-Dienstleistungen und Baukasten-Prototyping mit KMUs (BigDieMo)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.04.2019', 'project_start': '01.10.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126241322?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774,103480140', 'title': 'Zentrum Wasserstoff Bayern', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '30.09.2024', 'project_start': '01.10.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/230023648?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246',
                                       'title': 'Entwicklung von Methoden und Werkzeugen für smarte und nachhaltigkeitsorientierte Produkt-Service-Systeme',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.05.2023', 'project_start': '01.06.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/239536186?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '212658212',
                                       'title': 'Heterogenität makroökonomischer Erwartungen: Welche Rolle spielen individuelle historische Erfahrungen, das örtliche Umfeld und sozioökonomische Faktoren?',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.06.2022', 'project_start': '01.07.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210972719?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101585016',
                                       'title': 'Wie wirkt sich die Geschlechterzusammensetzung auf die Leistung von Teams aus?',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.11.2023', 'project_start': '01.12.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/246311837?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '103203388',
                                       'title': 'Identifikation von Automatisierungspotentialen mit Process Mining (IdAP)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '28.02.2021', 'project_start': '01.03.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/221187754?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104452594', 'title': 'Pharmaökonomie', 'funder': 'None',
                                       'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.09.2017', 'project_start': '01.12.2013',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/125836229?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Integriertes Fach- und Sprachlernen in Beruflicher (Anpassungs-) Qualifizierung - Berufsfeldbezogene Weiterbildung für Lehrende und Bildungsbegleitende',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2017', 'project_start': '01.07.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126165610?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101487604',
                                       'title': 'IIP-Ecosphere - Next Level Ecosphere for Intelligent Industrial Production',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2022', 'project_start': '01.01.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/234097982?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100502116',
                                       'title': 'Implizite Einschränkungen, Anreize und Systemische Risiken: Implikationen der neuen Versicherungsregulierung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2014', 'project_start': '01.01.2013',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126174398?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '242689003,101601774,105655152', 'title': 'None', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': 'None', 'project_start': '01.07.2021',
         'URL': 'https://cris.fau.de/converis/portal/Project/263863924?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105782552',
                                       'title': 'Wertschöpfungsübergreifende Implementierung von Industrie 4.0 bei der Robert Bosch GmbH',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.01.2020', 'project_start': '01.01.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/242032269?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Steigende Informationsflut am Arbeitsplatz - belastungsgünstiger Umgang mit elektronische Medien (E-Mail, Internet)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2002', 'project_start': '01.01.2000',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126304528?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100502116',
                                       'title': 'Investitionen in Infrastruktur und Erneuerbare Energien aus Sicht der Versicherungsindustrie',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.05.2017', 'project_start': '01.06.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126175412?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Innovation Leadership/Business Management Executive Education',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2016',
         'project_start': '01.01.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/126242336?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104421920', 'title': 'TransitionLab 2 - Umsetzungsphase, TP D', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Sub project', 'project_end': '30.11.2022',
         'project_start': '01.12.2021',
         'URL': 'https://cris.fau.de/converis/portal/Project/273174671?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Engagement internationaler Studierender als Element der Regionalentwicklung',
                                       'funder': 'None', 'project_type': 'Fremdprojekt', 'project_end': '31.12.2017',
                                       'project_start': '01.01.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210773039?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762,103205936',
                                       'title': 'InTAK: Interkulturelles Training für Neuzugewanderte – Angemessenes\r\nsprachliches Handeln in beruflichen Kommunikationssituationen',
                                       'funder': 'None', 'project_type': 'FAU Funds', 'project_end': '31.08.2023',
                                       'project_start': '01.10.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/265753095?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101305324,101487310',
                                       'title': 'Anforderungsanalyse, Entwicklung der Motivationsstrategie und des Geschäftsmodells, Test und Evaluierung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.08.2021', 'project_start': '01.09.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/205613594?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103342548', 'title': 'Interdependencies of Labor Market Reforms and the Business Cycle',
         'funder': 'None', 'project_type': 'Own Funds', 'project_end': 'None', 'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/210710543?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101975056',
                                       'title': 'Internationale Entwicklung im 21. Jahrhundert – Wo steht Lateinamerika in der Weltpolitik?',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': 'None', 'project_start': '01.09.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/228195674?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104386248', 'title': 'Internationale Unternehmensbesteuerung und Konzernstrukturen',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '30.06.2012',
         'project_start': '01.06.2010',
         'URL': 'https://cris.fau.de/converis/portal/Project/126056943?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774', 'title': 'Internationales Doktorandenkolleg (IDK) „Evidence Based Economics“',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project', 'project_end': '30.09.2017',
         'project_start': '01.10.2013',
         'URL': 'https://cris.fau.de/converis/portal/Project/126108826?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Internetbasiertes Railpanel', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2000', 'project_start': '01.01.1999',
         'URL': 'https://cris.fau.de/converis/portal/Project/235283787?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101975056', 'title': 'Interregionalism as a foreign policy tool: new concepts and trends',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2018',
         'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/200431535?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100248492', 'title': 'The Invisible Wall: Distinct Firm Networks in West and East Berlin',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '30.06.2019',
         'project_start': '01.07.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/226959649?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246,101487604', 'title': 'JOSEPHS® - Die Service Manufaktur', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': 'None', 'project_start': '01.01.2013',
         'URL': 'https://cris.fau.de/converis/portal/Project/126245547?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101533762', 'title': 'Karriereplanung für Open Source Software-Entwickler',
         'funder': 'None', 'project_type': 'Own Funds', 'project_end': '31.12.2012', 'project_start': '01.01.2011',
         'URL': 'https://cris.fau.de/converis/portal/Project/210774315?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101309146',
                                       'title': 'Kausale Effekte von Lohnsubventionen auf Arbeitsangebot und Arbeitsnachfrage',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2018', 'project_start': '01.10.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/237122857?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Kompetenzentwicklung und Modulare Übergangsbegleitung in den Ausbildungs- und Arbeitsmarkt',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.12.2014', 'project_start': '01.01.2012',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210686144?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104437110', 'title': 'Kreditrating', 'funder': 'None',
                                       'project_type': 'Third Party Funds Single', 'project_end': 'None',
                                       'project_start': '01.01.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/211410229?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Entwicklung einer Online-Recruitingplattform mit kulturbasiertem Jobmatching und Screening',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.04.2018', 'project_start': '01.05.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/202449725?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103271008', 'title': 'Eine Kundenanalyse zu SmartHome-Anwendungen bei Hörgeräten',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '07.02.2017',
         'project_start': '18.10.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/126267517?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105707876',
                                       'title': 'Künstliche Intelligenz, Chatbots und Rekrutierung: Die Sicht der Kandidaten',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2021', 'project_start': '01.11.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/208483806?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103586862', 'title': 'Löhne und Lohndifferenziale', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': 'None', 'project_start': '01.01.2000',
         'URL': 'https://cris.fau.de/converis/portal/Project/229909112?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Längerfristige Effekte von Networking im Karriereverlauf',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2010',
         'project_start': '01.03.2010',
         'URL': 'https://cris.fau.de/converis/portal/Project/229844625?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246,101487604', 'title': 'Leistungszentrum Elektroniksysteme (LZE)', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Overall project', 'project_end': '31.12.2017',
         'project_start': '01.01.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/213936695?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101487604,102333246',
                                       'title': 'Wirtschaftswissenschaftliche Begleitung des Leistungszentrum Elektroniksysteme LZE Phase II',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2020', 'project_start': '03.12.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/233554892?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104056282', 'title': 'Makroökonomische Implikationen der Hartz IV-Arbeitsmarktreform',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '30.04.2022',
         'project_start': '01.05.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/216980616?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100502116',
                                       'title': 'Marktkonsistente Bewertung und Solvenzmessung in der Versicherungsindustrie',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2012', 'project_start': '01.01.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126175243?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Maßnahmen und Empfehlungen für die gesunde Arbeit von morgen (MEgA)',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '30.04.2019',
         'project_start': '01.06.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/126212085?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104991104,101146760',
                                       'title': 'Die Effektivität von Interventionen zur Gesundheitsförderung und -Prävention bei Arbeitslosen – eine Metaanalyse',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2021', 'project_start': '01.09.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/246075156?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246,103652228',
                                       'title': 'Metaprojekt BALANCE: Flexibilität und Stabilität in der Forschungswelt',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '31.12.2013', 'project_start': '01.09.2009',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126476908?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101494856', 'title': 'Midijobs verstehen', 'funder': 'None',
                                       'project_type': 'Third Party Funds Single', 'project_end': '30.09.2021',
                                       'project_start': '01.10.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/216980841?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100088458', 'title': 'gif Policy Paper: Angebotseffekte der Mietpreisbremse',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2018',
         'project_start': '01.07.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/203409396?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774',
                                       'title': 'Zugehörigkeit Frau Prof. Dr. Veronika Grimms zur Kommission aus Energieexperten zur Unterstützung des Monitoring-Prozesses zur Überprüfung des Maßnahmenprogramms der Bundesregierung, mit dem Ziel sich zu einer der energieeffizientesten und umweltschonendsten Volkswirtschaften der Welt zu entwickeln.',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.06.2023', 'project_start': '01.07.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/226016315?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103586862', 'title': 'Monopsonistische Diskriminierung am deutschen Arbeitsmarkt',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '30.11.2015',
         'project_start': '01.01.2009',
         'URL': 'https://cris.fau.de/converis/portal/Project/211299156?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Persönliches Wachstum in Beruf, Ausbildung und Leben: Ein Kurs zur Motivationssteigerung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2022', 'project_start': '01.04.2022',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/272753030?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101532292',
                                       'title': 'Nachhaltige Weiterentwicklung der betrieblichen Informationsverarbeitung',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': 'None',
                                       'project_start': '01.01.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/231732152?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100489180', 'title': 'NEPS', 'funder': 'None', 'project_type': 'Third Party Funds Single',
         'project_end': '31.12.2016', 'project_start': '01.01.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/125975147?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Networking: Eine Längsschnittstudie (Hans-Frisch-Stiftung)',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2004',
         'project_start': '01.01.2001',
         'URL': 'https://cris.fau.de/converis/portal/Project/235288035?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101487604', 'title': 'Neue Arbeitswelten in Pilotflächen', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.03.2020', 'project_start': '01.10.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/201306732?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104385954', 'title': 'Nichtfinanzielle Unternehmenspublizität', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': 'None', 'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/210709481?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104452594', 'title': 'NN / NZ Klinikcheck', 'funder': 'None', 'project_type': 'Own Funds',
         'project_end': 'None', 'project_start': '01.01.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/265666346?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105329106',
                                       'title': 'Objektive und subjektiv erfahrene finanzielle Ungleichheit von Einkommen und Vermögen und deren Konsequenzen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.08.2024', 'project_start': '01.09.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/258843837?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '239219621',
                                       'title': 'Ökonomische Effekte aus einem bürgerfreundlichen Einkommensteuerbescheid',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2021', 'project_start': '01.01.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/250333875?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101487604', 'title': 'Service Innovation 2019 – Open Service Lab', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2019', 'project_start': '01.01.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/232130608?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102917228',
                                       'title': 'Patientenzufriedenheit in den sozialen Medien – Handlungsempfehlung für niedersächsische Kliniken',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '31.08.2021', 'project_start': '01.09.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/242851869?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105108214', 'title': 'Software-Prototypen für die erfahrbare Integration', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Sub project', 'project_end': '30.11.2015',
         'project_start': '01.12.2013',
         'URL': 'https://cris.fau.de/converis/portal/Project/126473866?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Performance Management in Teams', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.08.2017', 'project_start': '01.09.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/203233379?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760,105006980', 'title': 'Personalpolitik in genossenschaftlichen Unternehmen',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '30.04.2014',
         'project_start': '01.04.2013',
         'URL': 'https://cris.fau.de/converis/portal/Project/229845061?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101305324', 'title': 'Prescriptive healthcare analytics', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2019', 'project_start': '01.01.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/217300806?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760,103861360',
                                       'title': 'Projektseminar zur praxisorientierten Vermittlung von Moderations- und Evaluationskompetenzen anhand eines Trainings zur Bewältigung von digitalem Stress',
                                       'funder': 'None', 'project_type': 'FAU Funds', 'project_end': '30.09.2018',
                                       'project_start': '01.04.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229846209?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105108214',
                                       'title': 'Deutsch-Russisches Innovationsforum - Promoting business process management excellence in Russia',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '30.04.2012', 'project_start': '01.11.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126342891?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Psychologische Aspekte der Leiharbeit', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2002', 'project_start': '01.01.2000',
         'URL': 'https://cris.fau.de/converis/portal/Project/235286076?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Psychologisches Kapital als Determinante von Eskalierendem Commitment in Organisationen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.06.2013', 'project_start': '01.03.2013',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229843930?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101320710',
                                       'title': 'Public financial disclosure and labor costs: Empirical evidence from a quasi-experiment',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '01.07.2019', 'project_start': '01.01.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/213828632?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105108214', 'title': 'PUSH Münsterland: Produkt-Servicekombinationen entwickeln und nutzen',
         'funder': 'None', 'project_type': 'Fremdprojekt', 'project_end': '14.08.2015', 'project_start': '15.08.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/126251462?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Anschlüsse eröffnen - Entwicklungen ermöglichen.\r\nQualifizierungsbausteine inklusiv in einer dualisierten Ausbildungsvorbereitung',
                                       'funder': 'None', 'project_type': 'Fremdprojekt', 'project_end': '30.06.2018',
                                       'project_start': '01.01.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210687479?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104452594',
                                       'title': 'Qualitätstransparenz in der Hüftendoprothetik durch Patient Reported Outcomes',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.04.2022', 'project_start': '01.05.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/239358876?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102917228',
                                       'title': 'Qualitätstransparenz in der Hüftendoprothetik durch Patient Reported Outcomes',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '28.02.2022', 'project_start': '01.01.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/208670663?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Rechtfertigungsdruck und eskalierendes Commitment', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2005', 'project_start': '01.01.2003',
         'URL': 'https://cris.fau.de/converis/portal/Project/235290009?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Reziprozitätsprozesse im Kontext von Peer-Feedback', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.10.2018', 'project_start': '01.01.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/204086652?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101975056',
                                       'title': 'Relations between the European Union and Latin America: Future scenarios in a changing world',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': 'None', 'project_start': '01.07.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/253525846?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774,100248492', 'title': 'Die Entstehung von Reputation in Wirtschaftsbeziehungen',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '20.09.2012',
         'project_start': '01.04.2010',
         'URL': 'https://cris.fau.de/converis/portal/Project/126395450?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Forschung zu den psychischen Auswirkungen von Arbeitslosigkeit',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.03.2017',
         'project_start': '01.10.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/235000494?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Resilire - Altersübergreifendes Resilienz-Management',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project', 'project_end': '31.12.2017',
         'project_start': '01.11.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/126176257?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760,101148916', 'title': 'Resilire - Altersübergreifendes Resilienz-Management',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project', 'project_end': '31.10.2017',
         'project_start': '01.11.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/126433813?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246',
                                       'title': 'Maschinenfehlerdiagnose und Entwicklung von Rollen, Views, Schnittstellen und Anwender-Mockup',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.12.2016', 'project_start': '01.01.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/211013315?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105108214',
                                       'title': 'Propelling Business Process Management by Research and Innovation Staff Exchange',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.04.2019', 'project_start': '01.05.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126486372?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101320710',
                                       'title': 'Social Media-Kanäle als Informations\xadintermediäre (Schöller Junior Fellow 2017 Tim Herberger)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': 'None', 'project_start': '01.01.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/213829478?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Selbstkonzept und Selbstbeurteilung beruflicher Leistung',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2004',
         'project_start': '01.01.2003',
         'URL': 'https://cris.fau.de/converis/portal/Project/235290786?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101487604', 'title': 'Service Innovation (Teilvereinbarung 2017)', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2017', 'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/226980444?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Service Innovation – Teilvereinbarung 2018', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2018', 'project_start': '01.01.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/226532119?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Service Innovation Teilprojekt Vereinbarung 2012', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2012', 'project_start': '01.01.2012',
         'URL': 'https://cris.fau.de/converis/portal/Project/125854481?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Service Innovation Teilprojekt Vereinbarung 2013', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2013', 'project_start': '01.01.2013',
         'URL': 'https://cris.fau.de/converis/portal/Project/125803950?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Service innovation - Teilvereinbarung 2014', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2014', 'project_start': '01.01.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/126012158?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Service innovation - Teilvereinbarung 2015', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2015', 'project_start': '01.01.2015',
         'URL': 'https://cris.fau.de/converis/portal/Project/125804795?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Service innovation - Teilvereinbarung 2016', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2016', 'project_start': '01.01.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/126214451?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774,105358016,101433312,103589606',
                                       'title': 'Wohlfahrtsoptimale Nominierungen in Gasnetzen und zugehörige Gleichgewichte',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.06.2018', 'project_start': '01.10.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126509525?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104373606,212578052',
                                       'title': 'Siemens Competence Center Foresight für die industrielle Automatisierung und Digitalisierung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': 'None', 'project_start': '01.06.2022',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/274757098?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101597854',
                                       'title': 'Sino-German Perspectives on Corporate Social Responsibility and Sustainable Development',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2022', 'project_start': '01.01.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/233205494?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105108214',
                                       'title': 'Bilaterale Kooperationsanbahnung Brasilien - Evaluating Standards for Interorganizational Process Integration in Brazilian-German Value Networks',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': '31.05.2010',
                                       'project_start': '01.05.2010',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126488062?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '228682808,101585016',
                                       'title': 'Fähigkeiten, Erwartungen und Persönlichkeit als Determinanten des fächerspezifischen Studienerfolges',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2023', 'project_start': '01.10.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/246312300?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Skype as instrument to promote intercultural competences - a cross-cultural study between students of Germany and England',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': '31.12.2013',
                                       'project_start': '01.01.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210775078?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101487604,102333246',
                                       'title': 'Methodik und Konzeption für ein Fakten-basiertes Service Engineering (SmartDiF)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.08.2019', 'project_start': '01.09.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126240646?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246',
                                       'title': 'Harmonisierung der Entwicklung von komplexen Produkt-Smart-Service-Systemen bei KMU',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '31.05.2023', 'project_start': '01.06.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/239451749?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105108214',
                                       'title': 'smartmarket²: Entwicklung mobiler Applikationen für standortbezogene Dienstleistungen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '29.02.2020', 'project_start': '01.03.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126489583?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '103203388',
                                       'title': 'Analyse von Positonsdaten zur Ermittlung von Durchlaufzeiten in der Fertigung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.01.2021', 'project_start': '01.04.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/237637268?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '235233833',
                                       'title': 'Ein Brückenschlag: Reinforcement Learning auf Molekül- und Prozessgraphen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '28.02.2022', 'project_start': '01.03.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/248230232?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '219128459', 'title': 'Multidimensionales Conformance Checking für Prozesse',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.01.2023',
         'project_start': '01.02.2021',
         'URL': 'https://cris.fau.de/converis/portal/Project/247978698?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '203599239', 'title': 'Deep Learning im Kontext von Predictive Maintenance',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2021',
         'project_start': '01.01.2020',
         'URL': 'https://cris.fau.de/converis/portal/Project/231273464?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '228208413', 'title': 'Digitales Nudging und persuasives Design im Software-Kontext',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.01.2023',
         'project_start': '01.02.2021',
         'URL': 'https://cris.fau.de/converis/portal/Project/248303281?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105358800',
                                       'title': 'Interorganisationale Interdependenzen in Industrial-Internet-of-Things Geschäftsmodellen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.12.2020', 'project_start': '01.01.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/221261171?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '227730973', 'title': 'Nonparametric Bayesian Learning in Distributed Systems',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.01.2023',
         'project_start': '01.02.2021',
         'URL': 'https://cris.fau.de/converis/portal/Project/248241839?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774,103589606', 'title': 'Implementierung im Marktumfeld', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2015',
         'project_start': '01.06.2012',
         'URL': 'https://cris.fau.de/converis/portal/Project/126509694?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Soziale Beziehungen zwischen Lernenden an beruflichen Schulen fördern: Abbau von Vorurteilen, Umgang mit Diskriminierung und Toleranzerziehung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.12.2016', 'project_start': '01.01.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210571289?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Soziale und ökonomische Kosten der Erwerbslosigkeit',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2020',
         'project_start': '01.01.1999',
         'URL': 'https://cris.fau.de/converis/portal/Project/235278882?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104373606,204206709', 'title': 'Spedicam & Logistik GmbH goes digital', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.05.2021', 'project_start': '01.06.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/239353667?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Evidenzbasiertes Motivationsmanagement zur Leistungsoptimierung im Profisport',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2013', 'project_start': '01.10.2012',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229841948?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101494856',
                                       'title': 'Erwerbstätigkeit von Müttern und kindliche Entwicklung: Eine Analyse der Determinanten im gesellschaftlichen Wandel',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.09.2017', 'project_start': '01.08.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/125846538?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102330404', 'title': 'Ausländische Bildungszertifikate auf dem deutschen Arbeitsmarkt',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.07.2017',
         'project_start': '01.08.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/125966021?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100248492', 'title': 'Ausländische Bildungszertifikate auf dem deutschen Arbeitsmarkt',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': 'None',
         'project_start': '01.08.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/126188594?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103222008', 'title': 'Löhne, Heterogenitäten und Arbeitsmarktdynamik', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2020',
         'project_start': '01.08.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/125914307?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101533762', 'title': '„Sprachförderung“ an der FOS Regensburg', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': '31.12.2013', 'project_start': '01.01.2012',
         'URL': 'https://cris.fau.de/converis/portal/Project/210774885?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101533762', 'title': 'Sprachförderung im fachlichen Unterricht an berufsbildenden Schulen',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2015',
         'project_start': '01.01.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/210684911?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Sprachsensibilisierung in der beruflichen Qualifizierung – Entwicklung und Erprobung von Qualifizierungsmodulen für Lehrkräfte in der beruflichen Weiterbildung für Migrantinnen und Migranten',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.12.2014', 'project_start': '01.01.2013',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210685301?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105782552', 'title': 'Sustainable Smart Industry', 'funder': 'None',
         'project_type': 'FAU Funds', 'project_end': '31.12.2018', 'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/126495836?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101320710', 'title': 'Smart Teaching in Accounting - Meeting Place Online',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '29.12.2022',
         'project_start': '30.12.2020',
         'URL': 'https://cris.fau.de/converis/portal/Project/261258597?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Stark in Alltag und Arbeit', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.08.2019', 'project_start': '01.09.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/203495671?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246,101487604',
                                       'title': '7 start-up summer schools in Europe on Information and Communications Technologies for young aspiring entrepreneurs',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2016', 'project_start': '01.01.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/213933123?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104386248,101309930', 'title': 'Steuerliche Anreize für Unternehmensansiedlungen',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2019',
         'project_start': '01.01.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/208484053?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100489180',
                                       'title': 'Stigma-Bewusstsein von Arbeitslosen und Vorurteile gegenüber Arbeitslosen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.06.2017', 'project_start': '01.07.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126107981?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Stimmung und Kategorisierung: Zum Einfluß emotionaler Zustände auf berufseignungsdiagnostische  Urteilsprozesse',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.1999', 'project_start': '01.01.1997',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235266965?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101320710',
                                       'title': 'Cooperation and Innovation for Good Practices – „International Learning Platform for Accountancy (ILPA)“',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.08.2017', 'project_start': '01.09.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/211009466?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104373606,102369016', 'title': 'Studie zur Digitalisierung im Mittelstand',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2017',
         'project_start': '01.07.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/204126968?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'SummerSchool "Electronic Monitoring" (10.-12.9.2018)',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.10.2018',
         'project_start': '01.01.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/236579489?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760,100489180',
                                       'title': 'Summer School: The Interplay of Work, Health and Organizational Success',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2014', 'project_start': '01.04.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235002008?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100502116',
                                       'title': 'Sustainable Business Models in Energy Markets: Perspectives for the Implementation of Smart Energy Systems',
                                       'funder': 'None', 'project_type': 'FAU Funds', 'project_end': '31.12.2016',
                                       'project_start': '01.01.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126391394?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101567376,101489466,101601774',
                                       'title': 'Koordinierte Kleinspeicher im Verteilnetz der N-ERGIE Aktiengesellschaft - Storage With Amply Redundant Megawatt (SWARM)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2017', 'project_start': '01.01.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126212930?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Symposium „Individuals in Temporary Agency Jobs“.', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.05.2007', 'project_start': '01.01.2007',
         'URL': 'https://cris.fau.de/converis/portal/Project/236493456?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774',
                                       'title': 'Taxation, Social Norms, and Compliance: Lessons for Institution Design',
                                       'funder': 'None', 'project_type': 'FAU Funds', 'project_end': '31.12.2014',
                                       'project_start': '01.01.2012',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/125938305?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100710170,101601774,104848514',
                                       'title': 'Teamwork Performance: Effects of Tracking Based Feedback Mechanisms on Performance and Health Biomarkers',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': 'None',
                                       'project_start': '01.03.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126151583?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101975056', 'title': 'The Bavarian Scientific Expedition to Brazil (1817-1820)',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': 'None',
         'project_start': '01.09.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/239284640?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101320710',
                                       'title': 'The Effects of the Financial Crisis on Cooperative Banks in Europe – A Critical Comparison',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.06.2017', 'project_start': '01.01.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/213828851?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100248492,102330404',
                                       'title': 'Die Arbeitsmarktintegration qualifizierter MigrantInnen im internationalen Vergleich',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.09.2020', 'project_start': '01.10.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/202161989?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Die psychologische Bedeutung von Arbeit', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.08.2018', 'project_start': '01.09.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/202228384?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'The R and RStudio Environment. Handling, Visualisation und Communication of Data in Science',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '28.02.2021', 'project_start': '01.03.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/234197063?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774', 'title': 'Die Rolle von Sozialer Identität für das Lernen in Netzwerken',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '09.10.2021',
         'project_start': '01.10.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/228016913?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101305324',
                                       'title': 'Entwicklung von Maßnahmen zur Schaffung von Transparenz und Vertrauen in DataAnalytics-Projekten',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '29.02.2020', 'project_start': '01.03.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/226959158?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774,101433312',
                                       'title': 'Mehrstufige gemischt-ganzzahlig nichtlineare Optimierung für Gasmärkte (B08) (2018 - 2022)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.06.2022', 'project_start': '01.07.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/204141447?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774', 'title': 'Trust in Character, Capability and Institutions', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.05.2015', 'project_start': '01.06.2012',
         'URL': 'https://cris.fau.de/converis/portal/Project/126408801?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104437110', 'title': 'Twitter-Daten', 'funder': 'None',
                                       'project_type': 'Third Party Funds Single', 'project_end': 'None',
                                       'project_start': '01.01.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/211410028?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Umsetzungskonzept: Training gegen Informationsüberflutung',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2003',
         'project_start': '01.01.2003',
         'URL': 'https://cris.fau.de/converis/portal/Project/235289231?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103342548', 'title': 'Understanding Job Creation: The Role of Firm Age and Job Duration',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2017',
         'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/202306978?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104386248', 'title': 'Steuerhinterziehung und Steuerbetrug bei der Mehrwertsteuer',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '30.09.2018',
         'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/125974302?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101585016',
                                       'title': 'Unternehmen, Märkte, Volkswirtschaften: Von der Massenveranstaltung zum arbeitsgruppenorientierten Forum.\r\nEin Pilot für die Transformation der Lehre in den WiSo‐Bachelorstudiengängen',
                                       'funder': 'None', 'project_type': 'FAU Funds', 'project_end': '30.09.2020',
                                       'project_start': '01.10.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/246311579?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102369016',
                                       'title': 'Vereinbarkeit strategischer Entscheidungen im Rahmen der digitalen Transformation mit moralisch-ethischen Werten der Mitarbeiter',
                                       'funder': 'None', 'project_type': 'FAU Funds', 'project_end': 'None',
                                       'project_start': '01.07.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/275131357?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104386248',
                                       'title': 'Einrichtung eines wissenschafttlichen Dienstes an der FAU im Rahmen der erneuten Übernahme des Vorsitzes des Unabhängigen Beirats beim Stabilitätsrat durch Herrn Prof. Dr. Büttner',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.08.2022', 'project_start': '01.09.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/264525710?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246,101487604',
                                       'title': 'Open Innovation für IT-Sicherheit Kritischer Infrastrukturen (VeSiKi)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.06.2018', 'project_start': '01.01.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126239801?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100502116,103271008', 'title': 'verschiedene Dienstleistungen', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.05.2026', 'project_start': '01.01.2012',
         'URL': 'https://cris.fau.de/converis/portal/Project/125827779?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Verwaltungsbenchmarking süddeutscher Universitäten', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': '31.12.2007', 'project_start': '01.01.2006',
         'URL': 'https://cris.fau.de/converis/portal/Project/235546753?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104452594',
                                       'title': 'Entwicklung eines Weiterbildungsangebotes im Bereich der altersgerechten Assistenzsysteme (AAL) für die Europäische Metropolregion Nürnberg (EMN)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2014', 'project_start': '01.07.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/239359745?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101487604', 'title': 'Weiterbildungszentrum Digital Transformation', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.03.2021', 'project_start': '01.01.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/238566523?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101530724', 'title': 'Weichenstellung', 'funder': 'None',
                                       'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.07.2022', 'project_start': '01.04.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/208609420?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104452594', 'title': 'Weiterbildungsprogramm Telemedizin', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '30.09.2016', 'project_start': '01.08.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/213950547?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100088458', 'title': 'Wer profitiert vom Wohnungsneubau?', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '30.06.2021', 'project_start': '01.07.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/204192458?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246,103652228',
                                       'title': 'WiIPOD Wertschätzungsnetzwerke als integrierte Innovationsinstrumente der Personal- und Organisationsentwicklung im Demografischen Wandel',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '30.04.2015', 'project_start': '01.08.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126283572?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101975056', 'title': 'Wirtschaft, Politik und Gesellschaft in Lateinamerika',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': 'None',
         'project_start': '01.09.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/203496385?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246',
                                       'title': 'Einführung und Verankerung des Karrierewegs der Tenure-Track-Professur, die vollständig den Anforderungen der Verwaltungsvereinbarung zwischen Bund und Ländern gemäß Artikel 91b Absatz 1 des Grundgesetztes über ein Programm zur Förderung des wissenschaftlichen Nachwuchses vom 16.06.2016 entspricht',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.10.2027', 'project_start': '01.12.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/200466045?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101533762', 'title': 'Wissenschaftliche Begleitung des Projektes KASper', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2015',
         'project_start': '01.01.2015',
         'URL': 'https://cris.fau.de/converis/portal/Project/210684606?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104386248',
                                       'title': 'Wissenschafttlicher Dienst des Unabhängigen Beirats des Stabilitätsrats',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.08.2020', 'project_start': '01.09.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/226647026?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101320710', 'title': "Zielführende Betriebsprüfungen durch Nutzung von 'Alternative Data'",
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2020',
         'project_start': '01.01.2020',
         'URL': 'https://cris.fau.de/converis/portal/Project/230024656?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104386248', 'title': 'Zukunft der EU-Finanzen', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '20.12.2015', 'project_start': '22.04.2015',
         'URL': 'https://cris.fau.de/converis/portal/Project/126337145?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '231610692,212578052,105005510', 'title': 'Zukunftsforschung im Supply Chain Management',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': 'None',
         'project_start': '04.05.2022',
         'URL': 'https://cris.fau.de/converis/portal/Project/274752864?auxfun=&lang=de_DE'})


    return render_template('home/index.html', publications=json.dumps(filtered_data_all_wiso_publs), research_projects=json.dumps(filtered_data_all_wiso_pro))


@blueprint.route('/tables')
@blueprint.route('/tables.html')

def tables():
    filtered_data_all_wiso_publs = []
    filtered_data_all_wiso_publs.append(
        {'title': '100% organic? A sustainable entrepreneurship perspective on the diffusion of organic clothing',
         'keywords': 'Corporate social responsibility; Corporate sustainability; Germany; Integrated production; Organic cotton; Supply chain management; Sustainability-oriented innovation; Sustainable entrepreneurship; Textile industry; Transformation',
         'author': 'Hansen E. G., Schaltegger S.', 'language': 'None', 'publish_year': '2013',
         'URL': 'https://cris.fau.de/converis/portal/Publication/122909864?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': '10 Jahre Qualitätsmanagement im österreichischen berufsbildenden Schulwesen mit QIBB: Fragen zu Monitoring und Evaluation eines Mehrebenensystem',
                                            'keywords': 'None',
                                            'author': 'Gramlinger Franz, Jonach Michaela, Wilbers Karl',
                                            'language': 'None', 'publish_year': '2014',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/107789484?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '1913. The World before the Great War - by C. Emmerson', 'keywords': 'Great War',
         'author': 'GL Gardini', 'language': 'None', 'publish_year': '2014',
         'URL': 'https://cris.fau.de/converis/portal/Publication/113168484?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '2012 Mexico election: The return of the Partido Revolucionario Institucional (PRI)',
         'keywords': 'None', 'author': 'Gardini GL', 'language': 'None', 'publish_year': '2012',
         'URL': 'https://cris.fau.de/converis/portal/Publication/252934657?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': "2012 Venezuela elections: Will Chavez's 4th mandate bring moderation or radicalization?",
         'keywords': 'None', 'author': 'Gardini GL', 'language': 'None', 'publish_year': '2012',
         'URL': 'https://cris.fau.de/converis/portal/Publication/252934406?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': '2013-14 State of the Future, Glenn, J.C./ Gordon, T.J./ Florescu, E., The Millennium Project, April 2014 (247 pages)',
                                            'keywords': 'None', 'author': 'von der Gracht H. A.', 'language': 'None',
                                            'publish_year': '2014',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/206787687?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '20 Jahre Spruchverfahren: Empirische Ergebnisse zu Anlässen und Formen der Abfindung',
         'keywords': 'None', 'author': 'Henselmann Klaus, Munkert MichaelJ., Winkler Nadine, Schrenker Claudia',
         'language': 'None', 'publish_year': '2013',
         'URL': 'https://cris.fau.de/converis/portal/Publication/110635184?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '20 Jahre Spruchverfahren: Empirische Ergebnisse zu Anlässen und Formen der Abfindung',
         'keywords': 'None', 'author': 'Henselmann Klaus', 'language': 'None', 'publish_year': '2014',
         'URL': 'https://cris.fau.de/converis/portal/Publication/118229144?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': '20 Jahre Spruchverfahren: Empirische Ergebnisse zum gerichtlichen Verfahrensgang und zum Ausgang von Spruchverfahren',
                                            'keywords': 'None',
                                            'author': 'Henselmann Klaus, Munkert MichaelJ., Winkler Nadine, Schrenker Claudia',
                                            'language': 'None', 'publish_year': '2013',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/110638044?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': '20 Jahre Spruchverfahren: Empirische Ergebnisse zur Abfindungserhöhung in Abhängigkeit vom Antragsteller und von den Bewertungssubjekten',
                                            'keywords': 'None',
                                            'author': 'Henselmann Klaus, Munkert MichaelJ., Winkler Nadine, Schrenker Claudia',
                                            'language': 'None', 'publish_year': '2013',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/110650804?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '21 Open Labs as Islands of Reason in the Digital Age', 'keywords': 'None',
         'author': 'Albrecht Fritzsche', 'language': 'None', 'publish_year': '2020',
         'URL': 'https://cris.fau.de/converis/portal/Publication/239510774?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '2.2 Kurz vorgestellt – Bücher zum Thema E-Learning', 'keywords': 'E-Learning1; Buchbesprechung2;',
         'author': 'Jahn Dirk, Kalsperger Maria, Dr. Trager Bernhard', 'language': 'German', 'publish_year': '2013',
         'URL': 'https://cris.fau.de/converis/portal/Publication/106787604?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '5 Strategien zur Deeskalation von Commitment', 'keywords': 'None', 'author': 'None',
         'language': 'None', 'publish_year': '2021',
         'URL': 'https://cris.fau.de/converis/portal/Publication/260407515?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '6th DACH+ Conference on Energy Informatics (EnInf 2017)', 'keywords': 'None',
         'author': 'Santini S, Tiefenbeck V', 'language': 'None', 'publish_year': '2018',
         'URL': 'https://cris.fau.de/converis/portal/Publication/227859388?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '6 The Many Facets of Open Laboratories and Their Implications for Innovation Management',
         'keywords': 'None', 'author': 'Albrecht Fritzsche', 'language': 'None', 'publish_year': '2020',
         'URL': 'https://cris.fau.de/converis/portal/Publication/239627162?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abbildung der stationären allergologischen Expositionstestungen im deutschen DRG-System',
         'keywords': 'None', 'author': 'Treudler R, Meier F, Schöffski O, Simon J-C', 'language': 'German',
         'publish_year': '2012', 'URL': 'https://cris.fau.de/converis/portal/Publication/114711124?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Ab die Mail!', 'keywords': 'None', 'author': 'None', 'language': 'German', 'publish_year': '2003',
         'URL': 'https://cris.fau.de/converis/portal/Publication/108116844?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abgehängt - Unternehmenskultur und Veränderung.', 'keywords': 'Unternehmenskultur',
         'author': 'Widuckel W.', 'language': 'German', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/119458724?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abgeltungssteuer als Lösung?', 'keywords': 'Kohäsion', 'author': 'Scheffler W.', 'language': 'None',
         'publish_year': '2005', 'URL': 'https://cris.fau.de/converis/portal/Publication/107346844?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A bibliometric analysis of the German corporate governance research', 'keywords': 'None',
         'author': 'Eulerich M., Stiglbauer M., Haustein S.', 'language': 'None', 'publish_year': '2012',
         'URL': 'https://cris.fau.de/converis/portal/Publication/118817424?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A bibliometric review of scientific theory in futures and foresight: A commentary on Fergnani and Chermack 2021',
                                            'keywords': 'None', 'author': 'Münch C, von der Gracht HA',
                                            'language': 'English', 'publish_year': '2021',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/251576873?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abitur and what next? Reasons for gaining double qualifications in Germany',
         'keywords': 'Transformation; qualification; Forschungsbericht 2010; double qualification; Abitur',
         'author': 'None', 'language': 'None', 'publish_year': '2010',
         'URL': 'https://cris.fau.de/converis/portal/Publication/117482684?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Ablenkung oder Abkehr von der Politik? Mediennutzung im Geflecht politischer Orientierun\xadgen',
         'keywords': 'None', 'author': 'Holtz-Bacha C.', 'language': 'None', 'publish_year': '1990',
         'URL': 'https://cris.fau.de/converis/portal/Publication/217759061?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({'title': 'A Blueprint for Event-driven Business Activity Management',
                                         'keywords': 'Reference Architecture, Complex event processing, Business process management, Business process analytics, Business activity management',
                                         'author': 'Janiesch Christian, Matzner Matzner, Müller Oliver',
                                         'language': 'English', 'publish_year': '2011',
                                         'URL': 'https://cris.fau.de/converis/portal/Publication/112510244?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'About well-considered decisions, favorable alternatives and sudden ideas: A qualitative research to identify beliefs that influence women to study information systems in Germany',
                                            'keywords': 'None',
                                            'author': 'Oehlhorn Caroline, Laumer Sven, Maier Christian',
                                            'language': 'English', 'publish_year': '2017',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/205783058?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abschaffung der Abgeltungsteuer: Folgewirkungen auf die Unternehmensbesteuerung',
         'keywords': 'Kohäsion', 'author': 'Scheffler W., Christ R.', 'language': 'German', 'publish_year': '2016',
         'URL': 'https://cris.fau.de/converis/portal/Publication/116060164?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abschließende Bemerkungen zu den Erwiderungen von Foppa und Droz', 'keywords': 'None',
         'author': 'None', 'language': 'None', 'publish_year': '1989',
         'URL': 'https://cris.fau.de/converis/portal/Publication/119609424?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abschlussanalyse 4.0', 'keywords': 'None', 'author': 'Henselmann K', 'language': 'None',
         'publish_year': '2016', 'URL': 'https://cris.fau.de/converis/portal/Publication/200189263?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Abschlussbericht des Lehrforschungsprojekts Lebenswirklichkeit und Partizipation Jugendlicher in Nürnberg im Auftrag des Kreisjugendrings Nürnberg-Stadt',
                                            'keywords': 'None', 'author': 'Damelang A', 'language': 'None',
                                            'publish_year': '2013',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/117625244?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Abschlussprüferhonorare bei deutschen kapitalmarktorientierten Unternehmen\r\nEine Analyse der Entwicklung von Abschlussprüferhonoraren unter Berücksichtigung des IDW RS HFA 36 n. F. und der EU-Verordnung 537/2014',
                                            'keywords': 'None', 'author': 'Dimmer M', 'language': 'German',
                                            'publish_year': '2020',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/238554412?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abschreibungsfinanzierung', 'keywords': 'None', 'author': 'Fischer Thomas, Hitz J.',
         'language': 'None', 'publish_year': '2006',
         'URL': 'https://cris.fau.de/converis/portal/Publication/115230544?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abschreibungsfinanzierung', 'keywords': 'None', 'author': 'None', 'language': 'German',
         'publish_year': '2001', 'URL': 'https://cris.fau.de/converis/portal/Publication/245199850?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abschreibungsfinanzierunng', 'keywords': 'None', 'author': 'None', 'language': 'German',
         'publish_year': '2001', 'URL': 'https://cris.fau.de/converis/portal/Publication/123068264?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Absence from Work of the Self-Employed: A Comparison with Paid Employees', 'keywords': 'None',
         'author': 'Lechmann D, Schnabel C', 'language': 'None', 'publish_year': '2014',
         'URL': 'https://cris.fau.de/converis/portal/Publication/118443204?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Absenteeism and Employment Probation - A Panel Study for Germany', 'keywords': 'None',
         'author': 'None', 'language': 'English', 'publish_year': '1999',
         'URL': 'https://cris.fau.de/converis/portal/Publication/120944164?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Absenteeism and Employment Protection: 3 Case Studies', 'keywords': 'None', 'author': 'None',
         'language': 'None', 'publish_year': '2004',
         'URL': 'https://cris.fau.de/converis/portal/Publication/122969264?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Absorptive Capacity as a Prerequisite for Open Innovation', 'keywords': 'None',
         'author': 'Ixmeier Johannes, Scheiner Christian, Voigt Kai-Ingo', 'language': 'English',
         'publish_year': '2011', 'URL': 'https://cris.fau.de/converis/portal/Publication/121666864?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Abweichungen zwischen Handels- und Steuerbilanz, Übersichten über die Reichweite des Maßgeblichkeitsprinzips und die Ausnahmen von der Maßgeblichkeit der Handelsbilanz für die Steuerbilanz',
                                            'keywords': 'Kohäsion', 'author': 'Scheffler W.', 'language': 'None',
                                            'publish_year': '2004',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/111123584?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Abweichungen zwischen Handels- und Steuerbilanz, Übersichten über die Reichweite des Maßgeblichkeitsprinzips und die Ausnahmen von der Maßgeblichkeit der Handelsbilanz für die Steuerbilanz',
                                            'keywords': 'Kohäsion', 'author': 'Scheffler W.', 'language': 'None',
                                            'publish_year': '2004',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/114374524?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({'title': 'Abweichungsanalyse bei Projekten im F&E-Bereich', 'keywords': 'None',
                                         'author': 'Fischer Thomas, Coenenberg Adolf G., Raffel Andreas',
                                         'language': 'German', 'publish_year': '1992',
                                         'URL': 'https://cris.fau.de/converis/portal/Publication/122077824?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Academic Entrepreneurship - Examining Motivating and Hindering Influences Through the Gender Lense; Internationalizing Entrepreneurship Education and Training - Innovative Formats for Entrepreneurship Education Teaching',
                                            'keywords': 'None',
                                            'author': 'Laspita S., Scheiner Christian, Chlosta S., Brem Alexander, Voigt Kai-Ingo, Klandt H.',
                                            'language': 'English', 'publish_year': '2007',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/120565984?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Academic Writing – Guidelines for a Term Paper, Bachelor and Master Thesis', 'keywords': 'None',
         'author': 'None', 'language': 'None', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/234792548?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Case About the Diffusion of Co-Creation Expertise in Organizations', 'keywords': 'None',
         'author': 'Krämer K., Roth Angela, Möslein Kathrin M.', 'language': 'None', 'publish_year': '2014',
         'URL': 'https://cris.fau.de/converis/portal/Publication/118831724?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Case Mining based Recommender System for Knowledge Workers', 'keywords': 'None', 'author': 'None',
         'language': 'None', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/114537544?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Accelerating Scientific Research with Open Laboratories', 'keywords': 'None',
         'author': 'Fritzsche A, Möslein K', 'language': 'None', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/116512924?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Accepting a crowdsourced delivery - a choice-based conjoint analysis', 'keywords': 'None',
         'author': 'Bathke H, Hartmann E', 'language': 'English', 'publish_year': '2021',
         'URL': 'https://cris.fau.de/converis/portal/Publication/269365499?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Accessing complex patient data from Arden Syntax Medical Logic Modules', 'keywords': 'None',
         'author': 'Stefan Kraus, Martin Enders, Hans-Ulrich Prokosch, Ixchel Castellanos, Richard Lenz, Martin Sedlmayr',
         'language': 'None', 'publish_year': '2018',
         'URL': 'https://cris.fau.de/converis/portal/Publication/216630771?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Access to Commitment Devices Reduces Investment Incentives in Oligopoly', 'keywords': 'None',
         'author': 'Grimm Veronika, Zöttl Gregor', 'language': 'English', 'publish_year': '2005',
         'URL': 'https://cris.fau.de/converis/portal/Publication/121259204?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Accounting for Sustainable Organisations: Where is the Accountant and why it Matters',
         'keywords': 'None', 'author': 'None', 'language': 'None', 'publish_year': '2011',
         'URL': 'https://cris.fau.de/converis/portal/Publication/123255484?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Accounting fraud: Case studies and practical implications', 'keywords': 'None',
         'author': 'Henselmann Klaus, Hofmann Stefan', 'language': 'English', 'publish_year': '2010',
         'URL': 'https://cris.fau.de/converis/portal/Publication/110531124?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Accounting Rules for SMEs in Germany - General Structure and Changes over Time',
         'keywords': 'Rechungslegung; Deutschland; EU; historisch; Mittelstand; KMU; SME; Accounting; Germany; History; Europe',
         'author': 'Henselmann K', 'language': 'English', 'publish_year': '2020',
         'URL': 'https://cris.fau.de/converis/portal/Publication/243473537?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Accuracy, unbiasedness and efficiency of professional macroeconomic forecasts: An empirical comparison for the G7',
                                            'keywords': 'Evaluating forecasts\r\nMacroeconomic forecasting\r\nRationality\r\nSurvey data\r\nFixed-event forecasts',
                                            'author': 'None', 'language': 'English', 'publish_year': '2011',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/216788980?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({'title': 'Achieving and assuring high availability', 'keywords': 'Innovation',
                                         'author': 'K.S. Trivedi, Ciardo G., Dasarathy B., Grottke Michael, Matias R., Rindos A., Vashaw B.',
                                         'language': 'None', 'publish_year': '2008',
                                         'URL': 'https://cris.fau.de/converis/portal/Publication/115263544?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Achieving Competitive Advantage from Sustainable Supplier Management - Insights from the Chemical Industry',
                                            'keywords': 'Innovation',
                                            'author': 'Reuter C., Förstl K., Hartmann E., Blome C.', 'language': 'None',
                                            'publish_year': '2009',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/121689084?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Achtsamkeit im organisationalen Kontext: Der Einfluss individueller und organisationaler Achtsamkeit auf resilientes Verhalten, psychische Gesundheit und Arbeitsengagement',
                                            'keywords': 'None', 'author': 'None', 'language': 'German',
                                            'publish_year': '2018',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/107190864?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Cluster Analysis of Pediatric Cancer Incidence Rates in Florida: 2000–2010', 'keywords': 'None',
         'author': 'None', 'language': 'None', 'publish_year': '2014',
         'URL': 'https://cris.fau.de/converis/portal/Publication/114691764?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({'title': 'ACM SIGMIS CPR 2020 Introduction', 'keywords': 'None',
                                         'author': 'Sven Laumer, Jeria Quesenberry, Damien Joseph, Christian Maier, Daniel Beimborn, Shirish C. Srivastava',
                                         'language': 'None', 'publish_year': '2020',
                                         'URL': 'https://cris.fau.de/converis/portal/Publication/255637517?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A community-based toolkit for designing ride-sharing services: The case of a virtual network of ride access points in Germany',
                                            'keywords': 'Innovation',
                                            'author': 'Hansen E. G., Gomm M. L., Bullinger A.C., Möslein Kathrin M.',
                                            'language': 'None', 'publish_year': '2010',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/114151444?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A commuting-based refinement of the contiguity matrix for spatial models, and an application to local police expenditures',
                                            'keywords': 'spatial weights; contiguity matrix; commuting flows; police expenditures',
                                            'author': 'Rincke Johannes', 'language': 'English', 'publish_year': '2010',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/118021244?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Comparative Analysis of the Australian and German eHealth System', 'keywords': 'None',
         'author': 'None', 'language': 'English', 'publish_year': '2016',
         'URL': 'https://cris.fau.de/converis/portal/Publication/124065304?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Comparative Assessment of Basel II/III and Solvency II', 'keywords': 'Solvency II; Basel II/III',
         'author': 'Gatzert Nadine, Wesker Hannah', 'language': 'English', 'publish_year': '2012',
         'URL': 'https://cris.fau.de/converis/portal/Publication/114515984?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A comparative perspective on political advertising in western democracies: implications of media and political system characteristics',
                                            'keywords': 'None', 'author': 'Holtz-Bacha C, Kaid Lynda L.',
                                            'language': 'None', 'publish_year': '1995',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/219599238?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({'title': 'A comprehensive wealth index for cities in Germany',
                                         'keywords': 'Cities in Germany; Comprehensive wealth index',
                                         'author': 'Dovern J., Quaas M., Rickels W.', 'language': 'None',
                                         'publish_year': '2014',
                                         'URL': 'https://cris.fau.de/converis/portal/Publication/204170331?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Conceptual Framework of Service Innovation and Its Implications for Future Research',
         'keywords': 'Conceptual framework; Service innovation; Service science; Service-dominant logic',
         'author': 'Sven Schwarz, Carolin Durst, Freimut Bodendorf', 'language': 'None', 'publish_year': '2012',
         'URL': 'https://cris.fau.de/converis/portal/Publication/120019504?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Conceptualized Investment Model of Crowdfunding', 'keywords': 'Crowdfunding',
         'author': 'Tomczak A, Brem A', 'language': 'English', 'publish_year': '2013',
         'URL': 'https://cris.fau.de/converis/portal/Publication/108691924?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A conceptualized investment model of crowdfunding', 'keywords': 'None',
         'author': 'Tomczak Alan, Brem Alexander', 'language': 'None', 'publish_year': '2016',
         'URL': 'https://cris.fau.de/converis/portal/Publication/108692144?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A configuration of sustainable sourcing and supply management strategies', 'keywords': 'None',
         'author': 'None', 'language': 'English', 'publish_year': '2017',
         'URL': 'https://cris.fau.de/converis/portal/Publication/119561904?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Context Aware Mobile Application for Physical Activity Promotion', 'keywords': 'None',
         'author': 'Hamper Andreas', 'language': 'None', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/114567684?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Continuous Logit Hotelling Model with Endogenous Locations of Consumers',
         'keywords': 'Spatial competition; Continuous logit model; Minimum differentiation principle',
         'author': 'Matthias Wrede', 'language': 'English', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/108803244?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({'title': 'A Continuous Spatial Choice Logit Model of a Polycentric City.',
                                         'keywords': 'Urban spatial equilibrium; Polycentric city; Probabilistic location choices; Continuous logit model; Cross-commuting',
                                         'author': 'Matthias Wrede', 'language': 'English', 'publish_year': '2015',
                                         'URL': 'https://cris.fau.de/converis/portal/Publication/122098724?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Acquiring new customers by price comparison sites vs. direct marketing: Long-term effects on customer loyalty and cross-buying in a contractual setting',
                                            'keywords': 'None', 'author': 'None', 'language': 'None',
                                            'publish_year': '2020',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/240747535?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Credit Portfolio Framework under Dependent Risk Parameters PD, LGD and EAD', 'keywords': 'None',
         'author': 'Matthias Fischer, Kevin Jakob, Johanna Eckert', 'language': 'English', 'publish_year': '2016',
         'URL': 'https://cris.fau.de/converis/portal/Publication/116016164?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A cross-domain comparison of application areas for service systems based on cyber-physical systems',
         'keywords': 'service systems; service systems engineering, cyber-physical systems', 'author': 'Oks S J',
         'language': 'English', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/110252604?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A Cross-National Study of the Effects of Education on Pre-Service Teachers’ Attitudes, Intentions, Concerns, and Self-Efficacy Regarding Inclusive Education',
                                            'keywords': 'Inclusion; teacher education; Canada; Germany; attitudes; intentions; concerns; self-efficacy; Inklusion;',
                                            'author': 'Miesera Susanne, Sokal Laura, Kimmelmann Nicole',
                                            'language': 'English', 'publish_year': '2021',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/268597337?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A cross-sectional study assessing the association between online ratings and clinical quality of care measures for US hospitals: results from an observational study.',
                                            'keywords': 'None', 'author': 'Emmert M, Meszmer N, Schlesinger M',
                                            'language': 'None', 'publish_year': '2018',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/106835784?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A cross-sectional study assessing the association between online ratings and structural and quality of care measures: results from two German physician rating websites.',
                                            'keywords': 'None',
                                            'author': 'Emmert M, Adelhardt T, Sander U, Wambach V, Lindenthal J',
                                            'language': 'None', 'publish_year': '2015',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/120070324?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Active Sourcing und Social Recruiting - Ausgewählte Ergebnisse der Recruiting Trends 2016 und der Bewerbungspraxis 2016',
                                            'keywords': 'None',
                                            'author': 'Weitzel Tim, Laumer Sven, Maier Christian, Oehlhorn Caroline, Wirth Jakob, Weinert Christoph, Eckhardt Andreas',
                                            'language': 'German', 'publish_year': '2016',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/208765364?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Active Sourcing und Social Recruiting - Ausgewählte Ergebnisse der Recruiting Trends 2017 und der Bewerbungspraxis 2017',
                                            'keywords': 'None',
                                            'author': 'Weitzel Tim, Laumer Sven, Maier Christian, Oehlhorn Caroline, Wirth Jakob, Weinert Christoph, Eckhardt Andreas',
                                            'language': 'German', 'publish_year': '2017',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/206235115?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Activity-Based Costing and Performance Measurement in the Electronics Industry', 'keywords': 'None',
         'author': 'None', 'language': 'None', 'publish_year': '1995',
         'URL': 'https://cris.fau.de/converis/portal/Publication/245268155?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Activity-based working: How the use of available workplace options increases perceived autonomy in the workplace',
                                            'keywords': 'None', 'author': 'None', 'language': 'English',
                                            'publish_year': '2022',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/266062440?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Actor and Institutional Dynamics in the Development of Multi-Stakeholder Initiatives',
         'keywords': 'Business self-regulation; Club theory; Global governance; Institutional entrepreneurship; Institutional theory; Management of diverse interests; Multi-stakeholder initiatives; Political role of the firm; Soft law',
         'author': 'Zeyen Anica, Beckmann Markus, Wolters Stella', 'language': 'None', 'publish_year': '2016',
         'URL': 'https://cris.fau.de/converis/portal/Publication/122177264?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Actor integration in service systems – exploring effects on a micro level', 'keywords': 'None',
         'author': 'Jonas J, Roth A, Möslein K', 'language': 'None', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/122100924?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A Customer Perspective on Product Eliminations: How the Removal of Products Affects Customers and Business Relationships',
                                            'keywords': 'Forschungsbericht 2010; Innovation',
                                            'author': 'Homburg Ch., Fürst Andreas, Prigge J.-K.', 'language': 'None',
                                            'publish_year': '2010',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/117743604?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Adaptation to the market? Status differences between target occupations in the application process and realized training occupation of German adolescents',
                                            'keywords': 'None', 'author': 'Schels B, Abraham M', 'language': 'English',
                                            'publish_year': '2021',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/262083973?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Adaption der Berufsaspiration bei Jugendlichen - eine Befragung von Haupt- und Realschüler/innen in Nürnberg. Überblick über die Studie und Datendokumentation',
                                            'keywords': 'None', 'author': 'Abraham M, Dietrich H, Sachse H, Schels B',
                                            'language': 'German', 'publish_year': '2015',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/108913904?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Adaptive Case Management: Anwendung des Business Process Management 2.0-Konzepts auf schwach strukturierte Geschäftsprozesse',
                                            'keywords': 'None', 'author': 'Christian Herrmann, Matthias Kurz',
                                            'language': 'None', 'publish_year': '2011',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/109360284?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Adaptive Innovation Management - Concept and Tool Support', 'keywords': 'None',
         'author': 'Sebastian Huber, Christian Mühlroth, Freimut Bodendorf', 'language': 'None', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/122114564?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Adaptive Open Innovation - Solution Approach and Tool Support', 'keywords': 'None',
         'author': 'Sebastian Huber, Peter Schott, Matthias Lederer', 'language': 'English', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/109270084?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Dark Side of Telework: A Social Comparison-Based Study from the Perspective of Office Workers',
         'keywords': 'Social comparison theory; Telework; Envy; Turnover; Job performance; Empirical study; COVID-19',
         'author': 'None', 'language': 'English', 'publish_year': '2022',
         'URL': 'https://cris.fau.de/converis/portal/Publication/277654048?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Additive Fertigung für industrielle Anwendungen - Entwicklung einer Auswahlsystematik für Bauteile zur Generierung funktionalen Mehrwerts mittels additiver Fertigung',
                                            'keywords': 'None',
                                            'author': 'Thomas Papke, Dominic Bartels, Michael Schmidt, Marion Merklein, Daniel Gerhard, Jonas Baumann, Indra Pitz',
                                            'language': 'None', 'publish_year': '2020',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/245752967?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': "Addressing a product management's orphan: How to externally implement product eliminations in a B2B setting",
                                            'keywords': 'None', 'author': 'Prigge JK, Homburg C, Fürst A',
                                            'language': 'English', 'publish_year': '2018',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/119815784?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Addressing sustainability information needs along supply chains', 'keywords': 'Nachhaltigkeit;',
         'author': 'None', 'language': 'English', 'publish_year': '2019',
         'URL': 'https://cris.fau.de/converis/portal/Publication/229265156?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': '[A Decade of Online Physician-Rating Websites in Germany: an Assessment of the Current Level of Development].',
                                            'keywords': 'None', 'author': 'Emmert M, Meszmer N', 'language': 'None',
                                            'publish_year': '2017',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/106774844?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A decision support scheme for software process improvement prioritization', 'keywords': 'Innovation',
         'author': 'A. Beckhaus, L.M. Karg, C. Graf, Grottke Michael, D. Neumann', 'language': 'English',
         'publish_year': '2011', 'URL': 'https://cris.fau.de/converis/portal/Publication/111819664?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A Deep Learning Approach for Managing Medical Consumable Materials in Intensive Care Units via Convolutional Neural Networks: Technical Proof-of-Concept Study',
                                            'keywords': 'convolutional neural networks; deep learning; critical care; intensive care; image recognition; medical economics; medical consumables; artificial intelligence; machine learning',
                                            'author': 'Peine A., Hallawa A., Schöffski O., Dartmann G., Begic Fazlic L., Schmeink A., Marx G., Martin L.',
                                            'language': 'None', 'publish_year': '2019',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/229850573?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A Delphi-based risk analysis — Identifying and assessing future challenges for supply chain security in a multi-stakeholder environment',
                                            'keywords': 'Risk; Supply chain security; Terroristic attacks; Delphi; Multi-stakeholder; Future',
                                            'author': 'Markmann C, Darkow I, von der Gracht H', 'language': 'None',
                                            'publish_year': '2013',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/205750466?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A description of the operative decision-making process of a power generating company on the Nordic electricity market',
                                            'keywords': 'Bidding strategy; Decisions under uncertainty; Electricity trading; Nordic power system; Power producer; Risk management',
                                            'author': 'Scharff R., Egerer J., Söder L.', 'language': 'None',
                                            'publish_year': '2014',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/119616024?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A discussion on the General Data Protection Regulation Eine Diskussion zur Datenschutz-Grundverordnung',
                                            'keywords': 'None', 'author': 'Peter Mertens', 'language': 'None',
                                            'publish_year': '2020',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/244599733?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A dissent-based approach for multi-stakeholder scenario development — The future of electric drive vehicles',
                                            'keywords': 'Scenarios; Delphi; Multi-stakeholder; Dissent; Electric drive vehicles',
                                            'author': 'Warth J, von der Gracht HA, Darkow I', 'language': 'None',
                                            'publish_year': '2013',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/205775947?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Distortive Wage Tax and a Countervailing Commuting Subsidy', 'keywords': 'Transformation',
         'author': 'Wrede Matthias', 'language': 'English', 'publish_year': '2009',
         'URL': 'https://cris.fau.de/converis/portal/Publication/114251984?auxfun=&lang=de_DE'})

    filtered_data_all_wiso_pro = []
    filtered_data_all_wiso_pro.append({'project_leader': '105707876,101530724,105329106',
                                       'title': 'Individuell empfohlen? - Wie KI-basierte Beratungssysteme die Diversität der Studierenden beeinflussen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '28.02.2021', 'project_start': '01.03.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235228880?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'AI for Public Services', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '01.06.2024', 'project_start': '01.04.2021',
         'URL': 'https://cris.fau.de/converis/portal/Project/257929870?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '200418444', 'title': 'AI for Industry 4.0: models and technologies', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.07.2020', 'project_start': '01.07.2020',
         'URL': 'https://cris.fau.de/converis/portal/Project/237715326?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '203395223',
                                       'title': 'Künstliche Intelligenz zur Erschließung von Potentialen zur Semi-Prozessautomatisierung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2020', 'project_start': '01.01.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/221488811?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105329106',
                                       'title': 'Eine lebensverlaufssoziologische Perspektive auf das Arbeitsangebot: Zeitliche, institutionelle und soziale Einbettung als Determinanten individueller Reservationslöhne',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.01.2022', 'project_start': '01.02.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/228016423?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Alles Sprache oder was? Qualifizierung von Mentorinnen und Mentoren für ein sprachsensibles Mentoring von Geflüchteten',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': '30.09.2021',
                                       'project_start': '01.04.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/250249701?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760,104991104',
                                       'title': 'Arbeitslosigkeit und Behinderung unter Berücksichtigung der Covid-19-Pandemie und ihrer Bewältigung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.11.2024', 'project_start': '01.12.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/271088154?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760,101148916', 'title': 'Konzeption von Diagnose- und Evaluationsinstrumenten',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.10.2017',
         'project_start': '01.11.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/126433982?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101305324',
                                       'title': 'Analyse und Optimierung standardisierter Behandlungsprozesse im Krankenhaus',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2016', 'project_start': '01.05.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/203774296?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Arbeiten, Lernen und Weiterbildung in der Zeitarbeit - Eine Befragung von Erwerbstätigen in der Zeitarbeit',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2007', 'project_start': '01.01.2005',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235292385?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101494856', 'title': 'Arbeitsmarkteffekte der Reform des vorzeitigen Rentenbezugs',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.03.2020',
         'project_start': '01.09.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/205223927?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Arbeitszeugnisse in Deutschland: Der Einfluss von Geschlecht, Position und Unternehmensmerkmalen auf Inhalt und Bewertung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2012', 'project_start': '01.04.2012',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229844378?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100502116',
                                       'title': 'Eine Analyse von Reputationsrisiken und Spillover-Risiken aus Perspektive der Versicherungswirtschaft',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.11.2018', 'project_start': '01.06.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126185890?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '242689003', 'title': 'None', 'funder': 'None', 'project_type': 'Own Funds',
         'project_end': 'None', 'project_start': '01.09.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/263866704?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101975056', 'title': 'Atlantic Future - Regionalism and inter-regionalism (WP8)',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2015',
         'project_start': '01.01.2013',
         'URL': 'https://cris.fau.de/converis/portal/Project/125810879?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104386248,239219621', 'title': 'Aufkommenseffekte von Steuerrechtsänderungen',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2022',
         'project_start': '01.01.2022',
         'URL': 'https://cris.fau.de/converis/portal/Project/267037038?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101494856',
                                       'title': 'Auswirkungen der Elterngeldreform auf Haushaltsstrukturen und Familiengründung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2016', 'project_start': '01.01.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/213945993?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760,103888408',
                                       'title': 'AVENUE - Zusammenstellung von Verfahren zur Ermittlung von neuen Formen der Arbeitsverdichtung und ihren Folgen sowie von Maßnahmen zur Prävention (Arbeitstitel: AVENUE)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.05.2021', 'project_start': '01.03.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/226649511?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105108214',
                                       'title': 'Bayessche Vorhersagemodelle auf Basis von Kontextinformationen für das Monitoring von Geschäftsprozessen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2018', 'project_start': '06.03.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/201722116?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Belastungen und Beanspruchung im Kontext atypischer Karrieren und flexibler Beschäftigungsverhältnisse',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2006', 'project_start': '01.01.2004',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235292115?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101872450',
                                       'title': 'Ausweitung der Bedarfsorientierten Budgetierung auf städtische berufliche Schulen mit Schwerpunkt Heterogenität',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2024', 'project_start': '01.10.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/266476875?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101872450',
                                       'title': 'Bedarfsorientierte Budgetierung an ausgewählte städtischen Berufsschulen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2021', 'project_start': '01.01.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/226019340?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101533762', 'title': 'Berufssprache Deutsch', 'funder': 'None', 'project_type': 'Own Funds',
         'project_end': '31.12.2014', 'project_start': '01.01.2011',
         'URL': 'https://cris.fau.de/converis/portal/Project/210774505?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '103586862',
                                       'title': 'Betriebsschließungen in Deutschland: Umfang, Verlauf und Einflussfaktoren',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.03.2013', 'project_start': '01.02.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126148710?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762,101734956',
                                       'title': 'Bildungsbenachteiligung und COVID-19: Herausforderungen und Auswirkungen des pandemiebedingten Homeschoolings sowie damit verbundener digitaler Lehr-Lernformate auf junge Geflüchtete in dualer Ausbildung.',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': '31.03.2021',
                                       'project_start': '01.04.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/250249303?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101530724',
                                       'title': 'BIRD steht für kaufmännische und gewerblich-technische Angebote zu Industrie 4.0 auf der Plattform der DQR-Stufe 5 als Motor der Durchlässigkeit zwischen Berufsausbildung und schulischer Fortbildung (Fach-/Technikerschule), IHK-Fortbildung (Fachwirt/in, Fachmeister/in) und akademischer Bildung (Bachelorstudium)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '29.02.2020', 'project_start': '01.09.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/228125107?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101530724',
                                       'title': 'Attraktive, durchlässige und Bildungs- und Beratungsangebote in der schulischen und außerschulischen beruflichen Aus- und Weiterbildung sowie der akademischen Bildung im blended-learning-Design am Beispiel neuer Anforderungen durch Industrie 4.0 unter strategischer Nutzung der ersten Fortbildungsstufe',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2024', 'project_start': '01.10.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/246600157?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105108214',
                                       'title': 'Internationales Forschnungsnetzwerk für E-Government zwischen Deutschland und Brasilien',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '30.06.2009', 'project_start': '01.01.2006',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126475556?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103861360', 'title': 'Careers in transition: Karrierecoaching und Karriereerfolg',
         'funder': 'None', 'project_type': 'Own Funds', 'project_end': 'None', 'project_start': '01.04.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/229903464?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '242689003,inv,inv', 'title': 'None', 'funder': 'None', 'project_type': 'Fremdprojekt',
         'project_end': 'None', 'project_start': '01.09.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/263863669?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101309146',
                                       'title': 'Kausale Effekte von Lohnsubventionen auf Arbeitsangebot und Arbeitsnachfrage',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2017', 'project_start': '01.01.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126123867?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760,104991104',
                                       'title': 'Veränderung von Covid-19-bezogenen Sorgen und Ängsten, Risikowahrnehmungen und Präventionsverhalten im Verlauf der Pandemie: Längsschnittliche Vorhersage präventionsbezogener Variablen in einer vulnerablen Stichprobe ehemals arbeitsloser Personen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2022', 'project_start': '01.01.2022',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/271344712?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Connecting the Cooperative (CoCo)', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '30.06.2016', 'project_start': '01.07.2013',
         'URL': 'https://cris.fau.de/converis/portal/Project/211012798?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246,101487604', 'title': 'Cooperatives in the Digital Age (CoDi)', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.03.2018', 'project_start': '01.10.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/126231182?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246,101487604',
                                       'title': 'Community-basierte Dienstleistungs-Innovation für e-Mobility (CODIFeY)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.10.2017', 'project_start': '01.11.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/203640687?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105782552',
                                       'title': 'Conjoint-basierte Bedürfnisanalyse von Kreditgenossenschaftskunden im digitalen Zeitalter und Implikationen für das genossenschaftliche Geschäftsmodell',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.04.2017', 'project_start': '01.05.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126163244?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100501136,102333246',
                                       'title': 'Advanced Systems Configuration zur komplexitätsreduzierten sensorgetriebenen Entwicklung von Produktionssystemen im digitalen Zeitalter (ConSensE)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '29.02.2024', 'project_start': '01.03.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/272534948?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Corporate Social Responsibility und die Attraktivität von Arbeitgebermarken am Beispiel von Genossenschaftsbanken',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': 'None', 'project_start': '01.04.2012',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229844855?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105782552', 'title': 'Creating the bank account of the future', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '30.04.2018', 'project_start': '01.10.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/200434253?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105108214', 'title': 'Nutzerakzeptanz und Dienstleistungskonzeption', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Sub project', 'project_end': '28.02.2015',
         'project_start': '01.12.2013',
         'URL': 'https://cris.fau.de/converis/portal/Project/126338835?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Methoden der Datenerhebung in den Sozial- und Verhaltenswissenschaften',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '28.02.2022', 'project_start': '01.03.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/248524831?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '275370701',
                                       'title': 'Data-driven analysis, benchmarking, and coordination of European IS-curricula',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.05.2023', 'project_start': '01.06.2022',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/276125534?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104052166',
                                       'title': 'Entwicklung der Systematik und der Algorithmen des Umfeld-Scanning-Systems',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.07.2020', 'project_start': '01.08.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/202426626?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101975056',
                                       'title': 'Debunking Interregionalism: concepts, types, critiques. German-Portuguese strategic action fund. To train young researchers.',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': 'None', 'project_start': '01.01.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/213823018?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104991104,101146760',
                                       'title': 'Deprivierte Bedürfnisse und inkongruente Werte - Untersuchungen zu den Ursachen des seelischen Leidens Arbeitsloser',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.07.2016', 'project_start': '01.08.2013',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126112544?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101585016',
                                       'title': 'Der Algorithmus, Dein Freund und Helfer: \r\nDatenbasierte Orientierungshilfe in der Studieneingangsphase des Bachelorstudiengangs Wirtschaftswissenschaften',
                                       'funder': 'None', 'project_type': 'FAU Funds', 'project_end': '30.09.2020',
                                       'project_start': '01.10.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/246311348?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102917228,104452594',
                                       'title': 'Der Einfluss von Patient Reported Outcomes auf die Akzeptanz von Qualitätstransparenzinitiativen für die Krankenhausauswahl',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2019', 'project_start': '01.02.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/216817177?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100550528',
                                       'title': 'Der Reification Bias in der Marketing-Kommunikation: Einflussfaktoren und Auswirkungen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.03.2020', 'project_start': '01.04.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126504286?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101320710', 'title': 'Designing Innovative Pedagogy for Complex Accountancy Topics',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.08.2021',
         'project_start': '01.09.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/208528908?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Determinanten der Verkehrsmittelwahl', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2001', 'project_start': '01.01.1999',
         'URL': 'https://cris.fau.de/converis/portal/Project/235284276?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105108214',
                                       'title': 'German-Brazilian Workshop on Management and Engineering of IT-Supported Business Networks, Administration Networks and Social Networks',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '31.07.2011', 'project_start': '01.04.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126486034?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101533762', 'title': 'Deutsch am Arbeitsplatz', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': '31.12.2013', 'project_start': '01.01.2011',
         'URL': 'https://cris.fau.de/converis/portal/Project/210773338?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101597854',
                                       'title': 'Deutsch-Russische Wirtschaftskooperation im Spannungsfeld von Geschäftsinteressen und unternehmerischer Verantwortung (am Beispiel des Energie- und Finanzsektors)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2022', 'project_start': '01.02.2022',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/270550569?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774,103589606',
                                       'title': 'Dezentralität und zellulare Optimierung – Auswirkungen auf den Netzausbaubedarf',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.06.2016', 'project_start': '10.03.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126509356?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103589606', 'title': 'B09 „Strategische Buchungsentscheidungen im Entry-Exit-System“',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '30.06.2022',
         'project_start': '01.07.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/205660185?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104386248', 'title': 'Die Lebenssteuerlast von Arbeitnehmern', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2018', 'project_start': '01.01.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/126516116?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Die Opferpersönlichkeit als Determinante von Mobbing in Organisationen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2011', 'project_start': '01.06.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229844146?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100248492',
                                       'title': 'Die Regulierung von Berufen und ihr Einfluss auf die Positionierung im Arbeitsmarkt',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2019', 'project_start': '01.01.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126217155?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102330404,100248492',
                                       'title': 'Die Regulierung von Berufen und ihr Einfluss auf die Positionierung im Arbeitsmarkt',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2019', 'project_start': '01.01.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/221696747?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104056282,103342548',
                                       'title': 'Die Wirkungen der Kurzarbeit: Eine Analyse an der Schnittstelle von dynamischer Makro-Arbeitsmarkttheorie und angewandter Ökonometrie',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '01.06.2018', 'project_start': '01.06.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126018073?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '103271008',
                                       'title': 'Die Wirkung von Defaults bei sequentiellen Entscheidungen – Unterschiede zwischen Einzel- und Paarentscheidungen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '01.02.2018', 'project_start': '01.02.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/238570667?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Diffusion von Innovationen. Eine prognostische Studie',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2008',
         'project_start': '01.01.2008',
         'URL': 'https://cris.fau.de/converis/portal/Project/235549895?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'DIGItal COllaboration Platforms as enablers of organizational exchange',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2024', 'project_start': '01.01.2022',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/267037910?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101270338,104628504,100710170,102364998,100228696,101449090,104452594',
         'title': 'Integratives Konzept zur personalisierten Präzisionsmedizin in Prävention, Früh-Erkennung, Therapie und Rückfallvermeidung am Beispiel von Brustkrebs',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '30.09.2024',
         'project_start': '01.10.2020',
         'URL': 'https://cris.fau.de/converis/portal/Project/250673737?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101270338,100710170,102364998,100228696,101449090,104452594',
                                       'title': 'Integratives Konzept zur personalisierten Präzisionsmedizin in Prävention, Früh-Erkennung, Therapie undRückfallvermeidung am Beispiel von Brustkrebs - DigiOnko',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2024', 'project_start': '01.10.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/250674114?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100248492', 'title': 'Digitale Kontrolle in Arbeitsverhältnissen', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Overall project', 'project_end': '30.11.2023',
         'project_start': '01.12.2020',
         'URL': 'https://cris.fau.de/converis/portal/Project/243893068?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103586862', 'title': 'Digitalisierung und ihre Arbeitsmarktwirkungen', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': 'None', 'project_start': '01.07.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/229908870?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103861360', 'title': 'Digitaler Stress', 'funder': 'None', 'project_type': 'Own Funds',
         'project_end': 'None', 'project_start': '01.04.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/126172877?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104385954', 'title': 'Digitization in Controlling and Reporting', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': 'None', 'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/210709292?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101487604',
                                       'title': 'Digitalisierung des zentralen Überlassungsprozesses in der Zeitarbeit',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.07.2020', 'project_start': '29.07.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235835986?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105707876,105628398',
                                       'title': 'Transforming digitally: Digitale Innovationen zur erfolgreichen Gestaltung desorganisationalen Wandels',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.03.2025', 'project_start': '01.04.2022',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/270752781?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100489180', 'title': 'Diversität und Erfolg von Organisationen', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '30.05.2012', 'project_start': '01.11.2010',
         'URL': 'https://cris.fau.de/converis/portal/Project/126084828?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100489180', 'title': 'Diversität und individuelle Karrieren', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '30.11.2017', 'project_start': '01.12.2012',
         'URL': 'https://cris.fau.de/converis/portal/Project/126027537?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101533762', 'title': 'Diversity Management an beruflichen Schulen', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2015',
         'project_start': '01.01.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/210685110?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101487604',
                                       'title': 'Digitale Dienstleistungen als Erfolgsfaktor für die Wertschöpfung der Zukunft',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.03.2021', 'project_start': '01.08.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/228058372?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101320710', 'title': 'E-Bilanzen', 'funder': 'None',
                                       'project_type': 'Third Party Funds Single', 'project_end': '31.03.2016',
                                       'project_start': '01.04.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/125808851?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100088458', 'title': 'Auswirkungen der Mietpreisbremse', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': '14.01.2018', 'project_start': '15.01.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/125983766?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101494856',
                                       'title': 'Eine komparative Analyse der Ursachen und Konsequenzen von Ungleichheit: wie wirken sich frühkindliche Bedingungen auf die Entwicklung von Kindern aus?',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.10.2016', 'project_start': '01.03.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/237122562?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104452594', 'title': 'Einführung der elektronischen Gesundheitskarte', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.08.2017', 'project_start': '01.10.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/126510539?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104373606',
                                       'title': 'Einführung in die unternehmerische Zukunftsforschung - Verbesserungsprojekt',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2021', 'project_start': '01.06.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/261463580?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Einführung von Mitarbeitergesprächen', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': '31.12.2001', 'project_start': '01.01.1999',
         'URL': 'https://cris.fau.de/converis/portal/Project/235286374?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Einführung von Mitarbeitergesprächen in einer Stadtverwaltung - Längsschnittstudie',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2007', 'project_start': '01.01.2006',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235548600?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Einstellungen, Bedenken, Selbstwirksamkeit und Intentionen von Lehramtsstudierenden mit Blick auf Inklusion',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': 'None',
                                       'project_start': '01.04.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/250322029?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '103586862',
                                       'title': 'Einstellungsverhalten, Beschäftigungsperspektiven und Entlohnung in neu gegründeten Betrieben',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': 'None',
                                       'project_start': '01.01.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/211416558?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105707876', 'title': 'Electronic Human Resources Management', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.08.2020', 'project_start': '01.03.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/211149887?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101530724',
                                       'title': 'Module Distance Education System as a new product for reducing the Education Job Mismatch in European Area',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '01.02.2017', 'project_start': '01.02.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/125788571?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774', 'title': 'Economy', 'funder': 'None',
                                       'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.12.2015', 'project_start': '29.07.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126472514?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774,104082252,102089422,100329440,105358016,101433312,103589606',
         'title': 'Energiemarktdesign', 'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
         'project_end': '31.12.2021', 'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/126328188?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774,103589606', 'title': 'Speicher B - Effiziente Wasserstofflogistik',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2021',
         'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/126249941?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246,100501136,101487604',
                                       'title': 'Methodische Konzeptentwicklung für Dienstleistungsplattformen und Schnittstellen, Service Systems Engineering, Kommunikationsdesign',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.06.2020', 'project_start': '01.07.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/125918532?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246',
                                       'title': 'Kommunikationsmanagement und Organisation der Gestaltung von Dienstleistungssystemen im Rahmen pilotierender Einführungen (ExTEND)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.04.2019', 'project_start': '01.10.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126239632?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103291000', 'title': 'Enhancing European teacher education through University schools',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '30.11.2020',
         'project_start': '01.12.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/209613121?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Entering the learning landscape: teacher innovations in classroom and social spaces – a cross-institutional study of trainee teachers by the Universities of Derby and Nuremburg',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': '31.12.2013',
                                       'project_start': '01.01.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210686807?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104452594',
                                       'title': 'Entwicklung eines Befragungsinstruments zur Erfassung von Patientenpräferenzen zum Medikationsmanagement in Deutschland',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2016', 'project_start': '02.02.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/202964987?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Entwicklung eines internationalen Online-Panels', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2006', 'project_start': '01.07.2003',
         'URL': 'https://cris.fau.de/converis/portal/Project/235291497?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104373606',
                                       'title': 'Entwicklung eines Lieferantenauswahl-Prozesses hinsichtlich ausgewählter Nachhaltigkeitskriterien - Sustainable Supplier Selection Process',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2015', 'project_start': '15.01.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/213827010?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774',
                                       'title': 'EOM+: Analyse der kurz- und mittelfristige Auswirkungen von marktbasierten Engpassinstrumenten als regionale und temporäre Ergänzung zum bestehenden Energy-Only-Marktdesign',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '31.10.2022', 'project_start': '01.11.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229944472?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102215842',
                                       'title': 'Erwerbsintegration oder Maßnahmekarriere? Förder- und Erwerbsverlaufmuster von jungen Maßnahmeteilnehmer/innen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2017', 'project_start': '01.01.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/211298853?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101573844', 'title': 'Die Europawahl 2014 in den Medien', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': '31.12.2014', 'project_start': '01.03.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/231679316?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101975056', 'title': 'The Reconfiguration of the EU presence in Latin America',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.08.2022',
         'project_start': '01.09.2020',
         'URL': 'https://cris.fau.de/converis/portal/Project/252964093?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Evaluation eines Auswahlverfahrens hochbegabter Studierender für Studien- und Promotionsstipendien',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2009', 'project_start': '01.01.2009',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235561001?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774', 'title': 'Evaluation eines Smart Grid-Feldexperiments', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2015', 'project_start': '01.01.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/126331906?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Evaluation von Mitarbeitergesprächen (Stadt Fürth)', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2003', 'project_start': '01.01.2001',
         'URL': 'https://cris.fau.de/converis/portal/Project/235287512?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Evaluation von Trainings gegen Informationsüberflutung',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2003',
         'project_start': '01.01.2002',
         'URL': 'https://cris.fau.de/converis/portal/Project/235288576?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774,101582370',
                                       'title': 'Experimentelle Studien zur Auswirkung von kollektiven Lohnverhandlungen auf den Gender Wage Gap',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.12.2015', 'project_start': '01.12.2012',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126316696?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774,105006980',
                                       'title': 'Experimentelle Validierung von Indikatoren des Managerverhaltens in Betriebsbefragungen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2016', 'project_start': '02.04.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126396126?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Expertenstudie zur Reliabilität und Validität von Arbeitszeugnissen',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '30.04.2015',
         'project_start': '01.11.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/235210146?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '242689003,inv,inv', 'title': 'None', 'funder': 'None', 'project_type': 'Own Funds',
         'project_end': 'None', 'project_start': '01.08.2021',
         'URL': 'https://cris.fau.de/converis/portal/Project/263864679?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103256700', 'title': 'Schöller-Fellowship von Frau Dr. Cynthia Sende', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '19.06.2018', 'project_start': '20.06.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/201311736?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105108214', 'title': 'Föderales Informationsmanagement', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': '31.12.2012', 'project_start': '04.12.2012',
         'URL': 'https://cris.fau.de/converis/portal/Project/126487893?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102215842,inv',
                                       'title': 'Kompromissbildung und deren Konsequenzen - Pfadabhängigkeiten zwischen Berufsfindung, Bildungsentscheidungen und Ausbildungsverläufen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2021', 'project_start': '01.10.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126398323?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Flexibilisierte Beschäftigungsverhältnisse und die Beziehung zwischen Mitarbeitern und Unternehmen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2007', 'project_start': '01.01.2006',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235558885?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Integrations- und Kompetenzmanagement im Kontext von Flexibilisierungsstrategien bei KMU',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.04.2013', 'project_start': '01.07.2009',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229843182?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774,103589606', 'title': 'Flexible Verbraucher im Deutschen Strommarkt',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.01.2016',
         'project_start': '01.11.2015',
         'URL': 'https://cris.fau.de/converis/portal/Project/126460008?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105108214',
                                       'title': 'Flexible Informationssystem-Architekturen für hybride Wertschöpfungsnetzwerke',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '31.03.2010', 'project_start': '01.10.2006',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126491104?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246',
                                       'title': 'Mit Flexudy wollen wir Studierenden ein zeiteffizientes und mobiles Lernen ermöglichen. Mit Hilfe künstlicher Intelligenz generiert unsere Technologie aus jeglichen Lernmaterialien in verschiedenen Sprachen automatisiert Fragen-Antwort Karteikarten, Multiple Choice Fragen, Lückentexte und Zusammenfassungen.',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2021', 'project_start': '01.10.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/250326027?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105108214', 'title': 'FOKUS:SE - Das Forschernetzwerk Service Engineering',
         'funder': 'None', 'project_type': 'Own Funds', 'project_end': '01.01.2018', 'project_start': '01.01.2015',
         'URL': 'https://cris.fau.de/converis/portal/Project/126460853?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Förderung sprachlich-kommunikativer Fähigkeiten in der betrieblichen Ausbildung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.12.2014', 'project_start': '01.01.2013',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210685913?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760,103256700',
                                       'title': 'Forschungsvorhaben zur Untersuchung von Mediennutzung und Studienerfolg',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2019', 'project_start': '01.08.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229847147?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '103271008,100502116', 'title': 'Forum V', 'funder': 'None',
                                       'project_type': 'Third Party Funds Single', 'project_end': '31.05.2026',
                                       'project_start': '01.06.2013',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126170173?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105108214', 'title': 'Automatisiertes Content-Providing durch Smarte Steuersysteme',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2019',
         'project_start': '01.01.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/126488907?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246',
                                       'title': 'Führung und Zusammenarbeit im Kontext von Open Innovation bei der AUDI AG',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2013', 'project_start': '01.01.2012',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/125826089?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '248294705', 'title': 'Gamifizierung der Mensch-KI-Interaktion', 'funder': 'None',
         'project_type': 'FAU Funds', 'project_end': '30.06.2022', 'project_start': '01.07.2021',
         'URL': 'https://cris.fau.de/converis/portal/Project/276430350?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246,101487604',
                                       'title': 'Entwicklung von Big-Data-Dienstleistungen und Baukasten-Prototyping mit KMUs (BigDieMo)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.04.2019', 'project_start': '01.10.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126241322?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774,103480140', 'title': 'Zentrum Wasserstoff Bayern', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '30.09.2024', 'project_start': '01.10.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/230023648?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246',
                                       'title': 'Entwicklung von Methoden und Werkzeugen für smarte und nachhaltigkeitsorientierte Produkt-Service-Systeme',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.05.2023', 'project_start': '01.06.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/239536186?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '212658212',
                                       'title': 'Heterogenität makroökonomischer Erwartungen: Welche Rolle spielen individuelle historische Erfahrungen, das örtliche Umfeld und sozioökonomische Faktoren?',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.06.2022', 'project_start': '01.07.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210972719?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101585016',
                                       'title': 'Wie wirkt sich die Geschlechterzusammensetzung auf die Leistung von Teams aus?',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.11.2023', 'project_start': '01.12.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/246311837?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '103203388',
                                       'title': 'Identifikation von Automatisierungspotentialen mit Process Mining (IdAP)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '28.02.2021', 'project_start': '01.03.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/221187754?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104452594', 'title': 'Pharmaökonomie', 'funder': 'None',
                                       'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.09.2017', 'project_start': '01.12.2013',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/125836229?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Integriertes Fach- und Sprachlernen in Beruflicher (Anpassungs-) Qualifizierung - Berufsfeldbezogene Weiterbildung für Lehrende und Bildungsbegleitende',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2017', 'project_start': '01.07.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126165610?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101487604',
                                       'title': 'IIP-Ecosphere - Next Level Ecosphere for Intelligent Industrial Production',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2022', 'project_start': '01.01.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/234097982?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100502116',
                                       'title': 'Implizite Einschränkungen, Anreize und Systemische Risiken: Implikationen der neuen Versicherungsregulierung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2014', 'project_start': '01.01.2013',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126174398?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '242689003,101601774,105655152', 'title': 'None', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': 'None', 'project_start': '01.07.2021',
         'URL': 'https://cris.fau.de/converis/portal/Project/263863924?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105782552',
                                       'title': 'Wertschöpfungsübergreifende Implementierung von Industrie 4.0 bei der Robert Bosch GmbH',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.01.2020', 'project_start': '01.01.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/242032269?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Steigende Informationsflut am Arbeitsplatz - belastungsgünstiger Umgang mit elektronische Medien (E-Mail, Internet)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2002', 'project_start': '01.01.2000',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126304528?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100502116',
                                       'title': 'Investitionen in Infrastruktur und Erneuerbare Energien aus Sicht der Versicherungsindustrie',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.05.2017', 'project_start': '01.06.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126175412?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Innovation Leadership/Business Management Executive Education',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2016',
         'project_start': '01.01.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/126242336?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104421920', 'title': 'TransitionLab 2 - Umsetzungsphase, TP D', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Sub project', 'project_end': '30.11.2022',
         'project_start': '01.12.2021',
         'URL': 'https://cris.fau.de/converis/portal/Project/273174671?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Engagement internationaler Studierender als Element der Regionalentwicklung',
                                       'funder': 'None', 'project_type': 'Fremdprojekt', 'project_end': '31.12.2017',
                                       'project_start': '01.01.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210773039?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762,103205936',
                                       'title': 'InTAK: Interkulturelles Training für Neuzugewanderte – Angemessenes\r\nsprachliches Handeln in beruflichen Kommunikationssituationen',
                                       'funder': 'None', 'project_type': 'FAU Funds', 'project_end': '31.08.2023',
                                       'project_start': '01.10.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/265753095?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101305324,101487310',
                                       'title': 'Anforderungsanalyse, Entwicklung der Motivationsstrategie und des Geschäftsmodells, Test und Evaluierung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.08.2021', 'project_start': '01.09.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/205613594?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103342548', 'title': 'Interdependencies of Labor Market Reforms and the Business Cycle',
         'funder': 'None', 'project_type': 'Own Funds', 'project_end': 'None', 'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/210710543?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101975056',
                                       'title': 'Internationale Entwicklung im 21. Jahrhundert – Wo steht Lateinamerika in der Weltpolitik?',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': 'None', 'project_start': '01.09.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/228195674?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104386248', 'title': 'Internationale Unternehmensbesteuerung und Konzernstrukturen',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '30.06.2012',
         'project_start': '01.06.2010',
         'URL': 'https://cris.fau.de/converis/portal/Project/126056943?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774', 'title': 'Internationales Doktorandenkolleg (IDK) „Evidence Based Economics“',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project', 'project_end': '30.09.2017',
         'project_start': '01.10.2013',
         'URL': 'https://cris.fau.de/converis/portal/Project/126108826?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Internetbasiertes Railpanel', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2000', 'project_start': '01.01.1999',
         'URL': 'https://cris.fau.de/converis/portal/Project/235283787?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101975056', 'title': 'Interregionalism as a foreign policy tool: new concepts and trends',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2018',
         'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/200431535?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100248492', 'title': 'The Invisible Wall: Distinct Firm Networks in West and East Berlin',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '30.06.2019',
         'project_start': '01.07.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/226959649?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246,101487604', 'title': 'JOSEPHS® - Die Service Manufaktur', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': 'None', 'project_start': '01.01.2013',
         'URL': 'https://cris.fau.de/converis/portal/Project/126245547?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101533762', 'title': 'Karriereplanung für Open Source Software-Entwickler',
         'funder': 'None', 'project_type': 'Own Funds', 'project_end': '31.12.2012', 'project_start': '01.01.2011',
         'URL': 'https://cris.fau.de/converis/portal/Project/210774315?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101309146',
                                       'title': 'Kausale Effekte von Lohnsubventionen auf Arbeitsangebot und Arbeitsnachfrage',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2018', 'project_start': '01.10.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/237122857?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Kompetenzentwicklung und Modulare Übergangsbegleitung in den Ausbildungs- und Arbeitsmarkt',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.12.2014', 'project_start': '01.01.2012',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210686144?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104437110', 'title': 'Kreditrating', 'funder': 'None',
                                       'project_type': 'Third Party Funds Single', 'project_end': 'None',
                                       'project_start': '01.01.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/211410229?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Entwicklung einer Online-Recruitingplattform mit kulturbasiertem Jobmatching und Screening',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.04.2018', 'project_start': '01.05.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/202449725?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103271008', 'title': 'Eine Kundenanalyse zu SmartHome-Anwendungen bei Hörgeräten',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '07.02.2017',
         'project_start': '18.10.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/126267517?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105707876',
                                       'title': 'Künstliche Intelligenz, Chatbots und Rekrutierung: Die Sicht der Kandidaten',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2021', 'project_start': '01.11.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/208483806?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103586862', 'title': 'Löhne und Lohndifferenziale', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': 'None', 'project_start': '01.01.2000',
         'URL': 'https://cris.fau.de/converis/portal/Project/229909112?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Längerfristige Effekte von Networking im Karriereverlauf',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2010',
         'project_start': '01.03.2010',
         'URL': 'https://cris.fau.de/converis/portal/Project/229844625?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246,101487604', 'title': 'Leistungszentrum Elektroniksysteme (LZE)', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Overall project', 'project_end': '31.12.2017',
         'project_start': '01.01.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/213936695?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101487604,102333246',
                                       'title': 'Wirtschaftswissenschaftliche Begleitung des Leistungszentrum Elektroniksysteme LZE Phase II',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2020', 'project_start': '03.12.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/233554892?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104056282', 'title': 'Makroökonomische Implikationen der Hartz IV-Arbeitsmarktreform',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '30.04.2022',
         'project_start': '01.05.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/216980616?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100502116',
                                       'title': 'Marktkonsistente Bewertung und Solvenzmessung in der Versicherungsindustrie',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2012', 'project_start': '01.01.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126175243?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Maßnahmen und Empfehlungen für die gesunde Arbeit von morgen (MEgA)',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '30.04.2019',
         'project_start': '01.06.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/126212085?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104991104,101146760',
                                       'title': 'Die Effektivität von Interventionen zur Gesundheitsförderung und -Prävention bei Arbeitslosen – eine Metaanalyse',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2021', 'project_start': '01.09.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/246075156?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246,103652228',
                                       'title': 'Metaprojekt BALANCE: Flexibilität und Stabilität in der Forschungswelt',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '31.12.2013', 'project_start': '01.09.2009',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126476908?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101494856', 'title': 'Midijobs verstehen', 'funder': 'None',
                                       'project_type': 'Third Party Funds Single', 'project_end': '30.09.2021',
                                       'project_start': '01.10.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/216980841?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100088458', 'title': 'gif Policy Paper: Angebotseffekte der Mietpreisbremse',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2018',
         'project_start': '01.07.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/203409396?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774',
                                       'title': 'Zugehörigkeit Frau Prof. Dr. Veronika Grimms zur Kommission aus Energieexperten zur Unterstützung des Monitoring-Prozesses zur Überprüfung des Maßnahmenprogramms der Bundesregierung, mit dem Ziel sich zu einer der energieeffizientesten und umweltschonendsten Volkswirtschaften der Welt zu entwickeln.',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.06.2023', 'project_start': '01.07.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/226016315?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103586862', 'title': 'Monopsonistische Diskriminierung am deutschen Arbeitsmarkt',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '30.11.2015',
         'project_start': '01.01.2009',
         'URL': 'https://cris.fau.de/converis/portal/Project/211299156?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Persönliches Wachstum in Beruf, Ausbildung und Leben: Ein Kurs zur Motivationssteigerung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2022', 'project_start': '01.04.2022',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/272753030?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101532292',
                                       'title': 'Nachhaltige Weiterentwicklung der betrieblichen Informationsverarbeitung',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': 'None',
                                       'project_start': '01.01.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/231732152?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100489180', 'title': 'NEPS', 'funder': 'None', 'project_type': 'Third Party Funds Single',
         'project_end': '31.12.2016', 'project_start': '01.01.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/125975147?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Networking: Eine Längsschnittstudie (Hans-Frisch-Stiftung)',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2004',
         'project_start': '01.01.2001',
         'URL': 'https://cris.fau.de/converis/portal/Project/235288035?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101487604', 'title': 'Neue Arbeitswelten in Pilotflächen', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.03.2020', 'project_start': '01.10.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/201306732?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104385954', 'title': 'Nichtfinanzielle Unternehmenspublizität', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': 'None', 'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/210709481?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104452594', 'title': 'NN / NZ Klinikcheck', 'funder': 'None', 'project_type': 'Own Funds',
         'project_end': 'None', 'project_start': '01.01.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/265666346?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105329106',
                                       'title': 'Objektive und subjektiv erfahrene finanzielle Ungleichheit von Einkommen und Vermögen und deren Konsequenzen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.08.2024', 'project_start': '01.09.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/258843837?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '239219621',
                                       'title': 'Ökonomische Effekte aus einem bürgerfreundlichen Einkommensteuerbescheid',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2021', 'project_start': '01.01.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/250333875?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101487604', 'title': 'Service Innovation 2019 – Open Service Lab', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2019', 'project_start': '01.01.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/232130608?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102917228',
                                       'title': 'Patientenzufriedenheit in den sozialen Medien – Handlungsempfehlung für niedersächsische Kliniken',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '31.08.2021', 'project_start': '01.09.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/242851869?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105108214', 'title': 'Software-Prototypen für die erfahrbare Integration', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Sub project', 'project_end': '30.11.2015',
         'project_start': '01.12.2013',
         'URL': 'https://cris.fau.de/converis/portal/Project/126473866?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Performance Management in Teams', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.08.2017', 'project_start': '01.09.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/203233379?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760,105006980', 'title': 'Personalpolitik in genossenschaftlichen Unternehmen',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '30.04.2014',
         'project_start': '01.04.2013',
         'URL': 'https://cris.fau.de/converis/portal/Project/229845061?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101305324', 'title': 'Prescriptive healthcare analytics', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2019', 'project_start': '01.01.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/217300806?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760,103861360',
                                       'title': 'Projektseminar zur praxisorientierten Vermittlung von Moderations- und Evaluationskompetenzen anhand eines Trainings zur Bewältigung von digitalem Stress',
                                       'funder': 'None', 'project_type': 'FAU Funds', 'project_end': '30.09.2018',
                                       'project_start': '01.04.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229846209?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105108214',
                                       'title': 'Deutsch-Russisches Innovationsforum - Promoting business process management excellence in Russia',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '30.04.2012', 'project_start': '01.11.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126342891?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Psychologische Aspekte der Leiharbeit', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2002', 'project_start': '01.01.2000',
         'URL': 'https://cris.fau.de/converis/portal/Project/235286076?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Psychologisches Kapital als Determinante von Eskalierendem Commitment in Organisationen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.06.2013', 'project_start': '01.03.2013',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229843930?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101320710',
                                       'title': 'Public financial disclosure and labor costs: Empirical evidence from a quasi-experiment',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '01.07.2019', 'project_start': '01.01.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/213828632?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105108214', 'title': 'PUSH Münsterland: Produkt-Servicekombinationen entwickeln und nutzen',
         'funder': 'None', 'project_type': 'Fremdprojekt', 'project_end': '14.08.2015', 'project_start': '15.08.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/126251462?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Anschlüsse eröffnen - Entwicklungen ermöglichen.\r\nQualifizierungsbausteine inklusiv in einer dualisierten Ausbildungsvorbereitung',
                                       'funder': 'None', 'project_type': 'Fremdprojekt', 'project_end': '30.06.2018',
                                       'project_start': '01.01.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210687479?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104452594',
                                       'title': 'Qualitätstransparenz in der Hüftendoprothetik durch Patient Reported Outcomes',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.04.2022', 'project_start': '01.05.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/239358876?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102917228',
                                       'title': 'Qualitätstransparenz in der Hüftendoprothetik durch Patient Reported Outcomes',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '28.02.2022', 'project_start': '01.01.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/208670663?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Rechtfertigungsdruck und eskalierendes Commitment', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2005', 'project_start': '01.01.2003',
         'URL': 'https://cris.fau.de/converis/portal/Project/235290009?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Reziprozitätsprozesse im Kontext von Peer-Feedback', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.10.2018', 'project_start': '01.01.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/204086652?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101975056',
                                       'title': 'Relations between the European Union and Latin America: Future scenarios in a changing world',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': 'None', 'project_start': '01.07.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/253525846?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774,100248492', 'title': 'Die Entstehung von Reputation in Wirtschaftsbeziehungen',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '20.09.2012',
         'project_start': '01.04.2010',
         'URL': 'https://cris.fau.de/converis/portal/Project/126395450?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Forschung zu den psychischen Auswirkungen von Arbeitslosigkeit',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.03.2017',
         'project_start': '01.10.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/235000494?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Resilire - Altersübergreifendes Resilienz-Management',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project', 'project_end': '31.12.2017',
         'project_start': '01.11.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/126176257?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760,101148916', 'title': 'Resilire - Altersübergreifendes Resilienz-Management',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project', 'project_end': '31.10.2017',
         'project_start': '01.11.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/126433813?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246',
                                       'title': 'Maschinenfehlerdiagnose und Entwicklung von Rollen, Views, Schnittstellen und Anwender-Mockup',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.12.2016', 'project_start': '01.01.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/211013315?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105108214',
                                       'title': 'Propelling Business Process Management by Research and Innovation Staff Exchange',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.04.2019', 'project_start': '01.05.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126486372?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101320710',
                                       'title': 'Social Media-Kanäle als Informations\xadintermediäre (Schöller Junior Fellow 2017 Tim Herberger)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': 'None', 'project_start': '01.01.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/213829478?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Selbstkonzept und Selbstbeurteilung beruflicher Leistung',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2004',
         'project_start': '01.01.2003',
         'URL': 'https://cris.fau.de/converis/portal/Project/235290786?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101487604', 'title': 'Service Innovation (Teilvereinbarung 2017)', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2017', 'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/226980444?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Service Innovation – Teilvereinbarung 2018', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2018', 'project_start': '01.01.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/226532119?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Service Innovation Teilprojekt Vereinbarung 2012', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2012', 'project_start': '01.01.2012',
         'URL': 'https://cris.fau.de/converis/portal/Project/125854481?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Service Innovation Teilprojekt Vereinbarung 2013', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2013', 'project_start': '01.01.2013',
         'URL': 'https://cris.fau.de/converis/portal/Project/125803950?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Service innovation - Teilvereinbarung 2014', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2014', 'project_start': '01.01.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/126012158?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Service innovation - Teilvereinbarung 2015', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2015', 'project_start': '01.01.2015',
         'URL': 'https://cris.fau.de/converis/portal/Project/125804795?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Service innovation - Teilvereinbarung 2016', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2016', 'project_start': '01.01.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/126214451?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774,105358016,101433312,103589606',
                                       'title': 'Wohlfahrtsoptimale Nominierungen in Gasnetzen und zugehörige Gleichgewichte',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.06.2018', 'project_start': '01.10.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126509525?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104373606,212578052',
                                       'title': 'Siemens Competence Center Foresight für die industrielle Automatisierung und Digitalisierung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': 'None', 'project_start': '01.06.2022',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/274757098?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101597854',
                                       'title': 'Sino-German Perspectives on Corporate Social Responsibility and Sustainable Development',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2022', 'project_start': '01.01.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/233205494?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105108214',
                                       'title': 'Bilaterale Kooperationsanbahnung Brasilien - Evaluating Standards for Interorganizational Process Integration in Brazilian-German Value Networks',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': '31.05.2010',
                                       'project_start': '01.05.2010',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126488062?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '228682808,101585016',
                                       'title': 'Fähigkeiten, Erwartungen und Persönlichkeit als Determinanten des fächerspezifischen Studienerfolges',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2023', 'project_start': '01.10.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/246312300?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Skype as instrument to promote intercultural competences - a cross-cultural study between students of Germany and England',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': '31.12.2013',
                                       'project_start': '01.01.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210775078?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101487604,102333246',
                                       'title': 'Methodik und Konzeption für ein Fakten-basiertes Service Engineering (SmartDiF)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.08.2019', 'project_start': '01.09.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126240646?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246',
                                       'title': 'Harmonisierung der Entwicklung von komplexen Produkt-Smart-Service-Systemen bei KMU',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '31.05.2023', 'project_start': '01.06.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/239451749?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105108214',
                                       'title': 'smartmarket²: Entwicklung mobiler Applikationen für standortbezogene Dienstleistungen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '29.02.2020', 'project_start': '01.03.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126489583?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '103203388',
                                       'title': 'Analyse von Positonsdaten zur Ermittlung von Durchlaufzeiten in der Fertigung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.01.2021', 'project_start': '01.04.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/237637268?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '235233833',
                                       'title': 'Ein Brückenschlag: Reinforcement Learning auf Molekül- und Prozessgraphen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '28.02.2022', 'project_start': '01.03.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/248230232?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '219128459', 'title': 'Multidimensionales Conformance Checking für Prozesse',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.01.2023',
         'project_start': '01.02.2021',
         'URL': 'https://cris.fau.de/converis/portal/Project/247978698?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '203599239', 'title': 'Deep Learning im Kontext von Predictive Maintenance',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2021',
         'project_start': '01.01.2020',
         'URL': 'https://cris.fau.de/converis/portal/Project/231273464?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '228208413', 'title': 'Digitales Nudging und persuasives Design im Software-Kontext',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.01.2023',
         'project_start': '01.02.2021',
         'URL': 'https://cris.fau.de/converis/portal/Project/248303281?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105358800',
                                       'title': 'Interorganisationale Interdependenzen in Industrial-Internet-of-Things Geschäftsmodellen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.12.2020', 'project_start': '01.01.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/221261171?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '227730973', 'title': 'Nonparametric Bayesian Learning in Distributed Systems',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.01.2023',
         'project_start': '01.02.2021',
         'URL': 'https://cris.fau.de/converis/portal/Project/248241839?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774,103589606', 'title': 'Implementierung im Marktumfeld', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2015',
         'project_start': '01.06.2012',
         'URL': 'https://cris.fau.de/converis/portal/Project/126509694?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Soziale Beziehungen zwischen Lernenden an beruflichen Schulen fördern: Abbau von Vorurteilen, Umgang mit Diskriminierung und Toleranzerziehung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.12.2016', 'project_start': '01.01.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210571289?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Soziale und ökonomische Kosten der Erwerbslosigkeit',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2020',
         'project_start': '01.01.1999',
         'URL': 'https://cris.fau.de/converis/portal/Project/235278882?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104373606,204206709', 'title': 'Spedicam & Logistik GmbH goes digital', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.05.2021', 'project_start': '01.06.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/239353667?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Evidenzbasiertes Motivationsmanagement zur Leistungsoptimierung im Profisport',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2013', 'project_start': '01.10.2012',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229841948?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101494856',
                                       'title': 'Erwerbstätigkeit von Müttern und kindliche Entwicklung: Eine Analyse der Determinanten im gesellschaftlichen Wandel',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.09.2017', 'project_start': '01.08.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/125846538?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102330404', 'title': 'Ausländische Bildungszertifikate auf dem deutschen Arbeitsmarkt',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.07.2017',
         'project_start': '01.08.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/125966021?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100248492', 'title': 'Ausländische Bildungszertifikate auf dem deutschen Arbeitsmarkt',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': 'None',
         'project_start': '01.08.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/126188594?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103222008', 'title': 'Löhne, Heterogenitäten und Arbeitsmarktdynamik', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2020',
         'project_start': '01.08.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/125914307?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101533762', 'title': '„Sprachförderung“ an der FOS Regensburg', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': '31.12.2013', 'project_start': '01.01.2012',
         'URL': 'https://cris.fau.de/converis/portal/Project/210774885?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101533762', 'title': 'Sprachförderung im fachlichen Unterricht an berufsbildenden Schulen',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2015',
         'project_start': '01.01.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/210684911?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Sprachsensibilisierung in der beruflichen Qualifizierung – Entwicklung und Erprobung von Qualifizierungsmodulen für Lehrkräfte in der beruflichen Weiterbildung für Migrantinnen und Migranten',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.12.2014', 'project_start': '01.01.2013',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210685301?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105782552', 'title': 'Sustainable Smart Industry', 'funder': 'None',
         'project_type': 'FAU Funds', 'project_end': '31.12.2018', 'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/126495836?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101320710', 'title': 'Smart Teaching in Accounting - Meeting Place Online',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '29.12.2022',
         'project_start': '30.12.2020',
         'URL': 'https://cris.fau.de/converis/portal/Project/261258597?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Stark in Alltag und Arbeit', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.08.2019', 'project_start': '01.09.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/203495671?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246,101487604',
                                       'title': '7 start-up summer schools in Europe on Information and Communications Technologies for young aspiring entrepreneurs',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2016', 'project_start': '01.01.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/213933123?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104386248,101309930', 'title': 'Steuerliche Anreize für Unternehmensansiedlungen',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2019',
         'project_start': '01.01.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/208484053?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100489180',
                                       'title': 'Stigma-Bewusstsein von Arbeitslosen und Vorurteile gegenüber Arbeitslosen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.06.2017', 'project_start': '01.07.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126107981?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Stimmung und Kategorisierung: Zum Einfluß emotionaler Zustände auf berufseignungsdiagnostische  Urteilsprozesse',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.1999', 'project_start': '01.01.1997',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235266965?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101320710',
                                       'title': 'Cooperation and Innovation for Good Practices – „International Learning Platform for Accountancy (ILPA)“',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.08.2017', 'project_start': '01.09.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/211009466?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104373606,102369016', 'title': 'Studie zur Digitalisierung im Mittelstand',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2017',
         'project_start': '01.07.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/204126968?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'SummerSchool "Electronic Monitoring" (10.-12.9.2018)',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.10.2018',
         'project_start': '01.01.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/236579489?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760,100489180',
                                       'title': 'Summer School: The Interplay of Work, Health and Organizational Success',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2014', 'project_start': '01.04.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235002008?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100502116',
                                       'title': 'Sustainable Business Models in Energy Markets: Perspectives for the Implementation of Smart Energy Systems',
                                       'funder': 'None', 'project_type': 'FAU Funds', 'project_end': '31.12.2016',
                                       'project_start': '01.01.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126391394?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101567376,101489466,101601774',
                                       'title': 'Koordinierte Kleinspeicher im Verteilnetz der N-ERGIE Aktiengesellschaft - Storage With Amply Redundant Megawatt (SWARM)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2017', 'project_start': '01.01.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126212930?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Symposium „Individuals in Temporary Agency Jobs“.', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.05.2007', 'project_start': '01.01.2007',
         'URL': 'https://cris.fau.de/converis/portal/Project/236493456?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774',
                                       'title': 'Taxation, Social Norms, and Compliance: Lessons for Institution Design',
                                       'funder': 'None', 'project_type': 'FAU Funds', 'project_end': '31.12.2014',
                                       'project_start': '01.01.2012',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/125938305?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100710170,101601774,104848514',
                                       'title': 'Teamwork Performance: Effects of Tracking Based Feedback Mechanisms on Performance and Health Biomarkers',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': 'None',
                                       'project_start': '01.03.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126151583?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101975056', 'title': 'The Bavarian Scientific Expedition to Brazil (1817-1820)',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': 'None',
         'project_start': '01.09.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/239284640?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101320710',
                                       'title': 'The Effects of the Financial Crisis on Cooperative Banks in Europe – A Critical Comparison',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.06.2017', 'project_start': '01.01.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/213828851?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100248492,102330404',
                                       'title': 'Die Arbeitsmarktintegration qualifizierter MigrantInnen im internationalen Vergleich',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.09.2020', 'project_start': '01.10.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/202161989?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Die psychologische Bedeutung von Arbeit', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.08.2018', 'project_start': '01.09.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/202228384?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'The R and RStudio Environment. Handling, Visualisation und Communication of Data in Science',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '28.02.2021', 'project_start': '01.03.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/234197063?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774', 'title': 'Die Rolle von Sozialer Identität für das Lernen in Netzwerken',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '09.10.2021',
         'project_start': '01.10.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/228016913?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101305324',
                                       'title': 'Entwicklung von Maßnahmen zur Schaffung von Transparenz und Vertrauen in DataAnalytics-Projekten',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '29.02.2020', 'project_start': '01.03.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/226959158?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774,101433312',
                                       'title': 'Mehrstufige gemischt-ganzzahlig nichtlineare Optimierung für Gasmärkte (B08) (2018 - 2022)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.06.2022', 'project_start': '01.07.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/204141447?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774', 'title': 'Trust in Character, Capability and Institutions', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.05.2015', 'project_start': '01.06.2012',
         'URL': 'https://cris.fau.de/converis/portal/Project/126408801?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104437110', 'title': 'Twitter-Daten', 'funder': 'None',
                                       'project_type': 'Third Party Funds Single', 'project_end': 'None',
                                       'project_start': '01.01.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/211410028?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Umsetzungskonzept: Training gegen Informationsüberflutung',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2003',
         'project_start': '01.01.2003',
         'URL': 'https://cris.fau.de/converis/portal/Project/235289231?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103342548', 'title': 'Understanding Job Creation: The Role of Firm Age and Job Duration',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2017',
         'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/202306978?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104386248', 'title': 'Steuerhinterziehung und Steuerbetrug bei der Mehrwertsteuer',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '30.09.2018',
         'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/125974302?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101585016',
                                       'title': 'Unternehmen, Märkte, Volkswirtschaften: Von der Massenveranstaltung zum arbeitsgruppenorientierten Forum.\r\nEin Pilot für die Transformation der Lehre in den WiSo‐Bachelorstudiengängen',
                                       'funder': 'None', 'project_type': 'FAU Funds', 'project_end': '30.09.2020',
                                       'project_start': '01.10.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/246311579?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102369016',
                                       'title': 'Vereinbarkeit strategischer Entscheidungen im Rahmen der digitalen Transformation mit moralisch-ethischen Werten der Mitarbeiter',
                                       'funder': 'None', 'project_type': 'FAU Funds', 'project_end': 'None',
                                       'project_start': '01.07.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/275131357?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104386248',
                                       'title': 'Einrichtung eines wissenschafttlichen Dienstes an der FAU im Rahmen der erneuten Übernahme des Vorsitzes des Unabhängigen Beirats beim Stabilitätsrat durch Herrn Prof. Dr. Büttner',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.08.2022', 'project_start': '01.09.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/264525710?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246,101487604',
                                       'title': 'Open Innovation für IT-Sicherheit Kritischer Infrastrukturen (VeSiKi)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.06.2018', 'project_start': '01.01.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126239801?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100502116,103271008', 'title': 'verschiedene Dienstleistungen', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.05.2026', 'project_start': '01.01.2012',
         'URL': 'https://cris.fau.de/converis/portal/Project/125827779?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Verwaltungsbenchmarking süddeutscher Universitäten', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': '31.12.2007', 'project_start': '01.01.2006',
         'URL': 'https://cris.fau.de/converis/portal/Project/235546753?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104452594',
                                       'title': 'Entwicklung eines Weiterbildungsangebotes im Bereich der altersgerechten Assistenzsysteme (AAL) für die Europäische Metropolregion Nürnberg (EMN)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2014', 'project_start': '01.07.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/239359745?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101487604', 'title': 'Weiterbildungszentrum Digital Transformation', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.03.2021', 'project_start': '01.01.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/238566523?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101530724', 'title': 'Weichenstellung', 'funder': 'None',
                                       'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.07.2022', 'project_start': '01.04.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/208609420?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104452594', 'title': 'Weiterbildungsprogramm Telemedizin', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '30.09.2016', 'project_start': '01.08.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/213950547?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100088458', 'title': 'Wer profitiert vom Wohnungsneubau?', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '30.06.2021', 'project_start': '01.07.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/204192458?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246,103652228',
                                       'title': 'WiIPOD Wertschätzungsnetzwerke als integrierte Innovationsinstrumente der Personal- und Organisationsentwicklung im Demografischen Wandel',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '30.04.2015', 'project_start': '01.08.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126283572?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101975056', 'title': 'Wirtschaft, Politik und Gesellschaft in Lateinamerika',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': 'None',
         'project_start': '01.09.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/203496385?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246',
                                       'title': 'Einführung und Verankerung des Karrierewegs der Tenure-Track-Professur, die vollständig den Anforderungen der Verwaltungsvereinbarung zwischen Bund und Ländern gemäß Artikel 91b Absatz 1 des Grundgesetztes über ein Programm zur Förderung des wissenschaftlichen Nachwuchses vom 16.06.2016 entspricht',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.10.2027', 'project_start': '01.12.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/200466045?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101533762', 'title': 'Wissenschaftliche Begleitung des Projektes KASper', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2015',
         'project_start': '01.01.2015',
         'URL': 'https://cris.fau.de/converis/portal/Project/210684606?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104386248',
                                       'title': 'Wissenschafttlicher Dienst des Unabhängigen Beirats des Stabilitätsrats',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.08.2020', 'project_start': '01.09.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/226647026?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101320710', 'title': "Zielführende Betriebsprüfungen durch Nutzung von 'Alternative Data'",
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2020',
         'project_start': '01.01.2020',
         'URL': 'https://cris.fau.de/converis/portal/Project/230024656?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104386248', 'title': 'Zukunft der EU-Finanzen', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '20.12.2015', 'project_start': '22.04.2015',
         'URL': 'https://cris.fau.de/converis/portal/Project/126337145?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '231610692,212578052,105005510', 'title': 'Zukunftsforschung im Supply Chain Management',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': 'None',
         'project_start': '04.05.2022',
         'URL': 'https://cris.fau.de/converis/portal/Project/274752864?auxfun=&lang=de_DE'})

    return render_template("home/tables.html",
                           research_projects=filtered_data_all_wiso_pro,
                           publications=filtered_data_all_wiso_publs)





@blueprint.route('/tables2')
@blueprint.route('/tables2.html')

def tables2():
    filtered_data_all_wiso_publs = []
    filtered_data_all_wiso_publs.append(
        {'title': '100% organic? A sustainable entrepreneurship perspective on the diffusion of organic clothing',
         'keywords': 'Corporate social responsibility; Corporate sustainability; Germany; Integrated production; Organic cotton; Supply chain management; Sustainability-oriented innovation; Sustainable entrepreneurship; Textile industry; Transformation',
         'author': 'Hansen E. G., Schaltegger S.', 'language': 'None', 'publish_year': '2013',
         'URL': 'https://cris.fau.de/converis/portal/Publication/122909864?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': '10 Jahre Qualitätsmanagement im österreichischen berufsbildenden Schulwesen mit QIBB: Fragen zu Monitoring und Evaluation eines Mehrebenensystem',
                                            'keywords': 'None',
                                            'author': 'Gramlinger Franz, Jonach Michaela, Wilbers Karl',
                                            'language': 'None', 'publish_year': '2014',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/107789484?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '1913. The World before the Great War - by C. Emmerson', 'keywords': 'Great War',
         'author': 'GL Gardini', 'language': 'None', 'publish_year': '2014',
         'URL': 'https://cris.fau.de/converis/portal/Publication/113168484?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '2012 Mexico election: The return of the Partido Revolucionario Institucional (PRI)',
         'keywords': 'None', 'author': 'Gardini GL', 'language': 'None', 'publish_year': '2012',
         'URL': 'https://cris.fau.de/converis/portal/Publication/252934657?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': "2012 Venezuela elections: Will Chavez's 4th mandate bring moderation or radicalization?",
         'keywords': 'None', 'author': 'Gardini GL', 'language': 'None', 'publish_year': '2012',
         'URL': 'https://cris.fau.de/converis/portal/Publication/252934406?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': '2013-14 State of the Future, Glenn, J.C./ Gordon, T.J./ Florescu, E., The Millennium Project, April 2014 (247 pages)',
                                            'keywords': 'None', 'author': 'von der Gracht H. A.', 'language': 'None',
                                            'publish_year': '2014',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/206787687?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '20 Jahre Spruchverfahren: Empirische Ergebnisse zu Anlässen und Formen der Abfindung',
         'keywords': 'None', 'author': 'Henselmann Klaus, Munkert MichaelJ., Winkler Nadine, Schrenker Claudia',
         'language': 'None', 'publish_year': '2013',
         'URL': 'https://cris.fau.de/converis/portal/Publication/110635184?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '20 Jahre Spruchverfahren: Empirische Ergebnisse zu Anlässen und Formen der Abfindung',
         'keywords': 'None', 'author': 'Henselmann Klaus', 'language': 'None', 'publish_year': '2014',
         'URL': 'https://cris.fau.de/converis/portal/Publication/118229144?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': '20 Jahre Spruchverfahren: Empirische Ergebnisse zum gerichtlichen Verfahrensgang und zum Ausgang von Spruchverfahren',
                                            'keywords': 'None',
                                            'author': 'Henselmann Klaus, Munkert MichaelJ., Winkler Nadine, Schrenker Claudia',
                                            'language': 'None', 'publish_year': '2013',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/110638044?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': '20 Jahre Spruchverfahren: Empirische Ergebnisse zur Abfindungserhöhung in Abhängigkeit vom Antragsteller und von den Bewertungssubjekten',
                                            'keywords': 'None',
                                            'author': 'Henselmann Klaus, Munkert MichaelJ., Winkler Nadine, Schrenker Claudia',
                                            'language': 'None', 'publish_year': '2013',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/110650804?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '21 Open Labs as Islands of Reason in the Digital Age', 'keywords': 'None',
         'author': 'Albrecht Fritzsche', 'language': 'None', 'publish_year': '2020',
         'URL': 'https://cris.fau.de/converis/portal/Publication/239510774?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '2.2 Kurz vorgestellt – Bücher zum Thema E-Learning', 'keywords': 'E-Learning1; Buchbesprechung2;',
         'author': 'Jahn Dirk, Kalsperger Maria, Dr. Trager Bernhard', 'language': 'German', 'publish_year': '2013',
         'URL': 'https://cris.fau.de/converis/portal/Publication/106787604?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '5 Strategien zur Deeskalation von Commitment', 'keywords': 'None', 'author': 'None',
         'language': 'None', 'publish_year': '2021',
         'URL': 'https://cris.fau.de/converis/portal/Publication/260407515?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '6th DACH+ Conference on Energy Informatics (EnInf 2017)', 'keywords': 'None',
         'author': 'Santini S, Tiefenbeck V', 'language': 'None', 'publish_year': '2018',
         'URL': 'https://cris.fau.de/converis/portal/Publication/227859388?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': '6 The Many Facets of Open Laboratories and Their Implications for Innovation Management',
         'keywords': 'None', 'author': 'Albrecht Fritzsche', 'language': 'None', 'publish_year': '2020',
         'URL': 'https://cris.fau.de/converis/portal/Publication/239627162?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abbildung der stationären allergologischen Expositionstestungen im deutschen DRG-System',
         'keywords': 'None', 'author': 'Treudler R, Meier F, Schöffski O, Simon J-C', 'language': 'German',
         'publish_year': '2012', 'URL': 'https://cris.fau.de/converis/portal/Publication/114711124?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Ab die Mail!', 'keywords': 'None', 'author': 'None', 'language': 'German', 'publish_year': '2003',
         'URL': 'https://cris.fau.de/converis/portal/Publication/108116844?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abgehängt - Unternehmenskultur und Veränderung.', 'keywords': 'Unternehmenskultur',
         'author': 'Widuckel W.', 'language': 'German', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/119458724?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abgeltungssteuer als Lösung?', 'keywords': 'Kohäsion', 'author': 'Scheffler W.', 'language': 'None',
         'publish_year': '2005', 'URL': 'https://cris.fau.de/converis/portal/Publication/107346844?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A bibliometric analysis of the German corporate governance research', 'keywords': 'None',
         'author': 'Eulerich M., Stiglbauer M., Haustein S.', 'language': 'None', 'publish_year': '2012',
         'URL': 'https://cris.fau.de/converis/portal/Publication/118817424?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A bibliometric review of scientific theory in futures and foresight: A commentary on Fergnani and Chermack 2021',
                                            'keywords': 'None', 'author': 'Münch C, von der Gracht HA',
                                            'language': 'English', 'publish_year': '2021',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/251576873?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abitur and what next? Reasons for gaining double qualifications in Germany',
         'keywords': 'Transformation; qualification; Forschungsbericht 2010; double qualification; Abitur',
         'author': 'None', 'language': 'None', 'publish_year': '2010',
         'URL': 'https://cris.fau.de/converis/portal/Publication/117482684?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Ablenkung oder Abkehr von der Politik? Mediennutzung im Geflecht politischer Orientierun\xadgen',
         'keywords': 'None', 'author': 'Holtz-Bacha C.', 'language': 'None', 'publish_year': '1990',
         'URL': 'https://cris.fau.de/converis/portal/Publication/217759061?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({'title': 'A Blueprint for Event-driven Business Activity Management',
                                         'keywords': 'Reference Architecture, Complex event processing, Business process management, Business process analytics, Business activity management',
                                         'author': 'Janiesch Christian, Matzner Matzner, Müller Oliver',
                                         'language': 'English', 'publish_year': '2011',
                                         'URL': 'https://cris.fau.de/converis/portal/Publication/112510244?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'About well-considered decisions, favorable alternatives and sudden ideas: A qualitative research to identify beliefs that influence women to study information systems in Germany',
                                            'keywords': 'None',
                                            'author': 'Oehlhorn Caroline, Laumer Sven, Maier Christian',
                                            'language': 'English', 'publish_year': '2017',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/205783058?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abschaffung der Abgeltungsteuer: Folgewirkungen auf die Unternehmensbesteuerung',
         'keywords': 'Kohäsion', 'author': 'Scheffler W., Christ R.', 'language': 'German', 'publish_year': '2016',
         'URL': 'https://cris.fau.de/converis/portal/Publication/116060164?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abschließende Bemerkungen zu den Erwiderungen von Foppa und Droz', 'keywords': 'None',
         'author': 'None', 'language': 'None', 'publish_year': '1989',
         'URL': 'https://cris.fau.de/converis/portal/Publication/119609424?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abschlussanalyse 4.0', 'keywords': 'None', 'author': 'Henselmann K', 'language': 'None',
         'publish_year': '2016', 'URL': 'https://cris.fau.de/converis/portal/Publication/200189263?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Abschlussbericht des Lehrforschungsprojekts Lebenswirklichkeit und Partizipation Jugendlicher in Nürnberg im Auftrag des Kreisjugendrings Nürnberg-Stadt',
                                            'keywords': 'None', 'author': 'Damelang A', 'language': 'None',
                                            'publish_year': '2013',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/117625244?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Abschlussprüferhonorare bei deutschen kapitalmarktorientierten Unternehmen\r\nEine Analyse der Entwicklung von Abschlussprüferhonoraren unter Berücksichtigung des IDW RS HFA 36 n. F. und der EU-Verordnung 537/2014',
                                            'keywords': 'None', 'author': 'Dimmer M', 'language': 'German',
                                            'publish_year': '2020',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/238554412?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abschreibungsfinanzierung', 'keywords': 'None', 'author': 'Fischer Thomas, Hitz J.',
         'language': 'None', 'publish_year': '2006',
         'URL': 'https://cris.fau.de/converis/portal/Publication/115230544?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abschreibungsfinanzierung', 'keywords': 'None', 'author': 'None', 'language': 'German',
         'publish_year': '2001', 'URL': 'https://cris.fau.de/converis/portal/Publication/245199850?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Abschreibungsfinanzierunng', 'keywords': 'None', 'author': 'None', 'language': 'German',
         'publish_year': '2001', 'URL': 'https://cris.fau.de/converis/portal/Publication/123068264?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Absence from Work of the Self-Employed: A Comparison with Paid Employees', 'keywords': 'None',
         'author': 'Lechmann D, Schnabel C', 'language': 'None', 'publish_year': '2014',
         'URL': 'https://cris.fau.de/converis/portal/Publication/118443204?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Absenteeism and Employment Probation - A Panel Study for Germany', 'keywords': 'None',
         'author': 'None', 'language': 'English', 'publish_year': '1999',
         'URL': 'https://cris.fau.de/converis/portal/Publication/120944164?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Absenteeism and Employment Protection: 3 Case Studies', 'keywords': 'None', 'author': 'None',
         'language': 'None', 'publish_year': '2004',
         'URL': 'https://cris.fau.de/converis/portal/Publication/122969264?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Absorptive Capacity as a Prerequisite for Open Innovation', 'keywords': 'None',
         'author': 'Ixmeier Johannes, Scheiner Christian, Voigt Kai-Ingo', 'language': 'English',
         'publish_year': '2011', 'URL': 'https://cris.fau.de/converis/portal/Publication/121666864?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Abweichungen zwischen Handels- und Steuerbilanz, Übersichten über die Reichweite des Maßgeblichkeitsprinzips und die Ausnahmen von der Maßgeblichkeit der Handelsbilanz für die Steuerbilanz',
                                            'keywords': 'Kohäsion', 'author': 'Scheffler W.', 'language': 'None',
                                            'publish_year': '2004',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/111123584?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Abweichungen zwischen Handels- und Steuerbilanz, Übersichten über die Reichweite des Maßgeblichkeitsprinzips und die Ausnahmen von der Maßgeblichkeit der Handelsbilanz für die Steuerbilanz',
                                            'keywords': 'Kohäsion', 'author': 'Scheffler W.', 'language': 'None',
                                            'publish_year': '2004',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/114374524?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({'title': 'Abweichungsanalyse bei Projekten im F&E-Bereich', 'keywords': 'None',
                                         'author': 'Fischer Thomas, Coenenberg Adolf G., Raffel Andreas',
                                         'language': 'German', 'publish_year': '1992',
                                         'URL': 'https://cris.fau.de/converis/portal/Publication/122077824?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Academic Entrepreneurship - Examining Motivating and Hindering Influences Through the Gender Lense; Internationalizing Entrepreneurship Education and Training - Innovative Formats for Entrepreneurship Education Teaching',
                                            'keywords': 'None',
                                            'author': 'Laspita S., Scheiner Christian, Chlosta S., Brem Alexander, Voigt Kai-Ingo, Klandt H.',
                                            'language': 'English', 'publish_year': '2007',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/120565984?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Academic Writing – Guidelines for a Term Paper, Bachelor and Master Thesis', 'keywords': 'None',
         'author': 'None', 'language': 'None', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/234792548?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Case About the Diffusion of Co-Creation Expertise in Organizations', 'keywords': 'None',
         'author': 'Krämer K., Roth Angela, Möslein Kathrin M.', 'language': 'None', 'publish_year': '2014',
         'URL': 'https://cris.fau.de/converis/portal/Publication/118831724?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Case Mining based Recommender System for Knowledge Workers', 'keywords': 'None', 'author': 'None',
         'language': 'None', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/114537544?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Accelerating Scientific Research with Open Laboratories', 'keywords': 'None',
         'author': 'Fritzsche A, Möslein K', 'language': 'None', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/116512924?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Accepting a crowdsourced delivery - a choice-based conjoint analysis', 'keywords': 'None',
         'author': 'Bathke H, Hartmann E', 'language': 'English', 'publish_year': '2021',
         'URL': 'https://cris.fau.de/converis/portal/Publication/269365499?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Accessing complex patient data from Arden Syntax Medical Logic Modules', 'keywords': 'None',
         'author': 'Stefan Kraus, Martin Enders, Hans-Ulrich Prokosch, Ixchel Castellanos, Richard Lenz, Martin Sedlmayr',
         'language': 'None', 'publish_year': '2018',
         'URL': 'https://cris.fau.de/converis/portal/Publication/216630771?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Access to Commitment Devices Reduces Investment Incentives in Oligopoly', 'keywords': 'None',
         'author': 'Grimm Veronika, Zöttl Gregor', 'language': 'English', 'publish_year': '2005',
         'URL': 'https://cris.fau.de/converis/portal/Publication/121259204?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Accounting for Sustainable Organisations: Where is the Accountant and why it Matters',
         'keywords': 'None', 'author': 'None', 'language': 'None', 'publish_year': '2011',
         'URL': 'https://cris.fau.de/converis/portal/Publication/123255484?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Accounting fraud: Case studies and practical implications', 'keywords': 'None',
         'author': 'Henselmann Klaus, Hofmann Stefan', 'language': 'English', 'publish_year': '2010',
         'URL': 'https://cris.fau.de/converis/portal/Publication/110531124?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Accounting Rules for SMEs in Germany - General Structure and Changes over Time',
         'keywords': 'Rechungslegung; Deutschland; EU; historisch; Mittelstand; KMU; SME; Accounting; Germany; History; Europe',
         'author': 'Henselmann K', 'language': 'English', 'publish_year': '2020',
         'URL': 'https://cris.fau.de/converis/portal/Publication/243473537?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Accuracy, unbiasedness and efficiency of professional macroeconomic forecasts: An empirical comparison for the G7',
                                            'keywords': 'Evaluating forecasts\r\nMacroeconomic forecasting\r\nRationality\r\nSurvey data\r\nFixed-event forecasts',
                                            'author': 'None', 'language': 'English', 'publish_year': '2011',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/216788980?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({'title': 'Achieving and assuring high availability', 'keywords': 'Innovation',
                                         'author': 'K.S. Trivedi, Ciardo G., Dasarathy B., Grottke Michael, Matias R., Rindos A., Vashaw B.',
                                         'language': 'None', 'publish_year': '2008',
                                         'URL': 'https://cris.fau.de/converis/portal/Publication/115263544?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Achieving Competitive Advantage from Sustainable Supplier Management - Insights from the Chemical Industry',
                                            'keywords': 'Innovation',
                                            'author': 'Reuter C., Förstl K., Hartmann E., Blome C.', 'language': 'None',
                                            'publish_year': '2009',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/121689084?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Achtsamkeit im organisationalen Kontext: Der Einfluss individueller und organisationaler Achtsamkeit auf resilientes Verhalten, psychische Gesundheit und Arbeitsengagement',
                                            'keywords': 'None', 'author': 'None', 'language': 'German',
                                            'publish_year': '2018',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/107190864?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Cluster Analysis of Pediatric Cancer Incidence Rates in Florida: 2000–2010', 'keywords': 'None',
         'author': 'None', 'language': 'None', 'publish_year': '2014',
         'URL': 'https://cris.fau.de/converis/portal/Publication/114691764?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({'title': 'ACM SIGMIS CPR 2020 Introduction', 'keywords': 'None',
                                         'author': 'Sven Laumer, Jeria Quesenberry, Damien Joseph, Christian Maier, Daniel Beimborn, Shirish C. Srivastava',
                                         'language': 'None', 'publish_year': '2020',
                                         'URL': 'https://cris.fau.de/converis/portal/Publication/255637517?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A community-based toolkit for designing ride-sharing services: The case of a virtual network of ride access points in Germany',
                                            'keywords': 'Innovation',
                                            'author': 'Hansen E. G., Gomm M. L., Bullinger A.C., Möslein Kathrin M.',
                                            'language': 'None', 'publish_year': '2010',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/114151444?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A commuting-based refinement of the contiguity matrix for spatial models, and an application to local police expenditures',
                                            'keywords': 'spatial weights; contiguity matrix; commuting flows; police expenditures',
                                            'author': 'Rincke Johannes', 'language': 'English', 'publish_year': '2010',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/118021244?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Comparative Analysis of the Australian and German eHealth System', 'keywords': 'None',
         'author': 'None', 'language': 'English', 'publish_year': '2016',
         'URL': 'https://cris.fau.de/converis/portal/Publication/124065304?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Comparative Assessment of Basel II/III and Solvency II', 'keywords': 'Solvency II; Basel II/III',
         'author': 'Gatzert Nadine, Wesker Hannah', 'language': 'English', 'publish_year': '2012',
         'URL': 'https://cris.fau.de/converis/portal/Publication/114515984?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A comparative perspective on political advertising in western democracies: implications of media and political system characteristics',
                                            'keywords': 'None', 'author': 'Holtz-Bacha C, Kaid Lynda L.',
                                            'language': 'None', 'publish_year': '1995',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/219599238?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({'title': 'A comprehensive wealth index for cities in Germany',
                                         'keywords': 'Cities in Germany; Comprehensive wealth index',
                                         'author': 'Dovern J., Quaas M., Rickels W.', 'language': 'None',
                                         'publish_year': '2014',
                                         'URL': 'https://cris.fau.de/converis/portal/Publication/204170331?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Conceptual Framework of Service Innovation and Its Implications for Future Research',
         'keywords': 'Conceptual framework; Service innovation; Service science; Service-dominant logic',
         'author': 'Sven Schwarz, Carolin Durst, Freimut Bodendorf', 'language': 'None', 'publish_year': '2012',
         'URL': 'https://cris.fau.de/converis/portal/Publication/120019504?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Conceptualized Investment Model of Crowdfunding', 'keywords': 'Crowdfunding',
         'author': 'Tomczak A, Brem A', 'language': 'English', 'publish_year': '2013',
         'URL': 'https://cris.fau.de/converis/portal/Publication/108691924?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A conceptualized investment model of crowdfunding', 'keywords': 'None',
         'author': 'Tomczak Alan, Brem Alexander', 'language': 'None', 'publish_year': '2016',
         'URL': 'https://cris.fau.de/converis/portal/Publication/108692144?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A configuration of sustainable sourcing and supply management strategies', 'keywords': 'None',
         'author': 'None', 'language': 'English', 'publish_year': '2017',
         'URL': 'https://cris.fau.de/converis/portal/Publication/119561904?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Context Aware Mobile Application for Physical Activity Promotion', 'keywords': 'None',
         'author': 'Hamper Andreas', 'language': 'None', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/114567684?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Continuous Logit Hotelling Model with Endogenous Locations of Consumers',
         'keywords': 'Spatial competition; Continuous logit model; Minimum differentiation principle',
         'author': 'Matthias Wrede', 'language': 'English', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/108803244?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({'title': 'A Continuous Spatial Choice Logit Model of a Polycentric City.',
                                         'keywords': 'Urban spatial equilibrium; Polycentric city; Probabilistic location choices; Continuous logit model; Cross-commuting',
                                         'author': 'Matthias Wrede', 'language': 'English', 'publish_year': '2015',
                                         'URL': 'https://cris.fau.de/converis/portal/Publication/122098724?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Acquiring new customers by price comparison sites vs. direct marketing: Long-term effects on customer loyalty and cross-buying in a contractual setting',
                                            'keywords': 'None', 'author': 'None', 'language': 'None',
                                            'publish_year': '2020',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/240747535?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Credit Portfolio Framework under Dependent Risk Parameters PD, LGD and EAD', 'keywords': 'None',
         'author': 'Matthias Fischer, Kevin Jakob, Johanna Eckert', 'language': 'English', 'publish_year': '2016',
         'URL': 'https://cris.fau.de/converis/portal/Publication/116016164?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A cross-domain comparison of application areas for service systems based on cyber-physical systems',
         'keywords': 'service systems; service systems engineering, cyber-physical systems', 'author': 'Oks S J',
         'language': 'English', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/110252604?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A Cross-National Study of the Effects of Education on Pre-Service Teachers’ Attitudes, Intentions, Concerns, and Self-Efficacy Regarding Inclusive Education',
                                            'keywords': 'Inclusion; teacher education; Canada; Germany; attitudes; intentions; concerns; self-efficacy; Inklusion;',
                                            'author': 'Miesera Susanne, Sokal Laura, Kimmelmann Nicole',
                                            'language': 'English', 'publish_year': '2021',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/268597337?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A cross-sectional study assessing the association between online ratings and clinical quality of care measures for US hospitals: results from an observational study.',
                                            'keywords': 'None', 'author': 'Emmert M, Meszmer N, Schlesinger M',
                                            'language': 'None', 'publish_year': '2018',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/106835784?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A cross-sectional study assessing the association between online ratings and structural and quality of care measures: results from two German physician rating websites.',
                                            'keywords': 'None',
                                            'author': 'Emmert M, Adelhardt T, Sander U, Wambach V, Lindenthal J',
                                            'language': 'None', 'publish_year': '2015',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/120070324?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Active Sourcing und Social Recruiting - Ausgewählte Ergebnisse der Recruiting Trends 2016 und der Bewerbungspraxis 2016',
                                            'keywords': 'None',
                                            'author': 'Weitzel Tim, Laumer Sven, Maier Christian, Oehlhorn Caroline, Wirth Jakob, Weinert Christoph, Eckhardt Andreas',
                                            'language': 'German', 'publish_year': '2016',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/208765364?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Active Sourcing und Social Recruiting - Ausgewählte Ergebnisse der Recruiting Trends 2017 und der Bewerbungspraxis 2017',
                                            'keywords': 'None',
                                            'author': 'Weitzel Tim, Laumer Sven, Maier Christian, Oehlhorn Caroline, Wirth Jakob, Weinert Christoph, Eckhardt Andreas',
                                            'language': 'German', 'publish_year': '2017',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/206235115?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Activity-Based Costing and Performance Measurement in the Electronics Industry', 'keywords': 'None',
         'author': 'None', 'language': 'None', 'publish_year': '1995',
         'URL': 'https://cris.fau.de/converis/portal/Publication/245268155?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Activity-based working: How the use of available workplace options increases perceived autonomy in the workplace',
                                            'keywords': 'None', 'author': 'None', 'language': 'English',
                                            'publish_year': '2022',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/266062440?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Actor and Institutional Dynamics in the Development of Multi-Stakeholder Initiatives',
         'keywords': 'Business self-regulation; Club theory; Global governance; Institutional entrepreneurship; Institutional theory; Management of diverse interests; Multi-stakeholder initiatives; Political role of the firm; Soft law',
         'author': 'Zeyen Anica, Beckmann Markus, Wolters Stella', 'language': 'None', 'publish_year': '2016',
         'URL': 'https://cris.fau.de/converis/portal/Publication/122177264?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Actor integration in service systems – exploring effects on a micro level', 'keywords': 'None',
         'author': 'Jonas J, Roth A, Möslein K', 'language': 'None', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/122100924?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A Customer Perspective on Product Eliminations: How the Removal of Products Affects Customers and Business Relationships',
                                            'keywords': 'Forschungsbericht 2010; Innovation',
                                            'author': 'Homburg Ch., Fürst Andreas, Prigge J.-K.', 'language': 'None',
                                            'publish_year': '2010',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/117743604?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Adaptation to the market? Status differences between target occupations in the application process and realized training occupation of German adolescents',
                                            'keywords': 'None', 'author': 'Schels B, Abraham M', 'language': 'English',
                                            'publish_year': '2021',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/262083973?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Adaption der Berufsaspiration bei Jugendlichen - eine Befragung von Haupt- und Realschüler/innen in Nürnberg. Überblick über die Studie und Datendokumentation',
                                            'keywords': 'None', 'author': 'Abraham M, Dietrich H, Sachse H, Schels B',
                                            'language': 'German', 'publish_year': '2015',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/108913904?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Adaptive Case Management: Anwendung des Business Process Management 2.0-Konzepts auf schwach strukturierte Geschäftsprozesse',
                                            'keywords': 'None', 'author': 'Christian Herrmann, Matthias Kurz',
                                            'language': 'None', 'publish_year': '2011',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/109360284?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Adaptive Innovation Management - Concept and Tool Support', 'keywords': 'None',
         'author': 'Sebastian Huber, Christian Mühlroth, Freimut Bodendorf', 'language': 'None', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/122114564?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Adaptive Open Innovation - Solution Approach and Tool Support', 'keywords': 'None',
         'author': 'Sebastian Huber, Peter Schott, Matthias Lederer', 'language': 'English', 'publish_year': '2015',
         'URL': 'https://cris.fau.de/converis/portal/Publication/109270084?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Dark Side of Telework: A Social Comparison-Based Study from the Perspective of Office Workers',
         'keywords': 'Social comparison theory; Telework; Envy; Turnover; Job performance; Empirical study; COVID-19',
         'author': 'None', 'language': 'English', 'publish_year': '2022',
         'URL': 'https://cris.fau.de/converis/portal/Publication/277654048?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'Additive Fertigung für industrielle Anwendungen - Entwicklung einer Auswahlsystematik für Bauteile zur Generierung funktionalen Mehrwerts mittels additiver Fertigung',
                                            'keywords': 'None',
                                            'author': 'Thomas Papke, Dominic Bartels, Michael Schmidt, Marion Merklein, Daniel Gerhard, Jonas Baumann, Indra Pitz',
                                            'language': 'None', 'publish_year': '2020',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/245752967?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': "Addressing a product management's orphan: How to externally implement product eliminations in a B2B setting",
                                            'keywords': 'None', 'author': 'Prigge JK, Homburg C, Fürst A',
                                            'language': 'English', 'publish_year': '2018',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/119815784?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'Addressing sustainability information needs along supply chains', 'keywords': 'Nachhaltigkeit;',
         'author': 'None', 'language': 'English', 'publish_year': '2019',
         'URL': 'https://cris.fau.de/converis/portal/Publication/229265156?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': '[A Decade of Online Physician-Rating Websites in Germany: an Assessment of the Current Level of Development].',
                                            'keywords': 'None', 'author': 'Emmert M, Meszmer N', 'language': 'None',
                                            'publish_year': '2017',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/106774844?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A decision support scheme for software process improvement prioritization', 'keywords': 'Innovation',
         'author': 'A. Beckhaus, L.M. Karg, C. Graf, Grottke Michael, D. Neumann', 'language': 'English',
         'publish_year': '2011', 'URL': 'https://cris.fau.de/converis/portal/Publication/111819664?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A Deep Learning Approach for Managing Medical Consumable Materials in Intensive Care Units via Convolutional Neural Networks: Technical Proof-of-Concept Study',
                                            'keywords': 'convolutional neural networks; deep learning; critical care; intensive care; image recognition; medical economics; medical consumables; artificial intelligence; machine learning',
                                            'author': 'Peine A., Hallawa A., Schöffski O., Dartmann G., Begic Fazlic L., Schmeink A., Marx G., Martin L.',
                                            'language': 'None', 'publish_year': '2019',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/229850573?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A Delphi-based risk analysis — Identifying and assessing future challenges for supply chain security in a multi-stakeholder environment',
                                            'keywords': 'Risk; Supply chain security; Terroristic attacks; Delphi; Multi-stakeholder; Future',
                                            'author': 'Markmann C, Darkow I, von der Gracht H', 'language': 'None',
                                            'publish_year': '2013',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/205750466?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A description of the operative decision-making process of a power generating company on the Nordic electricity market',
                                            'keywords': 'Bidding strategy; Decisions under uncertainty; Electricity trading; Nordic power system; Power producer; Risk management',
                                            'author': 'Scharff R., Egerer J., Söder L.', 'language': 'None',
                                            'publish_year': '2014',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/119616024?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A discussion on the General Data Protection Regulation Eine Diskussion zur Datenschutz-Grundverordnung',
                                            'keywords': 'None', 'author': 'Peter Mertens', 'language': 'None',
                                            'publish_year': '2020',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/244599733?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append({
                                            'title': 'A dissent-based approach for multi-stakeholder scenario development — The future of electric drive vehicles',
                                            'keywords': 'Scenarios; Delphi; Multi-stakeholder; Dissent; Electric drive vehicles',
                                            'author': 'Warth J, von der Gracht HA, Darkow I', 'language': 'None',
                                            'publish_year': '2013',
                                            'URL': 'https://cris.fau.de/converis/portal/Publication/205775947?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_publs.append(
        {'title': 'A Distortive Wage Tax and a Countervailing Commuting Subsidy', 'keywords': 'Transformation',
         'author': 'Wrede Matthias', 'language': 'English', 'publish_year': '2009',
         'URL': 'https://cris.fau.de/converis/portal/Publication/114251984?auxfun=&lang=de_DE'})

    filtered_data_all_wiso_pro = []
    filtered_data_all_wiso_pro.append({'project_leader': '105707876,101530724,105329106',
                                       'title': 'Individuell empfohlen? - Wie KI-basierte Beratungssysteme die Diversität der Studierenden beeinflussen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '28.02.2021', 'project_start': '01.03.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235228880?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'AI for Public Services', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '01.06.2024', 'project_start': '01.04.2021',
         'URL': 'https://cris.fau.de/converis/portal/Project/257929870?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '200418444', 'title': 'AI for Industry 4.0: models and technologies', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.07.2020', 'project_start': '01.07.2020',
         'URL': 'https://cris.fau.de/converis/portal/Project/237715326?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '203395223',
                                       'title': 'Künstliche Intelligenz zur Erschließung von Potentialen zur Semi-Prozessautomatisierung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2020', 'project_start': '01.01.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/221488811?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105329106',
                                       'title': 'Eine lebensverlaufssoziologische Perspektive auf das Arbeitsangebot: Zeitliche, institutionelle und soziale Einbettung als Determinanten individueller Reservationslöhne',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.01.2022', 'project_start': '01.02.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/228016423?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Alles Sprache oder was? Qualifizierung von Mentorinnen und Mentoren für ein sprachsensibles Mentoring von Geflüchteten',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': '30.09.2021',
                                       'project_start': '01.04.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/250249701?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760,104991104',
                                       'title': 'Arbeitslosigkeit und Behinderung unter Berücksichtigung der Covid-19-Pandemie und ihrer Bewältigung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.11.2024', 'project_start': '01.12.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/271088154?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760,101148916', 'title': 'Konzeption von Diagnose- und Evaluationsinstrumenten',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.10.2017',
         'project_start': '01.11.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/126433982?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101305324',
                                       'title': 'Analyse und Optimierung standardisierter Behandlungsprozesse im Krankenhaus',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2016', 'project_start': '01.05.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/203774296?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Arbeiten, Lernen und Weiterbildung in der Zeitarbeit - Eine Befragung von Erwerbstätigen in der Zeitarbeit',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2007', 'project_start': '01.01.2005',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235292385?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101494856', 'title': 'Arbeitsmarkteffekte der Reform des vorzeitigen Rentenbezugs',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.03.2020',
         'project_start': '01.09.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/205223927?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Arbeitszeugnisse in Deutschland: Der Einfluss von Geschlecht, Position und Unternehmensmerkmalen auf Inhalt und Bewertung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2012', 'project_start': '01.04.2012',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229844378?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100502116',
                                       'title': 'Eine Analyse von Reputationsrisiken und Spillover-Risiken aus Perspektive der Versicherungswirtschaft',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.11.2018', 'project_start': '01.06.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126185890?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '242689003', 'title': 'None', 'funder': 'None', 'project_type': 'Own Funds',
         'project_end': 'None', 'project_start': '01.09.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/263866704?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101975056', 'title': 'Atlantic Future - Regionalism and inter-regionalism (WP8)',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2015',
         'project_start': '01.01.2013',
         'URL': 'https://cris.fau.de/converis/portal/Project/125810879?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104386248,239219621', 'title': 'Aufkommenseffekte von Steuerrechtsänderungen',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2022',
         'project_start': '01.01.2022',
         'URL': 'https://cris.fau.de/converis/portal/Project/267037038?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101494856',
                                       'title': 'Auswirkungen der Elterngeldreform auf Haushaltsstrukturen und Familiengründung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2016', 'project_start': '01.01.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/213945993?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760,103888408',
                                       'title': 'AVENUE - Zusammenstellung von Verfahren zur Ermittlung von neuen Formen der Arbeitsverdichtung und ihren Folgen sowie von Maßnahmen zur Prävention (Arbeitstitel: AVENUE)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.05.2021', 'project_start': '01.03.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/226649511?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105108214',
                                       'title': 'Bayessche Vorhersagemodelle auf Basis von Kontextinformationen für das Monitoring von Geschäftsprozessen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2018', 'project_start': '06.03.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/201722116?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Belastungen und Beanspruchung im Kontext atypischer Karrieren und flexibler Beschäftigungsverhältnisse',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2006', 'project_start': '01.01.2004',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235292115?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101872450',
                                       'title': 'Ausweitung der Bedarfsorientierten Budgetierung auf städtische berufliche Schulen mit Schwerpunkt Heterogenität',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2024', 'project_start': '01.10.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/266476875?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101872450',
                                       'title': 'Bedarfsorientierte Budgetierung an ausgewählte städtischen Berufsschulen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2021', 'project_start': '01.01.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/226019340?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101533762', 'title': 'Berufssprache Deutsch', 'funder': 'None', 'project_type': 'Own Funds',
         'project_end': '31.12.2014', 'project_start': '01.01.2011',
         'URL': 'https://cris.fau.de/converis/portal/Project/210774505?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '103586862',
                                       'title': 'Betriebsschließungen in Deutschland: Umfang, Verlauf und Einflussfaktoren',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.03.2013', 'project_start': '01.02.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126148710?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762,101734956',
                                       'title': 'Bildungsbenachteiligung und COVID-19: Herausforderungen und Auswirkungen des pandemiebedingten Homeschoolings sowie damit verbundener digitaler Lehr-Lernformate auf junge Geflüchtete in dualer Ausbildung.',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': '31.03.2021',
                                       'project_start': '01.04.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/250249303?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101530724',
                                       'title': 'BIRD steht für kaufmännische und gewerblich-technische Angebote zu Industrie 4.0 auf der Plattform der DQR-Stufe 5 als Motor der Durchlässigkeit zwischen Berufsausbildung und schulischer Fortbildung (Fach-/Technikerschule), IHK-Fortbildung (Fachwirt/in, Fachmeister/in) und akademischer Bildung (Bachelorstudium)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '29.02.2020', 'project_start': '01.09.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/228125107?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101530724',
                                       'title': 'Attraktive, durchlässige und Bildungs- und Beratungsangebote in der schulischen und außerschulischen beruflichen Aus- und Weiterbildung sowie der akademischen Bildung im blended-learning-Design am Beispiel neuer Anforderungen durch Industrie 4.0 unter strategischer Nutzung der ersten Fortbildungsstufe',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2024', 'project_start': '01.10.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/246600157?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105108214',
                                       'title': 'Internationales Forschnungsnetzwerk für E-Government zwischen Deutschland und Brasilien',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '30.06.2009', 'project_start': '01.01.2006',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126475556?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103861360', 'title': 'Careers in transition: Karrierecoaching und Karriereerfolg',
         'funder': 'None', 'project_type': 'Own Funds', 'project_end': 'None', 'project_start': '01.04.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/229903464?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '242689003,inv,inv', 'title': 'None', 'funder': 'None', 'project_type': 'Fremdprojekt',
         'project_end': 'None', 'project_start': '01.09.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/263863669?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101309146',
                                       'title': 'Kausale Effekte von Lohnsubventionen auf Arbeitsangebot und Arbeitsnachfrage',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2017', 'project_start': '01.01.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126123867?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760,104991104',
                                       'title': 'Veränderung von Covid-19-bezogenen Sorgen und Ängsten, Risikowahrnehmungen und Präventionsverhalten im Verlauf der Pandemie: Längsschnittliche Vorhersage präventionsbezogener Variablen in einer vulnerablen Stichprobe ehemals arbeitsloser Personen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2022', 'project_start': '01.01.2022',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/271344712?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Connecting the Cooperative (CoCo)', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '30.06.2016', 'project_start': '01.07.2013',
         'URL': 'https://cris.fau.de/converis/portal/Project/211012798?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246,101487604', 'title': 'Cooperatives in the Digital Age (CoDi)', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.03.2018', 'project_start': '01.10.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/126231182?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246,101487604',
                                       'title': 'Community-basierte Dienstleistungs-Innovation für e-Mobility (CODIFeY)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.10.2017', 'project_start': '01.11.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/203640687?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105782552',
                                       'title': 'Conjoint-basierte Bedürfnisanalyse von Kreditgenossenschaftskunden im digitalen Zeitalter und Implikationen für das genossenschaftliche Geschäftsmodell',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.04.2017', 'project_start': '01.05.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126163244?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100501136,102333246',
                                       'title': 'Advanced Systems Configuration zur komplexitätsreduzierten sensorgetriebenen Entwicklung von Produktionssystemen im digitalen Zeitalter (ConSensE)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '29.02.2024', 'project_start': '01.03.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/272534948?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Corporate Social Responsibility und die Attraktivität von Arbeitgebermarken am Beispiel von Genossenschaftsbanken',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': 'None', 'project_start': '01.04.2012',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229844855?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105782552', 'title': 'Creating the bank account of the future', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '30.04.2018', 'project_start': '01.10.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/200434253?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105108214', 'title': 'Nutzerakzeptanz und Dienstleistungskonzeption', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Sub project', 'project_end': '28.02.2015',
         'project_start': '01.12.2013',
         'URL': 'https://cris.fau.de/converis/portal/Project/126338835?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Methoden der Datenerhebung in den Sozial- und Verhaltenswissenschaften',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '28.02.2022', 'project_start': '01.03.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/248524831?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '275370701',
                                       'title': 'Data-driven analysis, benchmarking, and coordination of European IS-curricula',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.05.2023', 'project_start': '01.06.2022',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/276125534?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104052166',
                                       'title': 'Entwicklung der Systematik und der Algorithmen des Umfeld-Scanning-Systems',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.07.2020', 'project_start': '01.08.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/202426626?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101975056',
                                       'title': 'Debunking Interregionalism: concepts, types, critiques. German-Portuguese strategic action fund. To train young researchers.',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': 'None', 'project_start': '01.01.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/213823018?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104991104,101146760',
                                       'title': 'Deprivierte Bedürfnisse und inkongruente Werte - Untersuchungen zu den Ursachen des seelischen Leidens Arbeitsloser',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.07.2016', 'project_start': '01.08.2013',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126112544?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101585016',
                                       'title': 'Der Algorithmus, Dein Freund und Helfer: \r\nDatenbasierte Orientierungshilfe in der Studieneingangsphase des Bachelorstudiengangs Wirtschaftswissenschaften',
                                       'funder': 'None', 'project_type': 'FAU Funds', 'project_end': '30.09.2020',
                                       'project_start': '01.10.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/246311348?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102917228,104452594',
                                       'title': 'Der Einfluss von Patient Reported Outcomes auf die Akzeptanz von Qualitätstransparenzinitiativen für die Krankenhausauswahl',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2019', 'project_start': '01.02.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/216817177?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100550528',
                                       'title': 'Der Reification Bias in der Marketing-Kommunikation: Einflussfaktoren und Auswirkungen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.03.2020', 'project_start': '01.04.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126504286?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101320710', 'title': 'Designing Innovative Pedagogy for Complex Accountancy Topics',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.08.2021',
         'project_start': '01.09.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/208528908?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Determinanten der Verkehrsmittelwahl', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2001', 'project_start': '01.01.1999',
         'URL': 'https://cris.fau.de/converis/portal/Project/235284276?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105108214',
                                       'title': 'German-Brazilian Workshop on Management and Engineering of IT-Supported Business Networks, Administration Networks and Social Networks',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '31.07.2011', 'project_start': '01.04.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126486034?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101533762', 'title': 'Deutsch am Arbeitsplatz', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': '31.12.2013', 'project_start': '01.01.2011',
         'URL': 'https://cris.fau.de/converis/portal/Project/210773338?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101597854',
                                       'title': 'Deutsch-Russische Wirtschaftskooperation im Spannungsfeld von Geschäftsinteressen und unternehmerischer Verantwortung (am Beispiel des Energie- und Finanzsektors)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2022', 'project_start': '01.02.2022',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/270550569?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774,103589606',
                                       'title': 'Dezentralität und zellulare Optimierung – Auswirkungen auf den Netzausbaubedarf',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.06.2016', 'project_start': '10.03.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126509356?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103589606', 'title': 'B09 „Strategische Buchungsentscheidungen im Entry-Exit-System“',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '30.06.2022',
         'project_start': '01.07.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/205660185?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104386248', 'title': 'Die Lebenssteuerlast von Arbeitnehmern', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2018', 'project_start': '01.01.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/126516116?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Die Opferpersönlichkeit als Determinante von Mobbing in Organisationen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2011', 'project_start': '01.06.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229844146?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100248492',
                                       'title': 'Die Regulierung von Berufen und ihr Einfluss auf die Positionierung im Arbeitsmarkt',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2019', 'project_start': '01.01.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126217155?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102330404,100248492',
                                       'title': 'Die Regulierung von Berufen und ihr Einfluss auf die Positionierung im Arbeitsmarkt',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2019', 'project_start': '01.01.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/221696747?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104056282,103342548',
                                       'title': 'Die Wirkungen der Kurzarbeit: Eine Analyse an der Schnittstelle von dynamischer Makro-Arbeitsmarkttheorie und angewandter Ökonometrie',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '01.06.2018', 'project_start': '01.06.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126018073?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '103271008',
                                       'title': 'Die Wirkung von Defaults bei sequentiellen Entscheidungen – Unterschiede zwischen Einzel- und Paarentscheidungen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '01.02.2018', 'project_start': '01.02.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/238570667?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Diffusion von Innovationen. Eine prognostische Studie',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2008',
         'project_start': '01.01.2008',
         'URL': 'https://cris.fau.de/converis/portal/Project/235549895?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'DIGItal COllaboration Platforms as enablers of organizational exchange',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2024', 'project_start': '01.01.2022',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/267037910?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101270338,104628504,100710170,102364998,100228696,101449090,104452594',
         'title': 'Integratives Konzept zur personalisierten Präzisionsmedizin in Prävention, Früh-Erkennung, Therapie und Rückfallvermeidung am Beispiel von Brustkrebs',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '30.09.2024',
         'project_start': '01.10.2020',
         'URL': 'https://cris.fau.de/converis/portal/Project/250673737?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101270338,100710170,102364998,100228696,101449090,104452594',
                                       'title': 'Integratives Konzept zur personalisierten Präzisionsmedizin in Prävention, Früh-Erkennung, Therapie undRückfallvermeidung am Beispiel von Brustkrebs - DigiOnko',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2024', 'project_start': '01.10.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/250674114?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100248492', 'title': 'Digitale Kontrolle in Arbeitsverhältnissen', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Overall project', 'project_end': '30.11.2023',
         'project_start': '01.12.2020',
         'URL': 'https://cris.fau.de/converis/portal/Project/243893068?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103586862', 'title': 'Digitalisierung und ihre Arbeitsmarktwirkungen', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': 'None', 'project_start': '01.07.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/229908870?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103861360', 'title': 'Digitaler Stress', 'funder': 'None', 'project_type': 'Own Funds',
         'project_end': 'None', 'project_start': '01.04.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/126172877?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104385954', 'title': 'Digitization in Controlling and Reporting', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': 'None', 'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/210709292?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101487604',
                                       'title': 'Digitalisierung des zentralen Überlassungsprozesses in der Zeitarbeit',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.07.2020', 'project_start': '29.07.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235835986?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105707876,105628398',
                                       'title': 'Transforming digitally: Digitale Innovationen zur erfolgreichen Gestaltung desorganisationalen Wandels',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.03.2025', 'project_start': '01.04.2022',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/270752781?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100489180', 'title': 'Diversität und Erfolg von Organisationen', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '30.05.2012', 'project_start': '01.11.2010',
         'URL': 'https://cris.fau.de/converis/portal/Project/126084828?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100489180', 'title': 'Diversität und individuelle Karrieren', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '30.11.2017', 'project_start': '01.12.2012',
         'URL': 'https://cris.fau.de/converis/portal/Project/126027537?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101533762', 'title': 'Diversity Management an beruflichen Schulen', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2015',
         'project_start': '01.01.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/210685110?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101487604',
                                       'title': 'Digitale Dienstleistungen als Erfolgsfaktor für die Wertschöpfung der Zukunft',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.03.2021', 'project_start': '01.08.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/228058372?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101320710', 'title': 'E-Bilanzen', 'funder': 'None',
                                       'project_type': 'Third Party Funds Single', 'project_end': '31.03.2016',
                                       'project_start': '01.04.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/125808851?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100088458', 'title': 'Auswirkungen der Mietpreisbremse', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': '14.01.2018', 'project_start': '15.01.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/125983766?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101494856',
                                       'title': 'Eine komparative Analyse der Ursachen und Konsequenzen von Ungleichheit: wie wirken sich frühkindliche Bedingungen auf die Entwicklung von Kindern aus?',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.10.2016', 'project_start': '01.03.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/237122562?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104452594', 'title': 'Einführung der elektronischen Gesundheitskarte', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.08.2017', 'project_start': '01.10.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/126510539?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104373606',
                                       'title': 'Einführung in die unternehmerische Zukunftsforschung - Verbesserungsprojekt',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2021', 'project_start': '01.06.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/261463580?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Einführung von Mitarbeitergesprächen', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': '31.12.2001', 'project_start': '01.01.1999',
         'URL': 'https://cris.fau.de/converis/portal/Project/235286374?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Einführung von Mitarbeitergesprächen in einer Stadtverwaltung - Längsschnittstudie',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2007', 'project_start': '01.01.2006',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235548600?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Einstellungen, Bedenken, Selbstwirksamkeit und Intentionen von Lehramtsstudierenden mit Blick auf Inklusion',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': 'None',
                                       'project_start': '01.04.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/250322029?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '103586862',
                                       'title': 'Einstellungsverhalten, Beschäftigungsperspektiven und Entlohnung in neu gegründeten Betrieben',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': 'None',
                                       'project_start': '01.01.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/211416558?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105707876', 'title': 'Electronic Human Resources Management', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.08.2020', 'project_start': '01.03.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/211149887?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101530724',
                                       'title': 'Module Distance Education System as a new product for reducing the Education Job Mismatch in European Area',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '01.02.2017', 'project_start': '01.02.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/125788571?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774', 'title': 'Economy', 'funder': 'None',
                                       'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.12.2015', 'project_start': '29.07.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126472514?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774,104082252,102089422,100329440,105358016,101433312,103589606',
         'title': 'Energiemarktdesign', 'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
         'project_end': '31.12.2021', 'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/126328188?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774,103589606', 'title': 'Speicher B - Effiziente Wasserstofflogistik',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2021',
         'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/126249941?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246,100501136,101487604',
                                       'title': 'Methodische Konzeptentwicklung für Dienstleistungsplattformen und Schnittstellen, Service Systems Engineering, Kommunikationsdesign',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.06.2020', 'project_start': '01.07.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/125918532?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246',
                                       'title': 'Kommunikationsmanagement und Organisation der Gestaltung von Dienstleistungssystemen im Rahmen pilotierender Einführungen (ExTEND)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.04.2019', 'project_start': '01.10.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126239632?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103291000', 'title': 'Enhancing European teacher education through University schools',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '30.11.2020',
         'project_start': '01.12.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/209613121?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Entering the learning landscape: teacher innovations in classroom and social spaces – a cross-institutional study of trainee teachers by the Universities of Derby and Nuremburg',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': '31.12.2013',
                                       'project_start': '01.01.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210686807?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104452594',
                                       'title': 'Entwicklung eines Befragungsinstruments zur Erfassung von Patientenpräferenzen zum Medikationsmanagement in Deutschland',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2016', 'project_start': '02.02.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/202964987?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Entwicklung eines internationalen Online-Panels', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2006', 'project_start': '01.07.2003',
         'URL': 'https://cris.fau.de/converis/portal/Project/235291497?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104373606',
                                       'title': 'Entwicklung eines Lieferantenauswahl-Prozesses hinsichtlich ausgewählter Nachhaltigkeitskriterien - Sustainable Supplier Selection Process',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2015', 'project_start': '15.01.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/213827010?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774',
                                       'title': 'EOM+: Analyse der kurz- und mittelfristige Auswirkungen von marktbasierten Engpassinstrumenten als regionale und temporäre Ergänzung zum bestehenden Energy-Only-Marktdesign',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '31.10.2022', 'project_start': '01.11.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229944472?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102215842',
                                       'title': 'Erwerbsintegration oder Maßnahmekarriere? Förder- und Erwerbsverlaufmuster von jungen Maßnahmeteilnehmer/innen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2017', 'project_start': '01.01.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/211298853?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101573844', 'title': 'Die Europawahl 2014 in den Medien', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': '31.12.2014', 'project_start': '01.03.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/231679316?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101975056', 'title': 'The Reconfiguration of the EU presence in Latin America',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.08.2022',
         'project_start': '01.09.2020',
         'URL': 'https://cris.fau.de/converis/portal/Project/252964093?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Evaluation eines Auswahlverfahrens hochbegabter Studierender für Studien- und Promotionsstipendien',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2009', 'project_start': '01.01.2009',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235561001?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774', 'title': 'Evaluation eines Smart Grid-Feldexperiments', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2015', 'project_start': '01.01.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/126331906?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Evaluation von Mitarbeitergesprächen (Stadt Fürth)', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2003', 'project_start': '01.01.2001',
         'URL': 'https://cris.fau.de/converis/portal/Project/235287512?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Evaluation von Trainings gegen Informationsüberflutung',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2003',
         'project_start': '01.01.2002',
         'URL': 'https://cris.fau.de/converis/portal/Project/235288576?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774,101582370',
                                       'title': 'Experimentelle Studien zur Auswirkung von kollektiven Lohnverhandlungen auf den Gender Wage Gap',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.12.2015', 'project_start': '01.12.2012',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126316696?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774,105006980',
                                       'title': 'Experimentelle Validierung von Indikatoren des Managerverhaltens in Betriebsbefragungen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2016', 'project_start': '02.04.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126396126?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Expertenstudie zur Reliabilität und Validität von Arbeitszeugnissen',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '30.04.2015',
         'project_start': '01.11.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/235210146?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '242689003,inv,inv', 'title': 'None', 'funder': 'None', 'project_type': 'Own Funds',
         'project_end': 'None', 'project_start': '01.08.2021',
         'URL': 'https://cris.fau.de/converis/portal/Project/263864679?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103256700', 'title': 'Schöller-Fellowship von Frau Dr. Cynthia Sende', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '19.06.2018', 'project_start': '20.06.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/201311736?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105108214', 'title': 'Föderales Informationsmanagement', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': '31.12.2012', 'project_start': '04.12.2012',
         'URL': 'https://cris.fau.de/converis/portal/Project/126487893?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102215842,inv',
                                       'title': 'Kompromissbildung und deren Konsequenzen - Pfadabhängigkeiten zwischen Berufsfindung, Bildungsentscheidungen und Ausbildungsverläufen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2021', 'project_start': '01.10.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126398323?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Flexibilisierte Beschäftigungsverhältnisse und die Beziehung zwischen Mitarbeitern und Unternehmen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2007', 'project_start': '01.01.2006',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235558885?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Integrations- und Kompetenzmanagement im Kontext von Flexibilisierungsstrategien bei KMU',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.04.2013', 'project_start': '01.07.2009',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229843182?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774,103589606', 'title': 'Flexible Verbraucher im Deutschen Strommarkt',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.01.2016',
         'project_start': '01.11.2015',
         'URL': 'https://cris.fau.de/converis/portal/Project/126460008?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105108214',
                                       'title': 'Flexible Informationssystem-Architekturen für hybride Wertschöpfungsnetzwerke',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '31.03.2010', 'project_start': '01.10.2006',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126491104?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246',
                                       'title': 'Mit Flexudy wollen wir Studierenden ein zeiteffizientes und mobiles Lernen ermöglichen. Mit Hilfe künstlicher Intelligenz generiert unsere Technologie aus jeglichen Lernmaterialien in verschiedenen Sprachen automatisiert Fragen-Antwort Karteikarten, Multiple Choice Fragen, Lückentexte und Zusammenfassungen.',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2021', 'project_start': '01.10.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/250326027?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105108214', 'title': 'FOKUS:SE - Das Forschernetzwerk Service Engineering',
         'funder': 'None', 'project_type': 'Own Funds', 'project_end': '01.01.2018', 'project_start': '01.01.2015',
         'URL': 'https://cris.fau.de/converis/portal/Project/126460853?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Förderung sprachlich-kommunikativer Fähigkeiten in der betrieblichen Ausbildung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.12.2014', 'project_start': '01.01.2013',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210685913?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760,103256700',
                                       'title': 'Forschungsvorhaben zur Untersuchung von Mediennutzung und Studienerfolg',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2019', 'project_start': '01.08.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229847147?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '103271008,100502116', 'title': 'Forum V', 'funder': 'None',
                                       'project_type': 'Third Party Funds Single', 'project_end': '31.05.2026',
                                       'project_start': '01.06.2013',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126170173?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105108214', 'title': 'Automatisiertes Content-Providing durch Smarte Steuersysteme',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2019',
         'project_start': '01.01.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/126488907?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246',
                                       'title': 'Führung und Zusammenarbeit im Kontext von Open Innovation bei der AUDI AG',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2013', 'project_start': '01.01.2012',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/125826089?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '248294705', 'title': 'Gamifizierung der Mensch-KI-Interaktion', 'funder': 'None',
         'project_type': 'FAU Funds', 'project_end': '30.06.2022', 'project_start': '01.07.2021',
         'URL': 'https://cris.fau.de/converis/portal/Project/276430350?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246,101487604',
                                       'title': 'Entwicklung von Big-Data-Dienstleistungen und Baukasten-Prototyping mit KMUs (BigDieMo)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.04.2019', 'project_start': '01.10.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126241322?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774,103480140', 'title': 'Zentrum Wasserstoff Bayern', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '30.09.2024', 'project_start': '01.10.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/230023648?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246',
                                       'title': 'Entwicklung von Methoden und Werkzeugen für smarte und nachhaltigkeitsorientierte Produkt-Service-Systeme',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.05.2023', 'project_start': '01.06.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/239536186?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '212658212',
                                       'title': 'Heterogenität makroökonomischer Erwartungen: Welche Rolle spielen individuelle historische Erfahrungen, das örtliche Umfeld und sozioökonomische Faktoren?',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.06.2022', 'project_start': '01.07.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210972719?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101585016',
                                       'title': 'Wie wirkt sich die Geschlechterzusammensetzung auf die Leistung von Teams aus?',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.11.2023', 'project_start': '01.12.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/246311837?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '103203388',
                                       'title': 'Identifikation von Automatisierungspotentialen mit Process Mining (IdAP)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '28.02.2021', 'project_start': '01.03.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/221187754?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104452594', 'title': 'Pharmaökonomie', 'funder': 'None',
                                       'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.09.2017', 'project_start': '01.12.2013',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/125836229?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Integriertes Fach- und Sprachlernen in Beruflicher (Anpassungs-) Qualifizierung - Berufsfeldbezogene Weiterbildung für Lehrende und Bildungsbegleitende',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2017', 'project_start': '01.07.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126165610?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101487604',
                                       'title': 'IIP-Ecosphere - Next Level Ecosphere for Intelligent Industrial Production',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2022', 'project_start': '01.01.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/234097982?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100502116',
                                       'title': 'Implizite Einschränkungen, Anreize und Systemische Risiken: Implikationen der neuen Versicherungsregulierung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2014', 'project_start': '01.01.2013',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126174398?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '242689003,101601774,105655152', 'title': 'None', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': 'None', 'project_start': '01.07.2021',
         'URL': 'https://cris.fau.de/converis/portal/Project/263863924?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105782552',
                                       'title': 'Wertschöpfungsübergreifende Implementierung von Industrie 4.0 bei der Robert Bosch GmbH',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.01.2020', 'project_start': '01.01.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/242032269?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Steigende Informationsflut am Arbeitsplatz - belastungsgünstiger Umgang mit elektronische Medien (E-Mail, Internet)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2002', 'project_start': '01.01.2000',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126304528?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100502116',
                                       'title': 'Investitionen in Infrastruktur und Erneuerbare Energien aus Sicht der Versicherungsindustrie',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.05.2017', 'project_start': '01.06.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126175412?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Innovation Leadership/Business Management Executive Education',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2016',
         'project_start': '01.01.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/126242336?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104421920', 'title': 'TransitionLab 2 - Umsetzungsphase, TP D', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Sub project', 'project_end': '30.11.2022',
         'project_start': '01.12.2021',
         'URL': 'https://cris.fau.de/converis/portal/Project/273174671?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Engagement internationaler Studierender als Element der Regionalentwicklung',
                                       'funder': 'None', 'project_type': 'Fremdprojekt', 'project_end': '31.12.2017',
                                       'project_start': '01.01.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210773039?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762,103205936',
                                       'title': 'InTAK: Interkulturelles Training für Neuzugewanderte – Angemessenes\r\nsprachliches Handeln in beruflichen Kommunikationssituationen',
                                       'funder': 'None', 'project_type': 'FAU Funds', 'project_end': '31.08.2023',
                                       'project_start': '01.10.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/265753095?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101305324,101487310',
                                       'title': 'Anforderungsanalyse, Entwicklung der Motivationsstrategie und des Geschäftsmodells, Test und Evaluierung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.08.2021', 'project_start': '01.09.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/205613594?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103342548', 'title': 'Interdependencies of Labor Market Reforms and the Business Cycle',
         'funder': 'None', 'project_type': 'Own Funds', 'project_end': 'None', 'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/210710543?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101975056',
                                       'title': 'Internationale Entwicklung im 21. Jahrhundert – Wo steht Lateinamerika in der Weltpolitik?',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': 'None', 'project_start': '01.09.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/228195674?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104386248', 'title': 'Internationale Unternehmensbesteuerung und Konzernstrukturen',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '30.06.2012',
         'project_start': '01.06.2010',
         'URL': 'https://cris.fau.de/converis/portal/Project/126056943?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774', 'title': 'Internationales Doktorandenkolleg (IDK) „Evidence Based Economics“',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project', 'project_end': '30.09.2017',
         'project_start': '01.10.2013',
         'URL': 'https://cris.fau.de/converis/portal/Project/126108826?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Internetbasiertes Railpanel', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2000', 'project_start': '01.01.1999',
         'URL': 'https://cris.fau.de/converis/portal/Project/235283787?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101975056', 'title': 'Interregionalism as a foreign policy tool: new concepts and trends',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2018',
         'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/200431535?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100248492', 'title': 'The Invisible Wall: Distinct Firm Networks in West and East Berlin',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '30.06.2019',
         'project_start': '01.07.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/226959649?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246,101487604', 'title': 'JOSEPHS® - Die Service Manufaktur', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': 'None', 'project_start': '01.01.2013',
         'URL': 'https://cris.fau.de/converis/portal/Project/126245547?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101533762', 'title': 'Karriereplanung für Open Source Software-Entwickler',
         'funder': 'None', 'project_type': 'Own Funds', 'project_end': '31.12.2012', 'project_start': '01.01.2011',
         'URL': 'https://cris.fau.de/converis/portal/Project/210774315?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101309146',
                                       'title': 'Kausale Effekte von Lohnsubventionen auf Arbeitsangebot und Arbeitsnachfrage',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2018', 'project_start': '01.10.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/237122857?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Kompetenzentwicklung und Modulare Übergangsbegleitung in den Ausbildungs- und Arbeitsmarkt',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.12.2014', 'project_start': '01.01.2012',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210686144?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104437110', 'title': 'Kreditrating', 'funder': 'None',
                                       'project_type': 'Third Party Funds Single', 'project_end': 'None',
                                       'project_start': '01.01.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/211410229?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Entwicklung einer Online-Recruitingplattform mit kulturbasiertem Jobmatching und Screening',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.04.2018', 'project_start': '01.05.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/202449725?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103271008', 'title': 'Eine Kundenanalyse zu SmartHome-Anwendungen bei Hörgeräten',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '07.02.2017',
         'project_start': '18.10.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/126267517?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105707876',
                                       'title': 'Künstliche Intelligenz, Chatbots und Rekrutierung: Die Sicht der Kandidaten',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2021', 'project_start': '01.11.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/208483806?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103586862', 'title': 'Löhne und Lohndifferenziale', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': 'None', 'project_start': '01.01.2000',
         'URL': 'https://cris.fau.de/converis/portal/Project/229909112?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Längerfristige Effekte von Networking im Karriereverlauf',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2010',
         'project_start': '01.03.2010',
         'URL': 'https://cris.fau.de/converis/portal/Project/229844625?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246,101487604', 'title': 'Leistungszentrum Elektroniksysteme (LZE)', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Overall project', 'project_end': '31.12.2017',
         'project_start': '01.01.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/213936695?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101487604,102333246',
                                       'title': 'Wirtschaftswissenschaftliche Begleitung des Leistungszentrum Elektroniksysteme LZE Phase II',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2020', 'project_start': '03.12.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/233554892?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104056282', 'title': 'Makroökonomische Implikationen der Hartz IV-Arbeitsmarktreform',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '30.04.2022',
         'project_start': '01.05.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/216980616?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100502116',
                                       'title': 'Marktkonsistente Bewertung und Solvenzmessung in der Versicherungsindustrie',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2012', 'project_start': '01.01.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126175243?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Maßnahmen und Empfehlungen für die gesunde Arbeit von morgen (MEgA)',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '30.04.2019',
         'project_start': '01.06.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/126212085?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104991104,101146760',
                                       'title': 'Die Effektivität von Interventionen zur Gesundheitsförderung und -Prävention bei Arbeitslosen – eine Metaanalyse',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2021', 'project_start': '01.09.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/246075156?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246,103652228',
                                       'title': 'Metaprojekt BALANCE: Flexibilität und Stabilität in der Forschungswelt',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '31.12.2013', 'project_start': '01.09.2009',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126476908?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101494856', 'title': 'Midijobs verstehen', 'funder': 'None',
                                       'project_type': 'Third Party Funds Single', 'project_end': '30.09.2021',
                                       'project_start': '01.10.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/216980841?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100088458', 'title': 'gif Policy Paper: Angebotseffekte der Mietpreisbremse',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2018',
         'project_start': '01.07.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/203409396?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774',
                                       'title': 'Zugehörigkeit Frau Prof. Dr. Veronika Grimms zur Kommission aus Energieexperten zur Unterstützung des Monitoring-Prozesses zur Überprüfung des Maßnahmenprogramms der Bundesregierung, mit dem Ziel sich zu einer der energieeffizientesten und umweltschonendsten Volkswirtschaften der Welt zu entwickeln.',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.06.2023', 'project_start': '01.07.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/226016315?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103586862', 'title': 'Monopsonistische Diskriminierung am deutschen Arbeitsmarkt',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '30.11.2015',
         'project_start': '01.01.2009',
         'URL': 'https://cris.fau.de/converis/portal/Project/211299156?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Persönliches Wachstum in Beruf, Ausbildung und Leben: Ein Kurs zur Motivationssteigerung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2022', 'project_start': '01.04.2022',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/272753030?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101532292',
                                       'title': 'Nachhaltige Weiterentwicklung der betrieblichen Informationsverarbeitung',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': 'None',
                                       'project_start': '01.01.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/231732152?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100489180', 'title': 'NEPS', 'funder': 'None', 'project_type': 'Third Party Funds Single',
         'project_end': '31.12.2016', 'project_start': '01.01.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/125975147?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Networking: Eine Längsschnittstudie (Hans-Frisch-Stiftung)',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2004',
         'project_start': '01.01.2001',
         'URL': 'https://cris.fau.de/converis/portal/Project/235288035?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101487604', 'title': 'Neue Arbeitswelten in Pilotflächen', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.03.2020', 'project_start': '01.10.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/201306732?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104385954', 'title': 'Nichtfinanzielle Unternehmenspublizität', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': 'None', 'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/210709481?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104452594', 'title': 'NN / NZ Klinikcheck', 'funder': 'None', 'project_type': 'Own Funds',
         'project_end': 'None', 'project_start': '01.01.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/265666346?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105329106',
                                       'title': 'Objektive und subjektiv erfahrene finanzielle Ungleichheit von Einkommen und Vermögen und deren Konsequenzen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.08.2024', 'project_start': '01.09.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/258843837?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '239219621',
                                       'title': 'Ökonomische Effekte aus einem bürgerfreundlichen Einkommensteuerbescheid',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2021', 'project_start': '01.01.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/250333875?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101487604', 'title': 'Service Innovation 2019 – Open Service Lab', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2019', 'project_start': '01.01.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/232130608?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102917228',
                                       'title': 'Patientenzufriedenheit in den sozialen Medien – Handlungsempfehlung für niedersächsische Kliniken',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '31.08.2021', 'project_start': '01.09.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/242851869?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105108214', 'title': 'Software-Prototypen für die erfahrbare Integration', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Sub project', 'project_end': '30.11.2015',
         'project_start': '01.12.2013',
         'URL': 'https://cris.fau.de/converis/portal/Project/126473866?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Performance Management in Teams', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.08.2017', 'project_start': '01.09.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/203233379?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760,105006980', 'title': 'Personalpolitik in genossenschaftlichen Unternehmen',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '30.04.2014',
         'project_start': '01.04.2013',
         'URL': 'https://cris.fau.de/converis/portal/Project/229845061?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101305324', 'title': 'Prescriptive healthcare analytics', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2019', 'project_start': '01.01.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/217300806?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760,103861360',
                                       'title': 'Projektseminar zur praxisorientierten Vermittlung von Moderations- und Evaluationskompetenzen anhand eines Trainings zur Bewältigung von digitalem Stress',
                                       'funder': 'None', 'project_type': 'FAU Funds', 'project_end': '30.09.2018',
                                       'project_start': '01.04.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229846209?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105108214',
                                       'title': 'Deutsch-Russisches Innovationsforum - Promoting business process management excellence in Russia',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '30.04.2012', 'project_start': '01.11.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126342891?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Psychologische Aspekte der Leiharbeit', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2002', 'project_start': '01.01.2000',
         'URL': 'https://cris.fau.de/converis/portal/Project/235286076?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Psychologisches Kapital als Determinante von Eskalierendem Commitment in Organisationen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.06.2013', 'project_start': '01.03.2013',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229843930?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101320710',
                                       'title': 'Public financial disclosure and labor costs: Empirical evidence from a quasi-experiment',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '01.07.2019', 'project_start': '01.01.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/213828632?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105108214', 'title': 'PUSH Münsterland: Produkt-Servicekombinationen entwickeln und nutzen',
         'funder': 'None', 'project_type': 'Fremdprojekt', 'project_end': '14.08.2015', 'project_start': '15.08.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/126251462?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Anschlüsse eröffnen - Entwicklungen ermöglichen.\r\nQualifizierungsbausteine inklusiv in einer dualisierten Ausbildungsvorbereitung',
                                       'funder': 'None', 'project_type': 'Fremdprojekt', 'project_end': '30.06.2018',
                                       'project_start': '01.01.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210687479?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104452594',
                                       'title': 'Qualitätstransparenz in der Hüftendoprothetik durch Patient Reported Outcomes',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.04.2022', 'project_start': '01.05.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/239358876?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102917228',
                                       'title': 'Qualitätstransparenz in der Hüftendoprothetik durch Patient Reported Outcomes',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '28.02.2022', 'project_start': '01.01.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/208670663?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Rechtfertigungsdruck und eskalierendes Commitment', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2005', 'project_start': '01.01.2003',
         'URL': 'https://cris.fau.de/converis/portal/Project/235290009?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Reziprozitätsprozesse im Kontext von Peer-Feedback', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.10.2018', 'project_start': '01.01.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/204086652?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101975056',
                                       'title': 'Relations between the European Union and Latin America: Future scenarios in a changing world',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': 'None', 'project_start': '01.07.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/253525846?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774,100248492', 'title': 'Die Entstehung von Reputation in Wirtschaftsbeziehungen',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '20.09.2012',
         'project_start': '01.04.2010',
         'URL': 'https://cris.fau.de/converis/portal/Project/126395450?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Forschung zu den psychischen Auswirkungen von Arbeitslosigkeit',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.03.2017',
         'project_start': '01.10.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/235000494?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Resilire - Altersübergreifendes Resilienz-Management',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project', 'project_end': '31.12.2017',
         'project_start': '01.11.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/126176257?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760,101148916', 'title': 'Resilire - Altersübergreifendes Resilienz-Management',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project', 'project_end': '31.10.2017',
         'project_start': '01.11.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/126433813?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246',
                                       'title': 'Maschinenfehlerdiagnose und Entwicklung von Rollen, Views, Schnittstellen und Anwender-Mockup',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.12.2016', 'project_start': '01.01.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/211013315?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105108214',
                                       'title': 'Propelling Business Process Management by Research and Innovation Staff Exchange',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.04.2019', 'project_start': '01.05.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126486372?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101320710',
                                       'title': 'Social Media-Kanäle als Informations\xadintermediäre (Schöller Junior Fellow 2017 Tim Herberger)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': 'None', 'project_start': '01.01.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/213829478?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Selbstkonzept und Selbstbeurteilung beruflicher Leistung',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2004',
         'project_start': '01.01.2003',
         'URL': 'https://cris.fau.de/converis/portal/Project/235290786?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101487604', 'title': 'Service Innovation (Teilvereinbarung 2017)', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2017', 'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/226980444?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Service Innovation – Teilvereinbarung 2018', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2018', 'project_start': '01.01.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/226532119?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Service Innovation Teilprojekt Vereinbarung 2012', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2012', 'project_start': '01.01.2012',
         'URL': 'https://cris.fau.de/converis/portal/Project/125854481?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Service Innovation Teilprojekt Vereinbarung 2013', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2013', 'project_start': '01.01.2013',
         'URL': 'https://cris.fau.de/converis/portal/Project/125803950?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Service innovation - Teilvereinbarung 2014', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2014', 'project_start': '01.01.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/126012158?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Service innovation - Teilvereinbarung 2015', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2015', 'project_start': '01.01.2015',
         'URL': 'https://cris.fau.de/converis/portal/Project/125804795?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102333246', 'title': 'Service innovation - Teilvereinbarung 2016', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.12.2016', 'project_start': '01.01.2016',
         'URL': 'https://cris.fau.de/converis/portal/Project/126214451?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774,105358016,101433312,103589606',
                                       'title': 'Wohlfahrtsoptimale Nominierungen in Gasnetzen und zugehörige Gleichgewichte',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.06.2018', 'project_start': '01.10.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126509525?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104373606,212578052',
                                       'title': 'Siemens Competence Center Foresight für die industrielle Automatisierung und Digitalisierung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': 'None', 'project_start': '01.06.2022',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/274757098?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101597854',
                                       'title': 'Sino-German Perspectives on Corporate Social Responsibility and Sustainable Development',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2022', 'project_start': '01.01.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/233205494?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105108214',
                                       'title': 'Bilaterale Kooperationsanbahnung Brasilien - Evaluating Standards for Interorganizational Process Integration in Brazilian-German Value Networks',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': '31.05.2010',
                                       'project_start': '01.05.2010',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126488062?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '228682808,101585016',
                                       'title': 'Fähigkeiten, Erwartungen und Persönlichkeit als Determinanten des fächerspezifischen Studienerfolges',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2023', 'project_start': '01.10.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/246312300?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Skype as instrument to promote intercultural competences - a cross-cultural study between students of Germany and England',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': '31.12.2013',
                                       'project_start': '01.01.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210775078?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101487604,102333246',
                                       'title': 'Methodik und Konzeption für ein Fakten-basiertes Service Engineering (SmartDiF)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.08.2019', 'project_start': '01.09.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126240646?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246',
                                       'title': 'Harmonisierung der Entwicklung von komplexen Produkt-Smart-Service-Systemen bei KMU',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '31.05.2023', 'project_start': '01.06.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/239451749?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105108214',
                                       'title': 'smartmarket²: Entwicklung mobiler Applikationen für standortbezogene Dienstleistungen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '29.02.2020', 'project_start': '01.03.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126489583?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '103203388',
                                       'title': 'Analyse von Positonsdaten zur Ermittlung von Durchlaufzeiten in der Fertigung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.01.2021', 'project_start': '01.04.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/237637268?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '235233833',
                                       'title': 'Ein Brückenschlag: Reinforcement Learning auf Molekül- und Prozessgraphen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '28.02.2022', 'project_start': '01.03.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/248230232?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '219128459', 'title': 'Multidimensionales Conformance Checking für Prozesse',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.01.2023',
         'project_start': '01.02.2021',
         'URL': 'https://cris.fau.de/converis/portal/Project/247978698?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '203599239', 'title': 'Deep Learning im Kontext von Predictive Maintenance',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2021',
         'project_start': '01.01.2020',
         'URL': 'https://cris.fau.de/converis/portal/Project/231273464?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '228208413', 'title': 'Digitales Nudging und persuasives Design im Software-Kontext',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.01.2023',
         'project_start': '01.02.2021',
         'URL': 'https://cris.fau.de/converis/portal/Project/248303281?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '105358800',
                                       'title': 'Interorganisationale Interdependenzen in Industrial-Internet-of-Things Geschäftsmodellen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.12.2020', 'project_start': '01.01.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/221261171?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '227730973', 'title': 'Nonparametric Bayesian Learning in Distributed Systems',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.01.2023',
         'project_start': '01.02.2021',
         'URL': 'https://cris.fau.de/converis/portal/Project/248241839?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774,103589606', 'title': 'Implementierung im Marktumfeld', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2015',
         'project_start': '01.06.2012',
         'URL': 'https://cris.fau.de/converis/portal/Project/126509694?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Soziale Beziehungen zwischen Lernenden an beruflichen Schulen fördern: Abbau von Vorurteilen, Umgang mit Diskriminierung und Toleranzerziehung',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.12.2016', 'project_start': '01.01.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210571289?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Soziale und ökonomische Kosten der Erwerbslosigkeit',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2020',
         'project_start': '01.01.1999',
         'URL': 'https://cris.fau.de/converis/portal/Project/235278882?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104373606,204206709', 'title': 'Spedicam & Logistik GmbH goes digital', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.05.2021', 'project_start': '01.06.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/239353667?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Evidenzbasiertes Motivationsmanagement zur Leistungsoptimierung im Profisport',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.09.2013', 'project_start': '01.10.2012',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/229841948?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101494856',
                                       'title': 'Erwerbstätigkeit von Müttern und kindliche Entwicklung: Eine Analyse der Determinanten im gesellschaftlichen Wandel',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.09.2017', 'project_start': '01.08.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/125846538?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '102330404', 'title': 'Ausländische Bildungszertifikate auf dem deutschen Arbeitsmarkt',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.07.2017',
         'project_start': '01.08.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/125966021?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100248492', 'title': 'Ausländische Bildungszertifikate auf dem deutschen Arbeitsmarkt',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': 'None',
         'project_start': '01.08.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/126188594?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103222008', 'title': 'Löhne, Heterogenitäten und Arbeitsmarktdynamik', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2020',
         'project_start': '01.08.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/125914307?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101533762', 'title': '„Sprachförderung“ an der FOS Regensburg', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': '31.12.2013', 'project_start': '01.01.2012',
         'URL': 'https://cris.fau.de/converis/portal/Project/210774885?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101533762', 'title': 'Sprachförderung im fachlichen Unterricht an berufsbildenden Schulen',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2015',
         'project_start': '01.01.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/210684911?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101533762',
                                       'title': 'Sprachsensibilisierung in der beruflichen Qualifizierung – Entwicklung und Erprobung von Qualifizierungsmodulen für Lehrkräfte in der beruflichen Weiterbildung für Migrantinnen und Migranten',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.12.2014', 'project_start': '01.01.2013',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/210685301?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '105782552', 'title': 'Sustainable Smart Industry', 'funder': 'None',
         'project_type': 'FAU Funds', 'project_end': '31.12.2018', 'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/126495836?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101320710', 'title': 'Smart Teaching in Accounting - Meeting Place Online',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '29.12.2022',
         'project_start': '30.12.2020',
         'URL': 'https://cris.fau.de/converis/portal/Project/261258597?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Stark in Alltag und Arbeit', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.08.2019', 'project_start': '01.09.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/203495671?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246,101487604',
                                       'title': '7 start-up summer schools in Europe on Information and Communications Technologies for young aspiring entrepreneurs',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2016', 'project_start': '01.01.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/213933123?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104386248,101309930', 'title': 'Steuerliche Anreize für Unternehmensansiedlungen',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2019',
         'project_start': '01.01.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/208484053?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100489180',
                                       'title': 'Stigma-Bewusstsein von Arbeitslosen und Vorurteile gegenüber Arbeitslosen',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.06.2017', 'project_start': '01.07.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126107981?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'Stimmung und Kategorisierung: Zum Einfluß emotionaler Zustände auf berufseignungsdiagnostische  Urteilsprozesse',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.1999', 'project_start': '01.01.1997',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235266965?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101320710',
                                       'title': 'Cooperation and Innovation for Good Practices – „International Learning Platform for Accountancy (ILPA)“',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.08.2017', 'project_start': '01.09.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/211009466?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104373606,102369016', 'title': 'Studie zur Digitalisierung im Mittelstand',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2017',
         'project_start': '01.07.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/204126968?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'SummerSchool "Electronic Monitoring" (10.-12.9.2018)',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.10.2018',
         'project_start': '01.01.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/236579489?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760,100489180',
                                       'title': 'Summer School: The Interplay of Work, Health and Organizational Success',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2014', 'project_start': '01.04.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/235002008?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100502116',
                                       'title': 'Sustainable Business Models in Energy Markets: Perspectives for the Implementation of Smart Energy Systems',
                                       'funder': 'None', 'project_type': 'FAU Funds', 'project_end': '31.12.2016',
                                       'project_start': '01.01.2014',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126391394?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101567376,101489466,101601774',
                                       'title': 'Koordinierte Kleinspeicher im Verteilnetz der N-ERGIE Aktiengesellschaft - Storage With Amply Redundant Megawatt (SWARM)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2017', 'project_start': '01.01.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126212930?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Symposium „Individuals in Temporary Agency Jobs“.', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.05.2007', 'project_start': '01.01.2007',
         'URL': 'https://cris.fau.de/converis/portal/Project/236493456?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774',
                                       'title': 'Taxation, Social Norms, and Compliance: Lessons for Institution Design',
                                       'funder': 'None', 'project_type': 'FAU Funds', 'project_end': '31.12.2014',
                                       'project_start': '01.01.2012',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/125938305?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100710170,101601774,104848514',
                                       'title': 'Teamwork Performance: Effects of Tracking Based Feedback Mechanisms on Performance and Health Biomarkers',
                                       'funder': 'None', 'project_type': 'Own Funds', 'project_end': 'None',
                                       'project_start': '01.03.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126151583?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101975056', 'title': 'The Bavarian Scientific Expedition to Brazil (1817-1820)',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': 'None',
         'project_start': '01.09.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/239284640?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101320710',
                                       'title': 'The Effects of the Financial Crisis on Cooperative Banks in Europe – A Critical Comparison',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '30.06.2017', 'project_start': '01.01.2016',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/213828851?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '100248492,102330404',
                                       'title': 'Die Arbeitsmarktintegration qualifizierter MigrantInnen im internationalen Vergleich',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.09.2020', 'project_start': '01.10.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/202161989?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Die psychologische Bedeutung von Arbeit', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.08.2018', 'project_start': '01.09.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/202228384?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101146760',
                                       'title': 'The R and RStudio Environment. Handling, Visualisation und Communication of Data in Science',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '28.02.2021', 'project_start': '01.03.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/234197063?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774', 'title': 'Die Rolle von Sozialer Identität für das Lernen in Netzwerken',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '09.10.2021',
         'project_start': '01.10.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/228016913?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101305324',
                                       'title': 'Entwicklung von Maßnahmen zur Schaffung von Transparenz und Vertrauen in DataAnalytics-Projekten',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '29.02.2020', 'project_start': '01.03.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/226959158?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101601774,101433312',
                                       'title': 'Mehrstufige gemischt-ganzzahlig nichtlineare Optimierung für Gasmärkte (B08) (2018 - 2022)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.06.2022', 'project_start': '01.07.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/204141447?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101601774', 'title': 'Trust in Character, Capability and Institutions', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.05.2015', 'project_start': '01.06.2012',
         'URL': 'https://cris.fau.de/converis/portal/Project/126408801?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104437110', 'title': 'Twitter-Daten', 'funder': 'None',
                                       'project_type': 'Third Party Funds Single', 'project_end': 'None',
                                       'project_start': '01.01.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/211410028?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Umsetzungskonzept: Training gegen Informationsüberflutung',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2003',
         'project_start': '01.01.2003',
         'URL': 'https://cris.fau.de/converis/portal/Project/235289231?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '103342548', 'title': 'Understanding Job Creation: The Role of Firm Age and Job Duration',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2017',
         'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/202306978?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104386248', 'title': 'Steuerhinterziehung und Steuerbetrug bei der Mehrwertsteuer',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '30.09.2018',
         'project_start': '01.01.2017',
         'URL': 'https://cris.fau.de/converis/portal/Project/125974302?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101585016',
                                       'title': 'Unternehmen, Märkte, Volkswirtschaften: Von der Massenveranstaltung zum arbeitsgruppenorientierten Forum.\r\nEin Pilot für die Transformation der Lehre in den WiSo‐Bachelorstudiengängen',
                                       'funder': 'None', 'project_type': 'FAU Funds', 'project_end': '30.09.2020',
                                       'project_start': '01.10.2019',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/246311579?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102369016',
                                       'title': 'Vereinbarkeit strategischer Entscheidungen im Rahmen der digitalen Transformation mit moralisch-ethischen Werten der Mitarbeiter',
                                       'funder': 'None', 'project_type': 'FAU Funds', 'project_end': 'None',
                                       'project_start': '01.07.2021',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/275131357?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104386248',
                                       'title': 'Einrichtung eines wissenschafttlichen Dienstes an der FAU im Rahmen der erneuten Übernahme des Vorsitzes des Unabhängigen Beirats beim Stabilitätsrat durch Herrn Prof. Dr. Büttner',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.08.2022', 'project_start': '01.09.2020',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/264525710?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246,101487604',
                                       'title': 'Open Innovation für IT-Sicherheit Kritischer Infrastrukturen (VeSiKi)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '30.06.2018', 'project_start': '01.01.2015',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126239801?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100502116,103271008', 'title': 'verschiedene Dienstleistungen', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.05.2026', 'project_start': '01.01.2012',
         'URL': 'https://cris.fau.de/converis/portal/Project/125827779?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101146760', 'title': 'Verwaltungsbenchmarking süddeutscher Universitäten', 'funder': 'None',
         'project_type': 'Own Funds', 'project_end': '31.12.2007', 'project_start': '01.01.2006',
         'URL': 'https://cris.fau.de/converis/portal/Project/235546753?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104452594',
                                       'title': 'Entwicklung eines Weiterbildungsangebotes im Bereich der altersgerechten Assistenzsysteme (AAL) für die Europäische Metropolregion Nürnberg (EMN)',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.12.2014', 'project_start': '01.07.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/239359745?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101487604', 'title': 'Weiterbildungszentrum Digital Transformation', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '31.03.2021', 'project_start': '01.01.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/238566523?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '101530724', 'title': 'Weichenstellung', 'funder': 'None',
                                       'project_type': 'Third Party Funds Group - Sub project',
                                       'project_end': '31.07.2022', 'project_start': '01.04.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/208609420?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104452594', 'title': 'Weiterbildungsprogramm Telemedizin', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '30.09.2016', 'project_start': '01.08.2014',
         'URL': 'https://cris.fau.de/converis/portal/Project/213950547?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '100088458', 'title': 'Wer profitiert vom Wohnungsneubau?', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '30.06.2021', 'project_start': '01.07.2019',
         'URL': 'https://cris.fau.de/converis/portal/Project/204192458?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246,103652228',
                                       'title': 'WiIPOD Wertschätzungsnetzwerke als integrierte Innovationsinstrumente der Personal- und Organisationsentwicklung im Demografischen Wandel',
                                       'funder': 'None', 'project_type': 'Third Party Funds Group - Overall project',
                                       'project_end': '30.04.2015', 'project_start': '01.08.2011',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/126283572?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101975056', 'title': 'Wirtschaft, Politik und Gesellschaft in Lateinamerika',
         'funder': 'None', 'project_type': 'Third Party Funds Group - Sub project', 'project_end': 'None',
         'project_start': '01.09.2018',
         'URL': 'https://cris.fau.de/converis/portal/Project/203496385?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '102333246',
                                       'title': 'Einführung und Verankerung des Karrierewegs der Tenure-Track-Professur, die vollständig den Anforderungen der Verwaltungsvereinbarung zwischen Bund und Ländern gemäß Artikel 91b Absatz 1 des Grundgesetztes über ein Programm zur Förderung des wissenschaftlichen Nachwuchses vom 16.06.2016 entspricht',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.10.2027', 'project_start': '01.12.2017',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/200466045?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101533762', 'title': 'Wissenschaftliche Begleitung des Projektes KASper', 'funder': 'None',
         'project_type': 'Third Party Funds Group - Sub project', 'project_end': '31.12.2015',
         'project_start': '01.01.2015',
         'URL': 'https://cris.fau.de/converis/portal/Project/210684606?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append({'project_leader': '104386248',
                                       'title': 'Wissenschafttlicher Dienst des Unabhängigen Beirats des Stabilitätsrats',
                                       'funder': 'None', 'project_type': 'Third Party Funds Single',
                                       'project_end': '31.08.2020', 'project_start': '01.09.2018',
                                       'URL': 'https://cris.fau.de/converis/portal/Project/226647026?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '101320710', 'title': "Zielführende Betriebsprüfungen durch Nutzung von 'Alternative Data'",
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': '31.12.2020',
         'project_start': '01.01.2020',
         'URL': 'https://cris.fau.de/converis/portal/Project/230024656?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '104386248', 'title': 'Zukunft der EU-Finanzen', 'funder': 'None',
         'project_type': 'Third Party Funds Single', 'project_end': '20.12.2015', 'project_start': '22.04.2015',
         'URL': 'https://cris.fau.de/converis/portal/Project/126337145?auxfun=&lang=de_DE'})
    filtered_data_all_wiso_pro.append(
        {'project_leader': '231610692,212578052,105005510', 'title': 'Zukunftsforschung im Supply Chain Management',
         'funder': 'None', 'project_type': 'Third Party Funds Single', 'project_end': 'None',
         'project_start': '04.05.2022',
         'URL': 'https://cris.fau.de/converis/portal/Project/274752864?auxfun=&lang=de_DE'})
    return render_template("home/tables2.html",
                           research_projects=filtered_data_all_wiso_pro,
                           publications=filtered_data_all_wiso_publs)




# @blueprint.route('/<template>')
# @login_required
# def route_template(template):
#
#     try:
#
#         if not template.endswith('.html'):
#             template += '.html'
#
#         # Detect the current page
#         segment = get_segment(request)
#
#         # Serve the file (if exists) from app/templates/home/FILE.html
#         return render_template("home/" + template)
#
#     except TemplateNotFound:
#         return render_template('home/page-404.html'), 404
#
#     except:
#         return render_template('home/page-500.html'), 500


# Helper - Extract current page name from request
def get_segment(request):
    try:

        segment = request.path.split('/')[-1]

        if segment == '':
            segment = 'index'

        return segment

    except:
        return None
