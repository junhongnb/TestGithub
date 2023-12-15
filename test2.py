# 定义API接口
@app.route('/predict', methods=['POST'])
def predict():
    # 获取请求中的数据
    data = request.get_json(force=True)

    # 将数据转换为NumPy数组
    input_data = np.array(data['input'])
    # 使用模型进行预测
    predictions = model.predict(input_data)
    
    # 返回预测结果
    return jsonify(predictions.tolist())

# 运行Flask应用
if __name__ == '__main__':
    app.run(debug=True)
