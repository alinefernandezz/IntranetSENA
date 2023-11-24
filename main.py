from comunidadesenai import app
from comunidadesenai import app, database
from comunidadesenai.models import Usuario

# Comandos para deletar e recriar o Banco de Dados
#with app.app_context():
    #database.drop_all()
    #database.create_all()


#Comando para verificar os usuarios no Banco de Dados
#with app.app_context():
    #meus_usuarios = Usuario.query.all()
    #meus_usuarios = Usuario.query.first()
    #print(meus_usuarios)

if __name__ == '__main__':
    app.run(debug=True)




