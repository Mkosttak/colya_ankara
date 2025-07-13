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
});