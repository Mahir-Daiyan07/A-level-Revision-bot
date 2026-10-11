import discord
import os
from discord import app_commands
from discord.ext import commands
import random
# A-LEVEL REVISION & STUDY ASSISTANT BOT
# Author: Mahir daiyan
# Description: A custom Discord bot designed to help A-Level students optimize 
# their revision strategies using evidence-based techniques like past paper 
# mastery, cheat sheets, and time-blocking.


class RevisionBot(commands.Bot):
    def __init__(self):
        # Setting up standard gateway intents required for bot operations
        intents = discord.Intents.default()
        intents.message_content = True
        super().__init__(command_prefix="!", intents=intents)

    async def setup_hook(self):
        # Automatically sync modern slash commands with Discord upon startup
        await self.tree.sync()
        print("Slash commands synced successfully with Discord API.")

bot = RevisionBot()

@bot.event
async def on_ready():
    print(f"*********")
    print(f"Logged in as: {bot.user} (ID: {bot.user.id})")
    print(f"Status: Online and ready to help!")
    print(f"*********")
# 1. /revision-plan Command
@bot.tree.command(name="revision-plan", description="Generate a high-yield, A*-focused 3-day revision strategy.")
@app_commands.describe(subject="The A-Level subject you want to revise (e.g., Maths, Physics, Chemistry)")
async def revision_plan(interaction: discord.Interaction, subject: str):
    """
    Generates a structured revision breakdown prioritizing past papers and 
    timed conditions[cite: 1].
    """
    embed = discord.Embed(
        title=f"High-Yield Revision Plan: {subject.upper()}",
        description="Designed to maximize efficiency using active recall and past paper repetition[cite: 1].",
        color=discord.Color.blue()
    )
    
    embed.add_field(
        name="Day 1: Timed Past Paper & Gap Analysis",
        value="• Sit a full past paper under strict exam conditions (no phone, water only)[cite: 1].\n• Mark it rigorously and log every question you struggled with.",
        inline=False
    )
    
    embed.add_field(
        name="Day 2: Targeted Weakness & Cheat Sheet Building",
        value="• Re-attempt the difficult questions from yesterday[cite: 1].\n• Build a concise 1-2 page cheat sheet for formulas and definitions you kept forgetting[cite: 1].",
        inline=False
    )
    
    embed.add_field(
        name="Day 3: Paper Iteration & Hard Questions",
        value="• Redo the same past paper to reinforce mastery until you hit close to 100%[cite: 1].\n• Focus heavily on the challenging end-of-paper questions that separate an A* from an A[cite: 1].",
        inline=False
    )
    
    embed.set_footer(text="A-Level Revision Bot • Portfolio Project")
    await interaction.response.send_message(embed=embed)
# 2. /study-tip Command
@bot.tree.command(name="study-tip", description="Get a proven, expert study tip for securing top grades.")
async def study_tip(interaction: discord.Interaction):
    """
    Pulls a randomized high-yield revision tip based on proven strategies.
    """
    tips = [
        "Past Papers are King: Dedicate 95% of your revision effort to past papers under timed, distraction-free exam conditions[cite: 1].",
        "Build Concise Cheat Sheets: Keep a 1-2 page summary of formulas and tricky concepts that you can review right before the exam[cite: 1].",
        "Hour-by-Hour Planning: Plan your study sessions to the exact hour the night before to maintain high efficiency (aim for 5-6 solid hours max)[cite: 1].",
        "Redo Papers: Don't skip a past paper just because you've done it before—redo it until you master every single question[cite: 1].",
        "Tackle Hard Questions: Don't shy away from difficult end-of-chapter questions; those are what secure an A* grade[cite: 1]."
    ]
    
    embed = discord.Embed(
        title="Expert Revision Tip",
        description=random.choice(tips),
        color=discord.Color.green()
    )
    embed.set_footer(text="Consistency beats cramming every single time.")
    await interaction.response.send_message(embed=embed)

# 3. /pomodoro Command
@bot.tree.command(name="pomodoro", description="Start a structured 25-minute focus session with a proper break plan.")
async def pomodoro(interaction: discord.Interaction):
    """
    Implements a focused study block to eliminate distractions.
    """
    embed = discord.Embed(
        title="Pomodoro Focus Session Started",
        description="Put your phone in another room, close unnecessary browser tabs, and lock in for 25 minutes!",
        color=discord.Color.orange()
    )
    embed.add_field(name="Next Step", value="Once the timer dings, take a proper 5-minute break to stay refreshed.", inline=False)
    embed.set_footer(text="Eliminate distractions to maximize study efficiency.")
    await interaction.response.send_message(embed=embed)

bot.run(os.getenv('DISCORD_TOKEN'))