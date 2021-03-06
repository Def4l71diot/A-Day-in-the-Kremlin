#!/usr/bin/python3
import os
from adventure_game.providers import *
from adventure_game.game_objects import ObjectsLoader
from adventure_game.factories import ItemFactory, PuzzleFactory, RoomFactory, PlayerFactory
from adventure_game.game_engine import GameEngine


def main():
    xml_data_file_name = os.path.abspath("game_data/data.xml")
    console_writer = ConsoleWriterProvider()
    console_reader = ConsoleReaderProvider()
    command_parser = CommandParserProvider()
    item_factory = ItemFactory()
    puzzle_factory = PuzzleFactory()
    room_factory = RoomFactory()
    player_factory = PlayerFactory()

    objects_loader = ObjectsLoader(item_factory, puzzle_factory, room_factory, player_factory, xml_data_file_name)
    game_engine = GameEngine(console_writer, console_reader, command_parser, objects_loader)

    game_engine.run()


if __name__ == "__main__":
    main()
