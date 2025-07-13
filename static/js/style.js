// --- YENİ: Marka ve kategori ekleme formları için submit eventini sadece bir kez ekle ---
document.addEventListener('DOMContentLoaded', function() {
  // --- Kategori Modalı ---
  var categoryModal = document.getElementById('addCategoryModal');
  var categoryForm = document.getElementById('addCategoryForm');
  let categoryHandler = null;
  if (categoryModal && categoryForm) {
    categoryModal.addEventListener('shown.bs.modal', function () {
      // Formu temizle
      categoryForm.reset();
      const submitBtn = categoryForm.querySelector('button[type="submit"]');
      if (submitBtn) submitBtn.disabled = false;
      
      if (!categoryHandler) {
        categoryHandler = function(e) {
          e.preventDefault();
          const submitBtn = categoryForm.querySelector('button[type="submit"]');
          if (submitBtn) submitBtn.disabled = true;
          const formData = new FormData(categoryForm);
          fetch('/users/ajax/add-category/', {
            method: 'POST',
            body: formData,
            headers: {
              'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            }
          })
          .then(response => response.json())
          .then(data => {
            if (data.status === 'success' || data.success === true) {
              var categorySelect = $('#id_category');
              var currentVal = categorySelect.val();
              // Yeni kategoriyi select'e ekle
              if (categorySelect.find('option[value="'+data.id+'"]').length === 0) {
                categorySelect.append(new Option(data.name, data.id));
              }
              // Yeni eklenen kategoriyi seç
              categorySelect.val(data.id).trigger('change');
              const categoryAddMsg = document.getElementById('categoryAddMsg');
              categoryAddMsg.textContent = 'Kategori başarıyla eklendi.';
              const modal = bootstrap.Modal.getInstance(categoryModal);
              if (modal) modal.hide();
              setTimeout(() => {
                categoryAddMsg.textContent = '';
              }, 2000);
            } else {
              if (submitBtn) submitBtn.disabled = false;
            }
          }).catch(() => {
            if (submitBtn) submitBtn.disabled = false;
          });
        };
        categoryForm.addEventListener('submit', categoryHandler);
      }
    });
    categoryModal.addEventListener('hidden.bs.modal', function () {
      if (categoryHandler) {
        categoryForm.removeEventListener('submit', categoryHandler);
        categoryHandler = null;
      }
      const submitBtn = categoryForm.querySelector('button[type="submit"]');
      if (submitBtn) submitBtn.disabled = false;
    });
  }

  // --- Marka Modalı ---
  var brandModal = document.getElementById('addBrandModal');
  var brandForm = document.getElementById('addBrandForm');
  let brandHandler = null;
  if (brandModal && brandForm) {
    brandModal.addEventListener('shown.bs.modal', function () {
      // Formu temizle
      brandForm.reset();
      const submitBtn = brandForm.querySelector('button[type="submit"]');
      if (submitBtn) submitBtn.disabled = false;
      
      if (!brandHandler) {
        brandHandler = function(e) {
          e.preventDefault();
          const submitBtn = brandForm.querySelector('button[type="submit"]');
          if (submitBtn) submitBtn.disabled = true;
          const formData = new FormData(brandForm);
          // Medicine formunda doğru endpointi kullan
          let endpoint = '/users/ajax/add-brand/';
          if (window.location.pathname.includes('/medicines/')) {
            endpoint = '/users/ajax/add-medicine-brand/';
          }
          fetch(endpoint, {
            method: 'POST',
            body: formData,
            headers: {
              'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
            }
          })
      .then(response => response.json())
      .then(data => {
            if (data.status === 'success' || data.success === true) {
              var $brandSelect = $('#id_brand');
              var oldVal = $brandSelect.val();
              if ($brandSelect.find('option[value="'+data.id+'"]').length === 0) {
                $brandSelect.append(new Option(data.name, data.id));
              }
              if (oldVal) {
                $brandSelect.val(oldVal).trigger('change');
              }
              $brandSelect.val(data.id).trigger('change');
              const brandAddMsg = document.getElementById('brandAddMsg');
              brandAddMsg.textContent = 'Marka başarıyla eklendi.';
              const modal = bootstrap.Modal.getInstance(brandModal);
              if (modal) modal.hide();
              setTimeout(() => {
                brandAddMsg.textContent = '';
              }, 2000);
            } else {
              if (submitBtn) submitBtn.disabled = false;
            }
          }).catch(() => {
            if (submitBtn) submitBtn.disabled = false;
          });
        };
        brandForm.addEventListener('submit', brandHandler);
      }
    });
    brandModal.addEventListener('hidden.bs.modal', function () {
      if (brandHandler) {
        brandForm.removeEventListener('submit', brandHandler);
        brandHandler = null;
      }
      const submitBtn = brandForm.querySelector('button[type="submit"]');
      if (submitBtn) submitBtn.disabled = false;
    });
  }

  // Kategori ve marka alanlarında select2 başlat
  if (window.jQuery) {
    // Kategori select2
    if ($('#id_category').length) {
      $('#id_category').select2({
        width: '100%',
        placeholder: 'Kategori seçin',
        allowClear: true,
        language: 'tr',
        theme: 'default',
        minimumResultsForSearch: 0
      });
    }
    // Marka select2
    if ($('#id_brand').length) {
      $('#id_brand').select2({
        width: '100%',
        placeholder: 'Marka seçin',
        allowClear: true,
        language: 'tr',
        theme: 'default',
        minimumResultsForSearch: 0
      });
    }
  }

  // --- Dinamik Şehir-İlçe Dropdown Kodu (GÜNCELLENMİŞ HALİ) ---

  // Form elemanlarını yakala
  const citySelect = document.getElementById('id_city');
  const districtSelect = document.getElementById('id_district');
  const cityOtherInput = document.getElementById('id_city_other');
  const districtOtherInput = document.getElementById('id_district_other');

  console.log('Elements found:');
  console.log('citySelect:', citySelect);
  console.log('districtSelect:', districtSelect);
  console.log('cityOtherInput:', cityOtherInput);
  console.log('districtOtherInput:', districtOtherInput);

  // Elementlerin etrafındaki sarmalayıcı div'leri yakala (Django'nun form yapısına göre)
  const districtSelectWrapper = document.getElementById('field-district');
  const cityOtherWrapper = document.getElementById('field-city_other');
  const districtOtherWrapper = document.getElementById('field-district_other');
  
  console.log('Wrapper elements found:');
  console.log('districtSelectWrapper:', districtSelectWrapper);
  console.log('cityOtherWrapper:', cityOtherWrapper);
  console.log('districtOtherWrapper:', districtOtherWrapper);

  // Fonksiyon: Manuel giriş alanlarının görünürlüğünü ayarlar
  function toggleManualInputs(show) {
      if (show) {
          // "Diğer" seçildiğinde:
          if (districtSelectWrapper) districtSelectWrapper.style.display = 'none'; // İlçe dropdown'ını gizle
          if (cityOtherWrapper) cityOtherWrapper.style.display = 'block'; // Manuel şehir input'unu göster
          if (districtOtherWrapper) districtOtherWrapper.style.display = 'block'; // Manuel ilçe input'unu göster
          if (cityOtherInput) cityOtherInput.required = true; // Manuel şehir alanını zorunlu yap
          if (districtOtherInput) districtOtherInput.required = true; // Manuel ilçe alanını zorunlu yap
          if (districtSelect) districtSelect.required = false; // Dropdown ilçe alanını zorunlu yapma
      } else {
          // "Diğer" dışında bir şehir seçildiğinde:
          if (cityOtherWrapper) cityOtherWrapper.style.display = 'none'; // Manuel şehir input'unu gizle
          if (districtOtherWrapper) districtOtherWrapper.style.display = 'none'; // Manuel ilçe input'unu gizle
          if (cityOtherInput) cityOtherInput.required = false; // Manuel şehir alanını zorunlu yapma
          if (districtOtherInput) districtOtherInput.required = false; // Manuel ilçe alanını zorunlu yapma
          if (districtSelect) districtSelect.required = true; // Dropdown ilçe alanını zorunlu yap
          if (cityOtherInput) cityOtherInput.value = ''; // Alanları temizle
          if (districtOtherInput) districtOtherInput.value = ''; // Alanları temizle
      }
  }

  // Fonksiyon: Sunucudan ilçeleri çeker ve dropdown'ı günceller
  function updateDistricts(city, selectedDistrict = null) {
      if (city && city !== 'Diğer') {
          const url = `/users/ajax/get-districts/?city=${encodeURIComponent(city)}`;
          fetch(url)
              .then(response => response.json())
              .then(data => {
                  if (districtSelectWrapper) districtSelectWrapper.style.display = 'block';
                  districtSelect.innerHTML = '<option value="">İlçe seçiniz</option>';
                  if (data.districts && data.districts.length > 0) {
                      data.districts.forEach(function(district) {
                          const option = new Option(district, district);
                          districtSelect.add(option);
                      });
                      
                      // Eğer selectedDistrict belirtilmişse ve listede varsa, onu seç
                      if (selectedDistrict && data.districts.includes(selectedDistrict)) {
                          districtSelect.value = selectedDistrict;
                      }
                  }
              });
      } else {
           if (districtSelectWrapper) districtSelectWrapper.style.display = 'none';
      }
  }

  // Sayfa ilk yüklendiğinde durumu kontrol et
  if (citySelect) {
      const initialCity = citySelect.value;
      const initialDistrict = districtSelect ? districtSelect.value : null;
      
      console.log('Initial city:', initialCity);
      console.log('Initial district:', initialDistrict);
      
      if (initialCity === 'Diğer') {
          console.log('City is "Diğer", showing manual inputs');
          toggleManualInputs(true);
          updateDistricts(null);
      } else {
          console.log('City is not "Diğer", showing district dropdown');
          toggleManualInputs(false);
          updateDistricts(initialCity, initialDistrict);
      }
      
      // Sayfa yüklendiğinde ilçe alanının zorunlu olup olmadığını ayarla
      if (initialCity && initialCity !== 'Diğer') {
          if (districtSelect) districtSelect.required = true;
      }

      // Şehir seçimi değiştiğinde olay dinleyici
      citySelect.addEventListener('change', function() {
          const selectedCity = this.value;
          if (selectedCity === 'Diğer') {
              toggleManualInputs(true);
              updateDistricts(null);
          } else {
              toggleManualInputs(false);
              updateDistricts(selectedCity, null); // Yeni şehir seçildiğinde ilçe seçimini sıfırla
          }
      });
  }
});

function setupCityDistrictFilters(citySelectId, districtSelectId, cities, districts, initialCity, initialDistrict) {
    const citySelect = document.getElementById(citySelectId);
    const districtSelect = document.getElementById(districtSelectId);

    if (!citySelect || !districtSelect) return;

    // Populate cities
    cities.forEach(city => {
        const option = new Option(city[1], city[0]);
        citySelect.add(option);
    });

    // Set initial city
    if (initialCity) {
        citySelect.value = initialCity;
    }

    // Populate districts based on city
    function updateDistricts() {
        const selectedCity = citySelect.value;
        districtSelect.innerHTML = '<option value="">Tüm İlçeler</option>';

        if (selectedCity && districts[selectedCity] && selectedCity !== 'Diğer') {
            // Şehir seçili - ilçe dropdown'ını etkinleştir
            districtSelect.disabled = false;
            districtSelect.style.opacity = '1';
            districtSelect.style.cursor = 'pointer';
            
            districts[selectedCity].forEach(district => {
                const option = new Option(district, district);
                districtSelect.add(option);
            });
        } else {
            // Şehir seçili değil - ilçe dropdown'ını devre dışı bırak
            districtSelect.disabled = true;
            districtSelect.style.opacity = '0.5';
            districtSelect.style.cursor = 'not-allowed';
        }

        // Set initial district
        if (selectedCity === initialCity && initialDistrict) {
            districtSelect.value = initialDistrict;
        }
    }

    // Initial population
    updateDistricts();

    // Event listener
    citySelect.addEventListener('change', updateDistricts);
}
