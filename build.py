#!/usr/bin/env python3
"""Génère les pages du site dans les six langues du jeu. python3 build.py, puis git push : GitHub Pages sert le résultat.
privacy.html / support.html / index.html sont la version française ; les autres langues ont un suffixe (-en, -es, -de, -it, -nl).
Les pages sont écrites dans le sous-dossier SITE_DIR, pas à la racine du dépôt : voir le commentaire de SITE_DIR."""
import html
from pathlib import Path

LANGS = ["fr", "en", "es", "de", "it", "nl"]
DATE = "2026-09-12"
MAIL = "ben@enami.fr"
BASE = "https://benjaminths.github.io/padel-idle-site/"

# Ce dépôt est le site racine du développeur (nommé <pseudo>.github.io), donc GitHub Pages
# sert sa racine sur https://benjaminths.github.io/. La racine est réservée à app-ads.txt,
# qu'AdMob ne lit qu'à cet endroit, et à la page d'accueil Enami. Les pages du jeu vivent
# donc dans ce sous-dossier, dont le nom reproduit l'ancienne URL du site pour que les
# liens déjà publiés (App Store, moteurs de recherche) continuent de répondre : BASE.
SITE_DIR = "padel-idle-site"


def page_name(kind, lang):
    return f"{kind}.html" if lang == "fr" else f"{kind}-{lang}.html"


T = {
"fr": dict(
  lang_bar_title="Langue", home="Accueil", support="Assistance", privacy="Confidentialité",
  app_name="Padel Idle : Club Manager", publisher="Un jeu Enami pour iPhone et iPad.",
  tagline="Construis ton club de padel : livre les raquettes, accueille les joueurs, lance les matchs, ramasse les balles, encaisse, agrandis. Six terrains, une boutique, des vestiaires et un tournoi le week-end.",
  links="Liens", link_support="Assistance et questions fréquentes", link_privacy="Politique de confidentialité",
  p_title="Politique de confidentialité",
  p_meta=f"Dernière mise à jour : 12 septembre 2026 · S'applique à l'application <strong>Padel Idle : Club Manager</strong> (iOS, Android) éditée par Enami.",
  p_intro="Padel Idle est un jeu gratuit financé par la publicité. Cette page explique quelles données sont traitées quand vous y jouez, par qui, pourquoi, et quels sont vos choix. Nous l'avons écrite pour être lue, pas pour être longue.",
  p1_h="1. Ce que le jeu ne collecte pas",
  p1="Padel Idle ne demande ni compte, ni adresse e-mail, ni nom, ni numéro de téléphone. Vous n'y saisissez aucune donnée personnelle. Votre partie (progression, achats en jeu, argent virtuel) est enregistrée <strong>uniquement sur votre appareil</strong> ; nous n'y avons pas accès et elle disparaît si vous désinstallez le jeu.",
  p2_h="2. Ce qui est traité, et par qui",
  p2="Deux services tiers interviennent. Ils reçoivent des données techniques directement depuis votre appareil ; Enami ne les reçoit pas et ne les stocke pas.",
  th=["Service", "Rôle", "Données", "Condition"],
  row_ads=["Afficher les publicités (bannière, vidéos récompensées), les mesurer, prévenir la fraude", "Identifiant publicitaire de l'appareil (IDFA sur iOS, si vous l'autorisez ; GAID sur Android), adresse IP, modèle et système de l'appareil, langue, pays approximatif, interactions avec les publicités", "Toujours pour des publicités non personnalisées ; personnalisées seulement avec votre accord"],
  row_ga=["Mesurer comment le jeu est utilisé pour l'améliorer (où les joueurs s'arrêtent, quelles améliorations sont achetées)", "Identifiant anonyme de l'appareil, modèle et système, sessions, événements de progression et achats <em>en jeu</em> (monnaie virtuelle)", "Seulement avec votre accord"],
  policies="Politiques de ces services",
  p3_h="3. Votre accord",
  p3="Au premier lancement, le jeu vous pose la question sur un écran « Vos données », avec deux boutons de même poids : accepter ou refuser.",
  p3_accept="<strong>Accepter</strong> : les publicités peuvent être adaptées à vos centres d'intérêt, et la mesure d'audience est activée.",
  p3_refuse="<strong>Refuser</strong> : vous voyez des publicités non personnalisées, et rien n'est mesuré. Le jeu est strictement identique.",
  p3_ios="Sur iOS, le système vous demande en plus l'autorisation de suivi (App Tracking Transparency).",
  p4_h="4. Base légale et durée",
  p4="Les publicités non personnalisées et la sécurité reposent sur notre intérêt légitime à financer un jeu gratuit. La personnalisation des publicités et la mesure d'audience reposent sur votre consentement. Les données restent sur votre appareil tant que le jeu est installé ; les données reçues par les services tiers sont conservées selon leurs propres politiques, en général quelques mois.",
  p5_h="5. Vos droits",
  p5=f"Vous pouvez demander l'accès, la rectification, l'effacement ou la limitation des données vous concernant, et vous opposer à leur traitement. Comme Enami ne détient aucune donnée personnelle sur vous, la plupart de ces demandes s'exercent auprès des services cités ci-dessus, via les liens de la section 2. Pour toute question, écrivez-nous : <a href=\"mailto:{MAIL}\">{MAIL}</a>. Vous pouvez aussi saisir la CNIL (France) ou l'autorité de votre pays.",
  p5_ca="Résidents de Californie : nous ne vendons pas de données personnelles. Le jeu transmet à la régie publicitaire un signal « ne pas vendre » lorsque vous refusez.",
  p6_h="6. Enfants",
  p6="Padel Idle ne s'adresse pas aux enfants de moins de 13 ans et ne collecte sciemment aucune donnée les concernant. Le jeu est déclaré comme n'étant pas destiné aux enfants auprès de la régie publicitaire.",
  p7_h="7. Modifications",
  p7="Si cette politique change, la date en haut de page est mise à jour et, pour un changement important, le jeu vous le signale au lancement.",
  s_title="Assistance", s_meta="Padel Idle : Club Manager · Enami",
  s_intro=f"Une question, un bug, une idée ? Écrivez-nous à <a href=\"mailto:{MAIL}\">{MAIL}</a> en précisant votre appareil et la version du jeu (visible dans l'App Store). Nous répondons en français et en anglais.",
  faq_h="Questions fréquentes",
  faq=[
    ("Ma partie a disparu.", "La partie est enregistrée sur l'appareil, pas sur un compte : désinstaller le jeu l'efface. Elle reprend exactement où vous l'avez laissée tant que le jeu reste installé, même après avoir fermé l'application."),
    ("Le bouton « LIBRE » dit « Pub indisponible ».", "Aucune vidéo n'était disponible à cet instant chez la régie publicitaire. Réessayez un peu plus tard ; sans vidéo, il n'y a pas de récompense, c'est voulu."),
    ("Je ne vois pas de bannière publicitaire.", "Elle n'apparaît qu'après le tutoriel de la première partie, et seulement quand la régie a une publicité à afficher."),
    ("Le jeu est-il gratuit ?", "Oui, entièrement, financé par la publicité. Il n'y a pas d'achat intégré dans cette version."),
    ("Les clients partent fâchés.", "Ils attendent des raquettes au comptoir : gardez la pile garnie, ou embauchez le coursier pour qu'il s'en charge. Les terrains sales ne se libèrent qu'une fois les balles ramassées."),
  ]),
"en": dict(
  lang_bar_title="Language", home="Home", support="Support", privacy="Privacy",
  app_name="Padel Idle: Club Manager", publisher="An Enami game for iPhone and iPad.",
  tagline="Build your padel club: deliver rackets, welcome players, start matches, collect balls, cash in, expand. Six courts, a pro shop, locker rooms and a weekend tournament.",
  links="Links", link_support="Support and frequently asked questions", link_privacy="Privacy policy",
  p_title="Privacy Policy",
  p_meta="Last updated: September 12, 2026 · Applies to the app <strong>Padel Idle: Club Manager</strong> (iOS, Android) published by Enami.",
  p_intro="Padel Idle is a free game funded by ads. This page explains what data is processed when you play, by whom, why, and what your choices are. It is written to be read, not to be long.",
  p1_h="1. What the game does not collect",
  p1="Padel Idle asks for no account, e-mail address, name or phone number. You never enter personal data. Your game (progress, in-game purchases, virtual money) is saved <strong>on your device only</strong>; we have no access to it and it is gone when you uninstall the game.",
  p2_h="2. What is processed, and by whom",
  p2="Two third-party services are involved. They receive technical data directly from your device; Enami neither receives nor stores it.",
  th=["Service", "Purpose", "Data", "Condition"],
  row_ads=["Showing ads (banner, rewarded videos), measuring them, preventing fraud", "Device advertising identifier (IDFA on iOS, if you allow it; GAID on Android), IP address, device model and OS, language, approximate country, interactions with ads", "Always, for non-personalised ads; personalised ads only with your consent"],
  row_ga=["Measuring how the game is used in order to improve it (where players stop, which upgrades are bought)", "Anonymous device identifier, device model and OS, sessions, progression events and <em>in-game</em> purchases (virtual currency)", "Only with your consent"],
  policies="Their policies",
  p3_h="3. Your consent",
  p3="On first launch the game asks you on a “Your data” screen, with two equal buttons: accept or refuse.",
  p3_accept="<strong>Accept</strong>: ads may be tailored to your interests, and audience measurement is enabled.",
  p3_refuse="<strong>Refuse</strong>: you see non-personalised ads, and nothing is measured. The game is exactly the same.",
  p3_ios="On iOS the system additionally asks for tracking permission (App Tracking Transparency).",
  p4_h="4. Legal basis and retention",
  p4="Non-personalised ads and security rely on our legitimate interest in funding a free game. Ad personalisation and audience measurement rely on your consent. Data stays on your device as long as the game is installed; data received by third-party services is kept according to their own policies, typically a few months.",
  p5_h="5. Your rights",
  p5=f"You may request access to, rectification, erasure or restriction of data about you, and object to its processing. Since Enami holds no personal data about you, most of these requests are exercised with the services listed above, through the links in section 2. For any question, write to us: <a href=\"mailto:{MAIL}\">{MAIL}</a>. You may also lodge a complaint with your local data protection authority (CNIL in France).",
  p5_ca="California residents: we do not sell personal data. The game sends a “do not sell” signal to the ad network when you refuse.",
  p6_h="6. Children",
  p6="Padel Idle is not directed at children under 13 and does not knowingly collect any data about them. The game is declared as not child-directed to the ad network.",
  p7_h="7. Changes",
  p7="If this policy changes, the date at the top is updated and, for a significant change, the game tells you at launch.",
  s_title="Support", s_meta="Padel Idle: Club Manager · Enami",
  s_intro=f"A question, a bug, an idea? Write to <a href=\"mailto:{MAIL}\">{MAIL}</a> with your device and the game version (shown in the App Store). We answer in English and in French.",
  faq_h="Frequently asked questions",
  faq=[
    ("My game is gone.", "The game is saved on the device, not on an account: uninstalling erases it. It resumes exactly where you left it as long as the game stays installed, even after closing the app."),
    ("The “FREE” button says “Ad unavailable”.", "No video was available from the ad network at that moment. Try again a little later; without a video there is no reward, by design."),
    ("I don't see the ad banner.", "It only appears after the first game's tutorial, and only when the network has an ad to show."),
    ("Is the game free?", "Yes, entirely, funded by ads. There are no in-app purchases in this version."),
    ("Customers leave angry.", "They are waiting for rackets at the front desk: keep the pile stocked, or hire the stock runner to do it. Dirty courts only free up once the balls are collected."),
  ]),
"es": dict(
  lang_bar_title="Idioma", home="Inicio", support="Asistencia", privacy="Privacidad",
  app_name="Padel Idle: Club Manager", publisher="Un juego de Enami para iPhone y iPad.",
  tagline="Construye tu club de pádel: recibe las palas, acoge a los jugadores, arranca los partidos, recoge las pelotas, cobra, amplía. Seis pistas, una tienda, vestuarios y un torneo el fin de semana.",
  links="Enlaces", link_support="Asistencia y preguntas frecuentes", link_privacy="Política de privacidad",
  p_title="Política de privacidad",
  p_meta="Última actualización: 12 de septiembre de 2026 · Se aplica a la aplicación <strong>Padel Idle: Club Manager</strong> (iOS, Android) publicada por Enami.",
  p_intro="Padel Idle es un juego gratuito financiado por la publicidad. Esta página explica qué datos se tratan cuando juegas, quién lo hace, por qué y qué opciones tienes. La hemos escrito para que se lea, no para que sea larga.",
  p1_h="1. Lo que el juego no recoge",
  p1="Padel Idle no pide cuenta, correo electrónico, nombre ni número de teléfono. No introduces ningún dato personal. Tu partida (progreso, compras en el juego, dinero virtual) se guarda <strong>únicamente en tu dispositivo</strong>; no tenemos acceso a ella y desaparece si desinstalas el juego.",
  p2_h="2. Qué se trata, y quién lo hace",
  p2="Intervienen dos servicios de terceros. Reciben datos técnicos directamente desde tu dispositivo; Enami no los recibe ni los almacena.",
  th=["Servicio", "Función", "Datos", "Condición"],
  row_ads=["Mostrar la publicidad (banner, vídeos con recompensa), medirla, prevenir el fraude", "Identificador publicitario del dispositivo (IDFA en iOS, si lo autorizas; GAID en Android), dirección IP, modelo y sistema del dispositivo, idioma, país aproximado, interacciones con los anuncios", "Siempre, para publicidad no personalizada; personalizada solo con tu consentimiento"],
  row_ga=["Medir cómo se usa el juego para mejorarlo (dónde se detienen los jugadores, qué mejoras se compran)", "Identificador anónimo del dispositivo, modelo y sistema, sesiones, eventos de progreso y compras <em>en el juego</em> (moneda virtual)", "Solo con tu consentimiento"],
  policies="Políticas de estos servicios",
  p3_h="3. Tu consentimiento",
  p3="En el primer inicio, el juego te lo pregunta en una pantalla «Tus datos», con dos botones del mismo peso: aceptar o rechazar.",
  p3_accept="<strong>Aceptar</strong>: la publicidad puede adaptarse a tus intereses y se activa la medición de audiencia.",
  p3_refuse="<strong>Rechazar</strong>: ves publicidad no personalizada y no se mide nada. El juego es exactamente el mismo.",
  p3_ios="En iOS, el sistema te pide además el permiso de seguimiento (App Tracking Transparency).",
  p4_h="4. Base legal y conservación",
  p4="La publicidad no personalizada y la seguridad se basan en nuestro interés legítimo por financiar un juego gratuito. La personalización de la publicidad y la medición de audiencia se basan en tu consentimiento. Los datos permanecen en tu dispositivo mientras el juego esté instalado; los datos recibidos por los servicios de terceros se conservan según sus propias políticas, por lo general unos meses.",
  p5_h="5. Tus derechos",
  p5=f"Puedes solicitar el acceso, la rectificación, la supresión o la limitación de los datos que te conciernen, y oponerte a su tratamiento. Como Enami no posee ningún dato personal tuyo, la mayoría de estas solicitudes se ejercen ante los servicios citados, a través de los enlaces de la sección 2. Para cualquier pregunta, escríbenos: <a href=\"mailto:{MAIL}\">{MAIL}</a>. También puedes acudir a la AEPD (España) o a la autoridad de tu país.",
  p5_ca="Residentes de California: no vendemos datos personales. El juego envía a la red publicitaria una señal de «no vender» cuando rechazas.",
  p6_h="6. Menores",
  p6="Padel Idle no está dirigido a menores de 13 años y no recoge a sabiendas ningún dato sobre ellos. El juego se declara como no dirigido a menores ante la red publicitaria.",
  p7_h="7. Cambios",
  p7="Si esta política cambia, se actualiza la fecha de la parte superior y, en caso de cambio importante, el juego te lo indica al iniciarse.",
  s_title="Asistencia", s_meta="Padel Idle: Club Manager · Enami",
  s_intro=f"¿Una pregunta, un error, una idea? Escríbenos a <a href=\"mailto:{MAIL}\">{MAIL}</a> indicando tu dispositivo y la versión del juego (visible en el App Store). Respondemos en inglés y en francés.",
  faq_h="Preguntas frecuentes",
  faq=[
    ("Mi partida ha desaparecido.", "La partida se guarda en el dispositivo, no en una cuenta: desinstalar el juego la borra. Continúa exactamente donde la dejaste mientras el juego siga instalado, incluso después de cerrar la aplicación."),
    ("El botón «GRATIS» dice «Anuncio no disponible».", "No había ningún vídeo disponible en ese momento en la red publicitaria. Inténtalo un poco más tarde; sin vídeo no hay recompensa, es intencionado."),
    ("No veo el banner publicitario.", "Solo aparece después del tutorial de la primera partida, y solo cuando la red tiene un anuncio que mostrar."),
    ("¿El juego es gratis?", "Sí, totalmente, financiado por la publicidad. No hay compras integradas en esta versión."),
    ("Los clientes se van enfadados.", "Esperan palas en el mostrador: mantén la pila llena o contrata al repartidor para que se ocupe. Las pistas sucias solo se liberan cuando se han recogido las pelotas."),
  ]),
"de": dict(
  lang_bar_title="Sprache", home="Start", support="Support", privacy="Datenschutz",
  app_name="Padel Idle: Club Manager", publisher="Ein Spiel von Enami für iPhone und iPad.",
  tagline="Bau deinen Padel-Club auf: Schläger liefern, Spieler empfangen, Spiele starten, Bälle einsammeln, kassieren, ausbauen. Sechs Plätze, ein Shop, Umkleiden und ein Turnier am Wochenende.",
  links="Links", link_support="Support und häufige Fragen", link_privacy="Datenschutzerklärung",
  p_title="Datenschutzerklärung",
  p_meta="Letzte Aktualisierung: 12. September 2026 · Gilt für die App <strong>Padel Idle: Club Manager</strong> (iOS, Android), herausgegeben von Enami.",
  p_intro="Padel Idle ist ein kostenloses, werbefinanziertes Spiel. Diese Seite erklärt, welche Daten beim Spielen verarbeitet werden, von wem, wozu, und welche Wahl du hast. Sie ist zum Lesen gedacht, nicht um lang zu sein.",
  p1_h="1. Was das Spiel nicht erhebt",
  p1="Padel Idle verlangt kein Konto, keine E-Mail-Adresse, keinen Namen und keine Telefonnummer. Du gibst keine personenbezogenen Daten ein. Dein Spielstand (Fortschritt, Käufe im Spiel, virtuelles Geld) wird <strong>ausschließlich auf deinem Gerät</strong> gespeichert; wir haben keinen Zugriff darauf, und er ist weg, wenn du das Spiel deinstallierst.",
  p2_h="2. Was verarbeitet wird, und von wem",
  p2="Zwei Drittanbieter sind beteiligt. Sie erhalten technische Daten direkt von deinem Gerät; Enami erhält und speichert sie nicht.",
  th=["Dienst", "Zweck", "Daten", "Bedingung"],
  row_ads=["Werbung anzeigen (Banner, belohnte Videos), messen, Betrug verhindern", "Werbe-ID des Geräts (IDFA auf iOS, falls du es erlaubst; GAID auf Android), IP-Adresse, Gerätemodell und Betriebssystem, Sprache, ungefähres Land, Interaktionen mit Werbung", "Immer für nicht personalisierte Werbung; personalisierte Werbung nur mit deiner Einwilligung"],
  row_ga=["Messen, wie das Spiel genutzt wird, um es zu verbessern (wo Spieler aufhören, welche Verbesserungen gekauft werden)", "Anonyme Geräte-ID, Gerätemodell und Betriebssystem, Sitzungen, Fortschrittsereignisse und Käufe <em>im Spiel</em> (virtuelle Währung)", "Nur mit deiner Einwilligung"],
  policies="Richtlinien dieser Dienste",
  p3_h="3. Deine Einwilligung",
  p3="Beim ersten Start fragt dich das Spiel auf einem Bildschirm „Deine Daten“ mit zwei gleichwertigen Schaltflächen: annehmen oder ablehnen.",
  p3_accept="<strong>Annehmen</strong>: Werbung kann auf deine Interessen abgestimmt werden, und die Nutzungsmessung ist aktiv.",
  p3_refuse="<strong>Ablehnen</strong>: du siehst nicht personalisierte Werbung, und nichts wird gemessen. Das Spiel ist exakt dasselbe.",
  p3_ios="Auf iOS fragt das System zusätzlich nach der Tracking-Erlaubnis (App Tracking Transparency).",
  p4_h="4. Rechtsgrundlage und Speicherdauer",
  p4="Nicht personalisierte Werbung und Sicherheit beruhen auf unserem berechtigten Interesse, ein kostenloses Spiel zu finanzieren. Personalisierte Werbung und Nutzungsmessung beruhen auf deiner Einwilligung. Die Daten bleiben auf deinem Gerät, solange das Spiel installiert ist; von Drittanbietern empfangene Daten werden gemäß deren Richtlinien aufbewahrt, in der Regel einige Monate.",
  p5_h="5. Deine Rechte",
  p5=f"Du kannst Auskunft, Berichtigung, Löschung oder Einschränkung der dich betreffenden Daten verlangen und der Verarbeitung widersprechen. Da Enami keine personenbezogenen Daten über dich besitzt, richten sich die meisten dieser Anfragen an die oben genannten Dienste über die Links in Abschnitt 2. Bei Fragen schreib uns: <a href=\"mailto:{MAIL}\">{MAIL}</a>. Du kannst dich auch an die Datenschutzbehörde deines Landes wenden.",
  p5_ca="Einwohner Kaliforniens: wir verkaufen keine personenbezogenen Daten. Das Spiel sendet dem Werbenetzwerk ein „Nicht verkaufen“-Signal, wenn du ablehnst.",
  p6_h="6. Kinder",
  p6="Padel Idle richtet sich nicht an Kinder unter 13 Jahren und erhebt wissentlich keine Daten über sie. Das Spiel ist beim Werbenetzwerk als nicht an Kinder gerichtet gemeldet.",
  p7_h="7. Änderungen",
  p7="Ändert sich diese Erklärung, wird das Datum oben aktualisiert, und bei einer wesentlichen Änderung weist das Spiel beim Start darauf hin.",
  s_title="Support", s_meta="Padel Idle: Club Manager · Enami",
  s_intro=f"Eine Frage, ein Fehler, eine Idee? Schreib an <a href=\"mailto:{MAIL}\">{MAIL}</a> mit deinem Gerät und der Spielversion (im App Store sichtbar). Wir antworten auf Englisch und Französisch.",
  faq_h="Häufige Fragen",
  faq=[
    ("Mein Spielstand ist weg.", "Der Spielstand liegt auf dem Gerät, nicht in einem Konto: Deinstallieren löscht ihn. Er geht genau dort weiter, wo du aufgehört hast, solange das Spiel installiert bleibt, auch nach dem Schließen der App."),
    ("Die Schaltfläche „GRATIS“ sagt „Werbung nicht verfügbar“.", "In diesem Moment hatte das Werbenetzwerk kein Video. Versuch es etwas später noch einmal; ohne Video gibt es keine Belohnung, das ist so gewollt."),
    ("Ich sehe kein Werbebanner.", "Es erscheint erst nach dem Tutorial der ersten Partie, und nur wenn das Netzwerk eine Anzeige hat."),
    ("Ist das Spiel kostenlos?", "Ja, vollständig, werbefinanziert. In dieser Version gibt es keine In-App-Käufe."),
    ("Die Kunden gehen verärgert.", "Sie warten am Empfang auf Schläger: halte den Stapel gefüllt oder stell den Lagerläufer ein. Verschmutzte Plätze werden erst frei, wenn die Bälle eingesammelt sind."),
  ]),
"it": dict(
  lang_bar_title="Lingua", home="Home", support="Assistenza", privacy="Privacy",
  app_name="Padel Idle: Club Manager", publisher="Un gioco Enami per iPhone e iPad.",
  tagline="Costruisci il tuo club di padel: consegna le racchette, accogli i giocatori, avvia le partite, raccogli le palline, incassa, amplia. Sei campi, un negozio, spogliatoi e un torneo nel weekend.",
  links="Link", link_support="Assistenza e domande frequenti", link_privacy="Informativa sulla privacy",
  p_title="Informativa sulla privacy",
  p_meta="Ultimo aggiornamento: 12 settembre 2026 · Si applica all'app <strong>Padel Idle: Club Manager</strong> (iOS, Android) pubblicata da Enami.",
  p_intro="Padel Idle è un gioco gratuito finanziato dalla pubblicità. Questa pagina spiega quali dati vengono trattati quando giochi, da chi, perché, e quali scelte hai. L'abbiamo scritta per essere letta, non per essere lunga.",
  p1_h="1. Ciò che il gioco non raccoglie",
  p1="Padel Idle non chiede account, indirizzo e-mail, nome né numero di telefono. Non inserisci alcun dato personale. La tua partita (progressi, acquisti nel gioco, denaro virtuale) è salvata <strong>solo sul tuo dispositivo</strong>; non vi abbiamo accesso e scompare se disinstalli il gioco.",
  p2_h="2. Cosa viene trattato, e da chi",
  p2="Intervengono due servizi di terze parti. Ricevono dati tecnici direttamente dal tuo dispositivo; Enami non li riceve e non li conserva.",
  th=["Servizio", "Ruolo", "Dati", "Condizione"],
  row_ads=["Mostrare la pubblicità (banner, video con ricompensa), misurarla, prevenire le frodi", "Identificatore pubblicitario del dispositivo (IDFA su iOS, se lo autorizzi; GAID su Android), indirizzo IP, modello e sistema del dispositivo, lingua, paese approssimativo, interazioni con gli annunci", "Sempre, per pubblicità non personalizzata; personalizzata solo con il tuo consenso"],
  row_ga=["Misurare come viene usato il gioco per migliorarlo (dove i giocatori si fermano, quali potenziamenti vengono acquistati)", "Identificatore anonimo del dispositivo, modello e sistema, sessioni, eventi di progressione e acquisti <em>nel gioco</em> (valuta virtuale)", "Solo con il tuo consenso"],
  policies="Informative di questi servizi",
  p3_h="3. Il tuo consenso",
  p3="Al primo avvio, il gioco te lo chiede in una schermata «I tuoi dati», con due pulsanti di pari peso: accetta o rifiuta.",
  p3_accept="<strong>Accetta</strong>: la pubblicità può essere adattata ai tuoi interessi e la misurazione dell'audience è attiva.",
  p3_refuse="<strong>Rifiuta</strong>: vedi pubblicità non personalizzata e non viene misurato nulla. Il gioco è esattamente lo stesso.",
  p3_ios="Su iOS il sistema chiede inoltre l'autorizzazione al tracciamento (App Tracking Transparency).",
  p4_h="4. Base giuridica e conservazione",
  p4="La pubblicità non personalizzata e la sicurezza si basano sul nostro legittimo interesse a finanziare un gioco gratuito. La personalizzazione della pubblicità e la misurazione dell'audience si basano sul tuo consenso. I dati restano sul tuo dispositivo finché il gioco è installato; i dati ricevuti dai servizi di terze parti sono conservati secondo le loro informative, in genere alcuni mesi.",
  p5_h="5. I tuoi diritti",
  p5=f"Puoi chiedere l'accesso, la rettifica, la cancellazione o la limitazione dei dati che ti riguardano, e opporti al loro trattamento. Poiché Enami non detiene alcun dato personale su di te, la maggior parte di queste richieste va rivolta ai servizi citati sopra, tramite i link della sezione 2. Per qualsiasi domanda scrivici: <a href=\"mailto:{MAIL}\">{MAIL}</a>. Puoi anche rivolgerti al Garante (Italia) o all'autorità del tuo paese.",
  p5_ca="Residenti in California: non vendiamo dati personali. Il gioco invia alla rete pubblicitaria un segnale «non vendere» quando rifiuti.",
  p6_h="6. Minori",
  p6="Padel Idle non è rivolto ai minori di 13 anni e non raccoglie consapevolmente alcun dato su di loro. Il gioco è dichiarato come non rivolto ai minori presso la rete pubblicitaria.",
  p7_h="7. Modifiche",
  p7="Se questa informativa cambia, la data in alto viene aggiornata e, per una modifica importante, il gioco te lo segnala all'avvio.",
  s_title="Assistenza", s_meta="Padel Idle: Club Manager · Enami",
  s_intro=f"Una domanda, un bug, un'idea? Scrivici a <a href=\"mailto:{MAIL}\">{MAIL}</a> indicando il tuo dispositivo e la versione del gioco (visibile nell'App Store). Rispondiamo in inglese e in francese.",
  faq_h="Domande frequenti",
  faq=[
    ("La mia partita è sparita.", "La partita è salvata sul dispositivo, non su un account: disinstallare il gioco la cancella. Riprende esattamente da dove l'hai lasciata finché il gioco resta installato, anche dopo aver chiuso l'app."),
    ("Il pulsante «GRATIS» dice «Annuncio non disponibile».", "In quel momento la rete pubblicitaria non aveva alcun video. Riprova poco dopo; senza video non c'è ricompensa, è voluto."),
    ("Non vedo il banner pubblicitario.", "Compare solo dopo il tutorial della prima partita, e solo quando la rete ha un annuncio da mostrare."),
    ("Il gioco è gratuito?", "Sì, del tutto, finanziato dalla pubblicità. In questa versione non ci sono acquisti in-app."),
    ("I clienti se ne vanno arrabbiati.", "Aspettano le racchette al banco: tieni la pila rifornita, o assumi il fattorino perché se ne occupi. I campi sporchi si liberano solo dopo aver raccolto le palline."),
  ]),
"nl": dict(
  lang_bar_title="Taal", home="Home", support="Ondersteuning", privacy="Privacy",
  app_name="Padel Idle: Club Manager", publisher="Een Enami-spel voor iPhone en iPad.",
  tagline="Bouw je padelclub: lever rackets, ontvang spelers, start wedstrijden, raap ballen op, incasseer, breid uit. Zes banen, een winkel, kleedkamers en een weekendtoernooi.",
  links="Links", link_support="Ondersteuning en veelgestelde vragen", link_privacy="Privacybeleid",
  p_title="Privacybeleid",
  p_meta="Laatst bijgewerkt: 12 september 2026 · Geldt voor de app <strong>Padel Idle: Club Manager</strong> (iOS, Android), uitgegeven door Enami.",
  p_intro="Padel Idle is een gratis spel dat door advertenties wordt gefinancierd. Deze pagina legt uit welke gegevens worden verwerkt wanneer je speelt, door wie, waarom, en welke keuzes je hebt. Ze is geschreven om gelezen te worden, niet om lang te zijn.",
  p1_h="1. Wat het spel niet verzamelt",
  p1="Padel Idle vraagt geen account, e-mailadres, naam of telefoonnummer. Je voert geen persoonsgegevens in. Je spel (voortgang, aankopen in het spel, virtueel geld) wordt <strong>alleen op je toestel</strong> opgeslagen; wij hebben er geen toegang toe en het verdwijnt als je het spel verwijdert.",
  p2_h="2. Wat er wordt verwerkt, en door wie",
  p2="Twee externe diensten zijn betrokken. Zij ontvangen technische gegevens rechtstreeks van je toestel; Enami ontvangt en bewaart ze niet.",
  th=["Dienst", "Doel", "Gegevens", "Voorwaarde"],
  row_ads=["Advertenties tonen (banner, beloningsvideo's), meten, fraude voorkomen", "Advertentie-ID van het toestel (IDFA op iOS, als je het toestaat; GAID op Android), IP-adres, toestelmodel en besturingssysteem, taal, land bij benadering, interacties met advertenties", "Altijd, voor niet-gepersonaliseerde advertenties; gepersonaliseerd alleen met jouw toestemming"],
  row_ga=["Meten hoe het spel wordt gebruikt om het te verbeteren (waar spelers stoppen, welke verbeteringen worden gekocht)", "Anonieme toestel-ID, toestelmodel en besturingssysteem, sessies, voortgangsgebeurtenissen en aankopen <em>in het spel</em> (virtuele valuta)", "Alleen met jouw toestemming"],
  policies="Beleid van deze diensten",
  p3_h="3. Je toestemming",
  p3="Bij de eerste start stelt het spel je de vraag op een scherm „Je gegevens”, met twee gelijkwaardige knoppen: accepteren of weigeren.",
  p3_accept="<strong>Accepteren</strong>: advertenties kunnen op je interesses worden afgestemd en de gebruiksmeting staat aan.",
  p3_refuse="<strong>Weigeren</strong>: je ziet niet-gepersonaliseerde advertenties en er wordt niets gemeten. Het spel is precies hetzelfde.",
  p3_ios="Op iOS vraagt het systeem daarnaast om toestemming voor tracking (App Tracking Transparency).",
  p4_h="4. Rechtsgrond en bewaartermijn",
  p4="Niet-gepersonaliseerde advertenties en beveiliging berusten op ons gerechtvaardigd belang om een gratis spel te financieren. Personalisatie van advertenties en gebruiksmeting berusten op je toestemming. De gegevens blijven op je toestel zolang het spel is geïnstalleerd; gegevens die externe diensten ontvangen, worden volgens hun eigen beleid bewaard, doorgaans enkele maanden.",
  p5_h="5. Je rechten",
  p5=f"Je kunt inzage, rectificatie, wissing of beperking van je gegevens vragen en bezwaar maken tegen de verwerking. Omdat Enami geen persoonsgegevens over jou bezit, richt je de meeste van deze verzoeken tot de hierboven genoemde diensten, via de links in deel 2. Voor vragen: <a href=\"mailto:{MAIL}\">{MAIL}</a>. Je kunt ook terecht bij de Autoriteit Persoonsgegevens (Nederland) of de toezichthouder van je land.",
  p5_ca="Inwoners van Californië: wij verkopen geen persoonsgegevens. Het spel stuurt het advertentienetwerk een „niet verkopen”-signaal wanneer je weigert.",
  p6_h="6. Kinderen",
  p6="Padel Idle is niet gericht op kinderen jonger dan 13 jaar en verzamelt bewust geen gegevens over hen. Het spel is bij het advertentienetwerk aangemeld als niet op kinderen gericht.",
  p7_h="7. Wijzigingen",
  p7="Als dit beleid verandert, wordt de datum bovenaan bijgewerkt en bij een belangrijke wijziging meldt het spel dit bij het opstarten.",
  s_title="Ondersteuning", s_meta="Padel Idle: Club Manager · Enami",
  s_intro=f"Een vraag, een bug, een idee? Mail naar <a href=\"mailto:{MAIL}\">{MAIL}</a> met je toestel en de spelversie (zichtbaar in de App Store). We antwoorden in het Engels en het Frans.",
  faq_h="Veelgestelde vragen",
  faq=[
    ("Mijn spel is weg.", "Het spel wordt op het toestel opgeslagen, niet in een account: verwijderen wist het. Het gaat precies verder waar je was zolang het spel geïnstalleerd blijft, ook na het sluiten van de app."),
    ("De knop „GRATIS” zegt „Advertentie niet beschikbaar”.", "Er was op dat moment geen video beschikbaar bij het advertentienetwerk. Probeer het iets later opnieuw; zonder video is er geen beloning, dat is zo bedoeld."),
    ("Ik zie geen advertentiebanner.", "Die verschijnt pas na de tutorial van het eerste spel, en alleen wanneer het netwerk een advertentie heeft."),
    ("Is het spel gratis?", "Ja, helemaal, gefinancierd door advertenties. In deze versie zijn er geen in-app-aankopen."),
    ("Klanten vertrekken boos.", "Ze wachten op rackets aan de balie: houd de stapel gevuld, of neem de loopjongen aan. Vuile banen komen pas vrij als de ballen zijn opgeraapt."),
  ]),
}


def lang_bar(kind, lang):
    items = []
    for code in LANGS:
        label = code.upper()
        items.append(f'<strong>{label}</strong>' if code == lang else f'<a href="{page_name(kind, code)}">{label}</a>')
    return '<span class="langs">' + " | ".join(items) + "</span>"


def shell(kind, lang, title, body):
    t = T[lang]
    nav = f'<a href="{page_name("support", lang)}">{t["support"]}</a><a href="{page_name("privacy", lang)}">{t["privacy"]}</a>'
    return f'''<!doctype html>
<html lang="{lang}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<link rel="stylesheet" href="style.css">
</head>
<body>
<header><div class="wrap"><h1><a href="{page_name("index", lang)}">Padel Idle</a></h1><nav>{nav}</nav>{lang_bar(kind, lang)}</div></header>
<main>
{body}
</main>
<footer>© 2026 Enami · {lang_bar(kind, lang)}</footer>
</body>
</html>
'''


def index(lang):
    t = T[lang]
    body = f'''<h2>{t["app_name"]}</h2>
<p class="meta">{t["publisher"]}</p>
<p>{t["tagline"]}</p>
<h3>{t["links"]}</h3>
<ul>
<li><a href="{page_name("support", lang)}">{t["link_support"]}</a></li>
<li><a href="{page_name("privacy", lang)}">{t["link_privacy"]}</a></li>
</ul>'''
    return shell("index", lang, "Padel Idle", body)


def privacy(lang):
    t = T[lang]
    th = "".join(f"<th>{h}</th>" for h in t["th"])
    ads = "".join(f"<td>{c}</td>" for c in t["row_ads"])
    ga = "".join(f"<td>{c}</td>" for c in t["row_ga"])
    body = f'''<h2>{t["p_title"]}</h2>
<p class="meta">{t["p_meta"]}</p>
<p>{t["p_intro"]}</p>
<h3>{t["p1_h"]}</h3>
<p>{t["p1"]}</p>
<h3>{t["p2_h"]}</h3>
<p>{t["p2"]}</p>
<table>
<tr>{th}</tr>
<tr><td><strong>Unity LevelPlay</strong> (ironSource / Unity Ads)</td>{ads}</tr>
<tr><td><strong>GameAnalytics</strong></td>{ga}</tr>
</table>
<p>{t["policies"]} : <a href="https://unity.com/legal/privacy-policy" rel="noopener">Unity</a> · <a href="https://www.is.com/privacy-policy/" rel="noopener">ironSource</a> · <a href="https://gameanalytics.com/privacy/" rel="noopener">GameAnalytics</a>.</p>
<h3>{t["p3_h"]}</h3>
<p>{t["p3"]}</p>
<ul>
<li>{t["p3_accept"]}</li>
<li>{t["p3_refuse"]}</li>
</ul>
<p>{t["p3_ios"]}</p>
<h3>{t["p4_h"]}</h3>
<p>{t["p4"]}</p>
<h3>{t["p5_h"]}</h3>
<p>{t["p5"]}</p>
<p>{t["p5_ca"]}</p>
<h3>{t["p6_h"]}</h3>
<p>{t["p6"]}</p>
<h3>{t["p7_h"]}</h3>
<p>{t["p7"]}</p>'''
    return shell("privacy", lang, f'Padel Idle – {t["p_title"]}', body)


def support(lang):
    t = T[lang]
    faq = "\n".join(f"<p><strong>{q}</strong> {a.replace('{privacy}', page_name('privacy', lang))}</p>" for q, a in t["faq"])
    body = f'''<h2>{t["s_title"]}</h2>
<p class="meta">{t["s_meta"]}</p>
<p>{t["s_intro"]}</p>
<h3>{t["faq_h"]}</h3>
{faq}'''
    return shell("support", lang, f'Padel Idle – {t["s_title"]}', body)


if __name__ == "__main__":
    out = Path(__file__).parent / SITE_DIR
    out.mkdir(exist_ok=True)
    for lang in LANGS:
        (out / page_name("index", lang)).write_text(index(lang), encoding="utf-8")
        (out / page_name("privacy", lang)).write_text(privacy(lang), encoding="utf-8")
        (out / page_name("support", lang)).write_text(support(lang), encoding="utf-8")
    print(f"{3 * len(LANGS)} pages générées dans {SITE_DIR}/.")
