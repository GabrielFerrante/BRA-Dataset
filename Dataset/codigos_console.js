/* Os códigos abaixo devem ser executados no console do navegador (Inspecionar elemento) */

/* Parte 1 
  - Essa função simula o clique do botão direito na imagem, para que dessa forma possamos capturar a URL da imagem usando o Menu de contexto 
           (que é aquela caixa com as opções que aparecem quando clica com o botão direito)
  - créditos desse trecho de código: @jmiserez (https://stackoverflow.com/a/52878847)
*/
function simulateRightClick( element ) {
    var event1 = new MouseEvent( 'mousedown', {
        bubbles: true,
        cancelable: false,
        view: window,
        button: 2,
        buttons: 2,
        clientX: element.getBoundingClientRect().x,
        clientY: element.getBoundingClientRect().y
    } );
    element.dispatchEvent( event1 );
    var event2 = new MouseEvent( 'mouseup', {
        bubbles: true,
        cancelable: false,
        view: window,
        button: 2,
        buttons: 0,
        clientX: element.getBoundingClientRect().x,
        clientY: element.getBoundingClientRect().y
    } );
    element.dispatchEvent( event2 );
    var event3 = new MouseEvent( 'contextmenu', {
        bubbles: true,
        cancelable: false,
        view: window,
        button: 2,
        buttons: 0,
        clientX: element.getBoundingClientRect().x,
        clientY: element.getBoundingClientRect().y
    } );
    element.dispatchEvent( event3 );
}

/* Parte 2
  - captura o parâmetro URL da query string (pois cada URL da imagem é armazenado em uma query string)
  - o que o código faz é pegar as URLs dessa query
*/
function getURLParam( queryString, key ) {
    var vars = queryString.replace( /^\?/, '' ).split( '&' );
    for ( let i = 0; i < vars.length; i++ ) {
        let pair = vars[ i ].split( '=' );
        if ( pair[0] == key ) {
            return pair[1];
        }
    }
    return false;
}

/* Parte 3
  - gera e automaticamente faz o download do arquivo .txt que contém as URLs das imagens 
  - Cada uma das URLs vão estar no parâmetro contents passado para a função createDownload. 
  - Primeiro criamos um "hiddenElement" e então populamos ele com o contents, em seguida é criado um link com o arquivo urls.txt, 
  então é simulado o click no elemento. Quando a função createDownload rodar o navegador deve fazer o download do arquivo
*/
function createDownload( contents ) {
    var hiddenElement = document.createElement( 'a' );
    hiddenElement.href = 'data:attachment/text,' + encodeURI( contents );
    hiddenElement.target = '_blank';
    hiddenElement.download = 'urls.txt';
    hiddenElement.click();
}

/* Parte 4
  - A função grabUrls cria o que o Javascript chama de um Promise. 
  - O que ele vai fazer é unir essas funções que definimos antes para que assim seja capturado todas as URLs das imagens
*/
function grabUrls() {
    var urls = [];
    return new Promise( function( resolve, reject ) {
        var count = document.querySelectorAll(
        	'.isv-r a:first-of-type' ).length,
            index = 0;
        Array.prototype.forEach.call( document.querySelectorAll(
        	'.isv-r a:first-of-type' ), function( element ) {
            // usando o menu do botao direito o google deve selecionar 
            // URL da imagem em tamanho real; não funciona no Internet Explorer
            // (http://pyimg.co/byukr)
            simulateRightClick( element.querySelector( ':scope img' ) );
            // espera para aparecer no elemento <a>
            var interval = setInterval( function() {
                if ( element.href.trim() !== '' ) {
                    clearInterval( interval );
                    // extrai a versão em tamanho real da imagem
                    let googleUrl = element.href.replace( /.*(\?)/, '$1' ),
                        fullImageUrl = decodeURIComponent(
                        	getURLParam( googleUrl, 'imgurl' ) );
                    if ( fullImageUrl !== 'false' ) {
                        urls.push( fullImageUrl );
                    }
                    // as vezes a URL returna a string "false" 
                    // e ainda queremos contabilizar nesses casos
                    index++;
                    if ( index == ( count - 1 ) ) {
                        resolve( urls );
                    }
                }
            }, 10 );
        } );
    } );
}

/* Parte 5
  - A ultima parta docódigo vai chamar a função principal para executar todas as instruções que definimos anteriormente, 
    e assim fazer o download do .txt
*/
grabUrls().then( function( urls ) {
    urls = urls.join( '\n' );
    createDownload( urls );
} );

/* Créditos do código: RealBigMarketing e PyImageSearch 
   https://www.pyimagesearch.com/2017/12/04/how-to-create-a-deep-learning-dataset-using-google-images/ 
*/