function renderiza_total_vendido(url){
    fetch(url, {
        method: 'get',
    }).then(function(result){
        return result.json()
    }).then(function(data){
        document.getElementById('faturamento_total').innerHTML = data.total
    })
}