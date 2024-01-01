

CodeMirror.defineMode("typewise", function() {
    
  return {
    startState: function() {
      return { enComentario: false, enFuncion: false };
      },
      token: function(stream,state) {
        if (state.enComentario) {
          if (stream.match("*/")) {
              state.enComentario = false;
          } else {
              stream.next();
          }
          return "comentario";
        } else if (stream.match("/*")) {
          state.enComentario = true;
          return "comentario";
        }else if  ((stream.sol() || /\s/.test(stream.string.charAt(stream.start - 1))) &&(stream.match(/create/i) || stream.match(/alter/i) || stream.match(/use/i) || stream.match(/drop/i) || stream.match(/truncate/i)|| stream.match(/select/i)|| stream.match(/update/i)|| stream.match(/delete/i)|| stream.match(/insert/i)|| stream.match(/function/i)|| stream.match(/procedure/i)|| stream.match(/data base/i)|| stream.match(/into/i)|| stream.match(/table/i)|| stream.match(/where/i)|| stream.match(/from/i) || stream.match(/values/i)|| stream.match(/colum/i)|| stream.match(/;/i)|| stream.match(/ ;/i))) {
          return "variable-2";
        } else if  ((stream.sol() || /\s/.test(stream.string.charAt(stream.start - 1))) && (stream.match(/primary key/i) || stream.match(/reference/i) ) ){
          return "keyword";
        }else if ((stream.sol() || /\s/.test(stream.string.charAt(stream.start - 1))) &&(stream.match(/cast/i) || stream.match(/suma/i) || stream.match(/contar/i) || stream.match(/concatena/i) || stream.match(/hoy/i)|| stream.match(/substraer/i))){
          return "property";
        }else if ((stream.sol() || /\s/.test(stream.string.charAt(stream.start - 1))) &&(stream.match(/int/i) || stream.match(/decimal/i) || stream.match(/nchar/i) || stream.match(/nvarchar/i) || stream.match(/bit/i)|| stream.match(/date/i)|| stream.match(/datetime/i))){
          return "variable-2";
        }else if ((stream.sol() || /\s/.test(stream.string.charAt(stream.start - 1))) &&(stream.match(/set/i) || stream.match(/declare/i) || stream.match(/exc/i) || stream.match(/as/i)|| stream.match(/and/i)|| stream.match(/or/i)|| stream.match(/not/i)|| stream.match(/between/i)|| stream.match(/null/i) )){
          return "variable-2";
        }else if ((stream.sol() || /\s/.test(stream.string.charAt(stream.start - 1))) &&(stream.match(/begin/i) || stream.match(/when/i) || stream.match(/then/i) || stream.match(/else/i) || stream.match(/if/i)|| stream.match(/case/i)|| stream.match(/while/i)|| stream.match(/end/i)|| stream.match(/return/i))){
          return "atom";
        
        }else if (stream.match(/\'[^\']\'/)) {
            return "string";
        } else if (stream.match(/\"(\\.|[^"\\])*\"/)) {
            return "string";
          
        }

       
        stream.next();
        return null;
      }
    };
  });


  



CodeMirror.defineMIME("text/x-typewise", "typewise");

function myHint(editor, options) {
    const cursor = editor.getCursor();
    const token = editor.getTokenAt(cursor);
    const start = token.start;
    const end = cursor.ch;
    const currentWord = token.string.slice(0, end - start);
    const suggestions = ["use", "int", "procedure", "create", "alter", "drop", "truncate", "select", "update", "delete", "insert", "function", "procedure", "if", "case", "while", "data", "base", "into", "table", "declare", "add", "set", "exc", "begin", "when", "then", "else", "from", "where", "end", "as", "key", "values", "primary", "reference", "column", "cast", "suma", "contar", "return", "concatena", "hoy", "substraer", "and", "or", "not", "between", "null", "nvarchar", "nchar", "int", "decimal", "bit", "date", "datetime"].filter(function(item) {
      return item.toLowerCase().indexOf(currentWord.toLowerCase()) == 0;
    });
    return {
      list: suggestions,
      from: CodeMirror.Pos(cursor.line, start),
      to: CodeMirror.Pos(cursor.line, end)
    };
}

