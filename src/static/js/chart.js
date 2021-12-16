var xValues = ['Ene','Feb','Mar','Abr','Jun','Jul','Ago','Sep','Nov','Dic'];

new Chart("myChart", {
  type: "line",
  data: {
    labels: xValues,
    datasets: [{
      label: 'Cosumidores',
      data: [860,1140,1060,1060,1070,1110,1330,2210,7830,2478],
      borderColor: "red",
      fill: false
    },{
      label: 'Vendedores',
      data: [1600,1700,1700,1900,2000,2700,4000,5000,6000,7000],
      borderColor: "green",
      fill: false
    }]
  },
  options: {
    legend: {display: true}
  }
});


new Chart("myChart2", {
  type: "line",
  data: {
    labels: xValues,
    datasets: [{
      label: 'Ventas',
      data: [1600,1700,1700,1900,2000,2700,4000,5000,6000,7000],
      borderColor: "green",
      fill: false
    }]
  },
  options: {
    legend: {display: true}
  }
});

new Chart("Tráfico", {
    type: "line",
    data: {
      labels: xValues,
      datasets: [{
        label: 'Cosumidores',
        data: [860,1140,1060,1060,1070,1110,1330,2210,7830,2478],
        borderColor: "blue",
        fill: false
      }]
    },
    options: {
      legend: {display: true}
    }
  });

var xValues = ['Ene', 'Feb- Abr','May - Ago','Sep - Dic'];

new Chart("earnings", {
  type: "bar",
  data: {
    labels: xValues,
    datasets: [{
      label: 'Crecimiento %',
      backgroundColor: 'blue',
      data:[0,10,12,15],
    }]
  },
  options: {
    legend: {display: true}
  }
});


new Chart("earnings2", {
  type: "bar",
  data: {
    labels: ['Predataor','The Batman','Alien','Pokemon'],
    datasets: [{
      label: 'Ventas por producto',
      backgroundColor: 'blue',
      data:[0,10,12,15],
    }]
  },
  options: {
    legend: {display: true}
  }
});