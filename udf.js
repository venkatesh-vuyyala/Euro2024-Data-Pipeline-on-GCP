function transform(line) {
    var values = line.split(',');
    var obj = new Object();
    obj.goals = values[0];
    obj.name = values[1];
    obj.teamName = values[2];
    obj.assists = values[3];
    obj.firstTeamAppearances = values[4];
    var jsonString = JSON.stringify(obj);
    return jsonString;
   }