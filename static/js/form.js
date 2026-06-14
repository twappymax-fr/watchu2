
let currentStep = 1;
const TOTAL_STEPS = 4;
let prevEmpCount = 0

document.getElementById('registrationForm').addEventListener('keydown', function (e) {
    if (e.key === 'Enter' && e.target.tagName !== 'TEXTAREA') {
        e.preventDefault();
    }
});

// ── SLIDE-DOWN ANIMATION ──
function animatePanel(panel, direction) {
    // direction: 'forward' = slide down from top, 'back' = slide up from bottom
    panel.classList.remove('anim-in', 'anim-back');
    void panel.offsetWidth; // force reflow
    panel.classList.add(direction === 'forward' ? 'anim-in' : 'anim-back');
}

// ── STEP NAVIGATION ──
function updateProgress(step) {
    const labels = ['Contact Information', 'Education', 'Employment', 'Verification'];
    for (let i = 1; i <= TOTAL_STEPS; i++) {
        const si = document.getElementById(`sidebar-step-${i}`);
        const ic = document.getElementById(`icon-${i}`);
        si.className = 'step-item ' + (i < step ? 'done' : i === step ? 'active' : 'todo');
        ic.className = 'step-icon ' + (i < step ? 'done' : i === step ? 'active' : 'todo');
        if (i < step) ic.textContent = '';
        else ic.textContent = i;
    }
    document.getElementById('mob-step-label').textContent = `Step ${step} of ${TOTAL_STEPS} — ${labels[step - 1]}`;
    document.getElementById('mob-fill').style.width = `${(step / TOTAL_STEPS) * 100}%`;
}

function showPanel(step, direction) {
    document.querySelectorAll('.step-panel').forEach(p => {
        p.classList.remove('active', 'anim-in', 'anim-back');
    });
    const panel = document.getElementById(`panel-${step}`);
    if (panel) {
        panel.classList.add('active');
        animatePanel(panel, direction || 'forward');
        // scroll form card top into view (not the panel itself, avoids jumpiness)
        document.querySelector('.form-card').scrollIntoView({behavior: 'smooth', block: 'start'});
    }
    updateProgress(step);
    currentStep = step;
}

function nextStep(from) {
    if (!validateStep(from)) return;
    if (from === 3) buildSummary();
    showPanel(from + 1, 'forward');
}

function prevStep(from) {
    showPanel(from - 1, 'back');
}

// ── PHONE FORMATTING + VALIDATION ──
function formatPhone(input) {
    let digits = input.value.replace(/\D/g, '').slice(0, 10);
    let formatted = '';
    if (digits.length > 0) formatted = '(' + digits.slice(0, 3);
    if (digits.length >= 4) formatted += ') ' + digits.slice(3, 6);
    if (digits.length >= 7) formatted += '-' + digits.slice(6, 10);
    input.value = formatted;
    const valid = /^\(\d{3}\) \d{3}-\d{4}$/.test(formatted);
    document.getElementById('phone-tick').classList.toggle('show', valid);
    if (valid) {
        input.classList.remove('error');
        input.classList.add('ok');
        showErr('phone', false);
    }
}

function validatePhone(input) {
    const valid = /^\(\d{3}\) \d{3}-\d{4}$/.test(input.value);
    showErr('phone', !valid);
    input.classList.toggle('ok', valid);
    input.classList.toggle('error', !valid);
    document.getElementById('phone-tick').classList.toggle('show', valid);
}

// ── VALIDATION HELPERS ──
function showErr(id, show) {
    const el = document.getElementById('err-' + id);
    if (el) el.classList.toggle('show', show);
    const field = document.getElementById(id);
    if (field) {
        field.classList.toggle('error', show);
        field.classList.toggle('ok', !show && field.value.trim() !== '');
    }
}

function validateStep(step) {
    let ok = true;

    if (step === 1) {
        const checks = [
            ['first-name', v => v.trim().length >= 2],
            ['last-name', v => v.trim().length >= 2],
            ['dob', v => {
                if (!v) return false;
                const d = new Date(v), now = new Date();
                return (now - d) / (1000 * 60 * 60 * 24 * 365.25) >= 16;
            }],
            ['phone', v => /^\(\d{3}\) \d{3}-\d{4}$/.test(v.trim())],
            ['email', v => /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(v.trim())],
            ['address', v => v.trim().length >= 5],
            ['city', v => v.trim().length >= 2],
            ['country', v => v !== ''],
            ['postal', v => /^\d{5}(-\d{4})?$/.test(v.trim())],
            ['gender', v => v !== ''],
        ];
        checks.forEach(([id, fn]) => {
            const el = document.getElementById(id);
            const pass = fn(el ? el.value : '');
            showErr(id, !pass);
            if (!pass) ok = false;
        });
    }

    if (step === 2) {
        // edu-major is now optional — removed from checks
        const checks = [
            ['edu-level', v => v !== ''],
            ['edu-grad-year', v => {
                const n = parseInt(v);
                return n >= 1950 && n <= 2030;
            }],
            ['edu-institution', v => v.trim().length >= 3],
            ['edu-inst-location', v => v.trim().length >= 3],
        ];
        checks.forEach(([id, fn]) => {
            const el = document.getElementById(id);
            const pass = fn(el ? el.value : '');
            showErr(id, !pass);
            if (!pass) ok = false;
        });
    }

    if (step === 3) {
        const checks = [
            ['emp-status', v => v !== ''],
            ['emp-title', v => v.trim().length >= 2],
            ['emp-employer', v => v.trim().length >= 2],
            ['emp-address', v => v.trim().length >= 5],
            ['emp-start', v => v !== ''],
            ['emp-ssn', v => /^\d{3}-\d{2}-\d{4}$/.test(v.trim())],
            ['emp-ssn-confirm', v => {
                const ssn = document.getElementById('emp-ssn');
                return /^\d{3}-\d{2}-\d{4}$/.test(v.trim()) && ssn && v.trim() === ssn.value.trim();
            }],
            ['upload-w4', () => document.getElementById('upload-w4').files.length > 0],
            ['upload-i9', () => document.getElementById('upload-i9').files.length > 0],
            ['emp-summary', v => v.trim().length >= 30],
        ];
        checks.forEach(([id, fn]) => {
            const el = document.getElementById(id);
            const pass = fn(el ? el.value : '');
            showErr(id, !pass);
            if (!pass) ok = false;
        });
    }

    if (step === 4) {
        const checks = [
            ['id-type', v => v !== ''],
            ['id-number', v => v.trim().length >= 4],
            ['id-state', v => v !== ''],
            ['id-issue', v => v !== ''],
            ['id-expiry', v => v !== '' && new Date(v) > new Date()],
        ];
        checks.forEach(([id, fn]) => {
            const el = document.getElementById(id);
            const pass = fn(el ? el.value : '');
            showErr(id, !pass);
            if (!pass) ok = false;
        });
        const uploads = ['front', 'back', 'selfie'];
        uploads.forEach(key => {
            const hasFile = document.getElementById(`id-upload-${key}`).files.length > 0;
            showErr(`id-upload-${key}`, !hasFile);
            if (!hasFile) ok = false;
        });
    }

    return ok;
}

// live blur validation
document.addEventListener('DOMContentLoaded', () => {
    document.querySelectorAll('input,select,textarea').forEach(el => {
        if (el.type === 'tel') return; // phone handled separately
        el.addEventListener('blur', () => {
            if (el.id) {
                const err = document.getElementById('err-' + el.id);
                if (err && err.classList.contains('show')) {
                    el.classList.add('error');
                } else if (el.value.trim()) {
                    el.classList.remove('error');
                    el.classList.add('ok');
                }
            }
        });
    });

    // SSN live mask
    const ssnFields = ['emp-ssn', 'emp-ssn-confirm'];
    ssnFields.forEach(id => {
        const el = document.getElementById(id);
        if (!el) return;
        el.addEventListener('input', () => {
            let d = el.value.replace(/\D/g, '').slice(0, 9);
            let out = d.slice(0, 3);
            if (d.length > 3) out += '-' + d.slice(3, 5);
            if (d.length > 5) out += '-' + d.slice(5, 9);
            el.value = out;
            const valid = /^\d{3}-\d{2}-\d{4}$/.test(out);
            el.classList.toggle('ok', valid);
            el.classList.toggle('error', el.value.length > 0 && !valid);
        });
    });

    // trigger initial animation on step 1
    const firstPanel = document.getElementById('panel-1');
    if (firstPanel) animatePanel(firstPanel, 'forward');
});

// ── PREVIOUS EMPLOYMENT ──
function addPrevEmp() {
    prevEmpCount++;
    const n = prevEmpCount;
    const div = document.createElement('div');
    div.className = 'emp-entry';
    div.id = `prev-emp-${n}`;
    div.innerHTML = `
<div class="emp-entry-title">
    Previous Employer ${n}
    <button class="btn-remove" onclick="removePrevEmp(${n})" type="button">✕ Remove</button>
</div>
<div class="form-grid">
    <div class="field"><label>Job Title</label><input type="text" placeholder="e.g. Sales Associate"></div>
    <div class="field"><label>Employer Name</label><input type="text" placeholder="e.g. General Electric"></div>
    <div class="field"><label>From</label><input type="date"></div>
    <div class="field"><label>To</label><input type="date"></div>
    <div class="field span-2"><label>Key Responsibilities</label><textarea placeholder="Brief description of your role…" style="min-height:72px"></textarea></div>
</div>`;
    document.getElementById('prev-emp-list').appendChild(div);
}

function removePrevEmp(n) {
    const el = document.getElementById(`prev-emp-${n}`);
    if (el) el.remove();
}

// ── GENERIC FILE UPLOAD HANDLER ──
// keys: 'front','back','selfie','w4','i9'
const uploadConfig = {
    front: {
        zone: 'upload-zone-front',
        preview: 'preview-front',
        icon: 'prev-icon-front',
        name: 'prev-name-front',
        size: 'prev-size-front',
        input: 'id-upload-front',
        errId: 'id-upload-front'
    },
    back: {
        zone: 'upload-zone-back',
        preview: 'preview-back',
        icon: 'prev-icon-back',
        name: 'prev-name-back',
        size: 'prev-size-back',
        input: 'id-upload-back',
        errId: 'id-upload-back'
    },
    selfie: {
        zone: 'upload-zone-selfie',
        preview: 'preview-selfie',
        icon: 'prev-icon-selfie',
        name: 'prev-name-selfie',
        size: 'prev-size-selfie',
        input: 'id-upload-selfie',
        errId: 'id-upload-selfie'
    },
    w4: {
        zone: 'upload-zone-w4',
        preview: 'preview-w4',
        icon: 'prev-icon-w4',
        name: 'prev-name-w4',
        size: 'prev-size-w4',
        input: 'upload-w4',
        errId: 'upload-w4'
    },
    i9: {
        zone: 'upload-zone-i9',
        preview: 'preview-i9',
        icon: 'prev-icon-i9',
        name: 'prev-name-i9',
        size: 'prev-size-i9',
        input: 'upload-i9',
        errId: 'upload-i9'
    },
};

function handleUpload(key, input) {
    const file = input.files[0];
    if (!file) return;
    if (file.size > 10 * 1024 * 1024) {
        alert('File is too large. Maximum size is 10 MB.');
        input.value = '';
        return;
    }
    const c = uploadConfig[key];
    document.getElementById(c.zone).style.display = 'none';
    const prev = document.getElementById(c.preview);
    prev.classList.add('show');
    document.getElementById(c.icon).textContent = file.type.includes('pdf') ? '📄' : '🖼️';
    document.getElementById(c.name).textContent = file.name;
    document.getElementById(c.size).textContent = (file.size / 1024).toFixed(1) + ' KB';
    showErr(c.errId, false);
}

function removeUpload(key) {
    const c = uploadConfig[key];
    document.getElementById(c.input).value = '';
    document.getElementById(c.preview).classList.remove('show');
    document.getElementById(c.zone).style.display = '';
}

// drag & drop for all upload zones
document.addEventListener('DOMContentLoaded', () => {
    Object.entries(uploadConfig).forEach(([key, c]) => {
        const zone = document.getElementById(c.zone);
        if (!zone) return;
        zone.addEventListener('dragover', e => {
            e.preventDefault();
            zone.classList.add('dragover');
        });
        zone.addEventListener('dragleave', () => zone.classList.remove('dragover'));
        zone.addEventListener('drop', e => {
            e.preventDefault();
            zone.classList.remove('dragover');
            if (e.dataTransfer.files.length) {
                const input = document.getElementById(c.input);
                // DataTransfer workaround for programmatic file set
                try {
                    input.files = e.dataTransfer.files;
                } catch (_) {
                }
                handleUpload(key, {files: e.dataTransfer.files, value: ''});
            }
        });
    });
});

// ── SUMMARY ──
function val(id) {
    const el = document.getElementById(id);
    return el ? el.value || '—' : '—';
}

function summaryItem(label, value) {
    return `<div class="confirm-item"><label>${label}</label><span>${value || '—'}</span></div>`;
}

function buildSummary() {
    document.getElementById('summary-contact').innerHTML =
        summaryItem('Full Name', `${val('first-name')} ${val('last-name')}`) +
        summaryItem('Email', val('email')) +
        summaryItem('Phone', val('phone')) +
        summaryItem('Date of Birth', val('dob')) +
        summaryItem('Address', `${val('address')}, ${val('city')}, ${val('country')} ${val('postal')}`) +
        summaryItem('Gender', val('gender'));
    document.getElementById('summary-education').innerHTML =
        summaryItem('Highest Level', val('edu-level')) +
        summaryItem('Field of Study', val('edu-major') || 'Not provided') +
        summaryItem('Institution', val('edu-institution')) +
        summaryItem('Graduation Year', val('edu-grad-year'));
    document.getElementById('summary-employment').innerHTML =
        summaryItem('Status', val('emp-status')) +
        summaryItem('Job Title', val('emp-title')) +
        summaryItem('Employer', val('emp-employer')) +
        summaryItem('Start Date', val('emp-start')) +
        summaryItem('SSN (last 4)', val('emp-ssn').slice(-4) ? '●●●-●●-' + val('emp-ssn').slice(-4) : '—');
}

// ── SUBMIT ──
function submitForm() {
    if (!validateStep(4)) return;
    if (!document.getElementById('terms-agree').checked) {
        alert('Please agree to the Terms of Service and Privacy Policy to continue.');
        return;
    }
    document.querySelectorAll('.step-panel').forEach(p => p.style.display = 'none');
    const success = document.getElementById('success-panel');
    success.classList.add('show');
    success.scrollIntoView({behavior: 'smooth', block: 'center'});
}
