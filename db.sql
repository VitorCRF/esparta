select ALUNO.Nome from turma t
join ALUNO a
on a.id = t.aluno_id  
join PROFESSOR p
on p.id = t.PROFESSOR_id
where p.nome = 'JOAO PEDRO'


select turma.dia_da_semana from turma t
join DISCIPLINA d
on d.id = t.disciplina_id
where d.nome = 'MATEMATICA'

select ALUNO.Nome from turma t
join DISCIPLINA d
on d.id = t.disciplina_id 
join ALUNO a
on a.id = a.t.aluno_id
where d.nome = 'MATEMATICA' and d.nome = 'FISICA'

select DISCIPLINA.Nome from disciplina d
join TURMA t
on d.id = t.disciplina_id
where t.disciplina_id is null

select aluno.nome from turma t
join disciplina d
on d.id = t.disciplina_id
join aluno a
on a.id = t.aluno_id
where d.nome = 'MATEMATICA' and d.nome != 'QUIMICA'
