// Türkiye şehirleri (alfabetik)
window.turkishCities = [
    "Adana", "Adıyaman", "Afyonkarahisar", "Ağrı", "Amasya", "Ankara", "Antalya", "Artvin", "Aydın", "Balıkesir", 
    "Bilecik", "Bingöl", "Bitlis", "Bolu", "Burdur", "Bursa", "Çanakkale", "Çankırı", "Çorum", "Denizli", 
    "Diyarbakır", "Edirne", "Elazığ", "Erzincan", "Erzurum", "Eskişehir", "Gaziantep", "Giresun", "Gümüşhane", 
    "Hakkari", "Hatay", "Isparta", "Mersin", "İstanbul", "İzmir", "Kars", "Kastamonu", "Kayseri", "Kırklareli",
    "Kırşehir", "Kocaeli", "Konya", "Kütahya", "Malatya", "Manisa", "Kahramanmaraş", "Mardin", "Muğla", "Muş", 
    "Nevşehir", "Niğde", "Ordu", "Rize", "Sakarya", "Samsun", "Siirt", "Sinop", "Sivas", "Tekirdağ", "Tokat", 
    "Trabzon", "Tunceli", "Şanlıurfa", "Uşak", "Van", "Yozgat", "Zonguldak", "Aksaray", "Bayburt", "Karaman", 
    "Kırıkkale", "Batman", "Şırnak", "Bartın", "Ardahan", "Iğdır", "Yalova", "Karabük", "Kilis", "Osmaniye", "Düzce"
];

// Türkiye şehir-ilçe eşlemesi (tam liste, özetlenmiş örnek; tam liste eklenecek)
window.cityDistricts = {
    "Adana": ["Aladağ", "Ceyhan", "Çukurova", "Feke", "İmamoğlu", "Karaisalı", "Karataş", "Kozan", "Pozantı", "Saimbeyli", "Sarıçam", "Seyhan", "Tufanbeyli", "Yumurtalık", "Yüreğir"],
    "Adıyaman": ["Besni", "Çelikhan", "Gerger", "Gölbaşı", "Kahta", "Merkez", "Samsat", "Sincik", "Tut"],
    "Afyonkarahisar": ["Başmakçı", "Bayat", "Bolvadin", "Çay", "Çobanlar", "Dazkırı", "Dinar", "Emirdağ", "Evciler", "Hocalar", "İhsaniye", "İscehisar", "Kızılören", "Merkez", "Sandıklı", "Sinanpaşa", "Sultandağı", "Şuhut"],
    "Ağrı": ["Diyadin", "Doğubayazıt", "Eleşkirt", "Hamur", "Merkez", "Patnos", "Taşlıçay", "Tutak"],
    "Amasya": ["Göynücek", "Gümüşhacıköy", "Hamamözü", "Merkez", "Merzifon", "Suluova", "Taşova"],
    "Ankara": ["Akyurt", "Altındağ", "Ayaş", "Bala", "Beypazarı", "Çamlıdere", "Çankaya", "Çubuk", "Elmadağ", "Etimesgut", "Evren", "Gölbaşı", "Güdül", "Haymana", "Kahramankazan", "Kalecik", "Keçiören", "Kızılcahamam", "Mamak", "Nallıhan", "Polatlı", "Pursaklar", "Sincan", "Şereflikoçhisar", "Yenimahalle"],
    "Antalya": ["Akseki", "Aksu", "Alanya", "Demre", "Döşemealtı", "Elmalı", "Finike", "Gazipaşa", "Gündoğmuş", "İbradı", "Kaş", "Kemer", "Kepez", "Konyaaltı", "Korkuteli", "Kumluca", "Manavgat", "Muratpaşa", "Serik"],
    "Artvin": ["Ardanuç", "Arhavi", "Borçka", "Hopa", "Kemalpaşa", "Merkez", "Murgul", "Şavşat", "Yusufeli"],
    "Aydın": ["Bozdoğan", "Buharkent", "Çine", "Didim", "Efeler", "Germencik", "İncirliova", "Karacasu", "Karpuzlu", "Koçarlı", "Köşk", "Kuşadası", "Kuyucak", "Nazilli", "Söke", "Sultanhisar", "Yenipazar"],
    "Balıkesir": ["Altıeylül", "Ayvalık", "Balya", "Bandırma", "Bigadiç", "Burhaniye", "Dursunbey", "Edremit", "Erdek", "Gömeç", "Gönen", "Havran", "İvrindi", "Karesi", "Kepsut", "Manyas", "Marmara", "Savaştepe", "Sındırgı", "Susurluk"],
    "Bilecik": ["Bozüyük", "Gölpazarı", "İnhisar", "Merkez", "Osmaneli", "Pazaryeri", "Söğüt", "Yenipazar"],
    "Bingöl": ["Adaklı", "Genç", "Karlıova", "Kiğı", "Merkez", "Solhan", "Yayladere", "Yedisu"],
    "Bitlis": ["Adilcevaz", "Ahlat", "Güroymak", "Hizan", "Merkez", "Mutki", "Tatvan"],
    "Bolu": ["Dörtdivan", "Gerede", "Göynük", "Kıbrıscık", "Mengen", "Merkez", "Mudurnu", "Seben", "Yeniçağa"],
    "Burdur": ["Ağlasun", "Altınyayla", "Bucak", "Çavdır", "Çeltikçi", "Gölhisar", "Karamanlı", "Kemer", "Merkez", "Tefenni", "Yeşilova"],
    "Bursa": ["Büyükorhan", "Gemlik", "Gürsu", "Harmancık", "İnegöl", "İznik", "Karacabey", "Keles", "Kestel", "Mudanya", "Mustafakemalpaşa", "Nilüfer", "Orhaneli", "Orhangazi", "Osmangazi", "Yenişehir", "Yıldırım"],
    "Çanakkale": ["Ayvacık", "Bayramiç", "Biga", "Bozcaada", "Çan", "Eceabat", "Ezine", "Gelibolu", "Gökçeada", "Lapseki", "Merkez", "Yenice"],
    "Çankırı": ["Atkaracalar", "Bayramören", "Çerkeş", "Eldivan", "Ilgaz", "Kızılırmak", "Korgun", "Kurşunlu", "Merkez", "Orta", "Şabanözü", "Yapraklı"],
    "Çorum": ["Alaca", "Bayat", "Boğazkale", "Dodurga", "İskilip", "Kargı", "Laçin", "Mecitözü", "Merkez", "Oğuzlar", "Ortaköy", "Osmancık", "Sungurlu", "Uğurludağ"],
    "Denizli": ["Acıpayam", "Babadağ", "Baklan", "Bekilli", "Beyağaç", "Bozkurt", "Buldan", "Çal", "Çameli", "Çardak", "Çivril", "Güney", "Honaz", "Kale", "Merkezefendi", "Pamukkale", "Sarayköy", "Serinhisar", "Tavas"],
    "Diyarbakır": ["Bağlar", "Bismil", "Çermik", "Çınar", "Çüngüş", "Dicle", "Eğil", "Ergani", "Hani", "Hazro", "Kayapınar", "Kocaköy", "Kulp", "Lice", "Silvan", "Sur", "Yenişehir"],
    "Edirne": ["Enez", "Havsa", "İpsala", "Keşan", "Lalapaşa", "Meriç", "Merkez", "Süloğlu", "Uzunköprü"],
    "Elazığ": ["Ağın", "Alacakaya", "Arıcak", "Baskil", "Karakoçan", "Keban", "Kovancılar", "Maden", "Merkez", "Palu", "Sivrice"],
    "Erzincan": ["Çayırlı", "İliç", "Kemah", "Kemaliye", "Merkez", "Otlukbeli", "Refahiye", "Tercan", "Üzümlü"],
    "Erzurum": ["Aşkale", "Aziziye", "Çat", "Hınıs", "Horasan", "İspir", "Karaçoban", "Karayazı", "Köprüköy", "Narman", "Oltu", "Olur", "Palandöken", "Pasinler", "Pazaryolu", "Şenkaya", "Tekman", "Tortum", "Uzundere", "Yakutiye"],
    "Eskişehir": ["Alpu", "Beylikova", "Çifteler", "Günyüzü", "Han", "İnönü", "Mahmudiye", "Mihalgazi", "Mihalıççık", "Odunpazarı", "Sarıcakaya", "Seyitgazi", "Sivrihisar", "Tepebaşı"],
    "Gaziantep": ["Araban", "İslahiye", "Karkamış", "Nizip", "Nurdağı", "Oğuzeli", "Şahinbey", "Şehitkamil", "Yavuzeli"],
    "Giresun": ["Alucra", "Bulancak", "Çamoluk", "Çanakçı", "Dereli", "Doğankent", "Espiye", "Eynesil", "Görele", "Güce", "Keşap", "Merkez", "Piraziz", "Şebinkarahisar", "Tirebolu", "Yağlıdere"],
    "Gümüşhane": ["Kelkit", "Köse", "Kürtün", "Merkez", "Şiran", "Torul"],
    "Hakkari": ["Çukurca", "Derecik", "Merkez", "Şemdinli", "Yüksekova"],
    "Hatay": ["Altınözü", "Antakya", "Arsuz", "Belen", "Defne", "Dörtyol", "Erzin", "Hassa", "İskenderun", "Kırıkhan", "Kumlu", "Payas", "Reyhanlı", "Samandağ", "Yayladağı"],
    "Isparta": ["Aksu", "Atabey", "Eğirdir", "Gelendost", "Gönen", "Keçiborlu", "Merkez", "Senirkent", "Sütçüler", "Şarkikaraağaç", "Uluborlu", "Yalvaç", "Yenişarbademli"],
    "Mersin": ["Akdeniz", "Anamur", "Aydıncık", "Bozyazı", "Çamlıyayla", "Erdemli", "Gülnar", "Mezitli", "Mut", "Silifke", "Tarsus", "Toroslar", "Yenişehir"],
    "İstanbul": ["Adalar", "Arnavutköy", "Ataşehir", "Avcılar", "Bağcılar", "Bahçelievler", "Bakırköy", "Başakşehir", "Bayrampaşa", "Beşiktaş", "Beykoz", "Beylikdüzü", "Beyoğlu", "Büyükçekmece", "Çatalca", "Çekmeköy", "Esenler", "Esenyurt", "Eyüpsultan", "Fatih", "Gaziosmanpaşa", "Güngören", "Kadıköy", "Kağıthane", "Kartal", "Küçükçekmece", "Maltepe", "Pendik", "Sancaktepe", "Sarıyer", "Şile", "Silivri", "Şişli", "Sultanbeyli", "Sultangazi", "Tuzla", "Ümraniye", "Üsküdar", "Zeytinburnu"],
    "İzmir": ["Aliağa", "Balçova", "Bayındır", "Bayraklı", "Bergama", "Beydağ", "Bornova", "Buca", "Çeşme", "Çiğli", "Dikili", "Foça", "Gaziemir", "Güzelbahçe", "Karabağlar", "Karaburun", "Karşıyaka", "Kemalpaşa", "Kınık", "Kiraz", "Konak", "Menderes", "Menemen", "Narlıdere", "Ödemiş", "Seferihisar", "Selçuk", "Tire", "Torbalı", "Urla"],
    "Kars": ["Akyaka", "Arpaçay", "Digor", "Kağızman", "Merkez", "Sarıkamış", "Selim", "Susuz"],
    "Kastamonu": ["Abana", "Ağlı", "Araç", "Azdavay", "Bozkurt", "Cide", "Çatalzeytin", "Daday", "Devrekani", "Doğanyurt", "Hanönü", "İhsangazi", "İnebolu", "Küre", "Merkez", "Pınarbaşı", "Seydiler", "Şenpazar", "Taşköprü", "Tosya"],
    "Kayseri": ["Akkışla", "Bünyan", "Develi", "Felahiye", "Hacılar", "İncesu", "Kocasinan", "Melikgazi", "Özvatan", "Pınarbaşı", "Sarıoğlan", "Sarız", "Talas", "Tomarza", "Yahyalı", "Yeşilhisar"],
    "Kırklareli": ["Babaeski", "Demirköy", "Kofçaz", "Lüleburgaz", "Merkez", "Pehlivanköy", "Pınarhisar", "Vize"],
    "Kırşehir": ["Akçakent", "Akpınar", "Boztepe", "Çiçekdağı", "Kaman", "Merkez", "Mucur"],
    "Kocaeli": ["Başiskele", "Çayırova", "Darıca", "Derince", "Dilovası", "Gebze", "Gölcük", "İzmit", "Kandıra", "Karamürsel", "Kartepe", "Körfez"],
    "Konya": ["Ahırlı", "Akören", "Akşehir", "Altınekin", "Beyşehir", "Bozkır", "Cihanbeyli", "Çeltik", "Çumra", "Derbent", "Derebucak", "Doğanhisar", "Emirgazi", "Ereğli", "Güneysınır", "Hadim", "Halkapınar", "Hüyük", "Ilgın", "Kadınhanı", "Karapınar", "Karatay", "Kulu", "Meram", "Sarayönü", "Selçuklu", "Seydişehir", "Taşkent", "Tuzlukçu", "Yalıhüyük", "Yunak"],
    "Kütahya": ["Altıntaş", "Aslanapa", "Çavdarhisar", "Domaniç", "Dumlupınar", "Emet", "Gediz", "Hisarcık", "İhsaniye", "Merkez", "Pazarlar", "Simav", "Şaphane", "Tavşanlı"],
    "Malatya": ["Akçadağ", "Arapgir", "Arguvan", "Battalgazi", "Darende", "Doğanşehir", "Doğanyol", "Hekimhan", "Kale", "Kuluncak", "Pütürge", "Yazıhan", "Yeşilyurt"],
    "Manisa": ["Ahmetli", "Akhisar", "Alaşehir", "Demirci", "Gölmarmara", "Gördes", "Kırkağaç", "Köprübaşı", "Kula", "Salihli", "Sarıgöl", "Saruhanlı", "Selendi", "Soma", "Şehzadeler", "Turgutlu", "Yunusemre"],
    "Kahramanmaraş": ["Afşin", "Andırın", "Çağlayancerit", "Dulkadiroğlu", "Ekinözü", "Elbistan", "Göksun", "Nurhak", "Onikişubat", "Pazarcık", "Türkoğlu"],
    "Mardin": ["Artuklu", "Dargeçit", "Derik", "Kızıltepe", "Mazıdağı", "Midyat", "Nusaybin", "Ömerli", "Savur", "Yeşilli"],
    "Muğla": ["Bodrum", "Dalaman", "Datça", "Fethiye", "Kavaklıdere", "Köyceğiz", "Marmaris", "Menteşe", "Milas", "Ortaca", "Seydikemer", "Ula", "Yatağan"],
    "Muş": ["Bulanık", "Hasköy", "Korkut", "Malazgirt", "Merkez", "Varto"],
    "Nevşehir": ["Acıgöl", "Avanos", "Derinkuyu", "Gülşehir", "Hacıbektaş", "Kozaklı", "Merkez", "Ürgüp"],
    "Niğde": ["Altunhisar", "Bor", "Çamardı", "Çiftlik", "Merkez", "Ulukışla"],
    "Ordu": ["Akkuş", "Altınordu", "Aybastı", "Çamaş", "Çatalpınar", "Çaybaşı", "Fatsa", "Gölköy", "Gülyalı", "Gürgentepe", "İkizce", "Kabadüz", "Kabataş", "Korgan", "Kumru", "Mesudiye", "Perşembe", "Ulubey", "Ünye"],
    "Rize": ["Ardeşen", "Çamlıhemşin", "Çayeli", "Derepazarı", "Fındıklı", "Güneysu", "Hemşin", "İkizdere", "İyidere", "Kalkandere", "Merkez", "Pazar"],
    "Sakarya": ["Adapazarı", "Akyazı", "Arifiye", "Erenler", "Ferizli", "Geyve", "Hendek", "Karapürçek", "Karasu", "Kaynarca", "Kocaali", "Pamukova", "Sapanca", "Serdivan", "Söğütlü", "Taraklı"],
    "Samsun": ["19 Mayıs", "Alaçam", "Asarcık", "Atakum", "Ayvacık", "Bafra", "Canik", "Çarşamba", "Havza", "İlkadım", "Kavak", "Ladik", "Salıpazarı", "Tekkeköy", "Terme", "Vezirköprü", "Yakakent"],
    "Siirt": ["Baykan", "Eruh", "Kurtalan", "Merkez", "Pervari", "Şirvan", "Tillo"],
    "Sinop": ["Ayancık", "Boyabat", "Dikmen", "Durağan", "Erfelek", "Gerze", "Merkez", "Saraydüzü", "Türkeli"],
    "Sivas": ["Akıncılar", "Altınyayla", "Divriği", "Doğanşar", "Gemerek", "Gölova", "Hafik", "İmranlı", "Kangal", "Koyulhisar", "Merkez", "Suşehri", "Şarkışla", "Ulaş", "Yıldızeli", "Zara", "Gürün"],
    "Tekirdağ": ["Çerkezköy", "Çorlu", "Ergene", "Hayrabolu", "Kapaklı", "Malkara", "Muratlı", "Saray", "Süleymanpaşa", "Şarköy", "Marmaraereğlisi"],
    "Tokat": ["Almus", "Artova", "Başçiftlik", "Erbaa", "Merkez", "Niksar", "Pazar", "Reşadiye", "Sulusaray", "Turhal", "Yeşilyurt", "Zile"],
    "Trabzon": ["Akçaabat", "Araklı", "Arsin", "Beşikdüzü", "Çarşıbaşı", "Çaykara", "Dernekpazarı", "Düzköy", "Hayrat", "Köprübaşı", "Maçka", "Of", "Ortahisar", "Sürmene", "Şalpazarı", "Tonya", "Vakfıkebir", "Yomra"],
    "Tunceli": ["Çemişgezek", "Hozat", "Mazgirt", "Merkez", "Nazımiye", "Ovacık", "Pertek", "Pülümür"],
    "Şanlıurfa": ["Akçakale", "Birecik", "Bozova", "Ceylanpınar", "Eyyübiye", "Halfeti", "Haliliye", "Harran", "Hilvan", "Karaköprü", "Siverek", "Suruç", "Viranşehir"],
    "Uşak": ["Banaz", "Eşme", "Karahallı", "Merkez", "Sivaslı", "Ulubey"],
    "Van": ["Bahçesaray", "Başkale", "Çaldıran", "Çatak", "Edremit", "Erciş", "Gevaş", "Gürpınar", "İpekyolu", "Muradiye", "Özalp", "Saray", "Tuşba"],
    "Yozgat": ["Akdağmadeni", "Aydıncık", "Boğazlıyan", "Çandır", "Çayıralan", "Çekerek", "Kadışehri", "Merkez", "Saraykent", "Sarıkaya", "Sorgun", "Şefaatli", "Yenifakılı", "Yerköy"],
    "Zonguldak": ["Alaplı", "Çaycuma", "Devrek", "Ereğli", "Gökçebey", "Kilimli", "Kozlu", "Merkez"],
    "Aksaray": ["Ağaçören", "Eskil", "Gülağaç", "Güzelyurt", "Merkez", "Ortaköy", "Sarıyahşi", "Sultanhanı"],
    "Bayburt": ["Aydıntepe", "Demirözü", "Merkez"],
    "Karaman": ["Ayrancı", "Başyayla", "Ermenek", "Kazımkarabekir", "Merkez", "Sarıveliler"],
    "Kırıkkale": ["Bahşılı", "Balışeyh", "Çelebi", "Delice", "Karakeçili", "Keskin", "Merkez", "Sulakyurt", "Yahşihan"],
    "Batman": ["Beşiri", "Gercüş", "Hasankeyf", "Kozluk", "Merkez", "Sason"],
    "Şırnak": ["Beytüşşebap", "Cizre", "Güçlükonak", "İdil", "Merkez", "Silopi", "Uludere"],
    "Bartın": ["Amasra", "Kurucaşile", "Merkez", "Ulus"],
    "Ardahan": ["Çıldır", "Damal", "Göle", "Hanak", "Merkez", "Posof"],
    "Iğdır": ["Aralık", "Karakoyunlu", "Merkez", "Tuzluca"],
    "Yalova": ["Altınova", "Armutlu", "Çınarcık", "Çiftlikköy", "Merkez", "Termal"],
    "Karabük": ["Eflani", "Eskipazar", "Merkez", "Ovacık", "Safranbolu", "Yenice"],
    "Kilis": ["Elbeyli", "Merkez", "Musabeyli", "Polateli"],
    "Osmaniye": ["Bahçe", "Düziçi", "Hasanbeyli", "Kadirli", "Merkez", "Sumbas", "Toprakkale"],
    "Düzce": ["Akçakoca", "Cumayeri", "Çilimli", "Gölyaka", "Gümüşova", "Kaynaşlı", "Merkez", "Yığılca"]
};

// Fill city select field
function fillCitySelect() {
    const citySelect = document.getElementById('id_city');
    if (citySelect && citySelect.options.length <= 1) { // Only fill if there's only one option
        citySelect.innerHTML = '<option value="">Şehir seçiniz</option>';
        window.turkishCities.forEach(function(city) {
            const option = document.createElement('option');
            option.value = city;
            option.text = city;
            // Select correct city if editing
            if (window.selectedCity && city === window.selectedCity && window.turkishCities.indexOf(window.selectedCity) !== -1) option.selected = true;
            citySelect.appendChild(option);
        });
        // Add "Other" option
        const otherOption = document.createElement('option');
        otherOption.value = 'Diğer';
        otherOption.text = 'Diğer';
        // Eğer kayıtlı şehir Türk şehirleri listesinde yoksa 'Diğer' seçili olsun
        if (window.selectedCity && window.turkishCities.indexOf(window.selectedCity) === -1) otherOption.selected = true;
        citySelect.appendChild(otherOption);
    }
}

function updateDistricts() {
    const citySelect = document.getElementById('id_city');
    const districtSelect = document.getElementById('id_district');
    const districtField = document.getElementById('field-district');
    const selectedCity = citySelect.value;
    
    // Show/hide district field based on city selection
    if (selectedCity && selectedCity !== '') {
        districtField.style.display = 'block';
        
        if (selectedCity === 'Diğer') {
            // Show custom city input field and convert district to text input
            showCustomCityInput();
            convertDistrictToTextInput();
        } else {
            // Hide custom city input and convert district back to select dropdown
            hideCustomCityInput();
            convertDistrictToSelect();
            districtSelect.innerHTML = '<option value="">İlçe seçiniz</option>';
            if (window.cityDistricts[selectedCity]) {
                window.cityDistricts[selectedCity].forEach(function(district) {
                    const option = document.createElement('option');
                    option.value = district;
                    option.text = district;
                    // Select correct district if editing
                    if ((window.selectedDistrict && district === window.selectedDistrict) || district === districtSelect.getAttribute('data-selected')) option.selected = true;
                    districtSelect.appendChild(option);
                });
            }
        }
    } else {
        districtField.style.display = 'none';
        hideCustomCityInput();
        districtSelect.innerHTML = '<option value="">İlçe seçiniz</option>';
    }
}

function convertDistrictToTextInput() {
    const districtField = document.getElementById('field-district');
    const districtSelect = document.getElementById('id_district');
    
    if (districtField && districtSelect && districtSelect.tagName === 'SELECT') {
        // Create text input
        const textInput = document.createElement('input');
        textInput.type = 'text';
        textInput.name = 'district';
        textInput.id = 'id_district';
        textInput.className = 'form-control';
        textInput.placeholder = 'İlçe adını giriniz';
        // Düzenleme ekranında ilçe varsa ve None değilse otomatik doldur
        if (window.selectedDistrict && window.selectedDistrict !== 'None') {
            textInput.value = window.selectedDistrict;
        }
        // Replace select with text input
        districtSelect.parentNode.replaceChild(textInput, districtSelect);
    }
}

function convertDistrictToSelect() {
    const districtField = document.getElementById('field-district');
    const districtInput = document.getElementById('id_district');
    
    if (districtField && districtInput && districtInput.tagName === 'INPUT') {
        // Create select dropdown
        const selectInput = document.createElement('select');
        selectInput.name = 'district';
        selectInput.id = 'id_district';
        selectInput.className = 'form-select';
        
        // Replace text input with select
        districtInput.parentNode.replaceChild(selectInput, districtInput);
    }
}

function showCustomCityInput() {
    const cityField = document.getElementById('field-city');
    const existingCustomInput = document.getElementById('custom-city-input');
    
    if (cityField && !existingCustomInput) {
        // Create custom city input field
        const customInputDiv = document.createElement('div');
        customInputDiv.className = 'mb-3';
        customInputDiv.id = 'custom-city-input';
        
        const label = document.createElement('label');
        label.htmlFor = 'custom_city_name';
        label.className = 'form-label';
        label.textContent = 'İl:';
        
        const input = document.createElement('input');
        input.type = 'text';
        input.name = 'custom_city_name';
        input.id = 'custom_city_name';
        input.className = 'form-control';
        input.placeholder = 'İl adı giriniz';
        // Eğer şehir Türk şehirleri listesinde yoksa ve None değilse otomatik doldur
        if (window.selectedCity && window.turkishCities.indexOf(window.selectedCity) === -1 && window.selectedCity !== 'None') {
            input.value = window.selectedCity;
        }
        
        customInputDiv.appendChild(label);
        customInputDiv.appendChild(input);
        
        // Insert after the city field
        cityField.parentNode.insertBefore(customInputDiv, cityField.nextSibling);
    }
}

function hideCustomCityInput() {
    const customInput = document.getElementById('custom-city-input');
    if (customInput) {
        customInput.remove();
    }
}

// --- users/login.html ---
// Giriş sayfası şifre göster/gizle fonksiyonu
window.togglePassword = function() {
  const passwordInput = document.getElementById('password');
  const passwordIcon = document.getElementById('passwordIcon');
  if (passwordInput.type === 'password') {
    passwordInput.type = 'text';
    passwordIcon.classList.remove('bi-eye');
    passwordIcon.classList.add('bi-eye-slash');
  } else {
    passwordInput.type = 'password';
    passwordIcon.classList.remove('bi-eye-slash');
    passwordIcon.classList.add('bi-eye');
  }
};

// --- users/admin_hotel_list.html & pages/gf_hotels.html ---
window.fillHotelCityFilter = function(selectedCity) {
  const citySelect = document.getElementById('hotel-filter-city');
  if (citySelect) {
    citySelect.innerHTML = '<option value="">Tüm Şehirler</option>';
    if (window.turkishCities) {
      window.turkishCities.forEach(function(city) {
        const option = document.createElement('option');
        option.value = city;
        option.text = city;
        if (city === selectedCity) option.selected = true;
        citySelect.appendChild(option);
      });
    }
  }
};
window.fillHotelDistrictFilter = function(selectedDistrict) {
  const citySelect = document.getElementById('hotel-filter-city');
  const districtSelect = document.getElementById('hotel-filter-district');
  districtSelect.innerHTML = '<option value="">Tüm İlçeler</option>';
  if (citySelect && citySelect.value && window.cityDistricts && window.cityDistricts[citySelect.value]) {
    window.cityDistricts[citySelect.value].forEach(function(district) {
      const option = document.createElement('option');
      option.value = district;
      option.text = district;
      if (district === selectedDistrict) option.selected = true;
      districtSelect.appendChild(option);
    });
  }
};
window.showHotelDetails = function(name, city, district, contact, website) {
  document.getElementById('hotelName').textContent = name;
  document.getElementById('hotelLocation').textContent = city + (district ? ' / ' + district : '');
  document.getElementById('hotelContact').textContent = contact || 'Bilgi yok';
  if (website) {
    document.getElementById('hotelWebsite').innerHTML = `<a href="${website}" target="_blank">${website}</a>`;
  } else {
    document.getElementById('hotelWebsite').textContent = 'Bilgi yok';
  }
  const modal = new bootstrap.Modal(document.getElementById('hotelDetailModal'));
  modal.show();
};

// --- pages/gf_places.html & users/admin_venue_list.html ---
window.fillVenueCityFilter = function(selectedCity) {
  const citySelect = document.getElementById('venue-filter-city');
  if (citySelect) {
    citySelect.innerHTML = '<option value="">Tüm Şehirler</option>';
    if (window.turkishCities) {
      window.turkishCities.forEach(function(city) {
        const option = document.createElement('option');
        option.value = city;
        option.text = city;
        if (city === selectedCity) option.selected = true;
        citySelect.appendChild(option);
      });
    }
  }
};
window.fillVenueDistrictFilter = function(selectedDistrict) {
  const citySelect = document.getElementById('venue-filter-city');
  const districtSelect = document.getElementById('venue-filter-district');
  districtSelect.innerHTML = '<option value="">Tüm İlçeler</option>';
  if (citySelect && citySelect.value && window.cityDistricts && window.cityDistricts[citySelect.value]) {
    window.cityDistricts[citySelect.value].forEach(function(district) {
      const option = document.createElement('option');
      option.value = district;
      option.text = district;
      if (district === selectedDistrict) option.selected = true;
      districtSelect.appendChild(option);
    });
  }
};
window.showVenueDetails = function(name, city, district, products) {
  document.getElementById('venueName').textContent = name;
  document.getElementById('venueLocation').textContent = city + (district ? ' / ' + district : '');
  document.getElementById('venueProducts').textContent = products || 'Bilgi yok';
  const modal = new bootstrap.Modal(document.getElementById('venueDetailModal'));
  modal.show();
};

// --- pages/gf_recipes.html ---
window.showRecipeDetails = function(name, description, ingredients, instructions) {
  document.getElementById('recipeName').textContent = name;
  document.getElementById('recipeDescription').textContent = description || 'Açıklama yok';
  document.getElementById('recipeIngredients').textContent = ingredients || 'Malzeme listesi yok';
  document.getElementById('recipeInstructions').textContent = instructions || 'Hazırlanış talimatı yok';
  const modal = new bootstrap.Modal(document.getElementById('recipeDetailModal'));
  modal.show();
};

// --- pages/gf_food.html ---
// Dinamik filtreleme için fonksiyonlar
window.updateFoodFilters = function(changed) {
  const brandSelect = document.getElementById('food-brand-filter');
  const categorySelect = document.getElementById('food-category-filter');
  if (!brandSelect || !categorySelect) return;

  if (changed === 'brand') {
    const prevCategory = categorySelect.value;
    const brandId = brandSelect.value;
    if (!brandId) return;
    fetch(`/glutensiz/gida/filter-options/?brand=${brandId}`)
      .then(response => response.json())
      .then(data => {
        if (data.categories) {
          categorySelect.innerHTML = '<option value="">Tüm Kategoriler</option>';
          let found = false;
          data.categories.forEach(category => {
            const option = document.createElement('option');
            option.value = category.id;
            option.textContent = category.name;
            if (prevCategory && prevCategory == category.id.toString()) {
              option.selected = true;
              found = true;
            }
            categorySelect.appendChild(option);
          });
          if (!found) categorySelect.value = '';
        }
      });
  } else if (changed === 'category') {
    const prevBrand = brandSelect.value;
    const categoryId = categorySelect.value;
    if (!categoryId) return;
    fetch(`/glutensiz/gida/filter-options/?category=${categoryId}`)
      .then(response => response.json())
      .then(data => {
        if (data.brands) {
          brandSelect.innerHTML = '<option value="">Tüm Markalar</option>';
          let found = false;
          data.brands.forEach(brand => {
            const option = document.createElement('option');
            option.value = brand.id;
            option.textContent = brand.name;
            if (prevBrand && prevBrand == brand.id.toString()) {
              option.selected = true;
              found = true;
            }
            brandSelect.appendChild(option);
          });
          if (!found) brandSelect.value = '';
        }
      });
  }
};

// --- users/admin_hotel_form.html, users/admin_venue_form.html ---
// Bu değişkenler template'ten window'a atanmalı. Template'te:
// <script>window.selectedCity = "{{ form.instance.city|escapejs }}"; ...</script>
// yerine, ilgili view'da context'e ekleyip burada window'a atayabilirsiniz.
// Alternatif: Template'te <body> tag'ına data-selected-city gibi attribute ekleyip burada okuyabilirsiniz.
// Şimdilik window.selectedCity, window.selectedDistrict, window.selectedCustomCity'nin atanmasını burada bırakıyoruz.

// --- partials/_forms.html ---
// Marka ve kategori ekleme, select2 başlatma, şehir-ilçe alanı kontrolü
window.toggleDistrictField = function() {
  const citySelect = document.getElementById('id_city');
  const districtField = document.getElementById('field-district');
  if (citySelect && districtField) {
    if (citySelect.value && citySelect.value !== '') {
      districtField.style.display = 'block';
      if (citySelect.value === 'Diğer') {
        window.showCustomCityInput();
        window.convertDistrictToTextInput();
      } else {
        window.hideCustomCityInput();
        window.convertDistrictToSelect();
      }
    } else {
      districtField.style.display = 'none';
      window.hideCustomCityInput();
      const districtSelect = document.getElementById('id_district');
      if (districtSelect) {
        districtSelect.value = '';
      }
    }
  }
};
window.showCustomCityInput = function() {
  const cityField = document.getElementById('field-city');
  const existingCustomInput = document.getElementById('custom-city-input');
  if (cityField && !existingCustomInput) {
    const customInputDiv = document.createElement('div');
    customInputDiv.className = 'mb-3';
    customInputDiv.id = 'custom-city-input';
    const label = document.createElement('label');
    label.htmlFor = 'custom_city_name';
    label.className = 'form-label';
    label.textContent = 'İl Adı';
    const input = document.createElement('input');
    input.type = 'text';
    input.name = 'custom_city_name';
    input.id = 'custom_city_name';
    input.className = 'form-control';
    input.placeholder = 'Özel şehir adını giriniz';
    customInputDiv.appendChild(label);
    customInputDiv.appendChild(input);
    cityField.parentNode.insertBefore(customInputDiv, cityField.nextSibling);
  }
};
window.hideCustomCityInput = function() {
  const customInput = document.getElementById('custom-city-input');
  if (customInput) {
    customInput.remove();
  }
};
window.convertDistrictToTextInput = function() {
  const districtField = document.getElementById('field-district');
  const districtSelect = document.getElementById('id_district');
  if (districtField && districtSelect && districtSelect.tagName === 'SELECT') {
    const textInput = document.createElement('input');
    textInput.type = 'text';
    textInput.name = 'district';
    textInput.id = 'id_district';
    textInput.className = 'form-control';
    textInput.placeholder = 'İlçe adını giriniz';
    districtSelect.parentNode.replaceChild(textInput, districtSelect);
  }
};
window.convertDistrictToSelect = function() {
  const districtField = document.getElementById('field-district');
  const districtInput = document.getElementById('id_district');
  if (districtField && districtInput && districtInput.tagName === 'INPUT') {
    const selectInput = document.createElement('select');
    selectInput.name = 'district';
    selectInput.id = 'id_district';
    selectInput.className = 'form-select';
    districtInput.parentNode.replaceChild(selectInput, districtInput);
  }
};
window.initSelect2 = function() {
  if (window.jQuery && $("#id_brand").length) {
    $("#id_brand").select2({
      width: '100%',
      placeholder: 'Marka seçin',
      allowClear: true,
      language: 'tr'
    });
  }
  if (window.jQuery && $("#id_category").length) {
    $("#id_category").select2({
      width: '100%',
      placeholder: 'Kategori seçin',
      allowClear: true,
      language: 'tr'
    });
  }
};
document.addEventListener('DOMContentLoaded', function() {
  window.initSelect2 && window.initSelect2();
  window.toggleDistrictField && window.toggleDistrictField();
  const citySelect = document.getElementById('id_city');
  if (citySelect && window.toggleDistrictField) {
    citySelect.addEventListener('change', window.toggleDistrictField);
  }
  // Modal kapandığında select2 tekrar başlat
  const brandModal = document.getElementById('addBrandModal');
  if (brandModal) {
    brandModal.addEventListener('hidden.bs.modal', function () {
      window.initSelect2();
    });
  }
  const categoryModal = document.getElementById('addCategoryModal');
  if (categoryModal) {
    categoryModal.addEventListener('hidden.bs.modal', function () {
      window.initSelect2();
    });
  }
});
// Marka ekle
window.addBrandFormHandler = function(brandUrl) {
  const form = document.getElementById('addBrandForm');
  if (form) {
    form.onsubmit = function(e) {
      e.preventDefault();
      var name = document.getElementById('brandName').value;
      fetch(brandUrl, {
        method: 'POST',
        headers: {
          'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'name=' + encodeURIComponent(name)
      })
      .then(response => response.json())
      .then(data => {
        if(data.success) {
          var select = document.getElementById('id_brand');
          var option = document.createElement('option');
          option.value = data.id;
          option.text = data.name;
          option.selected = true;
          select.appendChild(option);
          document.getElementById('brandAddMsg').textContent = 'Marka eklendi!';
          document.getElementById('brandName').value = '';
          setTimeout(() => {
            document.getElementById('brandAddMsg').textContent = '';
            var modal = bootstrap.Modal.getInstance(document.getElementById('addBrandModal'));
            modal.hide();
          }, 800);
        } else {
          document.getElementById('brandAddMsg').textContent = data.error || 'Hata oluştu.';
        }
      });
    };
  }
};
// Kategori ekle
window.addCategoryFormHandler = function(categoryUrl) {
  const form = document.getElementById('addCategoryForm');
  if (form) {
    form.onsubmit = function(e) {
      e.preventDefault();
      var name = document.getElementById('categoryName').value;
      fetch(categoryUrl, {
        method: 'POST',
        headers: {
          'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value,
          'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'name=' + encodeURIComponent(name)
      })
      .then(response => response.json())
      .then(data => {
        if(data.success) {
          var select = document.getElementById('id_category');
          var option = document.createElement('option');
          option.value = data.id;
          option.text = data.name;
          option.selected = true;
          select.appendChild(option);
          document.getElementById('categoryAddMsg').textContent = 'Kategori eklendi!';
          document.getElementById('categoryName').value = '';
          setTimeout(() => {
            document.getElementById('categoryAddMsg').textContent = '';
            var modal = bootstrap.Modal.getInstance(document.getElementById('addCategoryModal'));
            modal.hide();
          }, 800);
        } else {
          document.getElementById('categoryAddMsg').textContent = data.error || 'Hata oluştu.';
        }
      });
    };
  }
};
