function butao() {
    nome = document.getElementById('inputnome').value
    altura = parseFloat(document.getElementById('inputaltura').value)
    peso = parseFloat(document.getElementById('inputpeso').value)

    if (nome && peso && altura) {
        var altura = (altura / 100)

        var imc = (peso/(altura*altura)).toFixed(2)

        var aviso = ''

        if (imc < 18.5) {
            aviso = 'magro'
        } else if (imc > 18.5 && imc < 24.9) {
            aviso = 'normal'
        } else if (imc > 25 && imc < 29.9) {
            aviso = 'sobrepeso'
        } else if (imc > 30 && imc < 39.9) {
            aviso = 'obeso'
        } else if (imc > 40) {
            aviso = 'gravemente obeso'
        };

        resultado = document.getElementById('Resultado')
        resultado.innerHTML = `${nome}, seu IMC é: ${imc}, você está ${aviso} `
    } else {
        document.getElementById('Resultado').innerHTML = 'Resultado: Preencha tudo!'
    }
    
}