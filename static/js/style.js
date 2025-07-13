// --- YENİ: Marka ve kategori ekleme formları için submit eventini sadece bir kez ekle ---
document.addEventListener('DOMContentLoaded', function() {
  // --- Kategori Modalı ---
  var categoryModal = document.getElementById('addCategoryModal');
  var categoryForm = document.getElementById('addCategoryForm');
  let categoryHandler = null;
  if (categoryModal && categoryForm) {
    categoryModal.addEventListener('shown.bs.modal', function () {
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
              var selects = $('#category-fields select');
              var selectedVals = selects.map(function(){ return $(this).val(); }).get();
              // Tüm selectlere yeni option'ı ekle
              selects.each(function(){
                if ($(this).find('option[value="'+data.id+'"]').length === 0) {
                  $(this).append(new Option(data.name, data.id));
                }
              });
              // Seçili değerleri tekrar ata
              selects.each(function(i){
                if (i < selectedVals.length && selectedVals[i]) {
                  $(this).val(selectedVals[i]).trigger('change');
                }
              });
              // Son selectte yeni eklenen kategori seçili olsun
              $(selects[selects.length-1]).val(data.id).trigger('change');
              const categoryAddMsg = document.getElementById('categoryAddMsg');
              categoryAddMsg.textContent = 'Kategori başarıyla eklendi.';
              const modal = bootstrap.Modal.getInstance(categoryModal);
              if (modal) modal.hide();
              setTimeout(() => {
                categoryAddMsg.textContent = '';
                window.location.reload();
              }, 400);
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
                window.location.reload();
              }, 400);
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
    // Dinamik kategori alanları
    function initCategorySelect2(select) {
      $(select).select2({
        width: '100%',
        placeholder: 'Kategori seçin',
        allowClear: false,
        language: 'tr',
        theme: 'default',
        minimumResultsForSearch: 0
      });
    }
    // İlk kategori select2'yi başlat
    if ($('#category-fields select').length) {
      initCategorySelect2($('#category-fields select').first());
    }
    // Dinamik kategori ekleme
    function addCategorySelect() {
      var count = $('#category-fields select').length;
      if (count >= 5) return;
      var $first = $('#category-fields select').first();
      var $row = $('<div class="category-select-row" style="display: flex; gap: 4px; align-items: stretch; margin-bottom: 4px;"></div>');
      var $select = $first.clone();
      $select.val('');
      $select.removeAttr('name');
      $select.attr('name', 'category_' + count);
      $select.attr('id', 'id_category_' + count);
      $row.append($('<div style="flex: 1; min-width: 0;"></div>').append($select));
      var $removeBtn = $('<button type="button" class="btn btn-outline-danger" title="Kaldır">&times;</button>');
      $removeBtn.on('click', function() {
        $row.remove();
        updateCategorySelects();
      });
      $row.append($removeBtn);
      $('#category-fields').append($row);
      initCategorySelect2($select);
      updateCategorySelects();
    }
    // Kategori seçiminde yeni select ekle
    $('#category-fields').on('change', 'select', function() {
      var count = $('#category-fields select').length;
      if ($(this).val() && count < 5 && $('#category-fields select').last()[0] === this) {
        addCategorySelect();
      }
      updateCategorySelects();
    });
    // Seçili kategorileri diğer selectlerde gizle
    function updateCategorySelects() {
      var selected = [];
      $('#category-fields select').each(function() {
        var val = $(this).val();
        if (val) selected.push(val);
      });
      $('#category-fields select').each(function() {
        var $sel = $(this);
        var currentVal = $sel.val();
        $sel.find('option').each(function() {
          var v = $(this).attr('value');
          if (v && selected.includes(v) && currentVal !== v) {
            $(this).prop('disabled', true).hide();
          } else {
            $(this).prop('disabled', false).show();
          }
        });
        // select2'yi güncelle
        $sel.trigger('change.select2');
      });
    }
    // İlk select2 başlatıldığında da güncelle
    updateCategorySelects();
    // Marka select2
    if ($('#id_brand').length) {
      $('#id_brand').select2({
        width: '100%',
        placeholder: 'Marka seçin',
        allowClear: false,
        language: 'tr',
        theme: 'default',
        minimumResultsForSearch: 0
      });
    }
  }

  // --- Dinamik Şehir-İlçe Dropdown Kodu ---

  // Formdaki şehir ve ilçe seçim alanlarını ID'leri ile yakalıyoruz
  const citySelect = document.getElementById('id_city');
  const districtSelect = document.getElementById('id_district');

  // Eğer bu iki element sayfada varsa, kodu çalıştır
  if (citySelect && districtSelect) {
      
      // Düzenleme sayfasında, form ilk yüklendiğinde ilçe alanının dolu gelmesi için
      // mevcut ilçe değerini bir değişkende saklayalım
      const initialSelectedDistrict = districtSelect.value;

      // İlçe dropdown'ının etrafındaki div'i bulalım (başlangıçta gizlemek/göstermek için)
      // Bu genellikle form elemanının parent'ının parent'ı olur. Yapınıza göre ayarlayınız.
      // Genellikle Django formları <p><label>...</label> <select>...</select></p> gibi bir yapı oluşturur.
      // Veya bir <div> içinde olabilirler. Tarayıcının "Inspect" aracıyla doğru elementi bulun.
      // Örnek olarak, ilçe select elementinin parent elementini hedef alıyoruz.
      const districtWrapper = districtSelect.parentElement;

      // Şehir seçimi değiştiğinde tetiklenecek fonksiyon
      citySelect.addEventListener('change', function() {
          const selectedCity = this.value;
          updateDistricts(selectedCity);
      });

      // Sayfa ilk yüklendiğinde mevcut şehir seçiliyse ilçeleri doldur
      if (citySelect.value) {
          updateDistricts(citySelect.value, initialSelectedDistrict);
      } else {
          // Şehir seçili değilse ilçe alanını gizle
          if(districtWrapper) districtWrapper.style.display = 'none';
      }

      // Sunucudan ilçe verilerini çeken ve dropdown'ı güncelleyen fonksiyon
      function updateDistricts(city, selectedDistrict = null) {
          if (city) {
              // AJAX isteği için hazırlanan URL
              const url = `/users/ajax/get-districts/?city=${encodeURIComponent(city)}`;
              
              fetch(url)
                  .then(response => response.json())
                  .then(data => {
                      // Önceki ilçe seçeneklerini temizle
                      districtSelect.innerHTML = '<option value="">İlçe seçiniz</option>';
                      
                      // İlçe verisi boş değilse
                      if (data.districts && data.districts.length > 0) {
                          // Yeni ilçe seçeneklerini ekle
                          data.districts.forEach(function(district) {
                              // value ve text değeri aynı olan bir option oluştur
                              const option = new Option(district, district);
                              districtSelect.add(option);
                          });

                          // Eğer önceden seçili bir ilçe varsa, onu tekrar seç
                          if (selectedDistrict) {
                              districtSelect.value = selectedDistrict;
                          }
                          
                          // İlçe alanını görünür yap
                          if(districtWrapper) districtWrapper.style.display = 'block';
                      } else {
                           // O şehre ait ilçe bulunamazsa ilçe alanını gizle
                           if(districtWrapper) districtWrapper.style.display = 'none';
                      }
                  })
                  .catch(error => {
                      console.error('İlçeler alınırken bir hata oluştu:', error);
                      // Hata durumunda da ilçe alanını gizle
                      if(districtWrapper) districtWrapper.style.display = 'none';
                  });
          } else {
              // Şehir seçilmemişse ilçe alanını gizle ve temizle
              districtSelect.innerHTML = '<option value="">İlçe seçiniz</option>';
              if(districtWrapper) districtWrapper.style.display = 'none';
          }
      }
  }
});