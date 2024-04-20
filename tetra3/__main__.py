import argparse
import inspect
import typing

import tetra3


def _parse_tuple(types: tuple) -> typing.Callable[[str], tuple]:
    def _handler(value: str) -> tuple:
        value = (value
                 .replace("(", "")
                 .replace(")", "")
                 .replace(" ", ""))
        parts = value.split(",")

        if len(parts) != len(types):
            raise ValueError(f"Invalid number of arguments: {len(parts)}")

        result = []

        for i, p in enumerate(parts):
            result.append(types[i](p))

        return tuple(result)

    return _handler


def _tuple_help(types: tuple) -> str:
    names = [t.__name__ for t in types]
    return f"tuple string such as =\"({', '.join(names)})\""


def generate_database():
    # Create instance without loading any database.
    t3 = tetra3.Tetra3(load_database=None)

    parser = argparse.ArgumentParser()

    sig = inspect.signature(t3.generate_database)

    for param in sig.parameters.values():
        name = param.name.replace("_", "-")
        is_required = param.default == inspect.Parameter.empty

        if isinstance(param.default, bool):
            # boolean type parameters get special handling
            parser.add_argument(
                f"--{name}" if param.default else f"--no-{name}",
                action="store_true" if param.default else "store_false",
                required=is_required,
            )

        else:
            arg_type = None
            help = None
            if any(param.annotation is v for v in [float, int]):
                # parse as basic type
                arg_type = param.annotation
                help = f"{param.annotation.__name__} value"
            elif any(isinstance(param.annotation, t) for t in [typing.GenericAlias, typing._GenericAlias]):
                if param.annotation.__name__.lower() == "tuple":
                    # parse tuple to exact type (nesting not supported)
                    arg_type = _parse_tuple(types=param.annotation.__args__)
                    help = _tuple_help(param.annotation.__args__)

            parser.add_argument(
                f"--{name}",
                default=param.default,
                type=arg_type,
                help=help,
                required=is_required,
            )
    args = parser.parse_args()
    gen_db_kwargs = {}
    for arg_name in vars(args):
        arg_value = getattr(args, arg_name)

        arg_name = arg_name.lstrip("no_").replace("-", "_")

        gen_db_kwargs[arg_name] = arg_value

    # Generate and save database.
    t3.generate_database(**gen_db_kwargs)
