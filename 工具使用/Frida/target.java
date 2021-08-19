public class MainActivity extends AppCompatActivity {
    private  String TAG="Crackme";
    private TextView textView;
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        textView =findViewById(R.id.tv);
        textView.setText("是否优秀："+isExcellent(46,54));
    }

    private  boolean isExcellent(int chinese, int math){
        if( chinese + math >=180){
            return true;
        }
        else{
            return false;
        }
    }

}