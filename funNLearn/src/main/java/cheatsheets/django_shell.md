
# Django Shell Cheat sheet:
Current Django Version: [3.0](https://docs.djangoproject.com/en/3.0/ref/models/querysets/)

## Methods that return new [QuerySets](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#methods-that-return-new-querysets)
- - -
* Can be chained:

```python
Entry.objects.filter(**kwargs).exclude(**kwargs).order_by(**kwargs)
```

 * [filter](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#filter)
 * [exclude](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#exclude)
 * [annotate](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#annotate)
 * [order_by](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#order-by)
 * [reverse](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#reverse)
 * [distinct](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#distinct)
 * [values](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#values)
 * [values_list](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#values-list)
 * [dates](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#dates)
 * [datetimes](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#datetimes)
 * [none](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#none)
 * [all](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#all)
 * [union](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#union)
 * [intersection](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#intersection)
 * [difference](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#difference)
 * [select_related](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#select-related)
 * [prefetch_related](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#prefetch-related)
 * [extra](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#extra)
 * [defer](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#defer)
 * [only](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#only)
 * [using](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#using)
 * [select_for_update](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#select-for-update)
 * [raw](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#raw)

## Operators that return new [QuerySets](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#operators-that-return-new-querysets)
- - -

 * [AND (&)](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#and)
 * [OR (|)](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#or)

## Methods that do not return [QuerySets](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#methods-that-do-not-return-querysets)
- - -

 * [get](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#get)
 * [create](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#create)
 * [get_or_create](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#get-or-create)
 * [update_or_create](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#update-or-create)
 * [bulk_create](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#bulk-create)
 * [bulk_update](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#bulk-update)
 * [count](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#count)
 * [in_bulk](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#in-bulk)
 * [iterator](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#iterator)
 * [latest](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#latest)
 * [earliest](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#earliest)
 * [first](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#first)
 * [last](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#last)
 * [aggregate](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#aggregate)
 * [exists](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#exists)
 * [update](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#update)
 * [delete](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#delete)
 * [as_manager](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#as-manager)
 * [explain](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#explain)

## Field lookups
- - -
**Field lookups are how you specify the meat of an SQL WHERE clause. They’re specified as keyword arguments to the QuerySet methods *filter()*, *exclude()* and *get()*.**

```python
Example: Entry.objects.get(id__exact=14)  # note double underscore.
```

 * [exact](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#exact)
 * [iexact](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#iexact)
 * [contains](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#contains)
 * [icontains](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#icontains)
 * [in](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#in)
 * [gt](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#gt)
 * [gte](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#gte)
 * [lt](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#lt)
 * [lte](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#lte)
 * [startswith](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#startswith)
 * [istartswith](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#istartswith)
 * [endswith](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#endswith)
 * [iendswith](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#iendswith)
 * [range](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#range)
 * [date](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#date)
 * [year](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#year)
 * [iso_year](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#iso-year)
 * [month](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#month)
 * [day](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#day)
 * [week](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#week)
 * [week_day](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#week-day)
 * [quarter](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#quarter)
 * [time](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#time)
 * [hour](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#hour)
 * [minute](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#minute)
 * [second](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#second)
 * [isnull](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#isnull)
 * [regex](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#regex)
 * [iregex](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#iregex)

**Protip: Use [in](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#in) to avoid chaining [filter()](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#filter) and [exclude()](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#exclude)**

```python
Entry.objects.filter(status__in=['Hung over', 'Sober', 'Drunk'])
```

## Aggregation functions ([link](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#aggregation-functions))
- - -

 * [expression](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#expression)
 * [output_field](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#output-field)
 * [filter](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#aggregate-filter)
 * [\*\*extra](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#id7)
 * [Avg](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#avg)
 * [Count](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#id8)
 * [Max](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#max)
 * [Min](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#min)
 * [StdDev](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#stddev)
 * [Sum](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#sum)
 * [Variance](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#variance)

## Query-related tools ([link](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#query-related-tools))
- - -

 * [Q() objects](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#q-objects)
 * [Prefetch() objects](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#prefetch-objects)
 * [prefetch_related_objects()](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#prefetch-related-objects)
 * [FilteredRelation() objects](https://docs.djangoproject.com/en/3.0/ref/models/querysets/#filteredrelation-objects)

- - -
