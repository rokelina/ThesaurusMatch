countryNames = [
    'afghanistan', 'albania', 'algeria', 'andorra', 'angola', 'antigua and barbuda', 'argentina', 'armenia', 'australia', 'austria', 'azerbaijan',
    'bahamas', 'bahrain', 'bangladesh', 'barbados', 'belarus', 'belgium', 'belize', 'benin', 'bhutan', 'bolivia', 'bosnia and herzegovina', 'botswana', 'brazil', 'brunei', 'bulgaria', 'burkina faso', 'burundi',
    'cabo verde', 'cambodia', 'cameroon', 'canada', 'central african republic', 'chad', 'chile', 'china', 'colombia', 'comoros', 'congo', 'costa rica', 'croatia', 'cuba', 'cyprus', 'czechia',
    'denmark', 'djibouti', 'dominica', 'dominican republic', 'ecuador', 'egypt', 'el salvador', 'equatorial guinea', 'eritrea', 'estonia', 'eswatini', 'ethiopia',
    'fiji', 'finland', 'france', 'gabon', 'gambia', 'georgia', 'germany', 'ghana', 'greece', 'grenada', 'guatemala', 'guinea', 'guinea-bissau', 'guyana',
    'haiti', 'honduras', 'hungary', 'iceland', 'india', 'indonesia', 'iran', 'iraq', 'ireland', 'israel', 'italy', 'ivory coast', 'jamaica', 'japan', 'jordan',
    'kazakhstan', 'kenya', 'kiribati', 'kosovo', 'kuwait', 'kyrgyzstan', 'laos', 'latvia', 'lebanon', 'lesotho', 'liberia', 'libya', 'liechtenstein', 'lithuania', 'luxembourg', 'madagascar', 'malawi', 'malaysia', 'maldives',
    'mali', 'malta', 'marshall islands', 'mauritania', 'mauritius', 'mexico', 'micronesia', 'moldova', 'monaco', 'mongolia', 'montenegro', 'morocco', 'mozambique', 'myanmar',
    'namibia', 'nauru', 'nepal', 'netherlands', 'new zealand', 'nicaragua', 'niger', 'nigeria', 'north korea', 'north macedonia', 'norway',
    'oman', 'pakistan', 'palau', 'panama', 'papua new guinea', 'paraguay', 'peru', 'philippines', 'poland', 'portugal', 'qatar', 'romania', 'russia', 'rwanda',
    'saint kitts and nevis', 'saint lucia', 'saint vincent and the grenadines', 'samoa', 'san marino', 'sao tome and principe', 'saudi arabia', 'senegal', 'serbia', 'seychelles', 'sierra leone', 'singapore', 'slovakia', 'slovenia',
    "slovenia", "solomon islands", "somalia", "south africa", "south korea", "south sudan", "spain", "sri lanka", "sudan", "suriname", "sweden", "switzerland", "syria", "taiwan", "tajikistan",    "tanzania", "thailand", "timor-leste (east timor)",
    "togo", "tonga", "trinidad and tobago", "tunisia", "turkey", "turkmenistan", "tuvalu", "uganda",
    "ukraine", "united arab emirates", "united kingdom", "united states of america", "uruguay", "uzbekistan", "vanuatu", "vatican city", "venezuela", "vietnam", "yemen", "yugoslavia" "zambia",
    "zimbabwe"]

usStatesCities = [
    'alabama', 'birmingham', 'montgomery', 'mobile', 'alaska', 'anchorage', 'fairbanks', 'juneau', 'arizona', 'phoenix', 'tucson', 'mesa', 'arkansas', 'little rock', 'fort smith', 'fayetteville', 'california', 'los angeles',
    'san francisco', 'san diego', 'colorado', 'denver', 'colorado springs', 'aurora', 'connecticut', 'bridgeport', 'new haven', 'hartford', 'delaware', 'wilmington', 'dover', 'newark', 'florida', 'miami', 'orlando', 'tampa',
    'georgia', 'atlanta', 'savannah', 'augusta', 'hawaii', 'honolulu', 'hilo', 'kailua', 'idaho', 'boise', 'meridian', 'nampa', 'illinois', 'chicago', 'springfield', 'rockford', 'indiana', 'indianapolis', 'fort wayne', 'evansville',
    'iowa', 'des moines', 'cedar rapids', 'davenport', 'kansas', 'wichita', 'overland park', 'kansas city', 'kentucky', 'louisville', 'lexington', 'bowling green', 'louisiana', 'new orleans', 'baton rouge', 'shreveport', 'maine',
    'portland', 'lewiston', 'augusta', 'maryland', 'baltimore', 'frederick', 'annapolis', 'massachusetts', 'boston', 'worcester', 'springfield', 'michigan', 'detroit', 'grand rapids', 'ann arbor', 'minnesota', 'minneapolis', 'saint paul',
    'rochester', 'mississippi', 'jackson', 'gulfport', 'hattiesburg', 'missouri', 'kansas city', 'st. louis', 'springfield', 'montana', 'billings', 'missoula', 'great falls', 'nebraska', 'omaha', 'lincoln', 'bellevue', 'nevada', 'las vegas', 'henderson',
    'reno', 'new hampshire', 'manchester', 'nashua', 'concord', 'new jersey', 'newark', 'jersey city', 'trenton', 'new mexico', 'albuquerque', 'santa fe', 'las cruces', 'new york', 'new york city', 'buffalo', 'rochester', 'north carolina', 'charlotte',
    'raleigh', 'greensboro', 'north dakota', 'fargo', 'bismarck', 'grand forks', 'ohio', 'columbus', 'cleveland', 'cincinnati', 'oklahoma', 'oklahoma city', 'tulsa', 'norman', 'oregon', 'portland', 'eugene', 'salem', 'pennsylvania', 'philadelphia', 'pittsburgh',
    'allentown', 'rhode island', 'providence', 'warwick', 'cranston', 'south carolina', 'charleston', 'columbia', 'greenville', 'south dakota', 'sioux falls', 'rapid city', 'aberdeen', 'tennessee', 'nashville', 'memphis', 'knoxville', 'texas', 'houston',
    'san antonio', 'dallas', 'utah', 'salt lake city', 'west valley city', 'provo', 'vermont', 'burlington', 'south burlington', 'rutland', 'virginia', 'virginia beach', 'norfolk', 'richmond', 'washington', 'seattle', 'spokane', 'tacoma', 'west virginia', 'charleston',
    'huntington', 'parkersburg', 'wisconsin', 'milwaukee', 'madison', 'green bay', 'wyoming', 'cheyenne', 'casper', 'laramie']

codes = ["usa", "nyc", "lax", "gop", "dnc", "cia", "fbi", "tel", "cel", "com", "edu", "gov", "mil", "net", "org", "msn", "npr", "pbs", "sec", "aaa", "abc", "wow", "xyz", "iud",
         "dui", "mon", "tue", "wed", "thu", "fri", "sat", "sun", "jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec", "ross", "ussr"]

currencyCodes = ['aed', 'afn', 'all', 'amd', 'ang', 'aoa', 'ars', 'aud', 'awg', 'azn', 'bam', 'bbd', 'bdt', 'bgn', 'bhd', 'bif', 'bmd', 'bnd', 'bob', 'bov', 'brl',
                 'bsd', 'btn', 'bwp', 'byn', 'bzd', 'cad', 'cdf', 'che', 'chf', 'chw', 'clf', 'clp', 'cny', 'cop', 'cou', 'crc', 'cuc', 'cup', 'cve', 'czk', 'djf', 'dkk',
                 'dop', 'dzd', 'egp', 'ern', 'etb', 'eur', 'fjd', 'fkp', 'gbp', 'gel', 'ghs', 'gip', 'gmd', 'gnf', 'gtq', 'gyd', 'hkd', 'hnl', 'hrk', 'htg', 'huf', 'idr', 'ils',
                 'inr', 'iqd', 'irr', 'isk', 'jmd', 'jod', 'jpy', 'kes', 'kgs', 'khr', 'kmf', 'kpw', 'krw', 'kwd', 'kyd', 'kzt', 'lak', 'lbp', 'lkr', 'lrd', 'lsl', 'lyd', 'mad',
                 'mdl', 'mga', 'mkd', 'mmk', 'mnt', 'mop', 'mru', 'mur', 'mvr', 'mwk', 'mxn', 'mxv', 'myr', 'mzn', 'nad', 'ngn', 'nio', 'nok', 'npr', 'nzd', 'omr', 'pab', 'pen',
                 'pgk', 'php', 'pkr', 'pln', 'pyg', 'qar', 'ron', 'rsd', 'rub', 'rwf', 'sar', 'sbd', 'scr', 'sdg', 'sek', 'sgd', 'shp', 'sll', 'sos', 'srd', 'ssp', 'stn', 'svc',
                 'syp', 'szl', 'thb', 'tjs', 'tmt', 'tnd', 'top', 'try', 'ttd', 'twd', 'tzs', 'uah', 'ugx', 'usd', 'usn', 'uyi', 'uyu', 'uzs', 'ves', 'vnd', 'vuv', 'wst', 'xaf',
                 'xag', 'xau', 'xcd', 'xdr', 'xof', 'xpd', 'xpf', 'xpt', 'yer', 'zmw', 'zwl']

daysMonths = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'january',
              'february', 'march', 'april', 'may', 'june', 'july', 'august', 'september', 'october', 'november', 'december']

lastNames = ['smith', 'johnson', 'williams', 'brown', 'jones', 'miller', 'davis', 'garcia', 'rodriguez',
             'martinez', 'hernandez', 'lopez', 'gonzalez', 'perez', 'taylor', 'anderson', 'wilson', 'thomas',
             'jackson', 'white', 'harris', 'martin', 'thompson', 'moore', 'young', 'allen', 'king', 'wright',
             'scott', 'green', 'baker', 'adams', 'nelson', 'carter', 'mitchell', 'perez', 'roberts', 'turner',
             'phillips', 'campbell', 'parker', 'evans', 'edwards', 'collins', 'stewart', 'sanchez', 'morris',
             'murphy', 'bailey', 'rivera']

us_name_file = '/Users/rosinascampino/Desktop/names_project/raw_data/usa/yob2021.txt'
names = []

with open(us_name_file, 'r') as file:
    for row in file:
        line = row.split(',')
        names.append(line[0].lower())

filterWords = countryNames + usStatesCities + codes + \
    currencyCodes + daysMonths + lastNames + names
