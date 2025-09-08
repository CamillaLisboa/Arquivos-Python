from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
from abc import ABC, abstractmethod
from datetime import date

# ---------- Entidades de Domínio ----------

class Salary:
    """
    Composição: Salary 'pertence' ao Employee. Se Employee deixar de existir,
    normalmente seu Salary também deixa (forte relação).
    Mostra getters/setters com validação.
    """
    def __init__(self, gross: float) -> None:
        self.gross = gross  # chama setter

    @property
    def gross(self) -> float:
        return self._gross

    @gross.setter
    def gross(self, value: float) -> None:
        if value < 0:
            raise ValueError("Salário bruto não pode ser negativo")
        self._gross = float(value)

    @property
    def monthly(self) -> float:
        return self._gross

    @property
    def yearly(self) -> float:
        return self._gross * 12


class Person:
    """Classe base. Demonstra herança com Employee."""
    def __init__(self, name: str, age: int) -> None:
        self.name = name  # setter
        self.age = age    # setter

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        v = (value or "").strip()
        if len(v) < 2:
            raise ValueError("Nome muito curto")
        self._name = v

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if value < 0 or value > 120:
            raise ValueError("Idade inválida")
        self._age = int(value)


class Employee(Person):
    """
    Herança: Employee é uma Person.
    Composição: possui um Salary.
    """
    def __init__(self, name: str, age: int, salary: Salary, gender: str, contrib_years: int):
        super().__init__(name, age)
        self.salary = salary
        self.gender = gender  # setter
        self.contrib_years = contrib_years  # setter

    @property
    def gender(self) -> str:
        return self._gender

    @gender.setter
    def gender(self, value: str) -> None:
        v = (value or "").strip().lower()
        if v not in {"f","m"}:
            raise ValueError("Gênero deve ser 'f' ou 'm'")
        self._gender = v

    @property
    def contrib_years(self) -> int:
        return self._contrib_years

    @contrib_years.setter
    def contrib_years(self, value: int) -> None:
        if value < 0 or value > 60:
            raise ValueError("Anos de contribuição inválidos")
        self._contrib_years = int(value)


# ---------- Políticas (SOLID) ----------

class RetirementPolicy(ABC):
    """
    DIP/OCP/LSP: Calculadora depende desta abstração; políticas concretas podem
    variar sem alterar a calculadora.
    """
    @abstractmethod
    def min_age(self, gender: str) -> int: ...
    @abstractmethod
    def replacement_rate(self, gender: str, contrib_years: int) -> float: ...


class SimpleBrazilPolicy(RetirementPolicy):
    """
    * Educacional *: simplificação de regras brasileiras atuais.
    - Idade mínima: 62F, 65M
    - Taxa de reposição: 60% + 2% por ano acima de 15(F) / 20(M), teto 100%.
    """
    def min_age(self, gender: str) -> int:
        return 62 if gender == "f" else 65

    def replacement_rate(self, gender: str, contrib_years: int) -> float:
        base = 0.60
        limiar = 15 if gender == "f" else 20
        extra_years = max(0, contrib_years - limiar)
        rate = base + 0.02 * extra_years
        return max(0.0, min(1.0, rate))


class RetirementCalculator:
    """
    SRP: Responsável apenas por cálculos.
    DIP: Depende de RetirementPolicy (abstração), injetada via agregação.
    Agregação: mantém referência a uma policy que pode ser compartilhada.
    """
    def __init__(self, policy: RetirementPolicy) -> None:
        self._policy = policy

    def evaluate(self, emp: Employee) -> dict:
        min_age = self._policy.min_age(emp.gender)
        years_left = max(0, min_age - emp.age)
        eligible = years_left == 0
        rate = self._policy.replacement_rate(emp.gender, emp.contrib_years)

        # Benefício estimado
        estimated = emp.salary.monthly * rate

        current_year = date.today().year
        est_year = current_year + years_left

        return {
            "name": emp.name,
            "age": emp.age,
            "gender": emp.gender,
            "contrib_years": emp.contrib_years,
            "salary": emp.salary.monthly,
            "min_age": min_age,
            "years_left": years_left,
            "eligible": eligible,
            "replacement_rate": rate,
            "estimated_benefit": estimated,
            "estimated_year": est_year,
        }
