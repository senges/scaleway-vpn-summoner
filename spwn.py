#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
# Created By : @senges
# Created Date: Dec. 2021
# Description : CLI tool to quickly manage VPNs in a Scaleway infrastructure
# =============================================================================

from scaleway.apis import AccountAPI
from scaleway.apis import ComputeAPI
from slumber.exceptions import HttpClientError
from rich.console import Console

from pathlib import Path

import os
import json
import click

# + ----------------------------------------------------- +
# | Click area, kept clean for global readability purpose |
# + ----------------------------------------------------- +

@click.group()
# @click.option('-t', '--token', is_flag = False, required = False, help = 'Scaleway API Token')
def main():
    pass

@main.command( name = 'configure' )
def _configure():
    """Configure local setup."""

    configure()

@main.command( name = 'list' )
def _list():
    """List active VPN."""

    list_instances()

@main.command( name = 'new' )
def _new():
    """Create new VPN instance."""

    new_instance()

@main.command( name = 'destroy' )
@click.argument( 'name' , required = True, type=click.STRING)
def _destroy(name):
    """Destroy VPN instance."""

    delete_insance( name )

@main.command( name = 'describe' )
@click.argument( 'name' , required = True, type=click.STRING)
def _describe(name):
    """Describe VPN instance."""

    describe_instance( name )

@main.command( name = 'connect' )
@click.argument( 'name' , required = True, type=click.STRING)
def _connect(name):
    """Connect to VPN instance."""

    connect_instance( name )

# + ----------------------------------------- +
# | Program area, where all the magic happend |
# + ----------------------------------------- +

# Configure local env
# Todo: add project selection
def configure():
    config_folder = os.environ.get('HOME') + '/.scl-vpn-summoner'

    api_tok = click.prompt('API Token ', default = False, show_default = False, type = str)
    
    try:
        Path(config_folder).mkdir( exist_ok = True )

    except FileNotFoundError:
        panic( '$HOME directory must exist and be exported' )

    with open(os.path.join(config_folder, 'config.json'), 'w+') as f:
        config = {
            'api_tok' : api_tok
        }

        json.dump(config, f, indent = 4)

    success('Config file successfully created at ' + os.path.join(config_folder, 'config.json'))

# Get key from config file
def get_config(key: str):
    try:
        with open(os.environ.get('HOME') + '/.scl-vpn-summoner/config.json') as f:
            value = json.load(f).get(key)
    except:
        value = None

    return value

# Load api token from local config file
def load_api():

    if api_key := get_config('api_tok'):
        return ComputeAPI(auth_token = api_key)

    panic('Unproper local config, please run `spwn config` to fix it.')

# List scaleway instances tagged as vpn
def list_instances():
    instances = api.query().servers.get( tags = 'vpn-sum' )['servers']
    
    for instance in instances:
        info( instance['name'] )

# Create new instance
def new_instance():
    raise NotImplementedError()

# Delete instance `id'
def delete_insance(id: str):
    raise NotImplementedError()

# Connect to vpn `id'
def connect_instance(id: str):
    raise NotImplementedError()

# Describe vpn `id'
def describe_instance(id: str):
    raise NotImplementedError()
    
# Display info message
def info(msg: str):
    console.print('[yellow]~ ' + msg)

# Display success message
def success(msg: str):
    console.print('[green]✓ ' + msg)

# Program panic
def panic(err: str):
    console.print('[red]✗ ' + err)
    exit(1)

# Global loads
console     = Console()
api         = load_api()

if __name__ == '__main__':
    main()