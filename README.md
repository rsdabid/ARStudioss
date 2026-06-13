[13 june version index.html](https://github.com/user-attachments/files/28909157/13.june.version.index.html)
# ARStudioss<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>AR Studioss — OS</title>
<style>
  * { margin: 0; padding: 0; box-sizing: border-box; }
  :root {
    --bg: #050d0a; --bg-2: #0a1610; --surface: #0d1f18; --surface-2: #122a20;
    --border: #1c382b; --border-bright: #285441;
    --text: #e8fbf0; --text-dim: #9bbfa9; --text-muted: #5a7868;
    --green: #5EE7B0; --green-bright: #7CF2C0; --green-deep: #2d8060;
    --gold: #ffd700; --silver: #c0c0c0; --bronze: #cd7f32;
    --amber: #ffb547; --blue: #4a9eff; --red: #ff5252;
  }
  body {
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    background: radial-gradient(ellipse at top right, rgba(94,231,176,0.1), transparent 50%),
      radial-gradient(ellipse at bottom left, rgba(94,231,176,0.05), transparent 50%), var(--bg);
    color: var(--text); min-height: 100vh; padding: 20px; background-attachment: fixed;
  }
  .container { max-width: 1400px; margin: 0 auto; }
  .header {
    display: flex; justify-content: space-between; align-items: center;
    margin-bottom: 20px; padding: 14px 22px;
    background: rgba(13,31,24,0.6); backdrop-filter: blur(20px);
    border: 1px solid var(--border); border-radius: 100px;
  }
  .logo { font-size: 18px; font-weight: 800; letter-spacing: 1px; display: flex; align-items: center; gap: 10px; }
  .logo-mark {
    width: 30px; height: 30px; background: linear-gradient(135deg, var(--green-bright), var(--green));
    border-radius: 9px; display: flex; align-items: center; justify-content: center;
    color: #052e20; font-weight: 900; font-size: 15px;
  }
  .header-right { display: flex; gap: 10px; align-items: center; }
  .user-badge {
    font-size: 12px; color: var(--text-dim); padding: 8px 14px;
    background: rgba(94,231,176,0.08); border: 1px solid rgba(94,231,176,0.15);
    border-radius: 100px; font-weight: 600;
  }
  .btn {
    padding: 9px 18px; border: none; border-radius: 100px; font-size: 13px;
    font-weight: 600; cursor: pointer; transition: all 0.2s; font-family: inherit; white-space: nowrap;
  }
  .btn-primary {
    background: linear-gradient(135deg, var(--green-bright), var(--green));
    color: #052e20; box-shadow: 0 0 20px rgba(94,231,176,0.3);
  }
  .btn-primary:hover { box-shadow: 0 0 30px rgba(94,231,176,0.5); transform: translateY(-1px); }
  .btn-secondary { background: rgba(94,231,176,0.06); color: var(--text); border: 1px solid var(--border); }
  .btn-secondary:hover { background: rgba(94,231,176,0.12); border-color: var(--border-bright); }
  .btn-ghost { background: transparent; color: var(--text-dim); }
  .btn-ghost:hover { color: var(--text); }
  .btn-sm { padding: 6px 12px; font-size: 12px; }
  .login-screen { display: flex; align-items: center; justify-content: center; min-height: calc(100vh - 40px); }
  .login-card {
    background: rgba(13,31,24,0.7); backdrop-filter: blur(30px);
    border: 1px solid var(--border); border-radius: 24px; padding: 40px;
    width: 100%; max-width: 400px; box-shadow: 0 0 80px rgba(94,231,176,0.08);
  }
  .login-brand { text-align: center; margin-bottom: 28px; }
  .login-brand .logo-mark { width: 56px; height: 56px; margin: 0 auto 14px; font-size: 24px; border-radius: 16px; box-shadow: 0 0 40px rgba(94,231,176,0.4); }
  .login-brand h2 { font-size: 22px; letter-spacing: 1.5px; font-weight: 800; }
  .login-brand p { color: var(--text-muted); font-size: 13px; margin-top: 4px; }
  .form-group { margin-bottom: 16px; }
  .form-group label { display: block; font-size: 11px; color: var(--text-dim); margin-bottom: 6px; text-transform: uppercase; letter-spacing: 0.8px; font-weight: 600; }
  .form-group input, .form-group select {
    width: 100%; padding: 12px 16px; background: rgba(5,13,10,0.6);
    border: 1px solid var(--border); border-radius: 12px; color: var(--text);
    font-size: 14px; font-family: inherit; transition: all 0.2s;
  }
  .form-group input:focus, .form-group select:focus { outline: none; border-color: var(--green); box-shadow: 0 0 0 3px rgba(94,231,176,0.1); }
  .checkbox-row { display: flex; align-items: center; gap: 8px; margin-bottom: 20px; font-size: 13px; color: var(--text-dim); cursor: pointer; }
  .checkbox-row input { width: auto; accent-color: var(--green); cursor: pointer; }
  .role-tabs { display: flex; gap: 4px; margin-bottom: 22px; background: rgba(5,13,10,0.6); padding: 4px; border-radius: 100px; border: 1px solid var(--border); }
  .role-tab { flex: 1; padding: 9px; text-align: center; border-radius: 100px; cursor: pointer; font-size: 12px; color: var(--text-muted); transition: all 0.2s; font-weight: 600; }
  .role-tab.active { background: linear-gradient(135deg, var(--green-bright), var(--green)); color: #052e20; box-shadow: 0 0 20px rgba(94,231,176,0.3); }
  .error-msg { color: var(--red); font-size: 13px; margin-top: 8px; display: none; }
  .error-msg.show { display: block; }
  .nav-tabs { display: flex; gap: 4px; margin-bottom: 20px; background: rgba(13,31,24,0.5); padding: 5px; border: 1px solid var(--border); border-radius: 100px; width: fit-content; }
  .nav-tab { padding: 10px 22px; border-radius: 100px; cursor: pointer; font-size: 14px; font-weight: 600; color: var(--text-muted); transition: all 0.2s; display: flex; align-items: center; gap: 7px; }
  .nav-tab:hover { color: var(--text); }
  .nav-tab.active { background: linear-gradient(135deg, var(--green-bright), var(--green)); color: #052e20; }
  .page { display: none; }
  .page.active { display: block; }
  .section-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 16px; flex-wrap: wrap; gap: 12px; }
  .section-title { font-size: 20px; font-weight: 700; letter-spacing: -0.3px; }
  .section-sub { font-size: 13px; color: var(--text-muted); margin-top: 2px; }
  .toolbar { display: flex; gap: 10px; align-items: center; flex-wrap: wrap; margin-bottom: 14px; }
  .toolbar select, .toolbar input { padding: 9px 14px; background: rgba(13,31,24,0.6); border: 1px solid var(--border); border-radius: 100px; color: var(--text); font-size: 13px; font-family: inherit; cursor: pointer; }
  .toolbar select:focus { outline: none; border-color: var(--green); }
  .toolbar-label { font-size: 12px; color: var(--text-muted); font-weight: 600; }
  .table-wrap { background: rgba(13,31,24,0.5); border: 1px solid var(--border); border-radius: 16px; overflow-x: auto; }
  table.crm { width: 100%; border-collapse: collapse; min-width: 900px; }
  table.crm thead th { background: rgba(5,13,10,0.6); padding: 14px; text-align: left; font-size: 11px; text-transform: uppercase; letter-spacing: 0.6px; color: var(--text-dim); font-weight: 700; border-bottom: 1px solid var(--border); white-space: nowrap; }
  table.crm thead th .col-menu { opacity: 0; margin-left: 6px; cursor: pointer; color: var(--text-muted); font-size: 12px; transition: opacity 0.15s; }
  table.crm thead th:hover .col-menu { opacity: 1; }
  table.crm tbody td { padding: 0; border-bottom: 1px solid rgba(28,56,43,0.5); border-right: 1px solid rgba(28,56,43,0.3); font-size: 13px; vertical-align: middle; }
  table.crm tbody tr:hover { background: rgba(94,231,176,0.02); }
  .cell { padding: 12px 14px; min-height: 44px; cursor: text; display: flex; align-items: center; min-width: 80px; }
  .cell-input { width: 100%; padding: 12px 14px; background: rgba(94,231,176,0.06); border: 1px solid var(--green); color: var(--text); font-size: 13px; font-family: inherit; outline: none; }
  .cell-link { color: var(--green); text-decoration: none; display: inline-flex; align-items: center; gap: 5px; max-width: 180px; overflow: hidden; text-overflow: ellipsis; white-space: nowrap; }
  .cell-link:hover { text-decoration: underline; }
  .cell-empty { color: var(--text-muted); font-style: italic; opacity: 0.6; }
  .status-cell { padding: 12px 14px; cursor: pointer; }
  .status-pill { display: inline-flex; align-items: center; gap: 6px; padding: 5px 12px; border-radius: 100px; font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.4px; white-space: nowrap; }
  .status-pill::before { content: ''; width: 6px; height: 6px; border-radius: 50%; background: currentColor; }
  .status-assigned { background: rgba(74,158,255,0.15); color: var(--blue); }
  .status-progress { background: rgba(255,181,71,0.15); color: var(--amber); }
  .status-revision { background: rgba(255,82,82,0.15); color: var(--red); }
  .status-done { background: rgba(94,231,176,0.15); color: var(--green); }
  .editor-cell { padding: 12px 14px; cursor: pointer; }
  .editor-pill { display: inline-flex; align-items: center; gap: 7px; padding: 5px 12px; background: rgba(94,231,176,0.08); border: 1px solid var(--border); border-radius: 100px; font-size: 12px; font-weight: 600; }
  .editor-avatar { width: 20px; height: 20px; border-radius: 50%; background: linear-gradient(135deg, var(--green-bright), var(--green-deep)); display: flex; align-items: center; justify-content: center; font-size: 10px; font-weight: 800; color: #052e20; }
  .num-cell { padding: 12px 14px; cursor: text; font-weight: 600; }
  .revenue-val { color: var(--green-bright); }
  .points-val { color: var(--amber); }
  .points-auto { font-size: 10px; color: var(--text-muted); margin-left: 4px; font-weight: 500; }
  tr.totals-row td { background: rgba(94,231,176,0.04); border-top: 2px solid var(--border-bright); font-weight: 700; opacity: 0.85; }
  tr.totals-row .cell { color: var(--text-muted); font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; }
  .total-revenue { color: var(--green-bright); font-size: 15px; }
  .total-points { color: var(--amber); font-size: 15px; }
  .add-row-bar { display: flex; align-items: center; gap: 8px; padding: 12px 16px; color: var(--text-muted); cursor: pointer; font-size: 13px; font-weight: 600; border-top: 1px solid rgba(28,56,43,0.5); transition: all 0.15s; }
  .add-row-bar:hover { color: var(--green); background: rgba(94,231,176,0.03); }
  .row-delete { opacity: 0; cursor: pointer; color: var(--text-muted); font-size: 16px; padding: 4px 8px; transition: all 0.15s; }
  tr:hover .row-delete { opacity: 0.6; }
  .row-delete:hover { opacity: 1 !important; color: var(--red); }
  .dropdown-menu { position: fixed; background: var(--surface-2); border: 1px solid var(--border-bright); border-radius: 12px; padding: 6px; min-width: 200px; box-shadow: 0 10px 40px rgba(0,0,0,0.5); z-index: 500; max-height: 320px; overflow-y: auto; }
  .dropdown-item { display: flex; align-items: center; gap: 10px; padding: 9px 12px; border-radius: 8px; cursor: pointer; font-size: 13px; transition: background 0.12s; }
  .dropdown-item:hover { background: rgba(94,231,176,0.1); }
  .dropdown-item .item-edit { margin-left: auto; opacity: 0; color: var(--text-muted); cursor: pointer; font-size: 12px; padding: 2px 6px; }
  .dropdown-item:hover .item-edit { opacity: 1; }
  .dropdown-item .item-edit:hover { color: var(--green); }
  .dropdown-divider { height: 1px; background: var(--border); margin: 6px 4px; }
  .dropdown-add-input { display: flex; gap: 6px; padding: 6px; }
  .dropdown-add-input input { flex: 1; padding: 8px 10px; background: rgba(5,13,10,0.6); border: 1px solid var(--border); border-radius: 8px; color: var(--text); font-size: 13px; font-family: inherit; }
  .dropdown-add-input button { padding: 0 12px; background: var(--green); color: #052e20; border: none; border-radius: 8px; cursor: pointer; font-weight: 700; font-size: 13px; }
  .mini-calendar { position: fixed; background: var(--surface-2); border: 1px solid var(--border-bright); border-radius: 14px; padding: 14px; z-index: 500; box-shadow: 0 10px 40px rgba(0,0,0,0.5); width: 260px; }
  .cal-header { display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px; }
  .cal-header button { background: rgba(94,231,176,0.1); border: none; color: var(--green); width: 28px; height: 28px; border-radius: 8px; cursor: pointer; font-size: 14px; }
  .cal-month { font-size: 13px; font-weight: 700; }
  .cal-grid { display: grid; grid-template-columns: repeat(7, 1fr); gap: 2px; }
  .cal-day-name { text-align: center; font-size: 10px; color: var(--text-muted); padding: 4px 0; font-weight: 600; }
  .cal-day { text-align: center; padding: 7px 0; border-radius: 8px; cursor: pointer; font-size: 12px; transition: background 0.12s; }
  .cal-day:hover { background: rgba(94,231,176,0.1); }
  .cal-day.today { border: 1px solid var(--green); }
  .cal-day.selected { background: var(--green); color: #052e20; font-weight: 700; }
  .cal-day.empty { cursor: default; }
  .cal-clear { margin-top: 10px; text-align: center; font-size: 12px; color: var(--text-muted); cursor: pointer; padding: 6px; }
  .cal-clear:hover { color: var(--red); }
  .rankings-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 20px; }
  @media (max-width: 768px) { .rankings-grid { grid-template-columns: 1fr; } }
  .ranking-block { background: rgba(13,31,24,0.5); backdrop-filter: blur(20px); border: 1px solid var(--border); border-radius: 20px; padding: 22px; }
  .ranking-title { font-size: 12px; color: var(--green); text-transform: uppercase; letter-spacing: 1.2px; font-weight: 700; margin-bottom: 16px; display: flex; align-items: center; gap: 8px; }
  .ranking-title::before { content: ''; width: 6px; height: 6px; background: var(--green); border-radius: 50%; box-shadow: 0 0 12px var(--green); }
  .ranking-list { display: flex; flex-direction: column; gap: 8px; }
  .ranking-row { display: flex; align-items: center; gap: 14px; padding: 12px 14px; background: rgba(5,13,10,0.4); border: 1px solid transparent; border-radius: 12px; transition: all 0.2s; }
  .ranking-row:hover { border-color: var(--border); }
  .ranking-row.me { background: rgba(94,231,176,0.06); border-color: rgba(94,231,176,0.2); }
  .rank-num { width: 30px; height: 30px; display: flex; align-items: center; justify-content: center; border-radius: 50%; font-weight: 800; font-size: 13px; flex-shrink: 0; }
  .rank-num.rank-1 { background: linear-gradient(135deg, var(--gold), #f4c430); color: #2a1f00; }
  .rank-num.rank-2 { background: linear-gradient(135deg, var(--silver), #909090); color: #1a1a1a; }
  .rank-num.rank-3 { background: linear-gradient(135deg, var(--bronze), #8b5a2b); color: #2a1500; }
  .rank-num.other { background: rgba(94,231,176,0.08); color: var(--text-dim); border: 1px solid var(--border); }
  .ranking-name-wrap { flex: 1; min-width: 0; }
  .ranking-name { font-weight: 600; font-size: 14px; }
  .ranking-meta { font-size: 11px; color: var(--text-muted); margin-top: 2px; }
  .ranking-points { font-weight: 800; font-size: 18px; color: var(--green); letter-spacing: -0.5px; }
  .empty-rank { text-align: center; padding: 24px; color: var(--text-muted); font-size: 13px; }
  .you-tag { font-size: 10px; color: var(--green); margin-left: 6px; text-transform: uppercase; letter-spacing: 0.5px; }
  .ranking-section-label { font-size: 11px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.8px; font-weight: 700; margin: 10px 0 8px; padding-top: 8px; border-top: 1px dashed var(--border); }
  .locked-board { text-align: center; padding: 60px 24px; background: rgba(13,31,24,0.5); border: 1px solid var(--border); border-radius: 20px; }
  .locked-icon { font-size: 48px; margin-bottom: 16px; }
  .locked-title { font-size: 20px; font-weight: 700; margin-bottom: 8px; }
  .locked-sub { color: var(--text-dim); font-size: 14px; }
  .modal-overlay { display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.75); backdrop-filter: blur(8px); z-index: 600; align-items: center; justify-content: center; padding: 20px; }
  .modal-overlay.show { display: flex; }
  .modal { background: var(--surface); border: 1px solid var(--border); border-radius: 20px; padding: 32px; width: 100%; max-width: 480px; max-height: 90vh; overflow-y: auto; box-shadow: 0 0 80px rgba(94,231,176,0.1); }
  .modal h3 { font-size: 20px; margin-bottom: 8px; letter-spacing: -0.3px; }
  .modal-sub { color: var(--text-dim); font-size: 13px; margin-bottom: 22px; }
  .modal-actions { display: flex; gap: 8px; justify-content: flex-end; margin-top: 24px; flex-wrap: wrap; }
  .info-banner { background: rgba(94,231,176,0.06); border: 1px solid rgba(94,231,176,0.15); border-radius: 12px; padding: 12px 14px; margin-bottom: 16px; font-size: 12px; color: var(--text-dim); line-height: 1.5; }
  .team-section { padding: 16px; background: rgba(5,13,10,0.4); border: 1px solid var(--border); border-radius: 12px; margin-bottom: 12px; }
  .team-section h4 { font-size: 13px; color: var(--green); text-transform: uppercase; letter-spacing: 0.8px; font-weight: 700; margin-bottom: 12px; }
  .members-list { display: flex; flex-wrap: wrap; gap: 6px; margin-bottom: 12px; }
  .member-pill { display: inline-flex; align-items: center; gap: 6px; padding: 5px 10px 5px 12px; background: rgba(94,231,176,0.08); border: 1px solid var(--border); border-radius: 100px; font-size: 12px; color: var(--text); }
  .member-pill .leader-mark { font-size: 10px; color: var(--green); background: rgba(94,231,176,0.15); padding: 1px 6px; border-radius: 100px; }
  .member-pill button { background: transparent; border: none; color: var(--text-muted); cursor: pointer; font-size: 14px; padding: 0; transition: color 0.15s; }
  .member-pill button:hover { color: var(--red); }
  .add-member-row { display: flex; gap: 6px; margin-bottom: 16px; }
  .add-member-row input { flex: 1; padding: 11px 14px; background: rgba(5,13,10,0.6); border: 1px solid var(--border); border-radius: 12px; color: var(--text); font-size: 14px; font-family: inherit; }
  .add-member-row button { padding: 0 16px; background: rgba(94,231,176,0.1); border: 1px solid var(--border); border-radius: 12px; color: var(--green); cursor: pointer; font-weight: 600; font-size: 13px; font-family: inherit; }
  .pwd-field { position: relative; flex: 1; }
  .pwd-field input { width: 100%; padding: 11px 44px 11px 14px; background: rgba(5,13,10,0.6); border: 1px solid var(--border); border-radius: 12px; color: var(--text); font-size: 14px; font-family: inherit; }
  .pwd-toggle { position: absolute; right: 8px; top: 50%; transform: translateY(-50%); background: transparent; border: none; color: var(--text-muted); cursor: pointer; padding: 6px 8px; border-radius: 6px; font-size: 14px; }
  .pwd-toggle:hover { color: var(--green); background: rgba(94,231,176,0.08); }
  .password-row { display: flex; gap: 6px; align-items: center; margin-top: 10px; }
  .password-row button { padding: 11px 16px; background: rgba(94,231,176,0.1); border: 1px solid var(--border); border-radius: 12px; color: var(--green); cursor: pointer; font-weight: 600; font-size: 12px; font-family: inherit; white-space: nowrap; }
  .toast { position: fixed; bottom: 24px; left: 50%; transform: translateX(-50%); background: rgba(13,31,24,0.95); backdrop-filter: blur(10px); border: 1px solid var(--green-deep); color: var(--green); padding: 12px 20px; border-radius: 100px; font-size: 13px; font-weight: 600; box-shadow: 0 0 40px rgba(94,231,176,0.3); z-index: 700; opacity: 0; transition: opacity 0.3s, transform 0.3s; pointer-events: none; }
  .toast.show { opacity: 1; transform: translateX(-50%) translateY(-4px); }
  #loadingOverlay { position: fixed; inset: 0; background: var(--bg); display: flex; align-items: center; justify-content: center; z-index: 9999; flex-direction: column; gap: 16px; }
  .spin-mark { width: 56px; height: 56px; border-radius: 14px; display: flex; align-items: center; justify-content: center; animation: pulse 1.4s ease-in-out infinite; }
  @keyframes pulse { 0%,100% { transform: scale(1); opacity: 1; } 50% { transform: scale(1.08); opacity: 0.85; } }
  @media (max-width: 640px) { body { padding: 12px; } .header { flex-wrap: wrap; gap: 10px; } .nav-tab { padding: 9px 16px; font-size: 13px; } }

  /* FINANCE */
  .fin-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 16px; margin-bottom: 16px; }
  @media (max-width: 900px) { .fin-grid { grid-template-columns: 1fr; } }
  .fin-card { background: rgba(13,31,24,0.5); border: 1px solid var(--border); border-radius: 16px; padding: 20px; }
  .fin-card h3 { font-size: 13px; color: var(--green); text-transform: uppercase; letter-spacing: 0.8px; font-weight: 700; margin-bottom: 16px; }
  .fin-stat { display: flex; justify-content: space-between; align-items: center; padding: 10px 0; border-bottom: 1px solid rgba(28,56,43,0.4); }
  .fin-stat:last-child { border-bottom: none; }
  .fin-stat .label { color: var(--text-dim); font-size: 13px; }
  .fin-stat .val { font-weight: 700; font-size: 16px; }
  .fin-stat .val.pos { color: var(--green); }
  .fin-stat .val.neg { color: var(--red); }
  .fin-stat .val.rev { color: var(--green-bright); }
  .fin-big { text-align: center; padding: 18px; background: rgba(94,231,176,0.05); border-radius: 12px; margin-top: 10px; }
  .fin-big .num { font-size: 34px; font-weight: 800; letter-spacing: -1.5px; }
  .fin-big .num.pos { color: var(--green); }
  .fin-big .num.neg { color: var(--red); }
  .fin-big .cap { font-size: 11px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.8px; font-weight: 700; margin-top: 4px; }

  .exp-table { width: 100%; border-collapse: collapse; }
  .exp-table th { text-align: left; font-size: 10px; text-transform: uppercase; letter-spacing: 0.5px; color: var(--text-muted); padding: 8px; font-weight: 700; }
  .exp-table td { padding: 0; border-bottom: 1px solid rgba(28,56,43,0.4); }
  .exp-cell { padding: 10px 8px; cursor: text; min-height: 38px; display: flex; align-items: center; }
  .exp-cell.empty { color: var(--text-muted); font-style: italic; opacity: 0.6; }
  .exp-input { width: 100%; padding: 10px 8px; background: rgba(94,231,176,0.06); border: 1px solid var(--green); color: var(--text); font-size: 13px; font-family: inherit; outline: none; }
  .exp-amount { color: var(--red); font-weight: 600; }
  .exp-del { opacity: 0; cursor: pointer; color: var(--text-muted); font-size: 14px; transition: all 0.15s; }
  tr:hover .exp-del { opacity: 0.6; }
  .exp-del:hover { opacity: 1 !important; color: var(--red); }
  .exp-add { display: flex; align-items: center; gap: 6px; padding: 10px 8px; color: var(--text-muted); cursor: pointer; font-size: 13px; font-weight: 600; }
  .exp-add:hover { color: var(--green); }

  .tier-table { width: 100%; border-collapse: collapse; margin-top: 8px; }
  .tier-table th { text-align: left; font-size: 10px; text-transform: uppercase; color: var(--text-muted); padding: 6px 8px; letter-spacing: 0.5px; }
  .tier-table td { padding: 7px 8px; font-size: 13px; border-top: 1px solid rgba(28,56,43,0.4); }
  .tier-table td.pts { color: var(--amber); font-weight: 700; text-align: right; }
  .tier-table td.rng { color: var(--green-bright); }

  .calc-row { display: flex; gap: 10px; align-items: center; margin-bottom: 14px; }
  .calc-row input { flex: 1; padding: 12px 16px; background: rgba(5,13,10,0.6); border: 1px solid var(--border); border-radius: 12px; color: var(--text); font-size: 16px; font-family: inherit; font-weight: 700; }
  .calc-row input:focus { outline: none; border-color: var(--green); }
  .calc-result { padding: 12px 18px; background: rgba(255,181,71,0.1); border-radius: 12px; font-weight: 800; color: var(--amber); font-size: 18px; white-space: nowrap; }

  .split-row { display: flex; align-items: center; gap: 10px; margin-bottom: 10px; }
  .split-name { width: 80px; font-weight: 600; font-size: 14px; }
  .split-pct-input { width: 70px; padding: 8px 10px; background: rgba(5,13,10,0.6); border: 1px solid var(--border); border-radius: 8px; color: var(--text); font-size: 13px; font-family: inherit; text-align: center; }
  .split-pct-input:focus { outline: none; border-color: var(--green); }
  .split-amounts { margin-left: auto; text-align: right; }
  .split-rev-amt { color: var(--green-bright); font-weight: 700; font-size: 14px; }
  .split-profit-amt { color: var(--green); font-weight: 700; font-size: 14px; }
  .split-sub { font-size: 10px; color: var(--text-muted); }
  .split-warn { color: var(--amber); font-size: 12px; margin-top: 8px; }

  .report-box { background: rgba(5,13,10,0.5); border: 1px solid var(--border); border-radius: 12px; padding: 18px; font-size: 14px; line-height: 1.9; }
  .report-line { color: var(--text-dim); }
  .report-line strong { color: var(--text); }
  .report-num { color: var(--green-bright); font-weight: 700; }
  .report-num.pts { color: var(--amber); }
  .report-num.neg { color: var(--red); }
  .notes-area { width: 100%; min-height: 120px; padding: 14px; background: rgba(94,231,176,0.04); border: 1px solid rgba(94,231,176,0.25); border-radius: 12px; color: var(--green-bright); font-size: 14px; font-family: inherit; line-height: 1.6; resize: vertical; margin-top: 12px; }
  .notes-area:focus { outline: none; border-color: var(--green); }
  .notes-label { font-size: 11px; color: var(--green); text-transform: uppercase; letter-spacing: 0.8px; font-weight: 700; }

  .split-taka { color: var(--text-dim); font-weight: 700; font-size: 13px; margin-top: 2px; }
  .rate-row { display: flex; align-items: center; gap: 8px; margin-top: 16px; padding-top: 14px; border-top: 1px dashed var(--border); flex-wrap: wrap; }
  .rate-label { font-size: 11px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; font-weight: 600; }
  .rate-eq { font-size: 13px; color: var(--text-dim); font-weight: 600; }
  .rate-input { width: 80px; padding: 7px 10px; background: rgba(5,13,10,0.6); border: 1px solid var(--border); border-radius: 8px; color: var(--green-bright); font-size: 13px; font-family: inherit; font-weight: 700; text-align: center; }
  .rate-input:focus { outline: none; border-color: var(--green); }
  .converter { display: flex; align-items: flex-end; gap: 12px; margin: 16px 0; }
  .conv-side { flex: 1; }
  .conv-side label { display: block; font-size: 11px; color: var(--text-muted); text-transform: uppercase; letter-spacing: 0.5px; font-weight: 600; margin-bottom: 6px; }
  .conv-side input { width: 100%; padding: 11px 14px; background: rgba(5,13,10,0.6); border: 1px solid var(--border); border-radius: 10px; color: var(--text); font-size: 15px; font-family: inherit; font-weight: 700; }
  .conv-side input:focus { outline: none; border-color: var(--green); }
  .conv-eq { font-size: 18px; color: var(--green); padding-bottom: 10px; }
  .collapse-head { display: flex; justify-content: space-between; align-items: center; cursor: pointer; }
  .collapse-arrow { color: var(--text-muted); font-size: 12px; }
  .tier-head { display: flex; justify-content: space-between; align-items: center; margin: 16px 0 8px; }
  .tier-input { width: 100%; padding: 7px 9px; background: rgba(5,13,10,0.6); border: 1px solid var(--border); border-radius: 7px; color: var(--text); font-size: 13px; font-family: inherit; }
  .tier-input.pts { color: var(--amber); font-weight: 700; }
  .tier-input:focus { outline: none; border-color: var(--green); }
  .tier-note { font-size: 11px; color: var(--text-muted); margin-top: 8px; font-style: italic; }
  .rate-bar { display: flex; justify-content: space-between; align-items: center; gap: 16px; flex-wrap: wrap; }
  .rate-bar-input { display: flex; align-items: center; gap: 8px; }
</style>
</head>
<body>
<div id="loadingOverlay"><div class="spin-mark"><img src="data:image/png;base64,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" alt="A" style="width:34px;height:auto"></div><div id="loadingText" style="color:var(--text-dim);font-size:13px">Connecting to cloud...</div></div>

<div id="loginScreen" class="login-screen" style="display:none">
  <div class="login-card">
    <div class="login-brand"><img src="data:image/png;base64,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" alt="AR Studioss" style="width:88px;height:88px;border-radius:20px;margin:0 auto 16px;display:block;box-shadow:0 0 40px rgba(94,231,176,0.3)"><p>Agency OS — sign in to continue</p></div>
    <div class="role-tabs">
      <div class="role-tab active" data-role="admin" onclick="switchRole('admin')">Admin</div>
      <div class="role-tab" data-role="team" onclick="switchRole('team')">Team</div>
    </div>
    <div id="adminLogin"><div class="form-group"><label>Password</label><input type="password" id="adminPass" placeholder="Enter admin password"></div></div>
    <div id="teamLogin" style="display:none">
      <div class="form-group"><label>Team</label><select id="teamSelect"><option value="">Select your team</option></select></div>
      <div class="form-group"><label>Access Code</label><input type="password" id="teamCode" placeholder="Enter your team code"></div>
    </div>
    <label class="checkbox-row"><input type="checkbox" id="rememberMe" checked><span>Remember me on this device</span></label>
    <button class="btn btn-primary" onclick="login()" style="width:100%;padding:13px">Sign in</button>
    <div id="loginError" class="error-msg">Wrong credentials. Try again.</div>
  </div>
</div>

<div id="mainApp" class="container" style="display:none">
  <div class="header">
    <div class="logo"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAlgAAAB/CAYAAAAzULx7AAByEUlEQVR42u2deYBdRZX/v6eq7r1v6S3prBAIQiDQkc0mEBKwMyLqIIKgrxEQWQdU/DmOjjMuoy8PdXR0nHEbF1wQEcQ8lUVRBNQ8gRiWFhBoWeISCITs6fW9e29Vnd8f93anO/066ST90h24H3x20ul+7966Vae+derUOUBCQkJCQkJCQsK4QkkTxOTzAlghxvzzK3bjvWfMYLQUGQXYpKETEhISEhISXkHiah+Qy8lE1CYkJCQkJLz8SSb7qA04846Tj7dTvRZo3t4mEoAZ8mfEf5eAqYQwgYGU2783+BXbf89IQLlOJb0+6Oj6+YN/G/qZSdMnJCQkJCQkAuvlRz4vUCjAveTk/zNNqXdbJcbeKjxGfcTR+4nA9qvu4CtnfX/lfxQBgzxEsmWYkJCQkJCQCKyXF21tCqWSds5feKE5uOmHthIYWOYatQiBSIqUA7Gtclfm3r+f3925dgtyOYli0STdMCEhISEh4eWFfMUKy0suQcvGjc7Gw+tvtoqmwliASAEkavJiMGurUecdoWfWvzHd2HBreMeKHuRyEp2dyXZhQkJCQkLCywjxirzrfJtEoWCfPbHxnWj05iM0DKLaik0CAXBsOdCm0T2uMr/57uxbTpqJYjHaLkxISEhISEh42fBK9GARlq4Bts7M4NDpRZbUADsogPbBp5NAaDQyzmzj0RuyWe8nwQ829yEPgVIS+J6QkJCQkPBy4JXnOcm3SRRg1fGHvJvr3IM5NBa0j9uBSHEl0NzgHuMfMf1WMFwsyBGSU50JCQkJCQkvC+gVd78MNC49trG3peEZk1LToO2+816NJBRpx1EbKt8LrrvvcuTbFAolnXTLhISEhISE/ZtXlgcr3yZB4N5XpT9o673p0MZOoLgCAMdWwlBP8y7z3nXypSiUdJyMNCEhISEhIWE/5pU0mQusWGOzfzpmRjg1cyMDLhg0wQILYAgGW7ji9PqZU4v+z36zBUjisRISEhISEvZv0fFKYXmOQOBgat2HUec2wFgz4eIKiLYntQWnnbryjNQ3QGB05pJYrISEhISEhP2YV4YHKw+Bqzt5SmfrwZWm1PWWIWNxOTmEDJFgbTSy3jznsBlPmJvvejLJj5WQkJCQkLD/8srwYHVG3queOrdgMk4GxjImW4A/Q1iATVZ9Di0tLlpaJt81JiQkJCQkJIyJl78HKw+Br3dy3XnHHxVOyXydraUou/okEy9EBGMtst40p0H+3X7lh39Evk2htCapV5iQkJCQkLCf8fL3YEXxTNyfTX3GppUDy5PZM0RsmW2d/De0tSksKxkkXqyEhISEhIREYE0q4mLKKtd6Iuq8s7mibc1L4uyVvCKBUFvOuPPduf5bQGC0tSVpGxISEhISEhKBNQl1S4P3GfakAPN+ETRuBbH15NUAgKVLky3ChISEhISE/U17vGzvLPZepS466ZSgOXOvNXbfl8TZ86fCwrDJri0v6Ln1oWeQh0ABidBKSEhISEjYT3jZe7DCtPOfVhEA3n9SHlg2nHFUeYrIRd9oE0lXTUhISEhISATWxBJ7r9LvOOksrvdORaDNpI692hECwTLYVW8FgDjYPSEhISEhISERWBNIlENKBg3qU5Z4P0zWSZJDA3bksd5bjp8HAiOPxIuVkJCQkJCQCKwJoq1NoVCwqfNPvNA2pI5BoC1A+99JPMuGU45jm9x/iG8sEVgJCQkJCQmJwJoQCEuX2rlz56Z0vfsfYMvg/TaQn1kA7KlTk26akJCQkJCQCKyJI98mUSjYF06deblp9A7nwBgQif322RgLVrQwB0gUkqSjCQkJCQkJicDa9xBQsjNPPyaLOvcjbCzHJXH207shgmZA0qF3nX3sQQAY+URgJSQkJCQkJAJrX5JvkyjAbj0gc7Vt8OYgNLXPe8Ww4JrlpyJYa9lTbqWp/kgAA2V/EhISEhISEhKBtU8goGQb3tAy1WSdD9vQMkC1FiMsHCFIiVpmiLesJIyHFgBAy4ZEYCUkJCQkJCQCax8Re6/KBzb+q61zp0EbU1PvFcMKV5La1P8R2R/+jtIOgdnU5qMYABYkXTUhISEhISERWPtQXEFgWcmk3rDgIJtR/w+BqXFBZzZwJYne8MngBw/8l3qhfInsC7ci8mSN73ZhnHDUSjo0+kZSlzAhISEhISERWPuCBTkCgc3s+o/YrFfHxlrU+LQdEUj062VgUOUXHc/xpv4LJQuCEBbA+G0XciSwQDgQgEKhUPN7S0hISEhISNh75H599XkIXN3J3h9b5pnp9d+1zBSLxhqJEDbkKiG6/Mf1dSv/BcgD83sV/6Djaefw2ZqbvNdzOJ6pIQggEBlWdQfO/Fbw1IvlRGAlJCQkJCRMftR+ffULcgQqWnNZ4yds1nFRDjWIantPzCR7/WsMYNDZKVHsCJFvU0Gh9Bl1+ZLjuDn9di4H43MdAzWqCVly5BQAm5EHoYDJWv5nd8UfT6JrwSS69snzPPMgrGgTWBp/p3MGo6WFsWzZ9vtftozQ2UmDhzBWAFhasnE/5Un8DGvVB2gS9Bsah/5LL5OxQxNyPQxCe04MjosFMxhFAMuXDw/1aG8XyAF4cuj4WWpRKPAksDOEXJV7GGoDBsb/0HvonMFoKTIKsBN67fk8YcWKXduvBZ1U5dr3uv33X29IHgIFcDbX+urK7OwjhojirO01817BVUJuqzxqvrNyIfJ5jrfsBh9k8903Z7cdM/1BU+ceCX/cCkwzAaS6wuPD61c+inxeDPncySaueLcNEO2nQoVBWJbfPjA7ZzCKxfHdIp5Ig5oD0F7c+4Mby3MSReBl0jYJtRg7A5Pay6GP5HISLRsIy0pmXGzbwPuhZPeZWMlDRKXZltq9nmsYhGVtclzeaz+0X7Rfd+Ri0ajLl9ymm1NnoRyaWge3CyWleqHnjODHD/9q4PN3vJ7sOSe8unJg5iHjCAeaBWiv29iSEEKuLy/VP1pVGvG5k09k7Y7Qevl5sPJ5gc5O2g8ni8gwDelbLWhx17RnjghSqsVKaiFgLhQ1M6iJiZzBCYTQI7SpsKWNkvE3Duyz6Nedh9/y8DOdQLC9bdpUXJGAX0b2iRMP1jh6sHI5iQ0bCKXd6icT7cEitLVJlEp66DfTZx1/gM04RxpPHsWEeSRpFgQ1WaARYsglEXcJjYAtbyTGc2T4WacvfKr+2eCZ9X/6U9+wtgFQM/ufh0Bnjoa+f/1pRzaXp2VaKJU60krMB2gOe5SG4SkAOfH1WwhsESGXmeh5CszfpcWfxZbyn8t3PPbCMLHVPtzGjK+3qk2isP0ZzJ49O9N16kGHh654tVV0BAnMhUNTLUQdGOkB+0XGBgzukpZeYmv/LkI85fXozg/e/vCzBQwRtdHcu1t2ff8UWAPiqv3ERWZ2ZiVHeahqmJaBDVJKOl3+veG19792VC9SW5tCqaSd8064yMxp+IHVWoP3cquQ2QpHCWeD/wb/h/ffPekEVnw9qQtOOk9P9a6xgTEAy12YM4OUI1W3/93g+lWfx/KcHJfVRuTVtOk3H3tgMCv7a1bkRHkumMZ7LEOKHljuIsY6YvsMh/aR1GZ+sO/nD6zfsW32l/EEAHPnzk2tazvwDSYt3wpBr2WJw5BSgBBgAMQM5sH0IXFzxKuIga/GAhXDZPkvZOx9Qttbmn/1t3vWrVvXv8t2iZ9h5pzW2X5z6i6WcGvzDPfq+VsoKURZP6uvW3nm4Eq3vWicC0/4bzM1+xZUtAENHQcDvxP+WV/3h7fugb93rPac6087srk8d8o91hUZGDBoaNuRgauk2up/JLhx1S0jnkXc/t5bWw8zzak7rOLx9zFLsQ0WfQRaL7RZC0tPKeLHMk/h6c0rV/YM8x48uYfbTLGNbr7sH+ZvU8HtXF0HMwgk1vdepG997ME92h0Y0n4EIHXpKSdpR7zVSv4HCFrAjqyDI+Ley9H/ePjDp4GUjQPjxzLga5DhtaRtB7S9U/UFd1R+/PDzg/eGAsbRozVscZU+58Q5Zqo8VzvOmyHQCkc0w5GAiLsC84jUj9vvASAGoC3I131gPA5j7xI+3xJev/LRmlz/kGcwvaWlrvfEqf8YunwOS7GEpTgYKTlovzgyXiPbPzJgIGbAMMjXGkzPCG3udTT97Kjv9f+uAx3h7tr1/TMGq6UlaqJ69Tm4klAJbY3zipLQDGnooyEAdHZW/7BSSSPfpsJC6QbvkiVHhzPTH7b94xOPpTKO9Sfxswgz8j22IXUEl0MMW51VF42AK6FD8260tf0PckUDjN+UYz3r2ay7gF0ZfVatEEMMozGo1Jut6r1t91JZ33jMdfff0lEshpNeZMXXN72lpa5r8ZQr1rrqPUjLI4wkQNtILAXaDCgqRnWfbNzM0RcCQZGElPOgnHlS8yUb33b46lR53vfcJ//2re5iccuuVoNWpRzOOK+2tX6Ge7boAVwFgLeP63irS3vOodzgHQElho+Dgd8Z71QuVTAKrk07x9iMI2B4+DKaGfAc6H49JRq/1ZMXWzdMc33DfKto/IUgDczEgKFoUrO+QfAa86I69tQHyDe3ey/239HbXty4twsVnVJpzogj7Ch9iASBtwX12JldH9VjkicUCmbmzJnZbW8+/GKbEZcGUpxgPQW2Nho/1lpUjB32e1R17AwfP0QSnpyDrDOHgLM543Sr95z6C7Ut+EalULhvHBdwAgSLYtE4b1u4gGekPxBIaue0arAAoA1gmOGHZvQ72D7+t0sXEnBlFkosIkGLUNGfUFe/9reiW381KBRuG7frj9+jsW1uU/mIg67e4sl/gifnjma/qrb/9osear8UpGixSrVYzVc9enVdpxec+o2pv1j9vXXFYv9Yr33/E1i5nEShYLx3tJ4eNHhtPH6xTqN6ryjlSLHNv7vy3fvu32XDFkoG+TblF0r/pv5pSSumpF5n92b7kgjMDN1fnnwpNfIQKBRs6szWgwNPncj9voFlQI/BM6qNZU8dkprVf3KFcO+4CpGQGNr4ADvRcqtGnloCDwoPIjJSTEFKniUy8qzH3nvqY+5Wf1nwo+KtcawZMNm2DKMVu3HPW3jm1qnpL5p65wjWFgiNQcBRLU8CASR32YI0wkvJCC0jNNYAglw5z2Tkf+rWQ9+TOuyAf6/cWPwRmCle+o5sFyEYxpYRsFfTZ7hnRsECEGDuH6lM2EegLbTRw+1r/DsW5ZpfnhQM5j4EOotIWdCQ5xQv+Cjc6eNkYRFoC1sTgcWDfQSRb9KAJBx5AKXlOcjiHJNWG50rl/xIPFf5il8s/mVPxxCxsQiMrSrSCTY68W13z+4MxI4WCuxcuKh9c4P7KVPnHMGWgVAzyoEBIGKXlNjlqfLRera2DG0sE2CUaKC0e4F15QXqylOWy79v+bhfLK7eK7sZeytzDHnbFaf8h86Ij3DKSXFggEqoYxUsYsGndvseLDN8zQxYQ6SQVqeRp05z3n3qL1Nruv6lp1h8ZmDXZ496USxwU+848fze5tRnbdady9oM2C8Mtv8e2y/DHBprQAIp0WKz6qsbzp3/XnfzIR8Obi7eEdvPnQbC7395sGKPia5PX8NS1H51S0QUGqiucmHMww8lCwa5z2y9UPT6L8CVEnYvVq4WMGYfGObdpk0AgG52zuWMk4ZhjjoziV2+GICnKMzK83e2kt6L5xYbtjFcy56+ontVsfGRMMyohMYG2uiMc6yeXXeLc/mSrwzxzU0ekbA8J1EoWOeik5aZA+p+bjLqCC6HGqGxAOL72quUJwOTiwKR4NBaLgfaePKgYFbdTfLyxV8DEZDP7+xgSu2f4Z499+1fq911NKFW/x3aZza3etsNfJ/HsOVay3EzbOyQiqQfM1dCw0ForCum66bU+8N52T+qSxZ9lAfEVX4P2m9Xz3F3xHseAgSePXt2Rl2+5AdmVubHOqOO4EqoEWgbTepRn9/r+NsBTxZIwkZtY5nZNHnt4RHND6XOW3gBikWD5bndX7wPbMW3tcy69apT7w6bU8ssiRSXQw3LHN+D3Mt7oLitI3Hma8NaG13vntF/2JQH3fNOzA3s+uz2++ZyAoWCdS5e9KXgwPqbjCfncjnQCC3H9kvu5Vjbfu0EgcBYLofapMRRenb6F/LixZ9DoWCRy+3URu5fAqutTaFQsO6Fi87hBncRgrDm3it4SqDbv7OyvOP+Ma8WCrBoz4n+UudLalP5PBGyhiIG78FakEBkLDyirkiIFCeRFyTKLM8p2T7oXB37jQloAzjyLWibm4qDE/fvHF9DDaKvrdVa62mZ/6euOOUnIMhdDcZ957lqU2gvGueik/7Hzq7PW8uafW0HJ4axLCKG/jcWr0Istjg01oZa2+mZq9Xli5ePxUglvEIYOn40M5dDbZVoMDPq/tN992vvzpzRMgsF2CiGZyIclyAUYKe+6cSGDWcf/mszLX2RDXUkrMY+dnYcPWNNBRC3DYjLoWZHNoUH1t/oXrzow2gvmt0SKXkILAPXnTJvejB/yu90k/cPXA7DQWE1lrG4+9ePgWfLlVAbRzSa2dnlzvkLL0ShpAcD+Me2OBQoFo1z2eJv6tn1/2zDeGEYiSGqjf2KxVagrbXG2FmZf1eXLPoeikWDfJt8eQispUstAGnqnbzdF9stRCR8bcXW8id3+3ejhleV5R33O1vL/ywcJUG7Xa+QQUSw1jd9etukehbx9qB7buuRcOWJHBreLbFLEBwaa7POHG/OzNcCQDzR7itjyWDYvXjtXDBHK2TFZT8w09LnOpcs/j8Ui2af3mM1cjmJQkl7l5x8mZlV9y/GD0O2LCF2MjkwWzBrgKOTXYIIighKECQNbPNZgDWYzZjapT8MzbTM253LFn959HahqK2xh89obP1gT953ex94JbPnY2jXk9rAtpRh5koYhg3uaf7cafd6bz76UBQKdo88WXsr/9pzAovmpHsO9n5pG91TuByEwC6E1faxowFYEAC5w/gRA9HtbMBjGkOKtbXGWK1n1H3eu2jR/9sNkULozBEIqMyfebOZkj6S+4MQgDOqOGFwdE2sAZjt9yCi+9jx+gfsxE6uH9pYA2vttOwNqdwJbbENkGOyX+1F41686N/s9MxVY3oGQ6+LgJH2C5H94jHaLwvJ5TA0M+suVRcv+uTO2n7/EVj5yHuVumjRO7nOOTZ2x9bWe5VSQvSHt+pbHn1oj/a6C5H707/hga+LLZVvU8pVYKt3w4AhCt6nzVPW8ubYOzZJjHq0PWibvHNt2pWwo4rHnRlTy0pCp9UF0eDZh5cvieAIsccvRQQ5dGCOdo/kcjkITXPqSvfCk84asyGplSheXrSpc4+fq+udL1ttDCxGX/VFBcyZPCko7ShylBQMotD2U1l3UyXcInzTJwLDJEiQ5yhKOZKUoNio7UzkOFzRoZmSen/mvNecOaJdrCUQUlFbC7m7z4eUELtayxIR9uzZCwVHCAi4r2iBpfZwDCkRTcrRmTq90/ET9U0H5SC09c48PafpF41txzYBeezTuLz4lJ066uCv6aneknhid3Y6fwAMVwlKu4o8R5EQQmgLUdE+VXQXVfRGUdG9FJiyMICQjqSUO7YxRCRgWdpQ63Bq+iveeSctHZNtib0/7oUn/YttTr+Oy2EIGvU+ImEliZBSklKOIimk0BYUmD7qD3uorLvJ174wDFJSUtpVcJWMBhfrUW0/kYBhNq6gcGrq+ubF8+vj8B/aqbgqFq1zTutrTL33OeuHkf3a+TMAuUpS2lFCOVIYBoWmX/hmK5XDzRSYPhFaCCEEpVyFYW0/yiIt6rmKK1pzU7qQOu+ExaO1/f4S5E5Ayc5unZ3ZkJF5y8w131IgIlE2mrqDPAAaiP3abQolg+U5ecSyJ9/37CniNbrRbeXKGLc2iS0kSbBdu66jo39yJeYsWQCCPfU2jg7JiFEeHIFGC5UjidAASp4x9cR5DVvai91AjQ6w73BRIrBbgD2PayNmBUH11pEZdoVAYABjbdWVlGVhATb17mdbW1t/1bG8qCdkQyyufKCvzH7Spp26uPIBjbryTjlSBAayX3fYwP5GBvYhVfb/xj6vK2/pCaErJt1Y52nPaaB0ZrZJ0dHwxKlw1Ckm7cxmGwfMj9bXjZWsBPsNqf+ZN2/e3auXFwMsi8+YSdYUmr8Lhos9GO8EgAXNsBJO9RP6BBEaHyE27cE8bWG0EAGvfcVWX4/G0CYw/N19LmCWINSzEll2HcUEIDSAsWb7wYoRz8vhchjaJu+o/kPrvoNC4e3ozElgH5zQHchx+M4lp5eneJdxf6BHFVcD3rmUEwmRcvAshfi9rNiHtTVPie7KRlkOe1So+3vLNsjUpdLWJYey3nTtOQdal4+GqxaxQ4tt2p220zFEIGgrrKdgGp3vzFk05+i1LS3+Tmwoob1oG88+tqm3wf24DY0Fo3oAODNDEJHnSNkf9KEvuFcE9rcoh09yWa9xAn9L/7rA1DUI1ik3bRq9JnKdQzkjj4MjX2ulWGyzjse+iU5SVrOLRBJBqG1Tau62+VM/hEJhWZwrr7oTIpqDmad4n7EZh7gccFX7xfEYTTlSVDRkT7gKoVmhAvMwlc1fuRJuKFf8SqMumzCVTmsn22ganDnCw9Fw1Kns0Kk2405js4u2t5as58A0pL4IYHE1jbB/CKw4gdjGi+ZebhtSr0Kl5rFXWqQdJbZWbgqXP/xElOOmsKcDmfFkC3d2FgPvVUe3C2fqQ8aTTfGesdilC14QyOLPABBlxN2jExc12GYqGucdJx9vHXE8ou1BMWKC9pSgbv8RGN7CU9Ovgx8O9zoSCMYYzrrTy0dNfx0eXH1btYR94/xwDSklZVflvTPvee728sFZlbZ9u/155a1Z1d/S2Gjr1eE2RW+xjryCU6reRvEYYoQhCbXhrNPyeIt3Ogi/nID0DQLtRZN+87EHBkqcz8FOt3StdJWgHv+Xqtv/r8pND/0eAAyGZg2NiI/RrQPwNKIiH19tbDu2qXJopl1nnA/ajJrPvjGoVvdUkOBAG9uYPnzNSdPOBq1eHsUzlGz55pXr5syZswBz5gBYu1s3aqYZko9KfvHNh9yHlPsaBNoM63dRbKXknsrdB9y1tt0/rEF6fvduPos5WLtp03Z9tWDGK2i7MBpDqi+4dMadf//NbrXfWsBvaJB989P17NAcnXVezSmnDQJvNhlnGoc7WagQOVwOtJ7qvc29cOE5wY3FW/bJOIomTuFn6PMswENONI4UJVKQEESiL/i516e/PPv6P9y3GvAHDIwBMPT4Zh/Qvb1l8AiAXwBA3ZuOmx7OrjtHZ+iDNuvM57Ku3iaCBAKtTZN32EvzD/onFApfGVWkxPNo/8z6dlvnTkVllNJyzAxHkgyML7b6/ys29nzLv+2xvw/9kYF76N3+recA/AnArQDg5k6Yj6mpf4IrrmZXpWy4wxjcfgOCA8OUUlc1nzX/i5sLpZ6qAjEOSXHeduwCnVWnsx/aqvaLwRCAlFJQb7Dc2db/xfKPOh7EDu0OAFFQM7bF9uspAPcA+N+6Nx03PTwwe55Oyw/ZtHMI+2H1ayeS7IfW1LmLvPMWvs4vFH6zY3/cHwQWYVnJTLn/0MburPo4G8uobdIrhhCCyjpIbww+1QMQntzLwPJCwaKtTfl3lP7qvm3hxXxQ3c+tEBqWaVdBeQRAWX54UiVSik/82TrK2ZQiVK+9aElJISp8A/vBU6I5fZodzQktgdAVFwK4FTP2zURFnqysXbu2jLV5AexhCYen0RMbxt/Vn3X0t/oPaLwZWfc4VBNZDGZJbFN8PoBfIgeguE8XKQKFkg2bvTNt1kmPZlyJYEgIKbeU/zW47g9f1NG1R+UuBut4FYY7ffJxXEdLVDKoq1jchhKunXnMzBu3Ljz8v3WT+26rtQGPIugIzBl5MYDlQ4QKR89n7R7fsqBDdi6cSYRr164t43kmEO1mv1uLVzqUGhhDPJBecux0ojee2B4CcF32nGNmhFMartAZ8XH2VAa+tlwtLjBKm8om414D4OdYXjSxDa2N3RhIC3TeiW8I65zj4sMgsopHm1kJkpr7xLbKleH3V92kAawG4oSpcTmtgUNKQ0M98iAgj8F6np0zuLdY3Ajg2uktLTdtWzz1i6bJvdKGo40hEmwssyf/GfPmfQvLSgGqnnlfaoESWFJ7vKdAo4qrsl5Pm8tvCZc//FB0jXkBrBA71Okbcv3AoA3AUhsUCk8D+NdMbuEPg2mpH3DWOZorxkLssNNBEDDGmKw7q2f6tNOBp39WfZHdJoCSpWzqHKQdOUrdYYYACyaojZWr/BtWfruq/YqSnPJo9itu+681LGq5qXLM1K+Gjd4Fo4oswLJDZOqciwH8Zke7PvkFVr5Ngkq676Lp7+OG1EyUg9qfHEwpRZv6b+i59aFnBrw1e/2+8XHUoFD6hfuuRR8PZ9V9hsuBjo8oj2LBSApfQ/SaB6MOPClWyYRCycybN8/7qxLtrE3kHdmhFUlAyj7fiO7wjhkvvfT8uqmpbUipJmgevv4jkhwYWEecXndm67TeYnET9sU2obYSAKH1FxIde/hZDKA9JzDlr6Ln2o6nM29sPcM/XD5mHDFtxH0CApqJlTwJgEJ7cWI8kY6zZPTc3GzgKik39X86uG7VF5FvU+icwaCiGeY53dF4F8A7qEVCvk2uv6bUhz+tf49z8aJenp7513hyEiMmB22IJZ1UZZt4zxZSAwXReUzZbwjLlsrYubCnveCVycAYalsqUYLZ7VZbFhfivXoG97UXNwD4T+ec4+7gA+p/bFLOfPjajjh8QSThG4s699XyvIVthh76TU29WPFiUtepd1olOU5jMmLxBClYhTaQz/ec7d/2yG8Gx06xaHdZpaIAHjmoojG08ZpSLzpxlXPJ4i08Lf0RDqpM9HEaAWTUoV5r48k+YUWVNiEUCrax7dimXsJrWFuqkmaEIQQLbcvuC1vPLN/+xMPItbgodoZxhns7+vVjiLIoRR6nda2y/9qHHq0/7ch/KB8+7V6TdY7iwFRffAowK/FGAD/D0ugtqolD66olPGrKG7bCcaRa1/sh/8YHvo0rWx1sPdSOsF8Ym/3qLpS2YBUuVJct8U1z6lKOEppXsV+W2BGnzps3z1vdXhy2RTvZg9wFlpVM3Zmt00y990Ebaq6ae2acvVeyLwzklu7PAqBxTYsQJyENfrDqP9Xm/lso7ar4ZEa1K7FQghCYtTNeXPenqP8WJz7kIzrtxX9f2LSIU85h0NXc+WzZcYh9uzK49aFn1q5aWybNt8KRiE+YDO/Mxhpk3EZ/qnPGQOfeBzIxipWoqxsIwt/9F4FRLBpc2xEi3+L2/7pjnSj715MjacR9EhFbC0t0UOrsBbMH3d77imUrDABYRYfDMlWZJCyUlKInfPGA3677THza0OzhxMUolDQYAstzMrx+1YfFNv8h8hwxsl1AMMzsyubuQ6ccMaSPYY+fy7LdODoOcOw129PXK9iFFbfBjBl7NnYKBYtSSccChHBlqxPe8uhjas3mN4iKXg9HonqgMVvjSEadOm+oCKrRYlK3tLS47IhToS1VnTOJLSkp5NbgnyNx1eKiUNLx2NnTPrJ9DOXbVPj9lR+VXf4Kch1ZxYYCgDWuYpt23li1TeIxpQ/KzGEpmmCr1GRgNsJTQvb53y/f/sTDyLe4KHYGe3QPBVhc2xHiylan5zdPbXbXdr2TQhvE1Q14xDxvmCzx8ZGtKo28v0jgSStxKGyVlEDMFo6S6PX/HNz4wP8i36ZwbYfeK/uVh0A+L4793v1Xye7KM+RIMeLQAUHAWEDSQc/Nrzt4mEdv0gusfJsAgcOZqX+xde7UaDKvYXjwQN6rcvBt/9Yn/4LlOTHOFcw5Ell50bR627tEj/8UPKWqJyFlCyWYAnvvmtKaSpxMbuINenzSj7LOeXAFVz3lwtEJLaFxw8C3ZDm8QYSjB8ODGJySF0a/vXT/ix3uXGAAkDDOPaSr3ifBMkOJlPFS0wdd6vtqKoy2wBQB06r3aLZQAjDmvjVr1lTi57y3/c0OlJCR/fYLNGpSYDbsSLCkQwAAGzYkObFeeTCu7QiRa3Erv+h8Tmzs/wAJEqMc6hEwluCIU3OArFkOvXiiXH0IHQZJB8MYVI01dZREj/+4f+Oqb0UJfDvDcbwKO7Bzobb5H6PQjB4iw0zGk8dFtqX6bocGZrAUBFvFCkRB8xBQP0ceAium770dvrYjRL5N9f/i8T8KX/8SrhopUkCIBd+c2a2zM/Ezpx08zUBrqwch6yOBRSPbSQpQaH87xG7tZWgPLNb9QnYAoezTXyIpouz/Iz/ZsqOkbXRm72jXJ6/Aykfeq2nnnDpbZ9TVHKVlqGFBZzCkEKLP73O39n0OPA6xV6N9UmcnbSx19oqXet4hK6ZMjqiSU4kEaUuiYm4e5n2d6DVre9GgdXbGKPHWqm7mqB0l9QXdXk/vrfH3aNHz6d9TOVwNt9oqgIQNDVipU1NvOOGgCcpzMy7P1mjeFtV/q2oEGYIgpcpMxMW1AhTFtfCoj9eCuqK+P14ip2QBgHr6HkZZhyAhdujrDCIGEQslGgEASxO18Yql2Bkil5Ph8oeXi27/CThSVrEXBGPBgg75xZuOnr2j12D8Fk3RRGmmZA+Cp8Qo1TisEAIqND8AMFCTcnznjWLRgEGV4kOrqKyfRDVPCiBgGRDiUABiNM+NDkMv3hgfeY1MBGaQoCjwfjzjYRkEpt/F492O9IUyWFCm54gDMmPwmo6uRpn6xjUR7ewOA4BsObgf5cFDWjvYL2YWxEKI6TsuECfvJLYgRyBw11T9SZt2GqOTJbU83M6WXClkJfxG+ZbH12JZmxxn79XwAZNvU+Etjz4mNvZdJYQcnoSUYeFIIfqCtbPXvnRX/DsT79Vpa5MASB5+4Os5482GNmZkOQI25EqI0NzVW3x0I5bnJJa1yVKppEVgiiSj9Fkjho1hbbMqrWeps+MP2x8FFhAauXMzQwjL5aZ97h1gUAcQkrW9oyyABYwFCZwKAmPZUjsu+bri+AyFdD+IAwwcwt/+IjBHed61nZoojMSTFW9vWQT6p5BU3V5YZnZUClOyBwysyMedeKJkR0xjMYr3gkggNBBlu2pnnqO9ZllbNLEb/gOq2lAiWAYJUT+7tTU1zPMzBDflbY232ES1ORCOhAn9N6EAi1k9Y8vqPralOVOo+6K0PbyjDUCcABSkmkZtv7mbNllYa6peUZQ2AST5tfF24niGYLBKOVsi+0Uj7Ve0cUzaGGekUZ2s3qv2oq0/64T5Nu1ePuqRzHGcfkgKIfqCbe6W/i9EwbGl2gqaOAlp+OOHbxCb+/9XpFxFg/FYbEkJCN9ct6a0phKXQZj47cGro1gLyrjn8WilfwhEhiH6zU0ACP+3YXtb9gQ/otFTbBAzg10R1SbcH7cJAUCM4TSVEPv+3pbl41zLvBGCRq4EiQRCbbjOO9K5+JTPgQp2MHleLif31lixsSQ0s9CM0V5g+8qOaUrAMJFiaNUo2+2RGJACRuhZAIAVK8Z/Llsaf62E00Y7FRKnSQjgB88DqHkpMzL2L6PW32UG2KZ76npGeoHi6+L+yotCm6B6kXWSHGhr6lIfTOVaT8FX7/QBMPJtKl5s7Z3YMqCdjX/SvNMF4po1ayoErIvsF4+4dvjaot5blHrXkn9FoaRRgMXy2H6Ng9YhDQgz+rVLHuGZm6SnCDtzBBRteZpzjc1IB2Wtd1nNe+8UloHrKNEVfK3vlj9twLKdJDurJgYLexjwOhD0Xih9yLtqyTFho3ca+rWGIyT1+j1qrf/NMAq0nAxig9BeNI1vPnpKryffiNDSiNMscaA0+oJ1zU+Fv14HMEolgxIYzBQSPS6vPKUDDe6JI3ITEUmElpFSC90zX31kUCg8NVCQdL+aHCTTTg5BCliG4zlb933ajRUCgCVgJRGdxlXP2JFEaKyZ5v27uvKUeWJr8MmgWOwc6n/DsjaJFQCWluwY+z0DQH/2kI31G597je8ZOSI1pQwZSlO6218fDIyLhFcusRgQZf9FG7iAjIvDj3AeAWx0tubXY1mM3rMBAJq6+6O4q0KNryUIAkIGo5bqNuwZv98bOdfAAqBK8dAX5Htf+gtJcRSHeniiTgKxsWBHZsNZ9b92L1uST3Vu/V53obRl+3xXNV0D73KeA5DpKv/EhHRfoEOGcYbfgQd4ZW17nHu3jWjdQQ9eSYvAPmKFWFjVfhEJNtaG07wvqPecMl9u6vsvv724eq/sVzz/lNemX6qf0XecrxwamVo3ADwXjaZv7UYAKJUmcR6sgXT47Scea7Lu27kSF3GsofcKSkrR629Kv7Dtf0MGgcYsaGgvBQADJUsMZE/rutAcOaXDeGqmUJLktuBr5XseeXGnmW33qVexTaJQMv1TM29A1mlGoKt4otjCkYK6Kreu6+jojxK0xrEA0VF4TRV9s2j0TrTVBoi1htOOY6dmzgHw2YHcJ/vHpLCBkIdQa+gg3xFAYEyVFBwEw2wC3Rf9dR8G1sVeAer170DW/cRoSW4ZEByE1jZ6bxOeeIu6csmdFHJRbOm7z6fH/j543Lm0g8Ed8DoWCtWNVrFoeoBndzp3VJu6El659PczbB2iLbHRKlHRxPcVjrJ675vP2oWLnMCjetHzbRKFohZ6yZ1WiaMQYmTKCSKCNmykyPDU1Bf6XzPtA87RpxRFn74j9WT54a5CYRt23J7M5eRADqlRRBcDQNdtj21DlNhzV+N/VPtl+4Lb0JS6arRwIWYIo42leu8KluJ8ddXiX1LF/Eyt77+vTI+vHdV+7Up0lUq6J0qmPCobq9ivyZoHi1En/5NTSsRZ22v5UZYcIWlL8KXuuzq3YFmbGmO2dALAmdOOOr5/TdiJ1av3/DhrZ072/ba4PjXlhHaeW38/9fqb6573/2trPi9QKEyO1Xx8lJ2z7tsNxduDVVYQ0teg3uDGEfoh9sKpLd0/Deqdz8CRKdgdkt0RyDKDUs7bAXwOy0qm5ivC8fLuYYZAAdpcKXIgxohszwwmSSS06U5tK78QRu2z78RjsWiQzwtdKDwgr1xyr230TuWKHqUMBAlUQmMFudzonQXGWZRWZfnuJY8j5IdEYB+CwR+bXuj+28ZCoXe7wS2NXOVGsYPRuNjVNmMhSX2QkFA7Ihvs9dhrrRe830oitlXyzRERDLO1obUpeSDVOR9A1vlA2Oi+pBad+ij79kEZ2gep1z551m0PPF+sFlA/kFwVw0QL7fIwwmgOizjQ35zA98hGv9M2eEexr0cLNxFcDo2RIkvpdA51nDN1bq+46pQnSNtVIuQHUQkfn/YX/uu6QqF/0H6VMO72a3IJrDg5Wur8hScH9d4/jpY1d/y0VeRxET3+Sw3rN391S+S9GougiSJYDp/nBfOm/lrNMZ/Sq1d/dY8T3sWxLpVicaX3zpOusmy3bb2nowtTDpUAJs32YPack2eUJb0RoaERz4XZwlUCPX6nXt6xKhIYw9rCIp8XlULhOXXFkt/ajPvmkdnESSIwjJQ6NvuOhS199NCTNdsmJBbI5SR6eiRyuT2b1AdyzVxT0igUg/Q7Tny7n1Fvq95vozIaMLy65zdPbZ6QupKdnQQAbjn4YJBSD1gpmA3zKLXfJBjMFW1BALsiDaVOJEEnsmWgYrC5ado6cdSpTxPzo8LoR9yAH53yDD27tlAoD+u3y3MSRQCFIcYqISFh31KARS4ne39UfMq55KSv8qyGD3CfH4DIrWLxoxCQ0DJH9fgEp8QsKPEmJnoTaws0Gv+n7zl1jTD8Z2XwRxjxsAjCJ8s3/eE52jG5ar5NxR7uPbfl7TmBjmKoDl/4obDO+xULwbA7s1/MUXJQgB1ZR2mxiAUtspZBFQcbmnmtOOGUZ6XFw4D5o+uLx6eV1v5lTaFQGS/7NSk9WKYhdQ27khBlTq2pp4yUFLK373+23Lm6e8zeqzi7vHdR8+Xh1Ox00VXJp9909C3l5cUXsGwPBUGxaJCH8AsPXDvYxfdtrbqd32+hZIKp8s3IOPWj1IK0JIWg0N4MwFRvyxUCAIuQryPLb2aqWqrBcNpRYZ33dgBP1mqbkFj2xu271208Z86c9IbTD/qnoM79go18VdXuzJIUQhj7OwNMTF3JWMiXbyg+7F588r9gRvbLhkMDwwRRdctwu5C2zAi0ZQYzgSBJwpGzIWk2hFhqmWEqISqteE4df+oTMHy/7AtXNjzS8/DG9mLvMEMbxWQkQishYV9TLFrkcjK8r/gR+brFx9OUTBuXwzDWAjSK0Ip0gma2WlsgtgGu8CDoCEhxREh0NmkGBaioq0/9izL0IBnc53X7f+j98QN/jsJcSpFnvz0nhnmGdtN++TcX73QuXlKgmZm88UMNy2LkafYd7JdhZqvtQCVJliThyjkQYg4L+geyjEpF89oz565R5uDHRcj3Cb9y35TfvPDouvZi/57ar8kjsGLvj3f+wjfqrHr9Ttx/4+a9IkcK0V15oe7pLd/akocYY3AtASU78/RjspvqnI/ZcsCcdZoxp/7rIJw1UKx2b1YYg51p0rDUAiVmwReOfppGSOoPdLqrfHNP5G8d2QZxx6xbv+HurtSszTbjNLO2I0rKWMMwitsBfHrctwk5yrlijTnFe0erhZcKSdrde14aCG3YSEIdQK44/kVXnM4Z99C4UG31Cu9EAhVtna7wxhCYuLJHxaJBW5sKri99Rb1zUUpOS/2X9QQ4MBoguZNUKBT/+0A7AtoyDFvEoouJJDxxMKQ4mIAzTEZhS5u7Vp2y5HfCtz9rfGj1PRsLpd4h4z3xaCUk7FuibS+C39D40tk9rQcU7ZTU6bYSMizreM6lUSzA8INNlhnGMkLDHJ1hFJAiBUULIMUCYlxqPBj5nlMfF6H5leoNf1amhx4G4rltT3Z8ikWD5TkZtheXOZcsITR7nzTMQLgL+0Uj7BcjtAwyPLhoFCSh5CGQ4hAC3kKBwvpz5/1dhYf9RvQFtxx844P3rC6U/N259smTpiGuWK7rvc9YQTzqUdTx9F5JQaqsP73lwdXdcd6lXX9oPsqPtfWA7LttnXcgjDXsh9o2pd7ivHPRhSiU9F7lDyoWzeQSV1EVc+/sYw+xrjiFA8NVsxm7gmRg7+v52aPPIp8fzYvHWJ6TW+5c3U3G3la1dE6UV8ay57Skzl94Igg8LvmYhrw/awvd6P5HOLvhrnCq+7ugMVUaePk7+Trw56A5VbIz6m83M7Lf1FMzV9mUcygH2sCiurhi1pRyhOg3v+gvPvRoTWunjYVS1Ef1D1d9Xr7Ye5aomNWUdhWUiEr8MI9thTZotEgNGt7QWlRCw5VQs2Vr0mqOaUpfFE5L37K57cgnnEtP/kz6dcceOFhGZP9MKJuQsH+LrE9CbO34a5e+9r43yQ19n5UMTWlHxXnpdNUKHdU9RAIU2wAiAWZGYCzKoWY/NFaStBl1nJma/qg/PfuQuOrU3zsXL7oQA8lQ9yT9Q3v0e+H378+LF/vOl755IbJfRJHtGpP9osjrNcx+8VD7ZZnZeuoQ05i6XM/M/uJv7zn1T+5lp3wse/oxM1AsRvm4dmG/Jodxa2tTKBSsc/4J7bbBa+VgH8ReuVKInmC1//Ta67E73qtlJdPYdmyTyTr/xtoyQBJM0lq2tsH5Svr1xx+AlpaXz8SRjxJ+mimpcznjerDWVBkQLBgQA9mMsZOcNHHgu/LpOhFUKT0RPx/2FEzGaY/E9/iXTmHL1ho74sU7+cpDf04bw0GouRxohNaOunpitlCCRH/gi019HwGPc33LvRHyuZwMlj/888Zfv9jqbKt8RAX2OXKVRMqREDQgtiJjy2P0NEUpQ2OjBYHQWi4HhkNtbFrNNdMzHwsWND7mXrr4k62AM8xrm5CQsG+I0zaAweF1f/hY6oXuE2R38ENp4FPaUXCViI5xsQaziQUXj8kCRKIrEi0M5sBYWw61JYatd0410zM/lO997QOZdy1+QyxUdr+we2y/wh89cHP6sRePd7f516iQ11FKSbhV7NeYr32Y/SKE1nIl0DY01qTVEbo59ZnK/KbH1MUnf4g5ziKwE/s1GUQAYelSi9ZWx9Z7y5irZ+gZ509kIQRROfgMVq0t75b3isD9c70P2jp3BrSxcSZXQmjY1nlTw4NTX4sC+dpeHgIrLrxpXfUO5moFQsGQQlFf2O2sK/8iGrw7EavxaZCTnlOrUNFPVS/7QIK1gVXinHnz5nk1qjUm9u5FEiAVrdxGGUfMFpJYCCnFtsqVwa2P/BntucmT2ys2UltWr+4Orr3vv+pXPX+M2lC+zOkJ7pSh7ZWOkpT2ImMrKcquHRksHRmvMZz6GzBYUcCsteVQGyma9fRM4U/vPfV+963HHzVkJZuQkLAvPVnxDkHfTx/5k/7mvRdl1ofHyi4/L/rDx6QFKOUoSjkSjoxrMAyKFjPGhdcQwQUg0MYG2pi0OqHS7P3aueKUL4HhAHsusnrvW73Rv/befPrP/UfLjf3vVn3B3SK0ZekqOSgWBVF0vSPs11gWjGpgZ8VWAm0cMcvOzP63+55Tf5s6s/XgndmviRcB+TaJQsGqI3CZbUzNR+S9qmHNQbZwlKAu/+ljnnjgxth7NZZgY4FlJZM9/ZgZJuu+n0PNw+rwEUmuBNpOSZ/jvGNh+15vFU4K7xUECOyedWILXNWKqNDojqfjDLmSKbS/6r0zLo2zq0l3sHSOXS6qlX2g2PORceY+3zrlFACD1eD3E7PFYNZwpBAkpNrY/4Hwhw/+APk2Ncm2fwdi/Qj5NrW1469d4Q/+cF34zXv/0Xl2c4vY6J8ntpb/T/QFfxSB7hNCCEo5itKuIldJKKKRRncn4nHAWBlmWw60zroLzUEN93nntv5DIrISEibQBuQhkMvJnuLKp/W37rvGfuPe48VL/cfLjb0foq7yLbI//JvQ1gpHSUq7kejavvDiQRuwS+ESL7Z8ba01xkxL/bO6asntc9vmppDP0x6JrNh+9fzmoc36+6u+pb9x7xuc57YtEBvL7xJb/O+JvvBPIrT9pNQO9kvE7oKx2q9YKOrYftW7S8ND6lZmzl543GAb7sBEB7kTULKzW1szGxozH2Njd1/F7oH3ighClPU1HR0I8e85OaaEj/k2ASrpyqXZD3B9qhHlYGR2eYawzExTUl+uazvit70tLVv2y2zkg8Qn+JqdtyHjiKr3TCChLTm9+iYNICqNsyuiAPhUj39Tf1Z+DCJyJQ9/9mzZkcJk5AUAfoMcJkvB612jiMhxlOwL1oqt/f8c3PTwz+Kkq3qSXjEPegnb2iSWLrWVQuF5AM8DWA4A6Tcfe6BtSh1uXHEMpDyWFY6EEK9iwixOKQlJUdiksYC20dbCjkGxQ/oMQIorobaunKpnZ29zz209MSgWn9q/x0tCwn5KARYoxjFFbQKFkg6LDz0K4FEA/zMP8J4767jD0OAdZTxxNAl5NBQdZgXmspJNcJSEiKtdaQsYtgBbgKqf8BNRdn7bF4Y8JfOmFw4/6McoFN6KXE7swSJ0hP3yC4W/AfgbgBsAIH3OiXOCOnEkKTqWlVoAiRZIzLUkZsFTkiVFboHIfnEchyqqOnsG7Fd/qG3KOTA4MP3L1JmtiyrLOp4HhtuviRVY0fF/vfGK1KW23j0Yo9epG695xJCrhOiq/Dm8YdVy5PMC7WNI5JmPvVd/OmZGOeO8lwPN1ScOEgiN4Xp3VnBo85dQKLwzyv9R2j8njGUlky9AfMpBuzVVaoJFRakl9wfryut6fht5IIpjiz/Lt6meQulZeeXiDjSkThpROifeJmRPnTG9raUuPuo/jpXqx+giHvmMdxaUyUKASPMG0Vf5ntfZ+z+99z26EbkhGe0nu++tVNIolaI+35kjtGwgXFPS5TseewHACwBWDPzw9JaWuvLR9QcFaX0EXHmMVeI4JhwPiVdxylGWGQgMg9mOktBUcWC0yah6NHs3obX1JOBMAxTG8TknJCTsntAqRfFZeRDQJtA5g1cXiz5uf7QTQCeAn8beEWTfdNx005w+RKdUCyReY6U4DoJfzZ6ayio6UARtTJy6pppYcbg/CE1z+iz30sUfCK4r/u9eHAIabr9WtAlcPYPRXjTlWx5cC2AtgHsGfrh58fz67kOmHEJZcQSTPIaFaGWJYyDpIJtWig0j2rVhW3W+F6S4EmhT583GLP09EF4feeEKk8KDRUDJNp59bFOPJ/4jDhivebkBwSC3L/iPMqDR2TlGMRd5r4LLM//OWacR5XD02ohE0lZCo6ekLnQvWHhzUCj9YsJPje0JuZwEFc3n2084ASnn1QirnB4EW1JSkObrUersjcbeWIlEp/Dtty3RSbzjhEoQ0MZwxp3VNaf+dQB+jrY2idI45Y5yHUliN+dxJnCgUf2EKxs4SlKPf3/2T1vP6l7VuSUcaMf97dkPXdEOGTrIxYILAJatMBuJetGJPwP4M4DbAGDu3LmpDadMPzpMOaeRI89iV53MKSXjhKWimshCRWtuSh/vzTeX+IXCtydNeaiEhFcuccmbQedAJLgGFl0LZjC3F03vnY9uRFQl5iEA1wNA3Zmt04LpaqFx1ZtY0jmc8Q5ia4HQVA//YSj2Q2vSaln2LSfd1Fcsrt/rxfSAUCwNcZJ0DrVfJbOZnu7BSjwO4PEB0Ti7tTWzbYHz6tCVb2BJ53JaHW+VkghCU11kCcWVQNvG1GnuBSeeHRQKt6GtTQ3MUxMnsJbnBNqLpvdd3r8i682quv00rt2FDTwl0RM8XL7p4Vsw1jI0sfcq1dF6cJh2382B2fUJRwZZgE2j983GU44+uqulpSv2/uw/nqy4I+p6t51TCigHZuT2IAn4GqI3eFLmjmth6RCxHtM9MilBrC31VNZQVgXsKhc7ZhWPAujZpuV5AG7H1TN4cMDsjeGQgtS28s/Z4gnrKC3A1g55QEO/xqaFLINVxUw39eoKK8mJh/6QayUBawEljuo+yJV4Y5tCZ4knlbjaWYxTDsCTRd7J9pxFcYjgKtBIo9s5g9cUixWsWfNQbHA/lzr/pFNMvfNRU++eYUMzsvbZYPsy63rnvQC+u996fBMSJjeE5Tmx01CL0e1VLLiKI98zlxPbT3qXbG+hYxOAXwH41dQT532i+4jmC7nB+4jNqIPjKhdix/EPY42tcxrCqcG7AHxhYHdrt+xX+07y6u24YCygqv1aVyz2owMPAngQwGe8CxadZuvVJ3S991oOQjss7nrofC+IbdZ9P4DbsHSpRak0oR4sgVzRZt/y6pnlOu9qG+rqLrhx7lzSMrxy8PF+gNHZObag6QU5AhVteKn7HybjZsYkBKOtQm3qUwf2zdNfRKFwWbwq338mjkLJoK1NWdecDW2A6gciBFuGaU5fv8cHE5jZCgJslROKIGm1IXbEGQ1vaJna3V7cstcrG7AlQVJq+qr//fvvBranch/t6wAhAPVPS6bYKanzR3gxCQRtNdd5U52+8P1hofSJeHt48jzTnYm9PYtvq2Z0KXKTrxBYVjIVeuA+AG9237XoY7o5/RlrbBWRFZdIcsXR7kUL5wWFh55JYrESEmrglRr/UIVqi8hB0bWlUOrGg6u/Udd2RNE/ambR1DlL7Sgiiy2z9uRbAXwBy1aYeBE3ofbLp1X3ALjHuWTxf5vm1IdstUN40XxP1qHF6Tcfe2C5UHhhwH5NjMBaHomW4JL6j3Cd17RvvFeOFD3+78s/ePCu3fJetRetlzt+Xph1Lsbu1EYkUvC15inpS73zWm/2C6W79pvtovg61dxgsU2lDmdtRz/ZSYBVUuy55hE0alJZAsEYg6zbVD5wyusBFKuubPakSyhqRL5N4e9QOAS7fr8taYlT6zXd+sLnZdqcZ6r2AxJWG0ZKXdG8eP7nNy8r9aKAiY4nIgDcemWr86hX91UWYhqixMs09BGyJ4V6sftHwY8e/ule9lNGocAALApxX2rZQEGh9J/q0pMP52mZS7hqrCUb9pRi1z0BwDO1KpFU+ymMaaIvgaTgPYovnGxkMoRdbONLZgon3C20Lz/M8k5bhEGwO/TBeDzLt7Uu5bmN76PQWGbsKHBAFpWG0Ll667X3dO1lrdShootwZavqvbZj06G9+q1rFs15Eq48ANoODxlgEjCWIGlB/cIjm3uINg9pWm48+9imvgMa/s+6wttx5UsEy44Uosd+VX97RWnc7VcOCNuL/yquWHIYNaXeCj80PNx+EQxbpFTKTq9rAfACOnMEFCfAg5WPvFepc4+fG9Y5V6LWSUUHZj5jIXqCZQwMFr0dk/cKRWvqvE9yxnV3WwhaK6ySrKdmvjHz9GOOWQ9UAEz+AN7Y3csuXWAdgSjf1048VHuVdZ939c/MRMyuOB/A8vErMcMGhZJGWxtw/ZgEm8ZLORkWVz6qrjzlTmr0zhghFAjRIYcGb1bXqxovAOFbkyWeqMubLhiV82xaNUHb4bOCZVDagZEcBbCOZ2LXgfQL+bxIPf6L/yrXOReZ6ATR8FOjHJ8QEPJV+7UoECLYxXqCxtLt93goEWAVOSxi2077YRvGk5NNObPgSIyYjIeYHUuyPGGimYZ4X5Qr4vkN41raa0ccx+Ehz3qk4qRANqWG98ENsT0XfDinnLdZgZHhzkQQvkF5k/9RAF3j2iuv7QhxZavz12s7uuQxM7+DrJOHNmZ4mqPIDkGIBv+g7HQ8hM3IgyIPExBWVNoKcYFNOYDh4ffODPIcUHf/rwCUxt1+bWhTYJB4h/8FW+eebatV6wBbSCmMxKFD59B9n1toQY5A4LApnTcZN8PRlgHVcHAYSikhuoPf+jc9+Dvk82M7BprPC7QXrZs7Yb6t897Bfrj7QpBIcGAMN3iHbplT97koV0bbZM/1QyiU9OzW1gwUnYXQYh9s3+6sDSVCQyxxeuaMhbMG855MILK3/N+RSKl6KIPYMnPG+WcAaiBR64TzLADwVvhaw9cBKqEefAW6wr7WJFRfTdq2WLQoFGzTi84aNlgPIai6h4XBJmzeL4XVk7FBJbG1ehMSwVoQ84GNbXObauL8aI9yxYXCOxhKpmC5qm0lANJMYkd6PDlRymmNy2nZamtmGAsr5EsAgKVLx9/buSIe7ylvC41mKy0zK5miqXUHbBeHNdR6Shw86lkwAkBUzppX9Y9iS334WiPQlWHj39ch/NBQqH3u9yNhvmyc++bWQ6O+KPEwmWrhIFFWeShB0lWNI9pSCoa13ajo6HqH26/ovkgENbFfpZIFgZ3NPX9HRVcgBxeII9s/pdLD1lP73HvVXrT15590OLLqQuyJaNn9CZpEyFDd/jXYHe9V9HNsG9y8TStnNGM1hs9XtqK1afTelzr/hLZJn4C0LRKAm4+k1yPjzh7MVj+Rgs9abbNuNpzhnIkoqdzEtF+xaJDPC/+mjhWix3+QPCXifCnDRDVCY229d5R7wUmnj3stxT2k8c47LUIDEBTAcQb6+AUoIigoNQ8AY0FtClGXxVYVZ20e9VGDxH59epAMbx7l1qJtBE82+4cdeBQ4jlMZf2FCqHcWwlUYpZ4cwTIosNF1TlTR8Z3a3uiaWOLt0fGTEfMUQxBRaHzV2/dC9K0auI1mRNdhBdaTtQCjWlkvg5REmBGtAKgWZb3iWd5GbSJOhLXVBAqDCMzcs/7uuytDfJqD96GU2ELMCoCzw/h3wCB2lUdNdODgibvxZMCLZjizs9mELSOMcwINJa2cPhJUQeSZHW6/GJIFKejwKNTCN5yPry0lFRGL0byHDEbkkJgogRU9NPYz8tM27bh7LFp2w3sFTwnu9e+sFB8e+95s9HM2e8GioznrnIeKtnsVI2atYEmsG7zvzDxmZrYmq9fx4upoMBrPudAqEe1Fj9a2tXhV/SwQAzAuXRANoKUTF5uzYoUAwLLX/wKN1nuZwZJg69Q/RxNfy0ROYgxm6gBCWH4RglAltkJwaMEunYmWljo82TK+CX9zOYE8RPchDYfBEdNgLFdN2cAAC7Vuv1RWsbeDLD9DlkfrF5ZdCSPonSDwuE/GkTBmdunCKHVPlasgEgg0uK//+XjVMLna8cpWB8WicS848Wyu814Dv0p4AjNDCsDaNZXbnnwx1lfjP8bimqFiW/gCAsMQ1ZNOsmWwKy5ArUI/cjmJZWDnnOOORUq+BqEZeSiMmCEIwvDzAAzy+SHXGj1jDu0aBDtUIBnSN60rYVx5PgqwmPLX8dUGS6NPkSRbWQhU8QAxCETaaNnnbx7S/gyAtty+sgeW10MIVIlJibyZLr0NgIzHwfiNrc4cIQ/BTXXzOOV4VXULAWQZpOMF1op9LbBicZNuP2Ghzro53lvRMjbfB0lfs7fVX7YnE5Nfpwom8lLs3cAhEhxoY5vS87Ycd8inJ/FWIaG9aBre0DIVnjqdQ0Ojbg+mHFmTV/XdFYnAMDlyifemBYehULATVky7VDJgUHBzx63U4z8FR42spUhxKYiUOj37rpOOQaEwsV6sZUslAEjLj0DQyABoIgFjDNenZjkLm/IoFCy+daUaNyPVAokCrE2pq21KUlUhTSAyFkKbZyetZ2WnE0jkYSDfPir8wdi8HdtZWt+wScvL3LOOno9CSUcnTcfDvra4aC8a9x0nvh11qYU8InEvosTAUhBp+8LMjduejedeO2lsz5WtDq7tCNOvn3+Abkp9wzLzKJrFkhQsAr4/EhNtqibiZiD+Z/361aT5RURneXasmyrZ15Yz3hL3gpPOjXYoWtxxbZcpfxUgME/Nfpo9JavORwyGEEyBeTRW/GKIvrIAMO2v+As0r4MUNOI+iBT80Nqsc0Um95pWXNsRjtt95CGwbIWZ3tJSZ13xLoQGI0QeA5ACxFg/9aVNLw0TzctzIlr12ychaOSin0gg1IbrU0e4Fyz8KNqLBvmcM072i/D6KQIF2NBT/88qgep6gCRrC+bwmaFew30+SYX1zqfZk7TXomUs3quUI6gc3lr+accDWL5b3iuTbj9hIafVW3fj5CCP/I9tNPmyAUDWD30zJX11+pwTFk7KrcJY9JVnNp3OWXcKjDXVVsEEQG0r3622lm8V2/pvE1vLt47T6+fCcFg1xsBaY7OOa2Zkz4m+MWHFtBnL2iQALcr8OSGo+mkbZsspJXxXfhAAIzcJvCsV/RthLFXf8iVhg9DYqd6/ehct+n+46toQACPfpvZYzOZyMgryLwZue+tbud67fBRvMEMISRVdVtvKHdGkUNy/BFacUiL48QPPQNvVUFVX6QRrmV2VMrObbp46b14DCiWNK1v3fDLIQ0Ren86g7ozjj7LTUt80zBZc7VAKW1KCyWLl2lVry2OqG7rzkRBtSW7YMFBDbvdecf27QYF0bUfonnVcS3jEjLs5rWZDV0tuHPVVERqS/eXlNRbjjOU5iVVryzD2PijJo8SDgZmtnZr6pnvG8Ueh2BngylZnLxeBhLY2hXyecG1H6F588ofsFO9M9qsnvCRASG1JlPnuKm3CWJ6T6zo6+mHMA1Ci+n1YhlHCrcyoL7pnHdeCYmcQnaLLyT3sn4R8m8I1sCDirYubvmbq3Vkwxoz0YLOFFEyaH1vXsa4//szoHgbiGzX/WkS+our2S2ujp2evcS486Z0oFINB+7WnYyuXk1ieE7jq2tA778TL0ehV1wNRvkYiX2/J/vWlp2P7ZYF9lQcrFi1ee+s/hPXeG2LvVW3FhSCSZaO9ruCTGqAxe8Lj7Zyw3v2UcaVBOTQgyEFlMfD/Uer/eO0dP3QRPXoGxT9FBGIQUfQ9ZskphWB26qeNF5xybNfhxS5MplOFA7EPabqAKRaJw09rWLhKiF7/GfPtlW+oxUWrf1p8l21Kvx6VEfF5BMuwKScH4IvRNuEE5ZgqRF6sA5au/fHauoOXIa3mjshSTCQ5MGw91Z46+4RPVNqLaycst1MpCrRvfL73ni1Z9yVknJlVTmYRLKSFteH09Fecy5e0ZFb3frSrUNoWTeR5AawQ6JzBaClyHPLCQyZ6AvJR7GJcXmdgQZO6+OSLwnr32xytm6tEj7CFkoLKZmX/LR3r4jQq+1+KhvjEqAj5J0bKjwM7nJTa7s22tt49rue02fc0HFV/Qfe1HatHaWOuIqi2J0bEUhu1U4dNnb+orTzVu9F6ohlRMmSq7iVkkn3BcgOMsW7ozgarMAAYv//9nsXNDclB1Hj2sU19zXVX6LT8BKdUA3xtq27JWbZIKeKe4El/3SP3RBtLxdr1lbiNZL++iRvsebbqtisEQsPGldP5VfW/89550kX+tQ/cPThbfLJNYUXs1RjLc10QlXdBqaRzpZK89Yoln9YN7sdtWKU/xZ5JdgShL3hx6rPh79cNmeB3vA9V5h/oBj7Hjrp9bKxNqVeZgxrudS49+X3hdcUfDf778pzEk1FCzqr3Ue0eCiXdvHh+fdfR075s61MXYxSBCAIEQLJifqYBDNs+L0T2y93Y/auKp3rgiboRSakBgoGwkhnTMzd4l53SUnf/xs9uLpR6xjS2GMCyPGHFCoGlAAqx/SoC3qVLrg4bnC9byxZcbXnKhhwhRbf9bVdpzba47qzZdwJrQLQ0pj5llQRMyDUNQWLWlHKV3FT+cd/yh58YesO7FIKFgnHfuegt4fTsG2EskHFVFBwSP8UoyiE6UsoArI2OjVpricgnYy2E6GVjmZToYm2ZhOhiYzSk6EJ3UJGOCFkFh6OAB+PJZDIILEKxaLLnHDOj7IjXcWioigi2JIVAWd/MzIT3/6OLU+vHJyj53h6Fl+o1lZ+/nhpx+oiD0USSQ8NwZat71nFHBYVC5wQmo2Qsa1NrSqWKe9gBX7L17pc4NGYHjzDBWM1ZN22mBlcD+AjQJicotxMj36Y2Fkq9ziEnfcs2pvKsq03+AFsIZmN5aurdva+WZ7hHLPkqbej9iV8o/B07q0RQAA8NNGaA0heeeIqp9z4YZpy3mmiccPW4oGjuF37w9cjjtmL/qnqwXclaAJBduNakwg9aKbzYU08jRJYfGl3vLOw/pOFB94ol/yM3h98vFwprd3nfwxIjllCXO7HFb3L+X5hS7zaOQCyuqsbYwJWCeoI1M/7y4h1rGQTauxOu3Oun5wBp/6hp0uvcGL3XnPgf1w75wTnb/2jWguScObztuJlZv8GZDU+9mhy8rs+lf7Rp90AbGiAYRVxFey6WQEr1h58MStBoz0mghrkFB0ICFvTcqU5Vz3CddzhXSTbJggihscaTM7k5dZe6cskN6PO/qm98+KExpWnZIeHl1BPnNfQcNe0tP8u6H+Ss8xrrawtgFKcEW1JKSb9y7bqOjv6qqWHi+zj6hOCOx7LiGVvnHY5qSTMFCQTaGldM5VT6JvWe114u+oL/a3y4++64HuyY76Gx7dim/nmZc7a56mOmzp03qrhiWChJojfYmOop/9SPTrKbHT1wfe3F9c6lJ19v6rPvQznQwI6VRUAwgCVrw+bUR7e9bmbOPWX6V+XGvp+UC4UXdzq2CADi/FclIA+Iz73zpNNM1v23sM59vdWaYTBKXCNIhJZkb/hNDQwLa6y9wBoQLeef8BZd7y1BUOuCzmAIEtQfaGzq+3QsHHZLCIrQHC77/G9zjx/AlVtsxTB5aqMoh0yO3GIDE0LIHkJYQcgVguilih/KlOyldb7NYnrvxqeeZaxf31/NOxXEr6hTTpKVepTA0+ip2Tdzxq2rOhgESfQHodzs/9AQMfII0T5uE6EFwJlTjv5lT53azGmnGdoOn5AtG2RcZaelzwXQOaHJKCMDQNnngu93p9THjCenQ+8oICJRaD152ZTXH/rZrYVS94R5LAslgzxE3f36f3vSlSt01jkAvhk5kUWeV8GV0BhPHmwzzheEKwrqqiV/ECHfC988woH+m9pqN8utLwW9QH+9oLRubk7rrDcdaTkfrjxJuXIpe/I460qgou12T++Iid/Ac6TsqjwafP+BW+MFx/55krAAi+U5WWkvPudcuugbPKPug9wXaIgqsaZEkivaaiWm0JTUp4wnPyyuWvJ7EfLvuD/slBW9Rm31t8r128K6LJe7Q1vHs6fIMFPXTCkxj9PiNdZ1Xlt2aLFJOw58DYSWd5KvzkohlOjT+bWr1pb3TpiQZG1gUuq6l646xWcAOHX+2H6TGSwILCgDIZrYU2CJ6PSVHxowiVHvgVlTxlVqU9/twQ0P/GwfJW5mtOckOouBs/Dkf7f1dAsTdlxMbfcAhYYtEWxT6iJKqYvku5f8EQYrhK8f4QqvVr3hOrl5WyXTk+7b2NBtsv1uPeZmKCTVbNLuHPLEAqScE7sVTjFpZw4DGFWYDAhnR0jZ7b+UXRt+KRhdODPac7Kjoxi6Ry76iKijn1lBuurJSCIBzWxh2GbVaZRWp21Z6jynliy5X5T1KuPzE8rYv6ttlT61sTtIkR/0pjN1elpd1mRTc5Bxj4KDth6XlnLanc2WgcrO5n225EqFLv9zXbc9tq2qQGwvMhikTq981qbVO42nGqrmZ4xsDNlKYJCW82yd82WTomvUlUtWiQAl+PoxDiprnF5/i9jUFTY5sm9rv1tvD2lUoYMDKO3NhydP+rQnlrIrj7ZKYrAOYfWDKwYpR2JLueT/+KHf7JjEvPYCKxItZOpTBSv2wcTCbCjlKLGx/4bg9kc7d2sQxmKn8uOH/mdk7xz7krp/5C8TluVpMEXEruomTQhLLVBiK+U7qyayYzbkOUJu81cEdzz6bA22cRj5NtVVKG2VRy6+jRx5aexlUcPXrxbsyHMBfAbLSqamSf3GcL1bC6Uu58CTv2vr3I+yDoevqggEbbStT03vmd38LuCvX53AxKOMzpzYek+xy5u+8HKbdu60Eibesqu2XSARWsvasHVkBhnnNEPiNGgLBBpmOvfDHBYKQX19bDMg4bGiNLkOIAE2DA4NV9nqHXpFHAUrG6u29F2tATv2AuyTlPaiRT4vwrtvXiZddZapd+fB19UnF0EChplNaK0jGiijzrSgM7nRA/ua9exsHx85RfeR6Ge29SRIsBRZuApQArAMDg2iMAaSo6ZTiYWJ2FL+ZXjjquvHRZgwYNKqOQqHGbsZG7hEtvEuQBgaBOBoAhtlEosWV5rSSolt/l8zL/Ve0pXPCywr2H1yFjtOllu+vnirunzxckzLtNv+IASRU2XcRFdUDg0LkjbrvQZSvMYaBoUGgTY+Ds6E/UR9As26bLkBAgRBdewqQEWhR2wsEGoTn60bdfxACCtIKNGrr9x6T0fXToVzfB/BjcVb5GUnX08zshdzXxiCqqROiYUKAm2YQTalDkZWHGya6HyEGkFow2BGyqfDm/wegQAW9VDksZIOHAkQgbUBgl3dA2tKOUpsqzyk/7LyK5FDpur1W7TnZPme4oup6YvehwPdHxprw53bL2M5NGwd2YiM80YDeiO0BQUeDNs+HNKs+0n0Mdt6SCEhRQauAiQBxkT2K7Cjl/GLD43Isi7Ljf3vNQzCsuETUm0F1vKcRHvBOO86+XzT4B0/akXqcfVeCSH6Ql9uDT6lARo4art73hyIUYOoV8RfZwwJIhz6GYWqCcg4dj/GHX2STQp5CBQK1jvvpEO0JxYjMKiyMgAxSAX4XqQOarCNE8eAOX3BD4I67zKmavErhuGp4zLvOPm4fvrDIxNafiiqLUnOS8FXTZ1zNTuivso2mIgSj3rvBfCNCRWFxaJBW5vyf1T6tfuukz9sZmW+YPxQw0KOErMjAAJbZvjaxjF5BEmSlciACCA0Ysi2OQ9OmIg8EaMbVoaAEY6j1Eu976/89NGV+00pqV1KDxBWPt3jHdiQ8x11n3FlFqGpLrKi+E3JhpmNjhddJNgRAkR1IAITmsDx4SVmQGuDcCAaZCdtPGQCk92Vv3nrKheH+bwYZov2Bj1wQbvTODz0zmlUz8DQXyBoZBxH9oVr5Iu9b+y64/GtOOFxsRelXPZk7Fjk86Lx7puv6Hq1nM9N7rFcDquLrIEJngEOtAUiGcAgAVd6IOkBVDdY82agGY21MMZGdxU/V9pJuwhokVIOre+7Jvjhqp+PafwUixa5nHzV7x+5as1p8jDdlDqFy0EIjHIf8fPh0NoozjS+NiUcOMJhorrBbm9jj1oQDtzDzkUzs4arlOgLN9e9GJzXVYJGvihGVeyxQKz8qHijd8miV2NG3UeMH4awUKOmJAHAhhkDY4tArEiCVLaK/WKEoY0F/4AndXTPoSSWUkhnS/nyyu2PdqJ9ZPvXUmARnmzhlpYW95mUKjAzVw8Qq4H3qqv/ev/Wjr+MOfaqmqt/f6yDtsdEW20mK8+1KTeFyg4lgaIMu1L0h+uzW+0dle1bZOMvABi04ISHVz7aeOqfkXWOGhEnwGxM2lF+JnwHgEdql9hvTFgsz8n+9uI654BFP8T0uvfaHWMD4iPEyLpHpi848c1levA2tLUplCaofE4pSg0QFEr/rd61KCumZZdZYQBtd1YGavhEyIiMEXbwdY5lwhxwq0shpZJKbih/0r9hVezZK+qXxXAqFCxyOdlfLD7qnfuat9GBDT8xnqpjX+tYDNFoQmvYmLMDaYD2pI3BABuRdhT1BM+Jv3b9Y++vH9+E1o7xi1ukwROBtZCpDLCBEIo85YjuYKV6rueCyi8fWbMTL0eNhXOBNq9ET6ZJvikQzXfaRu9Y2x/owcVEdaElMHQ70TJvf6TDnmvkoQeJsYwfEkIIVzripd7/Cq9fld+N8cNoKfLqIvzGA7Nv6T+Sb9NN6ddyORjwNI1Wc1YMi9lkjhM98DArMcZ7YAAaKeXI/nALres7s+vnf/zbmJ5rsWiwPCf99uJHnUuXSDSnPmy0BgyPvgU5cmztrf3SUEJJElCb/XdXfvCHH43W/rU76p5vkygU7DOtDZeZRrdqYOC4DwAphOgPerMbyv8JBuHJIiNhLLOuBQCr6DyumqCQDRwF0vbWzbev7KlZ3hkAWNYmOzoQCl8vJylQxUsmoC3YpXPR1qYGYqEmrOmiPka0ue8r1B+EEGLkCowBIwk6634AQG3Keuye501jeU7qH6wqyHU9F4vQdlHaVQBsnKNq18+WBv8Tg38awwIIYEMpR0rDZfVi75XB9fd/arLUa6yJt/Bnf/y1+3z3UtEfPkVpN1ppM+sxFGOmPWtjMJg1JBGlHSW7Kr93nt18avDrx5+OJrBJfHhgQFQxm8Hrt1xWm/s/fdw3f790UFxNmMcaFnmI/l92vpT9w3NLxebKT4XnKDhSELMeJXP+WJ/rGCQzGzBbSilJlkO1rud94fWrPoLlOblb4ye+j67SY9vm/mb9G+SW8rdJSQlXCezZfYztHgb6JoEo7TiyL3xEvtB7ir7lj6t267m2R1648Lr7/43W9b1fGq5QypHgfWC/GJbSjhLadomX+t7hf//+ndabrZXgIaBkmxfPr+es+jgbO76ZVUe5eeEqocr6m9t++cgaLGub3MZkshCfxHPfevxR8NTxCI0BEw3m8IoO1oN8zdxbvgFAjZNAxgkbe8MfyXIYQhDFAyfOKUaA1hqeOlTN7F8MgKuWHNmeg2z770aGI/oaJawbH6O7PCeC2x9/miq6CFcKMIc7fCbBD7XJyFPT7ScsHPBwTOhzb49WguGPHvyB+lv3QtVV/qkQJOJkr5EIAJsxCIFdTQo2ei8AnpLkKCn7/F97a7tO9m964NvRpF8rcUXDn/mOfYBrvMVUinLd9d/6x46GB55YpLb0f1lYBJR2FCTR9goGe3kdgxMLG6hYmGjb5Wwqfzz81v3/ULmn87k9Eia8w9gZzxcGqzfouK9ZSCJ4SlLKkcLwVrm1fJ18vrs1/O7KT3QQQuQh9khcjX4N0dfd2WocECePrdmmv3Pf250N/ZdJ3/wdKUfBlSJ+zwGRsrfPdUBwahARUo4UjhKqO/i1XNt7sv/DB/8Pub3ZpQGtXr3a19++/0pnQ//bZb9+hlKOgqtEPHb3/j54UBgaSCKkHSUtldWmyn/NueO5xcGtj/x5D/omD2wX6htXfVU813ei7A1+IZSI7ReNn/0aaH8ASDlSKCFkl/9ztWbrSeFND/x4V4vD2gisfCRueg6d8h6u9+ZUjfYf75WPFJL6w62qz/x3lL2plIirMRHFmvEU7zKudx0IknCEgCOjlxICGU+Jin5a39SxChylc6jtKjEvguLDT1tfP4iMK6GGXI8jBIRQyDoCje6lADBim9AyQQovun4pt/+uFJDCgSsF7Dhuj0cxdeT2h18QoQFc5Q77zOhzFWddGTZ5HweACU08OlRk5XIyuOPRZ8Nv3f92d2PwWtUb/EQaLouUo+A6Eooo8iLGE+GA4ar2Gj5hGggiuEpQ2lECgOoPVzibK2/VX7/vTf23PPrYPvBGpOHGz3xEH1ACgrx94snK58XWjq1d4XdWfiD9kn+C7PK/I43dSilHUsqRUCKOxhnSxjzGNgaAeGIh15FS8zq1Lfjfuue7jgu+t/I/QZEg2N12Zsk0og+P18tVAq6KKjekXUUpRwkphNR2s+rVv5ZdwXu8Nd2v1t9eedngBMygPVkwM5nRr0PJSBTxblYUicUJ8nnh/+AP19Xdt+Z42RX8i6yYJ6RUQqRjkSIGF6q7O3Y0AIYigutISjlKWg5Ub/DL1Cb/jPBb970pvKXjj+MwfiLHRy4ngx8+8NNpP3v6Ne5W/0qnojukEEQD90FEg0Jj7H1z+z2kHClSjpQGW93u8JvpDeXW8Lv3fWTNmjWVPRbNA2Mrl5PhbR2P62/c+xZnY/kfVV94h7QcxtcuIavYr7FcP8PG9kuKtKMkw6o+/Su1uf8M/a37zgpuH/AI73xxWIsYLMKyksF9RzabevVhqw1HR29r6r4ywnWU6Or7Zt/ND6zH/JfhlkOtiIKuCaAjqD94mgJjh++1wwAkZV/4DQMYFGucdwYYzIPkls3Xg4qZxr42NDTYMIpPIWI+ZN68ed7qQskf6iEVLgIR2CetZUUjYnDZwkA4mrsCYPhhhb2cRPsLhUfdS5d8Xzc6iznQhnbIM8VR7Oer0q8//oBye/HFeIEzsQuBYtFEhzryqBQK9wK4t+G81sMqWe9s7YgzIelYuHIqO0oMnhjboYIJD/jcCQOZdkHGAn5YQUV3Sm3vUn740/INDz0c/wJhGajWcTRC22dQ1h4CPbxPW7YgIWRo/7pPGj86bUvI5URfsfg4gH9Kn3V8PpzmnWWVegs59BpIMYtdR0VL3igh2Y5r7yhumLafR7AMBBrkm7XoCx+Q2t6SXmt/1X3Xqi1dwGCC5z0RJqJP+LZiniYV5/4bT4y1AG1l5q2C6e8EfkoGeMLtCh7vufWhzQCgB66/pch7009URZSJ9NOianUZsCAil7m7DOxuzVAeKIHVVSxuw2NrvgTga9mLT2kLHD6LHNHGhCPhKQ9KiMG8fjvGLQ3OmnEYEFF8utIAgdkEYx4T1v5K9PEvghtXPq0jjxxhGY3X+Bn0Bq0vFvvwnfXfJuDb3rtOfm3oireyotdD0HyklMtKbG+46DoiozuwP0U0aIWJAQQG8O1GVMwDTmB/UbeRf7759pUvBtv7pt3rXaYh9ssvFO4EcGfdeccfFdRlzraueKMlHAdXNsFRgomG2K6RRRYG7oEYgDagQPeybx4nbe/yusJb+pc/+FjkQMoLoICxtP/4y57YZeZcsvgaPSPzCS4Htc17xWAogvTNlszTG+f33PPUloGTwIl62j2buos2m5D25Op1EYZe82gu7F3HNNRicQHsajuckMvRpDwtl8tJtLTwsPQbbUdMUwdmWyDdV7MnD4UUs2H4QChyeEjcAhnLzGIzsX1RGvwVYfBn6gqe8H/+p78NaXFCe07sq3vfRd+ZmD6dh8CCHA3d1pny+kMbK9OmHKlT7gIrxWGQNIeY57CkNIvt9RTIMhNTF1veBGPXClCn0+d3Zp8oP7Oxs3N7EsjlOYknizwOIRJUg2cC2lm7D2TcXlYy43hKsNa2gOI8gnroB7pvOeZVXJ8+0no0nwQdapWcQaBpTJxmEY8HApMByNh+ZmwEY40IzV+lrzvdbeU/d9/VuWVY23R21tJ2EHLDxycBcN/aehjXOS3WEUexxKEsaCZAzZAYmpKGhYbPoPUIzXqy9ilUgiezL4RPdN33+NYa9M0x2a/s6cfM0M2pVxtPHsWS5pGkOQw7E1KqocmsKbTMoE3EvJYs/1X4YacMwz+Vi4+9sDftT+NuPJaBM+e2zgoOyD6lHVEHw1TTs4PMBmlHqvX9n9TX/+HlGTA7OZiIBJmTp4zQ2GcQ2qfHx2slAtAmtpdi2csn+Mk2NS7v9XKCQVFNy3Fql4GYvuJky683qt0mtLeLwe39zhm831z7rgRKywYatzloQHCiZPdhTPH43kdtRPO+sV+D43TP2n98hU+cFsG5fPH/6ubMB7gc7Ozo9zh5rwRkJdxc93jXEV33Pr4t8V7VbKXH+9k1TYQHazJ8du2MLQAsmMF4cmArpQAsi+9lIJHu0AmzpUYr1f2/T++8jQFEiX+HtPGyHWo9AlFOvqVLbVxqiyegH++NI2uy9IHaXU8eYnvdyFHGzsBzBYAFnTRQ2HgSCU4aXv9yyH0sK8TXH93sJL2HMdgvBpYtoxHXPg72i8a1My0Du2ceN88c0vC4cYQDywTU1ntFaUc6G/v/NbjuD1+ssfeKdrjf7R1rIEM7AGzYQFha5bcXxLE+Ax1z+wZGIgYTEhISEhJeQR6L3SMOqFSXnvRDO73uQlsJRxZjHN81kIUjSJb1i1M7Nx+5cWlnf5xFfXwESz4vBlXuNbA1lEH73zZYQkJCQkJCwk4ZHwEUnwjI5lqPrtR550WVv6nGdQ6ZhRJC+ebTG0udvVjapoBx9F7tsHdLAA6eOzfVf0hWldNu2m12vV7BGWZKK+mkrQ4bOOV4HJopwnFcY81UoUSKQ9sMR7iWzRQWwgOjgRyZEr6uZFa/8Lau36/ZFhfcTOJTEhISEhISEoE1UvEEDd41Nu0qRCcHa6mtLFwpqNd/9qAXN1y3Og8xbqVbGIQFLU5q0dQv6qw60hqrYHkqCeE8z6YeQigwsv3EDkAeCyIjBUAuWNCwo6qGBqQZD7x3VLKJGbbRQ5+YcwNKa96CfJtAoVSrOIqEhISEhISEfczep0+ItwbT57eeGE7JfJGjpKK1zlJtyVFCbq58bNPPHn8QS9skSmvGxwPUmZMolTS9+oApdmr6w1bRIezImaxoOjuygaWoY0keS6E4zu7FzMyWGdZaGGuhh77M0L8zbPwKrUG9d5Q6dHrGfuX+u5BvU+N2DwkJCQkJCQkTyrhlVw8bUp9iV8Yl32sIs4WrhOjyVx9w70s/QD4vxrXw8EB22BtW3SRf6v2sIAEEOkBoLcJYJBnmuGjnwL1SXAxTAqRAo75k/DMSgGP9QJvp2X9Lndd6AQpREd6kSyYkJCQkJLzSBVbsvfIuXHiazbhvYD80+8B7xUREol8vW7NmTQULOsc/SLxYtMi3qfD6P3xcbqv8nlKOG6et3bE4597tg1qSlq0JZ2S/nTnrhONRiGqXJd0yISEhISHhlSywotICFKbdz1op9kEEERt4SlK33xH+cNWPkM+LPSp0OYYPAkoWDIjnNl5M/eFWKEFjrDI+dgiE0JJxVcY/MLW8sW1uE5Yvt6hdEe6EhISEhISESS2wcjmJQsG6Fy58Kxq9hQj2hfeKIAyDtlU+AsAOyz813hRg0Z4T/q+f/rva3H+JIBIQYvxjpAQJBFrbem9e/7wDbwIRI98mgNpWb0xISEhISEiYfAKLYu+Vo7Pep5iGRCPVCmZDKSVFX3CrWf7wPeNQSXzXFIsG+TYV3Pzw7XJT5UvCUyqqFD7eupEUl0OtmzP/6Lzr5M/H8VjJVmFCQkJCQsIrSmDl2yQKBetcvLidG7wF7OtanxxkCCIq6zC1of9jkcAr7puUBoWSwfKc/NgP/vAh2VVZiZRSYB5/YUek4AfaTkt/OHX+Se9Igt4TEhISEhJeWQKLgKV2zqI5aU7LZRydGqztdhazIU8J2RN8t/fWR/6M5TmxD2ucMZ4scoFgxUs9F8p+3R3FY42/z44tSWOt1dPS382cc+KxSdB7QkJCQkLCK0Vgxd6rjS0HX2wa3HkItAVR7YKyGRZKCNHrb3Of61kGBuHJ4r5NyFmAxdtz0r/tsb+7mypXCCIBohp4sUDQFtoVGX+W99OGRS1TsXy5jaqDJyQkJCQkJLxcBRYBJTv1TSc26JT8D9Z2sGJx7WAWjhRyW/D5vt8+sR7Ffeq92k4cj1X+8YNFubXyNUrVKB4rCno3tt49rLygKQp6RxL0npCQkJCQsD+xe9tP+TaFwhpjTjnoQ2ZK+q3wdW1PDg6UxOkL/6b/+uJFuOQDFu/7+sSVkymtYSzPSfuzTXfJZjqDM84caGvG3YNHJBAazQ2pI5zDp2ftl+//Na5sddCxLsn0npCQkJCQsB+wO8KAsKxk6s5snaYzzoc4NAxQbbeuCCyIyO0OP4rSmkqclmEi6/UxnmxhdHSEcr1/gSzrPpK1iccCkeJKoG1z9sOpCxZegGs7wiToPSEhISEh4eUmsJbnBAhcnup8hOu8qZHnpoaxQcwGriNll/+Hyo2rivskLcNYKBQs2tpUcOtDzzhbylcJKWoTjwUATNJaa8Lm9HedtyWZ3hMSEhISEl5eAisPgVzRpt909BzUO+/mQNu4nl4Nr4wgtAF3h/+OifVajaQUpVCo/OihG2lT33dEreKxCMShJeuqFM/I/KSu7YhpSdB7QkJCQkLCy0VgLcgRCKwPaPiYzXpZGGvjeny1gdmQ50jR4/9U//jBeyeN92oocX6sWb954f3U3f8YvBrlxxIkONDa1DuH+ofPSILeExISEhISXhYCKw+B9qJtOK/1MJtRl++bpKKCqBxUxNbyR8H7MKno7l7nky28du3asnyx/wJZMf1QAjWLxyqHWjenTnfetei/UShpXNmaxGMlJCQkJCTstwJrQY4AcKU+lbcZ5cLa2iYWZTbwlKDe8OvBzx59Fsva5ISkZRgLhYJFvk0Ftz/a6Wzz3yOklCCujaeNSHE50GZ69kOpC08+Pwl6T0hISEhImLzsXChFW3PWyR17rJnV1GFpjKJsj8UVLCmCCMym7LObj+o+ObcNhQJjssVg7Ui+TaFQ0uqyk79tp2WvsOVAg0jVoH0Yiqww8FPPdb+2/9Y/dkzK7dOEhISEhIRXOGMRS4z6us9wSglEZXFqCFsoKag3/HT3XZ1bgBVi0osrIIrHyuXkIS9ufB91+U+QpxTVpF4hCKEl64iMPzvz07pT5k1Pgt4TEhISEhL2J4EVe0ZS5x7/WlvvnlHz2CtmC09J0VV59pD7N12LfF6gUNpfPDOMlhZefedqP7Wp90Lp6wrXKh4ryvSuud6bW5k/42YQURL0npCQkJCQsL8IrJYWBoBwSurTxiXU3HtFYMEg2Rf8++rVq/1JkFR094jjsfp++sif5Gb//bWOx7LlUNvmzOu8S05Ogt4TEhISEhImGdU9UrmcxNe/brMXLHq9bk7/Bwe21t4rg5SSsquyIvz+Ax/Zb+OKSmss8m3KfO3+h+WRs+ZxQ/o4hEbXpBg2kYA2mutSS9xXzVhjvv/QH5FvUyitScrpJCQkJCQkTDDVJ/7Ie0VBnfyMlQRQjb1XgiB9Y51t/r/v9y1aKBnk86L5+b53i27/WbhKwXJNRA8zSWO10dNS30y/beEJSab3hISEhISEycHIybitTeH664178UlvM1PS/8KhNjXN2s5sKOVK2lr+cXDjQ195WZyKmzFD9P38d76aM22lqHMusY4gRKlZxzdOikAwDHaVw454Yzab+mFwx739AARK+9H2akJCQkJCwssMMWLKXrrUtra2OjblfNpGYdq1DJ5mSEHUF/SpLZM6qejuUSwa5NtUeOsfO7C1/CGhpKRaxWNFQe/GNLhzK4dPXx7Vh0yC3hMSEhISEiaS4Z6pfJtC4Xqz6bS5l9pp6cs4qP3JQUo5UnX5nw9ufvgWLMhJvK/z5RFDFMdj2a+uXOUcNauFG1JHcy3jsUKjuSF1mDNvRqP98v2/xPKcRLEz8WIlJCQkJCRMsMAiLF0D9M5O0yHTilaJBhigZjUHGRZKClHWLzWtt+eX3/G8xvteZoJgxRoG8qLx/lW/9qemc5x2pkFbG6VWqIHI0kZTvbfYO2zm3/Qn7noUuZxEZyKyEhISEhIS9jXbvSn5qCSNWnDQVbbBOxihsdF2U61gFkqQ6PY/tfn2lT3xttbLSwwQGJ2dtOXB1d1ed/87pLYhFHFN8mMBAJM01nJY7/xf5sLW2SgWTY23eBMSEhISEhJ2IrAIhZLJnnPMDM64/8baRL6r2mkrA1cRbat06h8+8N39LKno7hHHY/Xf9McOucn/sHAdCUI4RpHFO33t+B8B0Kw549QZqPkAgPZckuU9ISEhISFhQgRWLicAMKfSJ/CUzCwQSUghYonFIBgABuAhX1nv9MU7/HnoSxBIkECf/lcAwX6XVHR3KZQ08m0quPEPX5abyj8RdZ6LqHU5bt9RXkSjvgQR5A4vIkLWdURf+IK3kf4EBqFYTPJiJSQkJCQk7GOiGKzOToBB4fdnvSCMZiFFM1mbIYZLJIgECRJCkBSCBAkIIUjK6O8y+rNQMv6eFJBSkCMEqYGXFMKRgpQUpJQQREJuKn9T37DqS8jnBb7+9Ze/CCitYeTzYvpvH7sjaKLZLMVhREiR5UhKVXkJazUsDFm2Q1/CWkvaWjJDXpoNAb2you/1Nve/q/fnD61Bkq4hISEhISFhQhh1GzB91vEHaAfTWMk69sM6eB7gSgIRg5m4EjQDJAADSAmZdgHLBEHMvm601qQG3kukXQACIGIItqon7Kj8+MF7wSDQK0oADHrqMme0zMKUhgPC/j6gPwQcBwgBIP6zJhb1qW0QPgOpHd6mAmyrAJXh31XSKff99on1O35WQkJCQkJCwkSzfB9lAn/lBl9TTbOt5/MCeSRxVwkJCQkJCRM62e/s+3kQOnPVf2bDhtEF0tJdfGrnDN7vs7WPR9vn8wQUxu8dC4MB8AkJCQkJCQkJCQkJCQkJCQkvH/4/Iv7spY0s9nIAAAAASUVORK5CYII=" alt="AR Studioss" style="height:30px;width:auto;display:block"></div>
    <div class="header-right">
      <span id="userBadge" class="user-badge"></span>
      <button class="btn btn-secondary" onclick="openSettings()">⚙ Settings</button>
      <button class="btn btn-ghost" onclick="logout()">Sign out</button>
    </div>
  </div>
  <div class="nav-tabs" id="navTabs">
    <div class="nav-tab active" data-page="crm" onclick="switchPage('crm')">📋 CRM</div>
    <div class="nav-tab" data-page="leaderboard" onclick="switchPage('leaderboard')">🏆 Leaderboard</div>
    <div class="nav-tab" data-page="finance" onclick="switchPage('finance')" id="financeTab">💰 Finance</div>
  </div>

  <div class="page active" id="page-crm">
    <div class="section-header">
      <div><div class="section-title">Editor CRM</div><div class="section-sub" id="crmPeriodLabel"></div></div>
    </div>
    <div class="toolbar">
      <span class="toolbar-label">Period:</span>
      <select id="crmYear" onchange="changeYearMonth('crm')"></select>
      <select id="crmMonthSel" onchange="changeYearMonth('crm')"></select>
      <span class="toolbar-label">Sort:</span>
      <select id="crmSort" onchange="renderCRM()">
        <option value="none">Default order</option>
        <option value="editor">Editor (A-Z)</option>
        <option value="status">Status</option>
        <option value="deadline">Deadline</option>
        <option value="revenue">Revenue (high-low)</option>
      </select>
      <span class="toolbar-label">Filter editor:</span>
      <select id="crmFilterEditor" onchange="renderCRM()"><option value="">All editors</option></select>
      <span class="toolbar-label">Filter status:</span>
      <select id="crmFilterStatus" onchange="renderCRM()">
        <option value="">All statuses</option>
        <option value="Assigned">Assigned</option>
        <option value="In Progress">In Progress</option>
        <option value="Need Revision">Need Revision</option>
        <option value="Done">Done</option>
      </select>
      <button class="btn btn-secondary btn-sm" onclick="addColumn()" id="addColBtn">+ Add Column</button>
    </div>
    <div class="table-wrap">
      <table class="crm"><thead><tr id="crmHead"></tr></thead><tbody id="crmBody"></tbody></table>
      <div class="add-row-bar" onclick="addRow()">＋ Add row</div>
    </div>
  </div>

  <div class="page" id="page-leaderboard">
    <div class="section-header"><div><div class="section-title">Leaderboard</div><div class="section-sub" id="lbPeriodLabel"></div></div></div>
    <div id="leaderboardContent"></div>
  </div>

  <div class="page" id="page-finance">
    <div class="section-header"><div><div class="section-title">Finance</div><div class="section-sub" id="financePeriodLabel"></div></div></div>
    <div class="toolbar">
      <span class="toolbar-label">Period:</span>
      <select id="finYear" onchange="changeYearMonth('finance')"></select>
      <select id="finMonthSel" onchange="changeYearMonth('finance')"></select>
    </div>
    <div id="financeContent"></div>
  </div>
</div>

<div class="modal-overlay" id="settingsModal">
  <div class="modal" style="max-width:560px">
    <h3 id="settingsTitle">Settings</h3><p class="modal-sub" id="settingsSub"></p>
    <div id="settingsBody"></div>
    <div class="modal-actions"><button class="btn btn-secondary" onclick="closeModal('settingsModal')">Done</button></div>
  </div>
</div>

<div class="modal-overlay" id="confirmModal">
  <div class="modal" style="max-width:400px">
    <h3 id="confirmTitle">Confirm</h3><p class="modal-sub" id="confirmMessage"></p>
    <div class="modal-actions">
      <button class="btn btn-secondary" onclick="closeModal('confirmModal')">Cancel</button>
      <button class="btn btn-primary" id="confirmActionBtn">Confirm</button>
    </div>
  </div>
</div>

<div id="toast" class="toast"></div>

<script src="https://cdn.jsdelivr.net/npm/@supabase/supabase-js@2"></script>
<script>
  const SUPABASE_URL = 'https://qmryoypkjkytrdfqarip.supabase.co';
  const SUPABASE_KEY = 'sb_publishable_siFsXq2uc0D3lsFTvsp12A_5gsAIbKf';
  const db = window.supabase.createClient(SUPABASE_URL, SUPABASE_KEY);
</script>
<script>
  const SESSION_KEY = 'arstudioss_session_v4';
  const POINT_TIERS = [
    { min:1,max:5,points:2 },{ min:6,max:10,points:4 },{ min:11,max:15,points:5 },
    { min:16,max:25,points:8 },{ min:26,max:40,points:12 },{ min:41,max:60,points:16 },
    { min:61,max:85,points:22 },{ min:86,max:120,points:30 },{ min:121,max:160,points:40 },
    { min:161,max:220,points:55 },{ min:221,max:300,points:75 }
  ];
  function getTiers() { return (data && data.pointTiers && data.pointTiers.length) ? data.pointTiers : POINT_TIERS; }
  function pointsFromRevenue(rev) {
    rev = Number(rev) || 0;
    if (rev <= 0) return 0;
    const tiers = getTiers();
    const last = tiers[tiers.length - 1];
    if (rev > last.max) return last.points + Math.floor((rev - last.max) / 50) * 5;
    const t = tiers.find(t => rev >= t.min && rev <= t.max);
    return t ? t.points : 0;
  }
  const STATUS_OPTIONS = [
    { value:'Assigned', cls:'status-assigned' },{ value:'In Progress', cls:'status-progress' },
    { value:'Need Revision', cls:'status-revision' },{ value:'Done', cls:'status-done' }
  ];
  function statusClass(v) { const s = STATUS_OPTIONS.find(o => o.value === v); return s ? s.cls : 'status-assigned'; }
  const DEFAULT_COLUMNS = [
    { id:'rawFile', label:'Raw File', type:'link', adminOnly:false, locked:true },
    { id:'editor', label:'Editor', type:'editor', adminOnly:false, locked:true },
    { id:'revenue', label:'Revenue', type:'revenue', adminOnly:true, locked:true },
    { id:'points', label:'Points', type:'points', adminOnly:false, locked:true },
    { id:'status', label:'Status', type:'status', adminOnly:false, locked:true },
    { id:'deadline', label:'Deadline', type:'date', adminOnly:false, locked:true },
    { id:'frameio', label:'Frame.io', type:'link', adminOnly:false, locked:true },
    { id:'finalVideo', label:'Final Video', type:'link', adminOnly:false, locked:true }
  ];
  const DEFAULT_DATA = {
    adminPass: 'admin123',
    teams: [
      { id:'t_siam', name:'Team Siam', leader:'Siam', password:'siam123', members:['Siam','Raian','Mehraj'] },
      { id:'t_riad', name:'Team Riad', leader:'Riad', password:'riad123', members:['Riad','Nobin','Kiron'] }
    ],
    columns: JSON.parse(JSON.stringify(DEFAULT_COLUMNS)),
    rows: [],
    individuals: [],
    expenses: {},
    notes: {},
    split: { Rashid:77, Fahim:18, Siam:5 },
    pointTiers: [
      { min:1, max:5, points:2 },
      { min:6, max:10, points:4 },
      { min:11, max:15, points:5 },
      { min:16, max:25, points:8 },
      { min:26, max:40, points:12 },
      { min:41, max:60, points:16 },
      { min:61, max:85, points:22 },
      { min:86, max:120, points:30 },
      { min:121, max:160, points:40 },
      { min:161, max:220, points:55 },
      { min:221, max:300, points:75 }
    ],
    rates: { summary: 122, split: 122, expense: 122, calc: 122 },
    monthRates: {}
  };
  let data = JSON.parse(JSON.stringify(DEFAULT_DATA));
  let session = null, currentPage = 'crm';
  let isSaving = false, pendingSave = false;
  let selectedPeriod = null; // 'YYYY-MM' key representing the period START month (the 16th)

  function showError(msg) {
    let bar = document.getElementById('errorBar');
    if (!bar) {
      bar = document.createElement('div');
      bar.id = 'errorBar';
      bar.style.cssText = 'position:fixed;top:0;left:0;right:0;background:#ff5252;color:#fff;padding:10px 16px;font-size:13px;font-weight:600;text-align:center;z-index:99999;cursor:pointer';
      bar.onclick = () => bar.remove();
      document.body.appendChild(bar);
    }
    bar.textContent = '⚠ ' + msg + '  (tap to dismiss)';
  }
  function clearError() { const b = document.getElementById('errorBar'); if (b) b.remove(); }

  async function loadData() {
    try {
      if (!window.supabase) { showError('Supabase library failed to load — check internet / ad-blocker, then refresh'); throw new Error('no supabase lib'); }
      const { data: row, error } = await db.from('app_state').select('data').eq('id','main').single();
      if (error) { console.error('Load error:', JSON.stringify(error)); showError('Load error: ' + (error.message||error.code||'unknown')); return; }
      if (row && row.data && Object.keys(row.data).length > 0) {
        data = { ...DEFAULT_DATA, ...row.data };
        if (!data.teams || !data.teams.length) data.teams = DEFAULT_DATA.teams;
        if (!data.columns || !data.columns.length) data.columns = JSON.parse(JSON.stringify(DEFAULT_COLUMNS));
        if (!data.rows) data.rows = [];
        if (!data.expenses) data.expenses = {};
        if (!data.individuals) data.individuals = [];
        if (!data.notes) data.notes = {};
        if (!data.split) data.split = { Rashid:77, Fahim:18, Siam:5 };
        if (!data.pointTiers || !data.pointTiers.length) data.pointTiers = JSON.parse(JSON.stringify(DEFAULT_DATA.pointTiers));
        // One-time upgrade: if still on the old coarse tiers, replace with the new finer breakdown
        if (!data.tiersV2 && data.pointTiers.length === 8 && data.pointTiers[0] && data.pointTiers[0].max === 15 && data.pointTiers[0].points === 5) {
          data.pointTiers = JSON.parse(JSON.stringify(DEFAULT_DATA.pointTiers));
          data.tiersV2 = true;
        }
        if (data.tiersV2 === undefined) data.tiersV2 = true;
        if (!data.rates) data.rates = { summary:122, split:122, expense:122, calc:122 };
        if (!data.monthRates) data.monthRates = {};
        const seen = new Set();
        data.rows = data.rows.filter(r => { if (!r.id || seen.has(r.id)) return false; seen.add(r.id); return true; });
      } else { await saveData(); }
      clearError();
    } catch(e) { console.error('Load failed:', e); showError('Load failed: ' + (e.message||'unknown')); }
  }
  async function saveData() {
    if (isSaving) { pendingSave = true; return; }
    isSaving = true;
    try {
      const { error } = await db.from('app_state').update({ data: data, updated_at: new Date().toISOString() }).eq('id','main');
      if (error) { console.error('Save error:', JSON.stringify(error)); showError('Save error: ' + (error.message||error.code||'unknown')); }
      else { clearError(); }
    } catch(e) { console.error('Save failed:', e); showError('Save failed: ' + (e.message||'unknown')); }
    finally { isSaving = false; if (pendingSave) { pendingSave = false; saveData(); } }
  }
  function loadSession() { try { const r = localStorage.getItem(SESSION_KEY); if (r) session = JSON.parse(r); } catch(e) {} }
  function saveSession() { const r = document.getElementById('rememberMe'); if (!r || r.checked) localStorage.setItem(SESSION_KEY, JSON.stringify(session)); }
  function clearSession() { localStorage.removeItem(SESSION_KEY); session = null; }

  let autoRefreshTimer = null;
  function startAutoRefresh() {
    if (autoRefreshTimer) clearInterval(autoRefreshTimer);
    autoRefreshTimer = setInterval(async () => {
      if (isSaving || pendingSave) return;
      if (document.querySelector('.modal-overlay.show')) return;
      if (document.querySelector('.cell-input')) return;
      if (document.querySelector('.dropdown-menu') || document.querySelector('.mini-calendar')) return;
      try {
        const { data: row } = await db.from('app_state').select('data').eq('id','main').single();
        if (isSaving || pendingSave) return;
        if (row && row.data && JSON.stringify(row.data) !== JSON.stringify(data)) {
          data = { ...DEFAULT_DATA, ...row.data };
          if (!data.columns || !data.columns.length) data.columns = JSON.parse(JSON.stringify(DEFAULT_COLUMNS));
          if (!data.rows) data.rows = [];
          renderAll();
        }
      } catch(e) {}
    }, 15000);
  }
  function stopAutoRefresh() { if (autoRefreshTimer) clearInterval(autoRefreshTimer); autoRefreshTimer = null; }

  const MONTH_NAMES = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
  const MONTH_FULL = ['January','February','March','April','May','June','July','August','September','October','November','December'];

  // A period is keyed by its START year-month (the month containing the starting 16th).
  // periodKey 'YYYY-MM' => period runs 16th of that month to 16th of next month.
  function periodKeyFor(date) {
    const d = new Date(date);
    let y = d.getFullYear(), m = d.getMonth();
    if (d.getDate() < 16) { m -= 1; if (m < 0) { m = 11; y -= 1; } }
    return `${y}-${String(m+1).padStart(2,'0')}`;
  }
  function currentPeriodKey() { return periodKeyFor(new Date()); }
  function activePeriodKey() { return selectedPeriod || currentPeriodKey(); }
  function periodKeyToLabel(key) {
    const [y, m] = key.split('-').map(Number);
    const startM = m - 1;
    const endM = (startM + 1) % 12;
    const endY = startM === 11 ? y + 1 : y;
    return `16 ${MONTH_NAMES[startM]} – 16 ${MONTH_NAMES[endM]} ${endY !== y ? endY : y}`;
  }
  function periodLabel() { return periodKeyToLabel(activePeriodKey()); }

  // Build list of period keys to show in selector (current + past 23 months + a few future)
  function periodOptions() {
    const keys = [];
    const now = new Date();
    // start 2 months ahead, go back 24
    for (let offset = 2; offset >= -23; offset--) {
      const d = new Date(now.getFullYear(), now.getMonth() + offset, 16);
      keys.push(periodKeyFor(d));
    }
    // unique preserve order
    return [...new Set(keys)];
  }

  function isLeaderboardLocked() { const d = new Date().getDate(); return d >= 9 && d <= 15; }
  function daysUntilReveal() { return 16 - new Date().getDate(); }

  function populateLoginDropdown() {
    document.getElementById('teamSelect').innerHTML = '<option value="">Select your team</option>' +
      data.teams.map(t => `<option value="${t.id}">${escapeHtml(t.name)}</option>`).join('');
  }
  function switchRole(role) {
    document.querySelectorAll('.role-tab').forEach(t => t.classList.remove('active'));
    document.querySelector(`.role-tab[data-role="${role}"]`).classList.add('active');
    document.getElementById('adminLogin').style.display = role === 'admin' ? 'block' : 'none';
    document.getElementById('teamLogin').style.display = role === 'team' ? 'block' : 'none';
    document.getElementById('loginError').classList.remove('show');
  }
  function login() {
    const role = document.querySelector('.role-tab.active').dataset.role;
    const err = document.getElementById('loginError');
    if (role === 'admin') {
      if (document.getElementById('adminPass').value === data.adminPass) { session = { role:'admin' }; saveSession(); showApp(); }
      else err.classList.add('show');
    } else {
      const teamId = document.getElementById('teamSelect').value;
      const code = document.getElementById('teamCode').value;
      const team = data.teams.find(t => t.id === teamId);
      if (team && team.password === code) { session = { role:'team', teamId }; saveSession(); showApp(); }
      else err.classList.add('show');
    }
  }
  function logout() {
    stopAutoRefresh(); clearSession();
    document.getElementById('mainApp').style.display = 'none';
    document.getElementById('loginScreen').style.display = 'flex';
    document.getElementById('adminPass').value = ''; document.getElementById('teamCode').value = '';
    populateLoginDropdown();
  }
  function isAdmin() { return session && session.role === 'admin'; }
  function showApp() {
    document.getElementById('loginScreen').style.display = 'none';
    document.getElementById('mainApp').style.display = 'block';
    if (isAdmin()) {
      document.getElementById('userBadge').textContent = '⚡ Admin';
      document.getElementById('financeTab').style.display = 'flex';
      document.getElementById('addColBtn').style.display = 'inline-block';
    } else {
      const team = data.teams.find(t => t.id === session.teamId);
      document.getElementById('userBadge').textContent = `👥 ${team ? team.name : ''}`;
      document.getElementById('financeTab').style.display = 'none';
      document.getElementById('addColBtn').style.display = 'none';
      if (currentPage === 'finance') switchPage('crm');
    }
    renderAll(); startAutoRefresh();
  }
  function switchPage(page) {
    if (page === 'finance' && !isAdmin()) return;
    currentPage = page;
    document.querySelectorAll('.nav-tab').forEach(t => t.classList.toggle('active', t.dataset.page === page));
    document.querySelectorAll('.page').forEach(p => p.classList.toggle('active', p.id === 'page-' + page));
    renderAll();
  }
  function allEditors() {
    const names = [];
    data.teams.forEach(t => t.members.forEach(m => { if (!names.includes(m)) names.push(m); }));
    (data.individuals || []).forEach(m => { if (!names.includes(m)) names.push(m); });
    return names;
  }
  function editorTeam(name) { return data.teams.find(t => t.members.includes(name)); }
  function isIndividual(name) { return (data.individuals || []).includes(name); }

  function renderAll() {
    if (!selectedPeriod) selectedPeriod = currentPeriodKey();
    populateMonthSelectors();
    document.getElementById('crmPeriodLabel').textContent = 'Period: ' + periodLabel();
    document.getElementById('lbPeriodLabel').textContent = 'Period: ' + periodLabel();
    if (currentPage === 'crm') renderCRM();
    if (currentPage === 'leaderboard') renderLeaderboard();
    if (currentPage === 'finance') renderFinance();
    populateEditorFilter();
  }

  function populateMonthSelectors() {
    const active = activePeriodKey();
    const [activeY, activeM] = active.split('-').map(Number);
    const cur = currentPeriodKey();
    const [curY] = cur.split('-').map(Number);

    // Years: from 2024 up to current year + 2
    const years = [];
    for (let y = 2024; y <= curY + 2; y++) years.push(y);
    const yearHtml = years.map(y => `<option value="${y}">${y}</option>`).join('');
    const monthHtml = MONTH_FULL.map((mn, i) => {
      const key = `${activeY}-${String(i+1).padStart(2,'0')}`;
      const isCur = key === cur;
      return `<option value="${i+1}">${mn}${isCur ? ' (current)' : ''}</option>`;
    }).join('');

    [['crmYear','crmMonthSel'],['finYear','finMonthSel']].forEach(([yId, mId]) => {
      const yEl = document.getElementById(yId), mEl = document.getElementById(mId);
      if (yEl) { yEl.innerHTML = yearHtml; yEl.value = activeY; }
      if (mEl) { mEl.innerHTML = monthHtml; mEl.value = activeM; }
    });
  }

  function changeYearMonth(which) {
    const yId = which === 'crm' ? 'crmYear' : 'finYear';
    const mId = which === 'crm' ? 'crmMonthSel' : 'finMonthSel';
    const y = Number(document.getElementById(yId).value);
    const m = Number(document.getElementById(mId).value);
    selectedPeriod = `${y}-${String(m).padStart(2,'0')}`;
    populateMonthSelectors();
    document.getElementById('crmPeriodLabel').textContent = 'Period: ' + periodLabel();
    document.getElementById('lbPeriodLabel').textContent = 'Period: ' + periodLabel();
    if (currentPage === 'crm') renderCRM();
    if (currentPage === 'finance') renderFinance();
  }
  function visibleColumns() { return data.columns.filter(c => !c.adminOnly || isAdmin()); }
  function populateEditorFilter() {
    const sel = document.getElementById('crmFilterEditor'); if (!sel) return;
    const cur = sel.value;
    sel.innerHTML = '<option value="">All editors</option>' + allEditors().map(e => `<option value="${escapeHtml(e)}">${escapeHtml(e)}</option>`).join('');
    sel.value = cur;
  }
  function periodRows() {
    const pk = activePeriodKey();
    // Rows without a period belong to the current period (legacy/safety)
    return data.rows.filter(r => (r.period || currentPeriodKey()) === pk);
  }
  function getRows() {
    let rows = periodRows();
    const fE = document.getElementById('crmFilterEditor').value;
    const fS = document.getElementById('crmFilterStatus').value;
    const sort = document.getElementById('crmSort').value;
    if (fE) rows = rows.filter(r => r.editor === fE);
    if (fS) rows = rows.filter(r => (r.status||'Assigned') === fS);
    if (sort === 'editor') rows.sort((a,b) => (a.editor||'').localeCompare(b.editor||''));
    else if (sort === 'status') rows.sort((a,b) => (a.status||'').localeCompare(b.status||''));
    else if (sort === 'deadline') rows.sort((a,b) => (a.deadline||'9999').localeCompare(b.deadline||'9999'));
    else if (sort === 'revenue') rows.sort((a,b) => (Number(b.revenue)||0) - (Number(a.revenue)||0));
    return rows;
  }
  function renderCRM() {
    const cols = visibleColumns();
    document.getElementById('crmHead').innerHTML =
      cols.map(c => `<th>${escapeHtml(c.label)}${(!c.locked && isAdmin()) ? `<span class="col-menu" onclick="deleteColumn('${c.id}')" title="Delete column">✕</span>` : ''}</th>`).join('') +
      (isAdmin() ? '<th style="width:40px"></th>' : '');
    const rows = getRows();
    const body = document.getElementById('crmBody');
    if (rows.length === 0) {
      body.innerHTML = `<tr><td colspan="${cols.length+1}" style="padding:40px;text-align:center;color:var(--text-muted)">No rows yet. Click "＋ Add row" below to start.</td></tr>`;
      return;
    }
    body.innerHTML = rows.map(r => {
      const cells = cols.map(c => renderCell(r, c)).join('');
      const del = isAdmin() ? `<td style="text-align:center"><span class="row-delete" onclick="deleteRow('${r.id}')" title="Delete row">🗑</span></td>` : '';
      return `<tr data-row="${r.id}">${cells}${del}</tr>`;
    }).join('');
    if (isAdmin()) {
      const prows = periodRows();
      const totalRev = prows.reduce((s,r) => s + (Number(r.revenue)||0), 0);
      const totalPts = prows.reduce((s,r) => s + (r.points!=null ? Number(r.points) : pointsFromRevenue(r.revenue)), 0);
      const tc = cols.map(c => {
        if (c.id === 'revenue') return `<td><div class="cell total-revenue">$${totalRev.toLocaleString()}</div></td>`;
        if (c.id === 'points') return `<td><div class="cell total-points">${totalPts}</div></td>`;
        if (c.id === cols[0].id) return `<td><div class="cell">Totals</div></td>`;
        return `<td><div class="cell"></div></td>`;
      }).join('');
      body.innerHTML += `<tr class="totals-row">${tc}<td></td></tr>`;
    }
  }
  function renderCell(r, c) {
    const val = r[c.id];
    if (c.type === 'editor') {
      const inner = val ? `<span class="editor-pill"><span class="editor-avatar">${escapeHtml((val[0]||'?').toUpperCase())}</span>${escapeHtml(val)}</span>` : `<span class="cell-empty">Assign editor</span>`;
      return `<td><div class="editor-cell" onclick="openEditorDropdown(event,'${r.id}')">${inner}</div></td>`;
    }
    if (c.type === 'status') {
      const s = val || 'Assigned';
      return `<td><div class="status-cell" onclick="openStatusDropdown(event,'${r.id}')"><span class="status-pill ${statusClass(s)}">${escapeHtml(s)}</span></div></td>`;
    }
    if (c.type === 'revenue') {
      const disp = val ? `<span class="revenue-val">$${Number(val).toLocaleString()}</span>` : `<span class="cell-empty">$0</span>`;
      return `<td><div class="num-cell" onclick="editNumCell(event,'${r.id}','revenue')">${disp}</div></td>`;
    }
    if (c.type === 'points') {
      const auto = (r.points == null);
      const pts = auto ? pointsFromRevenue(r.revenue) : r.points;
      const tag = auto ? '<span class="points-auto">auto</span>' : '<span class="points-auto">manual</span>';
      const clickable = isAdmin() ? `onclick="editNumCell(event,'${r.id}','points')"` : '';
      return `<td><div class="num-cell" ${clickable}><span class="points-val">${pts}</span>${isAdmin()?tag:''}</div></td>`;
    }
    if (c.type === 'date') {
      const disp = val ? formatDate(val) : `<span class="cell-empty">Set date</span>`;
      return `<td><div class="cell" onclick="openCalendar(event,'${r.id}','${c.id}')">${disp}</div></td>`;
    }
    if (c.type === 'link') {
      const disp = val ? `<a href="${escapeAttr(linkify(val))}" target="_blank" class="cell-link" onclick="event.stopPropagation()">🔗 ${escapeHtml(truncate(val))}</a>` : `<span class="cell-empty">Add link</span>`;
      return `<td><div class="cell" onclick="editTextCell(event,'${r.id}','${c.id}')">${disp}</div></td>`;
    }
    const disp = val ? escapeHtml(val) : `<span class="cell-empty">—</span>`;
    return `<td><div class="cell" onclick="editTextCell(event,'${r.id}','${c.id}')">${disp}</div></td>`;
  }
  function truncate(s, n=22) { s = String(s); return s.length > n ? s.slice(0,n) + '…' : s; }
  function linkify(s) { s = String(s).trim(); if (/^https?:\/\//i.test(s)) return s; return 'https://' + s; }
  function formatDate(iso) { const d = new Date(iso + 'T00:00:00'); return d.toLocaleDateString('en-US', { month:'short', day:'numeric', year:'numeric' }); }

  function editTextCell(e, rowId, colId) {
    const r = data.rows.find(x => x.id === rowId); if (!r) return;
    const td = e.currentTarget.parentElement;
    td.innerHTML = `<input class="cell-input" type="text" value="${escapeAttr(r[colId]||'')}">`;
    const input = td.querySelector('input'); input.focus(); input.select();
    const commit = async () => { r[colId] = input.value.trim(); renderCRM(); await saveData(); };
    input.addEventListener('blur', commit, { once:true });
    input.addEventListener('keydown', ev => { if (ev.key==='Enter') input.blur(); if (ev.key==='Escape') { input.removeEventListener('blur',commit); renderCRM(); } });
  }
  function editNumCell(e, rowId, field) {
    if (!isAdmin()) return;
    const r = data.rows.find(x => x.id === rowId); if (!r) return;
    const td = e.currentTarget.parentElement;
    let cur = field === 'revenue' ? (r.revenue!=null?r.revenue:'') : (r.points!=null?r.points:pointsFromRevenue(r.revenue));
    td.innerHTML = `<input class="cell-input" type="number" min="0" value="${escapeAttr(cur)}">`;
    const input = td.querySelector('input'); input.focus(); input.select();
    const commit = async () => {
      const v = input.value.trim();
      if (field === 'revenue') r.revenue = v === '' ? null : Number(v);
      else r.points = v === '' ? null : Number(v);
      renderCRM(); await saveData();
    };
    input.addEventListener('blur', commit, { once:true });
    input.addEventListener('keydown', ev => { if (ev.key==='Enter') input.blur(); if (ev.key==='Escape') { input.removeEventListener('blur',commit); renderCRM(); } });
  }

  let openMenu = null;
  function closeMenus() { if (openMenu) { openMenu.remove(); openMenu = null; } document.querySelectorAll('.dropdown-menu, .mini-calendar').forEach(m => m.remove()); }
  function openEditorDropdown(e, rowId) {
    e.stopPropagation(); closeMenus();
    const r = data.rows.find(x => x.id === rowId); if (!r) return;
    const menu = document.createElement('div'); menu.className = 'dropdown-menu';
    const editors = allEditors();
    menu.innerHTML = editors.map(name => `
      <div class="dropdown-item" onclick="assignEditor('${rowId}','${escapeAttr(name)}')">
        <span class="editor-avatar">${escapeHtml((name[0]||'?').toUpperCase())}</span><span>${escapeHtml(name)}</span>
        ${isAdmin() ? `<span class="item-edit" onclick="event.stopPropagation();renameEditorPrompt('${escapeAttr(name)}')" title="Rename">✏️</span>` : ''}
      </div>`).join('') +
      (r.editor ? `<div class="dropdown-item" onclick="assignEditor('${rowId}','')" style="color:var(--text-muted)">✕ Clear</div>` : '') +
      (isAdmin() ? `<div class="dropdown-divider"></div><div class="dropdown-add" onclick="newEditorWithTeam('${rowId}')">＋ Add new editor</div>` : '');
    document.body.appendChild(menu); positionMenu(menu, e); openMenu = menu;
  }
  async function assignEditor(rowId, name) { const r = data.rows.find(x => x.id === rowId); if (!r) return; r.editor = name||null; closeMenus(); renderCRM(); await saveData(); }
  function newEditorWithTeam(rowId) {
    closeMenus();
    showPrompt('Add new editor', 'Editor name:', '', (name) => {
      name = name.trim(); if (!name) return;
      if (allEditors().includes(name)) { showToast('That name already exists'); return; }
      // Now show team choice
      showChoice('Add ' + name + ' to:', [
        { label: 'Team Siam', value: 't_siam' },
        { label: 'Team Riad', value: 't_riad' },
        { label: 'Individual', value: 'individual' }
      ], async (choice) => {
        if (choice === 'individual') {
          if (!data.individuals) data.individuals = [];
          data.individuals.push(name);
        } else {
          const t = data.teams.find(x => x.id === choice);
          if (t) t.members.push(name);
        }
        const r = data.rows.find(x => x.id === rowId); if (r) r.editor = name;
        renderCRM(); populateEditorFilter(); await saveData();
        showToast(`${name} added`);
      });
    });
  }
  function renameEditorPrompt(oldName) {
    closeMenus();
    showPrompt('Rename editor', `Rename "${oldName}" to:`, oldName, async (newName) => {
      newName = newName.trim(); if (!newName || newName === oldName) return;
      data.teams.forEach(t => { const i = t.members.indexOf(oldName); if (i>=0) t.members[i]=newName; if (t.leader===oldName) t.leader=newName; });
      data.rows.forEach(r => { if (r.editor === oldName) r.editor = newName; });
      renderAll(); await saveData(); showToast(`Renamed to ${newName}`);
    });
  }
  function openStatusDropdown(e, rowId) {
    e.stopPropagation(); closeMenus();
    const menu = document.createElement('div'); menu.className = 'dropdown-menu';
    menu.innerHTML = STATUS_OPTIONS.map(o => `<div class="dropdown-item" onclick="setStatus('${rowId}','${o.value}')"><span class="status-pill ${o.cls}">${o.value}</span></div>`).join('');
    document.body.appendChild(menu); positionMenu(menu, e); openMenu = menu;
  }
  async function setStatus(rowId, val) { const r = data.rows.find(x => x.id === rowId); if (!r) return; r.status = val; closeMenus(); renderCRM(); await saveData(); }

  let calState = { rowId:null, colId:null, viewYear:0, viewMonth:0 };
  function openCalendar(e, rowId, colId) {
    e.stopPropagation(); closeMenus();
    const r = data.rows.find(x => x.id === rowId); if (!r) return;
    const cur = r[colId] ? new Date(r[colId]+'T00:00:00') : new Date();
    calState = { rowId, colId, viewYear: cur.getFullYear(), viewMonth: cur.getMonth() };
    const cal = document.createElement('div'); cal.className = 'mini-calendar'; cal.id = 'miniCal';
    document.body.appendChild(cal); renderCalendar(); positionMenu(cal, e); openMenu = cal;
  }
  function renderCalendar() {
    const cal = document.getElementById('miniCal'); if (!cal) return;
    const { viewYear, viewMonth, rowId, colId } = calState;
    const r = data.rows.find(x => x.id === rowId);
    const selected = r && r[colId] ? r[colId] : null;
    const months = ['January','February','March','April','May','June','July','August','September','October','November','December'];
    const firstDay = new Date(viewYear, viewMonth, 1).getDay();
    const daysInMonth = new Date(viewYear, viewMonth+1, 0).getDate();
    const today = new Date();
    const todayStr = `${today.getFullYear()}-${String(today.getMonth()+1).padStart(2,'0')}-${String(today.getDate()).padStart(2,'0')}`;
    let html = `<div class="cal-header"><button onclick="calNav(-1)">‹</button><div class="cal-month">${months[viewMonth]} ${viewYear}</div><button onclick="calNav(1)">›</button></div><div class="cal-grid">${['S','M','T','W','T','F','S'].map(d=>`<div class="cal-day-name">${d}</div>`).join('')}`;
    for (let i=0;i<firstDay;i++) html += `<div class="cal-day empty"></div>`;
    for (let d=1;d<=daysInMonth;d++) {
      const ds = `${viewYear}-${String(viewMonth+1).padStart(2,'0')}-${String(d).padStart(2,'0')}`;
      const cls = ['cal-day']; if (ds===todayStr) cls.push('today'); if (ds===selected) cls.push('selected');
      html += `<div class="${cls.join(' ')}" onclick="pickDate('${ds}')">${d}</div>`;
    }
    html += `</div>`;
    if (selected) html += `<div class="cal-clear" onclick="pickDate('')">✕ Clear date</div>`;
    cal.innerHTML = html;
  }
  function calNav(dir) { calState.viewMonth += dir; if (calState.viewMonth<0) { calState.viewMonth=11; calState.viewYear--; } if (calState.viewMonth>11) { calState.viewMonth=0; calState.viewYear++; } renderCalendar(); }
  async function pickDate(ds) { const r = data.rows.find(x => x.id === calState.rowId); if (!r) return; r[calState.colId] = ds||null; closeMenus(); renderCRM(); await saveData(); }

  function positionMenu(menu, e) {
    const rect = menu.getBoundingClientRect();
    let x = e.clientX, y = e.clientY + 8;
    if (x + rect.width > window.innerWidth - 12) x = window.innerWidth - rect.width - 12;
    if (y + rect.height > window.innerHeight - 12) y = e.clientY - rect.height - 8;
    if (y < 12) y = 12;
    menu.style.left = Math.max(12, x) + 'px'; menu.style.top = y + 'px';
  }
  document.addEventListener('click', e => { if (openMenu && !openMenu.contains(e.target)) closeMenus(); });

  async function addRow() {
    data.rows.push({ id:'r_'+Date.now()+'_'+Math.floor(Math.random()*1000), period: activePeriodKey(), rawFile:'', editor:null, revenue:null, points:null, status:'Assigned', deadline:null, frameio:'', finalVideo:'', createdAt:new Date().toISOString() });
    renderCRM(); await saveData();
  }
  function deleteRow(rowId) {
    showConfirm('Delete row?', 'This row will be permanently deleted.', 'Delete', async () => {
      data.rows = data.rows.filter(r => r.id !== rowId); renderCRM(); await saveData(); showToast('Row deleted');
    }, true);
  }
  function addColumn() {
    showPrompt('Add column', 'Name your new column:', '', async (name) => {
      name = name.trim(); if (!name) return;
      data.columns.push({ id:'col_'+Date.now(), label:name, type:'text', adminOnly:false, locked:false });
      renderCRM(); await saveData(); showToast(`Column "${name}" added`);
    });
  }
  function deleteColumn(colId) {
    const col = data.columns.find(c => c.id === colId);
    if (!col || col.locked) { showToast('This column cannot be deleted'); return; }
    showConfirm('Delete column?', `"${col.label}" and all its data will be removed.`, 'Delete', async () => {
      data.columns = data.columns.filter(c => c.id !== colId);
      data.rows.forEach(r => delete r[colId]);
      renderCRM(); await saveData(); showToast('Column deleted');
    }, true);
  }

  function renderLeaderboard() {
    const container = document.getElementById('leaderboardContent');
    if (!isAdmin() && isLeaderboardLocked()) {
      const days = daysUntilReveal();
      container.innerHTML = `<div class="locked-board"><div class="locked-icon">🔒</div><div class="locked-title">Results coming on the 16th</div><div class="locked-sub">The leaderboard is hidden for the final stretch. Keep pushing — rankings reveal in ${days} day${days===1?'':'s'}.</div></div>`;
      return;
    }
    const editorPoints = {}, teamPoints = {};
    data.teams.forEach(t => teamPoints[t.id] = 0);
    allEditors().forEach(e => editorPoints[e] = 0);
    const pk = activePeriodKey();
    data.rows.filter(r => (r.period || currentPeriodKey()) === pk).forEach(r => {
      if (!r.editor) return;
      const pts = (r.points!=null) ? Number(r.points) : pointsFromRevenue(r.revenue);
      if (editorPoints[r.editor]==null) editorPoints[r.editor] = 0;
      editorPoints[r.editor] += pts;
      const t = editorTeam(r.editor); if (t) teamPoints[t.id] += pts;
    });
    const teams = data.teams.map(t => ({ id:t.id, leader:t.leader, name:t.name, points:teamPoints[t.id]||0 })).sort((a,b) => b.points - a.points);
    let html = '<div class="rankings-grid">';
    html += '<div class="ranking-block"><div class="ranking-title">Team Leader Ranking</div><div class="ranking-list">';
    html += teams.map((t,i) => {
      const isMe = !isAdmin() && session.teamId === t.id;
      const rc = i===0?'rank-1':i===1?'rank-2':i===2?'rank-3':'other';
      return `<div class="ranking-row ${isMe?'me':''}"><div class="rank-num ${rc}">${i+1}</div><div class="ranking-name-wrap"><div class="ranking-name">${escapeHtml(t.leader)} <span style="color:var(--text-muted);font-weight:500;font-size:11px">· ${escapeHtml(t.name)}</span>${isMe?'<span class="you-tag">You</span>':''}</div></div><div class="ranking-points">${t.points}</div></div>`;
    }).join('');
    html += '</div></div>';
    html += '<div class="ranking-block"><div class="ranking-title">Editor Ranking</div><div class="ranking-list">';
    if (isAdmin()) {
      data.teams.forEach(t => {
        const editors = t.members.map(m => ({ name:m, points:editorPoints[m]||0, leader:m===t.leader })).sort((a,b) => b.points - a.points);
        html += `<div class="ranking-section-label">${escapeHtml(t.name)}</div>`;
        html += editors.map((e,i) => { const rc = i===0?'rank-1':i===1?'rank-2':i===2?'rank-3':'other'; return `<div class="ranking-row"><div class="rank-num ${rc}">${i+1}</div><div class="ranking-name-wrap"><div class="ranking-name">${escapeHtml(e.name)}${e.leader?'<span style="color:var(--green);font-size:10px;margin-left:6px">★ Leader</span>':''}</div></div><div class="ranking-points">${e.points}</div></div>`; }).join('');
      });
      // Individuals section
      const indivs = (data.individuals || []).map(m => ({ name:m, points:editorPoints[m]||0 })).sort((a,b) => b.points - a.points);
      if (indivs.length) {
        html += `<div class="ranking-section-label">Individuals</div>`;
        html += indivs.map((e,i) => { const rc = i===0?'rank-1':i===1?'rank-2':i===2?'rank-3':'other'; return `<div class="ranking-row"><div class="rank-num ${rc}">${i+1}</div><div class="ranking-name-wrap"><div class="ranking-name">${escapeHtml(e.name)}</div></div><div class="ranking-points">${e.points}</div></div>`; }).join('');
      }
    } else {
      const team = data.teams.find(t => t.id === session.teamId);
      const editors = team.members.map(m => ({ name:m, points:editorPoints[m]||0, leader:m===team.leader })).sort((a,b) => b.points - a.points);
      html += editors.map((e,i) => { const rc = i===0?'rank-1':i===1?'rank-2':i===2?'rank-3':'other'; return `<div class="ranking-row"><div class="rank-num ${rc}">${i+1}</div><div class="ranking-name-wrap"><div class="ranking-name">${escapeHtml(e.name)}${e.leader?'<span style="color:var(--green);font-size:10px;margin-left:6px">★ Leader</span>':''}</div></div><div class="ranking-points">${e.points}</div></div>`; }).join('');
    }
    html += '</div></div></div>';
    container.innerHTML = html;
  }

  // ============ FINANCE ============
  function periodRevenue(pk) {
    return data.rows.filter(r => (r.period || currentPeriodKey()) === pk)
      .reduce((s,r) => s + (Number(r.revenue)||0), 0);
  }
  function expenseUSD(e, rate) {
    // USD value of an expense. usd is source of truth; fall back to taka/rate or legacy amount.
    if (e.usd != null) return Number(e.usd) || 0;
    if (e.amount != null) return Number(e.amount) || 0;
    const r = rate || monthRate();
    if (e.taka != null && r) return Math.round((e.taka / r) * 100) / 100;
    return 0;
  }
  function periodExpenses(pk) {
    const list = data.expenses[pk] || [];
    const r = monthRate(pk);
    return list.reduce((s,e) => s + expenseUSD(e, r), 0);
  }
  function periodPoints(pk) {
    return data.rows.filter(r => (r.period || currentPeriodKey()) === pk)
      .reduce((s,r) => s + (r.points!=null ? Number(r.points) : pointsFromRevenue(r.revenue)), 0);
  }

  function monthRate(pk) {
    pk = pk || activePeriodKey();
    if (!data.monthRates) data.monthRates = {};
    if (data.monthRates[pk] == null) {
      // seed from legacy global rate or default 122
      data.monthRates[pk] = Number((data.rates||{}).expense) || 122;
    }
    return Number(data.monthRates[pk]) || 0;
  }
  function taka(usd, rate) { return Math.round((Number(usd)||0) * (Number(rate)||0)); }

  function renderFinance() {
    const pk = activePeriodKey();
    document.getElementById('financePeriodLabel').textContent = 'Period: ' + periodLabel();

    const rate = monthRate(pk);
    const revenue = periodRevenue(pk);
    const expenses = periodExpenses(pk);
    const profit = revenue - expenses;
    const split = data.split || { Rashid:77, Fahim:18, Siam:5 };
    const splitTotal = Object.values(split).reduce((s,v) => s + (Number(v)||0), 0);

    const order = ['Rashid','Fahim','Siam'];
    const splitNames = [...order.filter(n => n in split), ...Object.keys(split).filter(n => !order.includes(n))];

    let html = '';

    // ONE exchange rate for the whole month, at the very top
    html += `
      <div class="fin-card" style="margin-bottom:16px">
        <div class="rate-bar">
          <div>
            <div class="notes-label" style="color:var(--green)">Exchange Rate — ${escapeHtml(periodKeyToLabel(pk))}</div>
            <div style="font-size:12px;color:var(--text-muted);margin-top:3px">Applies to all conversions this month</div>
          </div>
          <div class="rate-bar-input">
            <span class="rate-eq">1 USD =</span>
            <input type="number" class="rate-input" style="width:90px;font-size:15px" value="${rate}" onchange="updateMonthRate(this.value)">
            <span class="rate-label" style="font-size:14px">৳</span>
          </div>
        </div>
      </div>`;

    html += '<div class="fin-grid">';

    // Monthly summary
    html += `
      <div class="fin-card">
        <h3>Monthly Summary</h3>
        <div class="fin-stat"><span class="label">Total Revenue</span><span class="val rev">$${revenue.toLocaleString()}</span></div>
        <div class="fin-stat"><span class="label">Total Expenses</span><span class="val neg">- $${expenses.toLocaleString()}</span></div>
        <div class="fin-big">
          <div class="num ${profit>=0?'pos':'neg'}">$${profit.toLocaleString()}</div>
          <div class="cap">Net Profit</div>
          <div style="margin-top:8px;color:var(--text-dim);font-size:14px;font-weight:700">৳ ${taka(profit, rate).toLocaleString()}</div>
        </div>
      </div>`;

    // Profit split
    html += `
      <div class="fin-card">
        <h3>Profit Split (after expenses)</h3>
        ${splitNames.map(name => {
          const pct = Number(split[name])||0;
          const profitCut = Math.round(profit * pct / 100);
          return `
            <div class="split-row">
              <span class="split-name">${escapeHtml(name)}</span>
              <input type="number" class="split-pct-input" value="${pct}" min="0" max="100" onchange="updateSplit('${escapeAttr(name)}',this.value)">
              <span style="color:var(--text-muted);font-size:12px">%</span>
              <span class="split-amounts">
                <div class="split-profit-amt">$${profitCut.toLocaleString()}</div>
                <div class="split-taka">৳ ${taka(profitCut, rate).toLocaleString()}</div>
              </span>
            </div>`;
        }).join('')}
        ${splitTotal !== 100 ? `<div class="split-warn">⚠ Percentages total ${splitTotal}% (should be 100%)</div>` : ''}
      </div>`;

    html += '</div>';

    // Expenses
    const expList = data.expenses[pk] || [];
    html += '<div class="fin-grid">';
    html += `
      <div class="fin-card">
        <h3>Expenses — ${escapeHtml(periodKeyToLabel(pk))}</h3>
        <table class="exp-table">
          <thead><tr><th>Expense</th><th style="width:100px">Taka (৳)</th><th style="width:95px">USD ($)</th><th>Notes</th><th style="width:30px"></th></tr></thead>
          <tbody>
            ${expList.length === 0 ? '<tr><td colspan="5" style="padding:16px;text-align:center;color:var(--text-muted);font-size:13px">No expenses yet</td></tr>' :
              expList.map(e => {
                const usd = expenseUSD(e, rate);
                const tk = e.taka != null ? e.taka : Math.round(usd * rate);
                return `
                <tr>
                  <td><div class="exp-cell ${e.name?'':'empty'}" onclick="editExpense(event,'${e.id}','name')">${e.name?escapeHtml(e.name):'Name'}</div></td>
                  <td><div class="exp-cell ${e.taka?'':'empty'}" onclick="editExpense(event,'${e.id}','taka')">${tk?`<span style="color:var(--green-bright)">৳ ${Number(tk).toLocaleString()}</span>`:'৳ 0'}</div></td>
                  <td><div class="exp-cell ${usd?'':'empty'}" onclick="editExpense(event,'${e.id}','usd')">${usd?`<span class="exp-amount">$${usd.toLocaleString()}</span>`:'$0'}</div></td>
                  <td><div class="exp-cell ${e.notes?'':'empty'}" onclick="editExpense(event,'${e.id}','notes')">${e.notes?escapeHtml(e.notes):'—'}</div></td>
                  <td style="text-align:center"><span class="exp-del" onclick="deleteExpense('${e.id}')">🗑</span></td>
                </tr>`; }).join('')}
          </tbody>
        </table>
        <div class="exp-add" onclick="addExpense()">＋ Add expense</div>
        <div style="margin-top:12px;padding-top:12px;border-top:1px dashed var(--border);display:flex;justify-content:space-between;align-items:center">
          <span class="rate-label">Total expenses</span>
          <span style="font-weight:700"><span style="color:var(--green-bright)">৳ ${taka(expenses, rate).toLocaleString()}</span> · <span class="exp-amount">$${expenses.toLocaleString()}</span></span>
        </div>
      </div>`;
    html += '</div>';

    // Collapsible calculator
    const calcOpen = window._calcOpen || false;
    html += `
      <div class="fin-card">
        <div class="collapse-head" onclick="toggleCalc()">
          <h3 style="margin:0">Points Calculator & Converter</h3>
          <span class="collapse-arrow">${calcOpen ? '▲' : '▼'}</span>
        </div>
        <div id="calcBody" style="display:${calcOpen?'block':'none'};margin-top:16px">
          <div class="calc-row">
            <input type="number" id="calcRevInput" placeholder="Enter revenue ($)" oninput="updateCalcResult()" min="0">
            <div class="calc-result" id="calcResult">0 pts</div>
          </div>
          <div class="converter">
            <div class="conv-side">
              <label>USD ($)</label>
              <input type="number" id="convUsd" placeholder="0" oninput="convFromUsd()">
            </div>
            <div class="conv-eq">⇄</div>
            <div class="conv-side">
              <label>Taka (৳)</label>
              <input type="number" id="convBdt" placeholder="0" oninput="convFromBdt()">
            </div>
          </div>
          <div style="font-size:12px;color:var(--text-muted);margin-bottom:10px">Using this month's rate: 1 USD = ${rate} ৳</div>
          <div class="tier-head">
            <span class="notes-label" style="color:var(--text-dim)">Point Tiers (editable)</span>
            <button class="btn btn-secondary btn-sm" onclick="addTier()">+ Add tier</button>
          </div>
          <table class="tier-table">
            <thead><tr><th>Min $</th><th>Max $</th><th style="text-align:right">Points</th><th style="width:30px"></th></tr></thead>
            <tbody>
              ${getTiers().map((t,i) => `
                <tr>
                  <td><input type="number" class="tier-input" value="${t.min}" onchange="updateTier(${i},'min',this.value)"></td>
                  <td><input type="number" class="tier-input" value="${t.max}" onchange="updateTier(${i},'max',this.value)"></td>
                  <td style="text-align:right"><input type="number" class="tier-input pts" value="${t.points}" onchange="updateTier(${i},'points',this.value)"></td>
                  <td style="text-align:center"><span class="exp-del" onclick="deleteTier(${i})">🗑</span></td>
                </tr>`).join('')}
            </tbody>
          </table>
          <div class="tier-note">Anything above the highest tier's max gets the top points +5 for each $50 over.</div>
        </div>
      </div>`;

    // Report + notes
    html += `
      <div class="fin-card">
        <div class="collapse-head" style="cursor:default">
          <h3 style="margin:0">Monthly Report — ${escapeHtml(periodKeyToLabel(pk))}</h3>
          <button class="btn btn-primary btn-sm" onclick="downloadReportTXT()">⬇ Download Report</button>
        </div>
        <div style="margin-top:16px">${buildReport(pk, revenue, expenses, profit)}</div>
        <div style="margin-top:18px">
          <div class="notes-label">Custom Notes (your own text, shown in green)</div>
          <textarea class="notes-area" id="notesArea" placeholder="Add your own notes for this month here..." onchange="saveNote()">${escapeHtml(data.notes[pk] || '')}</textarea>
        </div>
      </div>`;

    document.getElementById('financeContent').innerHTML = html;
  }

  async function updateMonthRate(val) {
    const pk = activePeriodKey();
    if (!data.monthRates) data.monthRates = {};
    data.monthRates[pk] = Number(val) || 0;
    renderFinance(); await saveData();
  }

  function toggleCalc() { window._calcOpen = !window._calcOpen; renderFinance(); }

  function convFromUsd() {
    const usd = Number(document.getElementById('convUsd').value) || 0;
    const rate = monthRate();
    document.getElementById('convBdt').value = Math.round(usd * rate);
  }
  function convFromBdt() {
    const bdt = Number(document.getElementById('convBdt').value) || 0;
    const rate = monthRate() || 1;
    document.getElementById('convUsd').value = rate ? Math.round((bdt / rate) * 100) / 100 : 0;
  }

  async function addTier() {
    const tiers = getTiers();
    const last = tiers[tiers.length-1];
    data.pointTiers = [...tiers, { min: (last?last.max+1:1), max: (last?last.max+50:50), points: (last?last.points+10:5) }];
    renderFinance(); await saveData();
  }
  async function updateTier(i, field, val) {
    const tiers = getTiers();
    if (!tiers[i]) return;
    data.pointTiers = JSON.parse(JSON.stringify(tiers));
    data.pointTiers[i][field] = Number(val) || 0;
    renderFinance(); renderCRM(); await saveData();
  }
  function deleteTier(i) {
    showConfirm('Delete tier?', 'This point tier will be removed.', 'Delete', async () => {
      const tiers = getTiers();
      data.pointTiers = tiers.filter((_,idx) => idx !== i);
      renderFinance(); renderCRM(); await saveData(); showToast('Tier deleted');
    }, true);
  }


  function buildReport(pk, revenue, expenses, profit) {
    const prows = data.rows.filter(r => (r.period || currentPeriodKey()) === pk);
    const videoCount = prows.length;
    const doneCount = prows.filter(r => r.status === 'Done').length;
    const totalPts = periodPoints(pk);

    // top editors by revenue
    const byEditor = {};
    prows.forEach(r => { if (r.editor) byEditor[r.editor] = (byEditor[r.editor]||0) + (Number(r.revenue)||0); });
    const topEditors = Object.entries(byEditor).sort((a,b) => b[1]-a[1]).slice(0,3);

    let r = `<div class="report-box">`;
    r += `<div class="report-line">Total videos this month: <span class="report-num">${videoCount}</span> (<span class="report-num">${doneCount}</span> done)</div>`;
    r += `<div class="report-line">Total revenue: <span class="report-num">$${revenue.toLocaleString()}</span></div>`;
    r += `<div class="report-line">Total expenses: <span class="report-num neg">$${expenses.toLocaleString()}</span></div>`;
    r += `<div class="report-line"><strong>Net profit: <span class="report-num">$${profit.toLocaleString()}</span></strong></div>`;
    r += `<div class="report-line">Total points earned: <span class="report-num pts">${totalPts}</span></div>`;
    if (topEditors.length) {
      r += `<div class="report-line" style="margin-top:8px"><strong>Top earners:</strong></div>`;
      topEditors.forEach(([name, rev], i) => {
        r += `<div class="report-line">${i+1}. ${escapeHtml(name)} — <span class="report-num">$${rev.toLocaleString()}</span></div>`;
      });
    }
    r += `</div>`;
    return r;
  }

  function updateCalcResult() {
    const v = Number(document.getElementById('calcRevInput').value) || 0;
    document.getElementById('calcResult').textContent = pointsFromRevenue(v) + ' pts';
  }

  async function updateSplit(name, val) {
    data.split[name] = Number(val) || 0;
    renderFinance(); await saveData();
  }

  async function addExpense() {
    const pk = activePeriodKey();
    if (!data.expenses[pk]) data.expenses[pk] = [];
    data.expenses[pk].push({ id: 'e_'+Date.now()+'_'+Math.floor(Math.random()*1000), name:'', usd:null, taka:null, notes:'' });
    renderFinance(); await saveData();
  }
  function findExpense(id) {
    const pk = activePeriodKey();
    return (data.expenses[pk] || []).find(e => e.id === id);
  }
  function editExpense(ev, id, field) {
    const e = findExpense(id); if (!e) return;
    const td = ev.currentTarget.parentElement;
    const isNum = (field === 'usd' || field === 'taka');
    const type = isNum ? 'number' : 'text';
    const rate = monthRate();
    // migrate legacy expense (had .amount) to usd
    if (e.amount != null && e.usd == null) { e.usd = e.amount; delete e.amount; }
    const cur = e[field] != null ? e[field] : '';
    td.innerHTML = `<input class="exp-input" type="${type}" value="${escapeAttr(cur)}" step="any">`;
    const input = td.querySelector('input'); input.focus(); input.select();
    const commit = async () => {
      const raw = input.value.trim();
      const num = raw === '' ? null : Number(raw);
      if (field === 'name' || field === 'notes') {
        e[field] = raw;
      } else if (field === 'usd') {
        e.usd = num;
        e.taka = (num != null && rate) ? Math.round(num * rate) : e.taka;
      } else if (field === 'taka') {
        e.taka = num;
        e.usd = (num != null && rate) ? Math.round((num / rate) * 100) / 100 : e.usd;
      }
      renderFinance(); await saveData();
    };
    input.addEventListener('blur', commit, { once:true });
    input.addEventListener('keydown', k => { if (k.key==='Enter') input.blur(); if (k.key==='Escape') { input.removeEventListener('blur',commit); renderFinance(); } });
  }
  function deleteExpense(id) {
    showConfirm('Delete expense?', 'This expense will be removed.', 'Delete', async () => {
      const pk = activePeriodKey();
      data.expenses[pk] = (data.expenses[pk] || []).filter(e => e.id !== id);
      renderFinance(); await saveData(); showToast('Expense deleted');
    }, true);
  }

  async function saveNote() {
    const pk = activePeriodKey();
    data.notes[pk] = document.getElementById('notesArea').value;
    await saveData();
    showToast('Note saved');
  }

  function downloadReportTXT() {
    const pk = activePeriodKey();
    const label = periodKeyToLabel(pk);
    const rate = monthRate(pk);
    const revenue = periodRevenue(pk);
    const expenses = periodExpenses(pk);
    const profit = revenue - expenses;
    const split = data.split || {};
    const order = ['Rashid','Fahim','Siam'];
    const splitNames = [...order.filter(n => n in split), ...Object.keys(split).filter(n => !order.includes(n))];
    const prows = data.rows.filter(r => (r.period || currentPeriodKey()) === pk);
    const expList = data.expenses[pk] || [];

    function money(n) { return '$' + (Number(n)||0).toLocaleString(); }
    function tk(n) { return 'BDT ' + (Number(n)||0).toLocaleString(); }
    function pad(s, n) { s = String(s); return s.length >= n ? s.slice(0,n) : s + ' '.repeat(n - s.length); }
    const HR = '='.repeat(56);
    const hr = '-'.repeat(56);

    let L = [];
    L.push(HR);
    L.push('           AR STUDIOSS — MONTHLY REPORT');
    L.push('           ' + label);
    L.push(HR);
    L.push('');
    L.push('Exchange rate this month:  1 USD = ' + rate + ' BDT');
    L.push('Generated: ' + new Date().toLocaleString());
    L.push('');
    L.push('SUMMARY');
    L.push(hr);
    L.push(pad('Total Revenue', 28) + money(revenue));
    L.push(pad('Total Expenses', 28) + '- ' + money(expenses));
    L.push(pad('NET PROFIT', 28) + money(profit) + '   (' + tk(taka(profit, rate)) + ')');
    L.push('');
    L.push('PROFIT SPLIT (after expenses)');
    L.push(hr);
    splitNames.forEach(name => {
      const pct = Number(split[name])||0;
      const cut = Math.round(profit * pct / 100);
      L.push(pad(name + ' (' + pct + '%)', 28) + money(cut) + '   (' + tk(taka(cut, rate)) + ')');
    });
    L.push('');
    L.push('EXPENSES');
    L.push(hr);
    if (!expList.length) { L.push('No expenses recorded.'); }
    else {
      L.push(pad('Name', 24) + pad('Taka', 14) + pad('USD', 12) + 'Notes');
      expList.forEach(e => {
        const usd = expenseUSD(e, rate);
        const t = e.taka != null ? e.taka : Math.round(usd * rate);
        L.push(pad(e.name||'-', 24) + pad('BDT ' + t.toLocaleString(), 14) + pad('$' + usd.toLocaleString(), 12) + (e.notes||''));
      });
      L.push(pad('TOTAL', 24) + pad('BDT ' + taka(expenses,rate).toLocaleString(), 14) + money(expenses));
    }
    L.push('');
    L.push('VIDEOS / CRM');
    L.push(hr);
    L.push('Total videos: ' + prows.length + '   Done: ' + prows.filter(r=>r.status==='Done').length + '   Total points: ' + periodPoints(pk));
    L.push('');
    if (prows.length) {
      L.push(pad('Raw File', 24) + pad('Editor', 14) + pad('Revenue', 12) + pad('Points', 8) + 'Status');
      prows.forEach(r => {
        const pts = r.points!=null ? r.points : pointsFromRevenue(r.revenue);
        L.push(pad(r.rawFile||'-', 24) + pad(r.editor||'-', 14) + pad(money(r.revenue), 12) + pad(pts, 8) + (r.status||'-'));
      });
      L.push('');
    }
    // Top earners
    const byEditor = {};
    prows.forEach(r => { if (r.editor) byEditor[r.editor] = (byEditor[r.editor]||0) + (Number(r.revenue)||0); });
    const top = Object.entries(byEditor).sort((a,b)=>b[1]-a[1]).slice(0,5);
    if (top.length) {
      L.push('TOP EARNERS');
      L.push(hr);
      top.forEach(([n,rev],i) => L.push((i+1) + '. ' + pad(n, 20) + money(rev)));
      L.push('');
    }
    // Points earned per editor
    const ptsByEditor = {};
    prows.forEach(r => { if (r.editor) { const p = r.points!=null?Number(r.points):pointsFromRevenue(r.revenue); ptsByEditor[r.editor] = (ptsByEditor[r.editor]||0) + p; } });
    const ptsList = Object.entries(ptsByEditor).sort((a,b)=>b[1]-a[1]);
    if (ptsList.length) {
      L.push('POINTS BY EDITOR');
      L.push(hr);
      ptsList.forEach(([n,p],i) => L.push((i+1) + '. ' + pad(n, 20) + p + ' pts'));
      L.push('');
    }
    // Notes
    const note = (data.notes[pk]||'').trim();
    if (note) {
      L.push('NOTES');
      L.push(hr);
      L.push(note);
      L.push('');
    }
    L.push(HR);
    L.push('End of report — AR Studioss');
    L.push(HR);

    const blob = new Blob([L.join('\n')], { type: 'text/plain;charset=utf-8' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url; a.download = `AR-Studioss-Report-${pk}.txt`;
    document.body.appendChild(a); a.click(); document.body.removeChild(a);
    URL.revokeObjectURL(url);
    showToast('Report downloaded');
  }



  function openSettings() { document.getElementById('settingsModal').classList.add('show'); renderSettings(); }
  function renderSettings() {
    if (isAdmin()) { document.getElementById('settingsTitle').textContent = 'Admin Settings'; document.getElementById('settingsSub').textContent = 'Manage teams, members, and passwords'; renderAdminSettings(); }
    else { const team = data.teams.find(t => t.id === session.teamId); document.getElementById('settingsTitle').textContent = team.name + ' Settings'; document.getElementById('settingsSub').textContent = 'Manage your password'; renderTeamSettings(); }
  }
  function renderAdminSettings() {
    let html = `<div class="team-section"><h4>Admin Password</h4><div class="password-row"><div class="pwd-field"><input type="password" id="adminPassInput" value="${escapeAttr(data.adminPass)}"><button type="button" class="pwd-toggle" onclick="togglePwd('adminPassInput',this)">👁</button></div><button onclick="changeAdminPass()">Update</button></div></div>`;
    html += data.teams.map(t => `<div class="team-section"><h4>${escapeHtml(t.name)}</h4><div style="font-size:11px;color:var(--text-muted);margin-bottom:8px">LEADER</div><div class="members-list"><span class="member-pill"><span class="leader-mark">★</span>${escapeHtml(t.leader)}</span></div><div style="font-size:11px;color:var(--text-muted);margin-bottom:8px">MEMBERS</div><div class="members-list">${t.members.filter(m=>m!==t.leader).map(m=>`<span class="member-pill">${escapeHtml(m)}<button onclick="removeMember('${t.id}','${escapeAttr(m)}')">×</button></span>`).join('') || '<span style="color:var(--text-muted);font-size:12px">No additional members</span>'}</div><div class="add-member-row"><input type="text" id="newMember_${t.id}" placeholder="Add member name"><button onclick="addMember('${t.id}')">+ Add</button></div><div style="font-size:11px;color:var(--text-muted);margin-top:14px;margin-bottom:6px">PASSWORD</div><div class="password-row"><div class="pwd-field"><input type="password" id="teamPass_${t.id}" value="${escapeAttr(t.password)}"><button type="button" class="pwd-toggle" onclick="togglePwd('teamPass_${t.id}',this)">👁</button></div><button onclick="changeTeamPass('${t.id}')">Update</button></div></div>`).join('');
    document.getElementById('settingsBody').innerHTML = html;
  }
  function renderTeamSettings() {
    const team = data.teams.find(t => t.id === session.teamId);
    document.getElementById('settingsBody').innerHTML = `<div class="team-section"><h4>Team Members</h4><div style="font-size:11px;color:var(--text-muted);margin-bottom:8px">LEADER</div><div class="members-list"><span class="member-pill"><span class="leader-mark">★</span>${escapeHtml(team.leader)}</span></div><div style="font-size:11px;color:var(--text-muted);margin-bottom:8px;margin-top:10px">MEMBERS</div><div class="members-list">${team.members.filter(m=>m!==team.leader).map(m=>`<span class="member-pill">${escapeHtml(m)}</span>`).join('') || '<span style="color:var(--text-muted);font-size:12px">No additional members</span>'}</div><p style="color:var(--text-muted);font-size:12px;margin-top:10px">Ask admin to add or remove members.</p></div><div class="team-section"><h4>Change Team Password</h4><div class="password-row"><div class="pwd-field"><input type="password" id="teamPassInput" placeholder="New password"><button type="button" class="pwd-toggle" onclick="togglePwd('teamPassInput',this)">👁</button></div><button onclick="changeMyTeamPass()">Update</button></div></div>`;
  }
  function togglePwd(id, btn) { const i = document.getElementById(id); if (i.type==='password') { i.type='text'; btn.textContent='🙈'; } else { i.type='password'; btn.textContent='👁'; } }
  async function changeAdminPass() { const v = document.getElementById('adminPassInput').value.trim(); if (!v) { showToast('Password cannot be empty'); return; } data.adminPass = v; await saveData(); showToast('Admin password updated'); }
  async function changeTeamPass(teamId) { const v = document.getElementById('teamPass_'+teamId).value.trim(); if (!v) { showToast('Password cannot be empty'); return; } const t = data.teams.find(x=>x.id===teamId); if (t) { t.password=v; await saveData(); showToast(t.name+' password updated'); } }
  async function changeMyTeamPass() { const v = document.getElementById('teamPassInput').value.trim(); if (!v) { showToast('Password cannot be empty'); return; } const t = data.teams.find(x=>x.id===session.teamId); if (t) { t.password=v; await saveData(); showToast('Password updated'); document.getElementById('teamPassInput').value=''; } }
  async function addMember(teamId) {
    const input = document.getElementById('newMember_'+teamId); const name = input.value.trim(); if (!name) return;
    const t = data.teams.find(x=>x.id===teamId); if (!t) return;
    if (allEditors().includes(name)) { showToast('That name already exists'); return; }
    t.members.push(name); input.value=''; renderAdminSettings(); renderAll(); await saveData(); showToast(`${name} added to ${t.name}`);
  }
  function removeMember(teamId, name) {
    const t = data.teams.find(x=>x.id===teamId); if (!t) return;
    if (name === t.leader) { showToast('Cannot remove the team leader'); return; }
    showConfirm(`Remove ${name}?`, `${name} will be removed from ${t.name}. Their past points stay in the records.`, 'Remove', async () => {
      t.members = t.members.filter(m => m !== name); renderAdminSettings(); renderAll(); await saveData(); showToast(`${name} removed`);
    }, true);
  }

  function showConfirm(title, message, actionLabel, onConfirm, isDanger) {
    document.getElementById('confirmTitle').textContent = title;
    document.getElementById('confirmMessage').textContent = message;
    const btn = document.getElementById('confirmActionBtn'); btn.textContent = actionLabel; btn.style.display = '';
    if (isDanger) { btn.style.background = 'linear-gradient(135deg,#ff7373,#ff5252)'; btn.style.color = '#fff'; }
    else { btn.style.background = ''; btn.style.color = ''; }
    btn.onclick = () => { closeModal('confirmModal'); onConfirm(); };
    document.getElementById('confirmModal').classList.add('show');
  }
  function showPrompt(title, message, defaultVal, onSubmit) {
    document.getElementById('confirmTitle').textContent = title;
    document.getElementById('confirmMessage').innerHTML = `${escapeHtml(message)}<input type="text" id="promptInput" class="cell-input" style="margin-top:12px;border-radius:10px;width:100%" value="${escapeAttr(defaultVal||'')}">`;
    const btn = document.getElementById('confirmActionBtn'); btn.textContent = 'Save'; btn.style.background = ''; btn.style.color = ''; btn.style.display = '';
    btn.onclick = () => { const v = document.getElementById('promptInput').value; closeModal('confirmModal'); onSubmit(v); };
    document.getElementById('confirmModal').classList.add('show');
    setTimeout(() => { const i = document.getElementById('promptInput'); if (i){ i.focus(); i.select(); i.addEventListener('keydown', e=>{ if(e.key==='Enter') btn.click(); }); } }, 50);
  }
  function closeModal(id) { document.getElementById(id).classList.remove('show'); }

  // showChoice: presents buttons for each option
  let _choiceCb = null;
  function showChoice(title, options, onChoose) {
    document.getElementById('confirmTitle').textContent = title;
    document.getElementById('confirmMessage').innerHTML =
      '<div style="display:flex;flex-direction:column;gap:8px;margin-top:8px">' +
      options.map((o,i) => `<button class="btn btn-secondary" style="width:100%;padding:13px" onclick="_pickChoice('${escapeAttr(o.value)}')">${escapeHtml(o.label)}</button>`).join('') +
      '</div>';
    _choiceCb = onChoose;
    // hide the default action button for choice modal
    document.getElementById('confirmActionBtn').style.display = 'none';
    document.getElementById('confirmModal').classList.add('show');
  }
  function _pickChoice(val) {
    closeModal('confirmModal');
    document.getElementById('confirmActionBtn').style.display = '';
    const cb = _choiceCb; _choiceCb = null;
    if (cb) cb(val);
  }

  document.querySelectorAll('.modal-overlay').forEach(o => { o.addEventListener('click', e => { if (e.target === o) o.classList.remove('show'); }); });
  let toastT = null;
  function showToast(msg) { const t = document.getElementById('toast'); t.textContent = msg; t.classList.add('show'); if (toastT) clearTimeout(toastT); toastT = setTimeout(() => t.classList.remove('show'), 2200); }
  function escapeHtml(s) { const d = document.createElement('div'); d.textContent = s == null ? '' : s; return d.innerHTML; }
  function escapeAttr(s) { return (s == null ? '' : String(s)).replace(/"/g, '&quot;'); }
  document.addEventListener('keydown', e => {
    if (e.key === 'Enter' && document.getElementById('loginScreen').style.display !== 'none' && !document.querySelector('.modal-overlay.show')) login();
    if (e.key === 'Escape') { document.querySelectorAll('.modal-overlay.show').forEach(m => m.classList.remove('show')); closeMenus(); }
  });
  async function init() {
    try {
      await loadData(); loadSession(); populateLoginDropdown();
      document.getElementById('loadingOverlay').style.display = 'none';
      if (session) showApp(); else document.getElementById('loginScreen').style.display = 'flex';
    } catch(e) { console.error('Init failed:', e); document.getElementById('loadingText').textContent = 'Connection failed. Refresh the page.'; document.getElementById('loadingText').style.color = '#ff5252'; }
  }
  init();
</script>
</body>
</html>
