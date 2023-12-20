-- Select useful data for the analysis

Select Location, date, total_cases, new_cases, total_deaths, population
From portfolio.coviddeaths
order by 1,2;

-- Looking at total cases vs total deaths
-- Indicates death probability if you have covid

Select Location, date, total_cases, total_deaths, (total_deaths/total_cases)*100 as DeathRate
From portfolio.coviddeaths
Where location like '%south africa%'
order by 1,2;

-- Looking at total cases vs population
-- showing probablity of covid infection within a population

Select Location, date, total_cases, population, (total_cases/population)*100 as InfectionRate 
From portfolio.coviddeaths
Where location like '%south africa%'
order by 1,2;

-- highest infection rate per country

Select Location, max(total_cases) MaxInfectionCount, population, max(total_cases/population)*100 as MaxInfectionRate 
From portfolio.coviddeaths
Group by Location, population
order by MaxInfectionRate desc;

-- country with the highest death count by country

Select Location, max(CAST(total_deaths as unsigned)) as MaxDeathCount
From portfolio.coviddeaths
Group by Location
order by MaxDeathCount desc;

-- percentage of death from cases

select date, sum(new_cases) as total_cases, sum(cast(new_deaths as unsigned)) as total_deaths, sum(cast(new_deaths as unsigned))*100/sum(new_cases) as DeathPerecntage
from portfolio.coviddeaths
group by date
order by 1,2;

-- population vs vaccinations

select vax.continent, vax.location , vax.date, dea.population, vax.new_vaccinations
from portfolio.coviddeaths dea
join portfolio.covidvax vax
	on dea.location = vax.location
    and dea.date = vax.date
order by 2,3;