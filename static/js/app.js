function HideTable(){
    $("#tweet_string_div").hide();
    $('#twitter_table').hide();
    $("#loading_spinner").show();
}

function ShowTable(){
    $("#loading_spinner").hide();
    $("#tweet_string_div").hide();
    $('#twitter_table').show();
}

function ManualPredictSetup(){
    $('#twitter_table').hide();
    $("#loading_spinner").hide();
    $("#tweet_string_div").hide();
}

function BuiltTweetTable(data){
    var tbody = d3.select('tbody')
    tbody.html('');
    data['tweets'].forEach((el, index) => {
        var row = tbody.append('tr');
        row.attr( 'class', 'text-center')
        row.append('td').text(el);

        if(data['custom_predictions'][index] == data['vader_predictions'][index]){
            row.append('td').text(data['custom_predictions'][index]).attr('class', 'text-success');
            row.append('td').text(data['vader_predictions'][index]).attr('class', 'text-success');
        } else {
            row.append('td').text(data['custom_predictions'][index]);
            row.append('td').text(data['vader_predictions'][index]);
        }
    });
}

function BuildResults(){
    var q = $('#search_input').val()
    if(q){  
        HideTable();
        var url = '/search/' + q;
        d3.json(url).then(function(data){
            BuiltTweetTable(data);
            ShowTable();
        });
    }
}

function GetSinglePrediction(url, type = 'Michael'){
    var tweet_div = d3.select("#tweet_string_div");
    var input = $('#tweet_input');
    var tweet = input.val();
    input.val('');
    tweet_div.html('');
    if(tweet){
        var route = url + tweet;
        d3.json(route).then(function(data){
            tweet_div.append('p').text("Tweet: \"" + tweet + "\"").attr('class', 'h5');
            tweet_div.append('p').text(type + ' says your tweet is, ' + data[0] + '.').attr('class', 'h3');
            $("#tweet_string_div").show();
        });
    }
}

$("#search_term_btn").on('click', () => {
    BuildResults();
});

$("#tweet_predict").on('click', () => {
    ManualPredictSetup();
    GetSinglePrediction('/predict/')
});

$("#vader_predict").on('click', () => {
    ManualPredictSetup();
    GetSinglePrediction('/vaderpredict/', 'Vader')
});