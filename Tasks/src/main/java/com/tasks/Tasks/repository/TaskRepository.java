package com.tasks.Tasks.repository;

import com.tasks.Tasks.model.Task;

import org.springframework.data.jpa.repository.JpaRepository;

public interface TaskRepository extends JpaRepository<Task, Long> {

}
