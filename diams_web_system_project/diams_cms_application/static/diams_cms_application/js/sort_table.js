let currentSortColumn = -1;
let sortOrder = '';

function sortTable(column_index) {
  const table = document.getElementById("sortableTable");
  const tbody = table.getElementsByTagName("tbody")[0];
  const rows = Array.from(tbody.getElementsByTagName("tr"));
  const direction = sortOrder === 'asc' ? -1 : 1;
  sortOrder = sortOrder === 'asc' ? 'desc' : 'asc';
  rows.sort((a, b) => {
    const cell_a = a.getElementsByTagName("td")[column_index].innerText;
    const cell_b = b.getElementsByTagName("td")[column_index].innerText;
    const value_a = isNaN(cell_a) ? cell_a.toLocaleLowerCase() : parseFloat(cell_a);
    const value_b = isNaN(cell_b) ? cell_b.toLocaleLowerCase() : parseFloat(cell_b);
    if (value_a < value_b) return -1 * direction;
    if (value_a > value_b) return 1 * direction;
    return 0
  });
  while (tbody.firstChild) {
    tbody.removeChild(tbody.firstChild);
  }
  rows.forEach(row => tbody.appendChild(row));
  updateSortIcons(column_index);
}

function updateSortIcons(column_index) {
  const headers = document.querySelectorAll("#sortableTable th .sort-icon");
  headers.forEach((icon, index) => {
    icon.innerText = index === column_index ? (sortOrder === 'asc' ? '\u25B2' : '\u25BC') : '';
  });
}
