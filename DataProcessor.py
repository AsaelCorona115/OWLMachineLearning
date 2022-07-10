# The purpose of this first file is to preprocess the original data we have
# we will delete information that is not needed such as complete columns including
# the name of maps and modes that will not be used in this project. We will also
# the information provided by the file to only include the overall stat_amount for
# all heroes for each player.This file deals with the 2018 stage 1 file

import pandas as pd
from pandas import DataFrame


def ProcessData(UnprocessedDataFile, ProcessedDataFile):

    # Reading the file
    stats = pd.read_csv(UnprocessedDataFile)

    # Eliminating columns we don't need from the original file
    stats = stats.drop(columns=["start_time", "match_id",
                                "stage", "map_type", "map_name", ])

    # Eliminating the individual hero statistics for each player, keeping the overall
    # stats for each player
    stats = stats.loc[stats['hero'] == "All Heroes"]

    # Eliminating the "All heroes" column since now we know the data corresponds to
    # each players All heroes only

    stats = stats.drop(columns=["hero"])

    # Creating single for each category
    TeamsPerPlayer = []
    AllDamageDone = []
    Assists = []
    BarrierDamageDone = []
    DamageQuickMelee = []
    Deaths = []
    Eliminations = []
    FinalBlows = []
    HeroDamageDone = []
    MeleeFinalBlows = []
    MeleePercentageofFinalBlows = []
    ObjectiveKills = []
    ObjectiveTime = []
    ShotsFired = []
    TimeBuildingUltimate = []
    TimeElapsedperUltimateEarned = []
    TimeHoldingUltimate = []
    TimePlayed = []
    UltimatesUsed = []
    WeaponAccuracy = []
    DamageBlocked = []
    DefensiveAssists = []
    HealingDone = []
    OffensiveAssists = []
    Multikills = []
    SoloKills = []
    EnvironmentalDeaths = []
    ReconAssists = []
    AverageTimeAlive = []
    TimeAlive = []
    EnvironmentalKills = []
    TurretsDestroyed = []

    # Capturing the data per player
    for x in stats['player'].unique():
        # The name of each player
        playersName = x

        # All the stats of a single player, not organized
        singlePlayerStats = stats.loc[stats["player"] == x]

        # Getting the name of the team of the player
        TeamsPerPlayer.append(singlePlayerStats['team'].unique()[0])

        # Capturing All Damage done stats and calculating the average
        singlePlayerAllDamageDone = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                          == "All Damage Done"]
        AllDamageDone.append(
            singlePlayerAllDamageDone['stat_amount'].mean())

        # Capturing number of assists and calculating the average
        singlePlayerAssists = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                    == "Assists"]
        Assists.append(
            singlePlayerAssists['stat_amount'].mean())

        # Capturing number of BarrierDamageDone and calculating the average
        singlePlayerBarrierDamage = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                          == "Barrier Damage Done"]
        BarrierDamageDone.append(
            singlePlayerBarrierDamage['stat_amount'].mean())

        # Capturing number of DamageQuickMelee and calculating the average
        singlePlayerDamageQuickMelee = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                             == "Damage - Quick Melee"]
        DamageQuickMelee.append(
            singlePlayerDamageQuickMelee['stat_amount'].mean())

        # Deaths
        singlePlayerDeaths = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                   == "Deaths"]
        Deaths.append(
            singlePlayerDeaths['stat_amount'].mean())

        # Eliminations
        singlePlayerEliminations = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                         == "Eliminations"]
        Eliminations.append(
            singlePlayerEliminations['stat_amount'].mean())

        # FinalBlows
        singlePlayerFinalBlows = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                       == "Final Blows"]
        FinalBlows.append(
            singlePlayerFinalBlows['stat_amount'].mean())

        # HeroDamageDone
        singlePlayerHeroDamageDone = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                           == "Hero Damage Done"]
        HeroDamageDone.append(
            singlePlayerHeroDamageDone['stat_amount'].mean())

        # MeleeFinalBlows
        singlePlayerMeleeFinalBlows = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                            == "Melee Final Blows"]
        MeleeFinalBlows.append(
            singlePlayerMeleeFinalBlows['stat_amount'].mean())

        # MeleePercentageofFinalBlows
        singlePlayerMeleePercentageOfFinalBlows = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                                        == "Melee Percentage of Final Blows"]
        MeleePercentageofFinalBlows.append(
            singlePlayerMeleePercentageOfFinalBlows['stat_amount'].mean())

        # ObjectiveKills
        singlePlayerObjectiveKills = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                           == "Objective Kills"]
        ObjectiveKills.append(
            singlePlayerObjectiveKills['stat_amount'].mean())
        # ObjectiveTime
        singlePlayerObjectiveTime = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                          == "Objective Time"]
        ObjectiveTime.append(
            singlePlayerObjectiveTime['stat_amount'].mean())

        # ShotsFired
        singlePlayerShotsFired = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                       == "Shots Fired"]
        ShotsFired.append(
            singlePlayerShotsFired['stat_amount'].mean())

        # TimeBuildingUltimate
        singlePlayerTimeBuildingUltimate = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                                 == "Time Building Ultimate"]
        TimeBuildingUltimate.append(
            singlePlayerTimeBuildingUltimate['stat_amount'].mean())

        # TimeElapsedperUltimateEarned
        singlePlayerTimeElapsedperUltimateEarned = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                                         == "Time Elapsed per Ultimate Earned"]
        TimeElapsedperUltimateEarned.append(
            singlePlayerTimeElapsedperUltimateEarned['stat_amount'].mean())

        # TimeHoldingUltimate
        singlePlayerTimeHoldingUltimate = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                                == "Time Holding Ultimate"]
        TimeHoldingUltimate.append(
            singlePlayerTimeHoldingUltimate['stat_amount'].mean())

        # TimePlayed
        singlePlayerTimePlayed = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                       == "Time Played"]
        TimePlayed.append(
            singlePlayerTimePlayed['stat_amount'].mean())

        # UltimatesUsed
        singlePlayerUltimatesUsed = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                          == "Ultimates Used"]
        UltimatesUsed.append(
            singlePlayerUltimatesUsed['stat_amount'].mean())

        # WeaponAccuracy
        singlePlayerWeaponAccuracy = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                           == "Weapon Accuracy"]
        WeaponAccuracy.append(
            singlePlayerWeaponAccuracy['stat_amount'].mean())

        # DamageBlocked
        singlePlayerDamageBlocked = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                          == "Damage Blocked"]
        DamageBlocked.append(
            singlePlayerDamageBlocked['stat_amount'].mean())

        # DefensiveAssists
        singlePlayerDefensiveAssists = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                             == "Defensive Assists"]
        DefensiveAssists.append(
            singlePlayerDefensiveAssists['stat_amount'].mean())

        # HealingDone
        singlePlayerHealingDone = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                        == "Healing Done"]
        HealingDone.append(
            singlePlayerHealingDone['stat_amount'].mean())

        # OffensiveAssists
        singlePlayerOffensiveAssists = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                             == "Offensive Assists"]
        OffensiveAssists.append(
            singlePlayerOffensiveAssists['stat_amount'].mean())

        # Multikills
        singlePlayerMultikills = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                       == "Multikills"]
        Multikills.append(
            singlePlayerMultikills['stat_amount'].mean())

        # SoloKills
        singlePlayerSoloKills = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                      == "Solo Kills"]
        SoloKills.append(
            singlePlayerSoloKills['stat_amount'].mean())

        # EnvironmentalDeaths
        singlePlayerEnvironmentalDeaths = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                                == "Environmental Deaths"]
        EnvironmentalDeaths.append(
            singlePlayerEnvironmentalDeaths['stat_amount'].mean())

        # ReconAssists
        singlePlayerReconAssists = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                         == "Recon Assists"]
        ReconAssists.append(
            singlePlayerReconAssists['stat_amount'].mean())

        # AverageTimeAlive
        singlePlayerAverageTimeAlive = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                             == "Average Time Alive"]
        AverageTimeAlive.append(
            singlePlayerAverageTimeAlive['stat_amount'].mean())

        # TimeAlive
        singlePlayerTimeAlive = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                      == "Time Alive"]
        TimeAlive.append(
            singlePlayerTimeAlive['stat_amount'].mean())

        # EnvironmentalKills
        singlePlayerEnvironmentalKills = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                               == "Environmental Kills"]
        EnvironmentalKills.append(
            singlePlayerEnvironmentalKills['stat_amount'].mean())

        # TurretsDestroyed
        singlePlayerTurretsDestroyed = singlePlayerStats.loc[singlePlayerStats['stat_name']
                                                             == "Turrets Destroyed"]
        TurretsDestroyed.append(
            singlePlayerTurretsDestroyed['stat_amount'].mean())

    # Defining the object Dataframe
    players = {
        # unique method returns the possible values of the given column
        'playersName': stats['player'].unique(),
        'team': TeamsPerPlayer,
        'AvgAllDamageDone': AllDamageDone,
        "AvgAssists": Assists,
        "AvgBarrierDamage": BarrierDamageDone,
        "AvgQuickMeleeDamage": DamageQuickMelee,
        "AvgDeaths": Deaths,
        "AvgEliminations": Eliminations,
        "AvgFinalBlows": FinalBlows,
        "AvgHeroDamageDone": HeroDamageDone,
        "AvgMeleeFinalBlows": MeleeFinalBlows,
        "AvgMeleePercentageofFinalBlows": MeleePercentageofFinalBlows,
        "AvgObjectiveKills": ObjectiveKills,
        "AvgObjectiveTime": ObjectiveTime,
        "AvgShotsFired": ShotsFired,
        "AvgTimeBuildingUltimate": TimeBuildingUltimate,
        "AvgTimeElapsedperUltimateEarned": TimeElapsedperUltimateEarned,
        "AvgTimeHoldingUltimate": TimeHoldingUltimate,
        "AvgTimePlayed": TimePlayed,
        "AvgUltimatesUsed": UltimatesUsed,
        "AvgWeaponAccuracy": WeaponAccuracy,
        "AvgDamageBlocked": DamageBlocked,
        "AvgDefensiveAssists": DefensiveAssists,
        "AvgHealingDone": HealingDone,
        "AvgOffensiveAssists": OffensiveAssists,
        "AvgMultikills": Multikills,
        "AvgSoloKills": SoloKills,
        "AvgEnvironmentalDeaths": EnvironmentalDeaths,
        "AvgReconAssists": ReconAssists,
        "AvgAverageTimeAlive": AverageTimeAlive,
        "AvgTimeAlive": TimeAlive,
        "AvgEnvironmentalKills": EnvironmentalKills,
        "AvgTurretsDestroyed": TurretsDestroyed,
    }

    # Creating the target Dataframe
    df = DataFrame(players)

    # Saving the dataframe in an excel file
    df.to_csv(ProcessedDataFile)

    return df


# Saving the data to a .csv
# df.to_csv('ProcessedData/2018/Processed2018_stage_1.csv')
