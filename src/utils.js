export function buildRegex(search){
    var reg = '(';
    var words = search.split(' ');
    words.forEach(word => {
        if(word !== ""){
            reg += '\\b' + word + '|';
        }
    });
    reg = reg.slice(0, reg.lastIndexOf('|'));
    reg += ')';

    return new RegExp(reg, 'i');
}