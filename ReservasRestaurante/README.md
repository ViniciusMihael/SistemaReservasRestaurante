#! Desenvolver uma api Restful #

#* Registrar reservas de mesas#
#* Controlar o status das reservas e das mesas#
#* Bloquear reservas quando a mesa estiver ocupada#



#! Funcionalidades#


#? Autenticaçao de usuarios#

#* Registro: O usuário deve ser capaz de se registrar com um nome, e-mail e senha.

#* Login: Usuários autenticados recebem um token JWT para acesso às funcionalidades de reservas.

#* Restrição de Acesso: Apenas usuários logados podem criar e visualizar reservas.


#? Gestão de Mesas #

#* Listagem: Listar todas as mesas disponíveis no restaurante.

#* Criar Mesa: Administradores podem adicionar novas mesas ao sistema com um nome e capacidade de pessoas.

#* Status da Mesa: Cada mesa pode estar disponível, reservada ou inativa.


#? Sistemas de Reservas #

#* Criar Reserva: Usuários autenticados podem criar reservas para mesas específicas.

#* Verificar Disponibilidade: A API deve verificar se a mesa está disponível no horário solicitado antes de confirmar a reserva.

#* Cancelar Reserva: Usuários podem cancelar suas reservas, o que libera a mesa para novas reservas.


#? Controle de Status

#* Status das Mesas: Mesas ficam reservadas automaticamente ao serem associadas a uma reserva.

#* Status das Mesas: Mesas ficam reservadas automaticamente ao serem associadas a uma reserva.