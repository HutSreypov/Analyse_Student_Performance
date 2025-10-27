// static/js/progress.js
document.addEventListener('DOMContentLoaded', function () {
  if (typeof STUDENT_ID === 'undefined') return;

  const apiUrl = `/api/student/${STUDENT_ID}/progress`;

  fetch(apiUrl)
    .then(r => r.json())
    .then(data => {
      if (data.error) {
        console.error(data.error);
        return;
      }
      const scores = data.scores || [];

      // aggregate totals by subject (if multiple terms exist)
      const subjectTotals = {};
      const gradeCounts = {};

      scores.forEach(s => {
        const subj = s.subject_name;
        subjectTotals[subj] = subjectTotals[subj] || [];
        subjectTotals[subj].push({total: s.total, term: s.term, created_at: s.created_at});

        gradeCounts[s.grade] = (gradeCounts[s.grade] || 0) + 1;
      });

      // Build chart data arrays
      const subjectLabels = Object.keys(subjectTotals);
      const subjectAverages = subjectLabels.map(lbl => {
        const arr = subjectTotals[lbl];
        const sum = arr.reduce((a,b)=>a+(b.total||0),0);
        return (arr.length ? (sum/arr.length).toFixed(2) : 0);
      });

      // Subject Totals Chart (bar)
      const ctx = document.getElementById('subjectTotalsChart').getContext('2d');
      new Chart(ctx, {
        type: 'bar',
        data: {
          labels: subjectLabels,
          datasets: [{
            label: 'Average total',
            data: subjectAverages,
            borderWidth: 1
          }]
        },
        options: {
          scales: { y: { beginAtZero: true, max: 100 } },
          plugins: { legend: { display: false } }
        }
      });

      // Grade distribution (pie)
      const gradeLabels = Object.keys(gradeCounts);
      const gradeValues = gradeLabels.map(g => gradeCounts[g]);
      const ctx2 = document.getElementById('gradeDistChart').getContext('2d');
      new Chart(ctx2, {
        type: 'pie',
        data: {
          labels: gradeLabels,
          datasets: [{ data: gradeValues }]
        },
        options: {}
      });

      // populate scores table
      const tbody = document.querySelector('#scoresTable tbody');
      tbody.innerHTML = '';
      scores.forEach(s => {
        const tr = document.createElement('tr');
        tr.innerHTML = `
          <td>${s.subject_name}</td>
          <td>${s.midterm}</td>
          <td>${s.assignment}</td>
          <td>${s.final}</td>
          <td>${(s.total!==null? s.total.toFixed(2): '')}</td>
          <td>${s.grade}</td>
          <td>${s.term || ''}</td>
          <td>${new Date(s.created_at).toLocaleString()}</td>
        `;
        tbody.appendChild(tr);
      });
    })
    .catch(err => {
      console.error('Failed to load progress:', err);
    });
});
