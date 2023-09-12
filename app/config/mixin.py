from pydantic import BaseSettings


class PrintSettingsMixin(BaseSettings):
    def print_config(self, ident: int = 0):
        for key, value in self.dict().items():
            if isinstance(value, dict):
                print(f"{key}:")  # noqa
                for key_, value_ in value.items():
                    print(f"{'  ' * (ident + 1)}{key_}:  {value_}")  # noqa
            else:
                print(f"{'  ' * ident}{key}:  {value}")  # noqa
