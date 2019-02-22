import json
import requests


session = requests.session()
# 应用工厂登录


def factoryLogin(account, password):
    print("登录应用工厂")
    posturl = "http://sso.play.cloudtogo.cn/api/user/login"
    postdata = {
        "account": account,
        "password": password,
        "type": "pwd"
    }
    # 使用session直接post请求
    responseres = session.post(posturl, json=postdata)
    print(responseres.status_code)
    print(responseres.text)
    token = json.loads(responseres.text)["data"]["token"]
    print(token)
    return token


# 发布应用
def deploy_app(session, token, payload):
    url = "http://factory.play.cloudtogo.cn/api/factory/composer/deploy"
    data = payload
    deploy = session.post(
        url,
        data=json.dumps(data),
        headers={
            "token": token,
            "Content-Type": "application/json"})

    print(deploy.text)


token = factoryLogin("13798955353", "123456")
payload = {"composerId": "e8d9bda8-359d-11e9-9b2e-00505686c6ba",
           "projectId": "FP1902210559532890000006052197",
           "deployMode": "strict",
           "configs": [{"type": "domain",
                        "internal": "false",
                        "protocol": "HTTP",
                        "port": 8080,
                        "required": "true",
                        "description": "8080端口服务的子域名",
                        "initValue": "null",
                        "hidden": "false",
                        "keyData": "bp1_domain8080",
                        "valueData": "84a31f9c46eb.play.cloudtogo.cn",
                        "default": "null",
                        "labelData": "Python>8080端口访问域名",
                        "domain": "84a31f9c46eb",
                        "invalid": "false",
                        "domainSuffix": ".play.cloudtogo.cn"},
                       {"type": "string",
                        "internal": "false",
                        "protocol": "null",
                        "port": "null",
                        "required": "false",
                        "description": "请填入镜像地址",
                        "initValue": "null",
                        "hidden": "true",
                        "keyData": "bp1_image",
                        "valueData": "null",
                        "default": "null",
                        "labelData": "Python>镜像地址"},
                       {"type": "domain",
                        "internal": "false",
                        "protocol": "TCP",
                        "port": 6379,
                        "required": "true",
                        "description": "Redis port服务的子域名",
                        "initValue": "null",
                        "hidden": "true",
                        "keyData": "bp_domain6379",
                        "valueData": "undefined.play.cloudtogo.cn",
                        "default": "$domain.ignore$",
                        "labelData": "redis>Redis port访问域名",
                        "domainSuffix": ".play.cloudtogo.cn"},
                       {"paramType": "env",
                        "keyData": "env",
                        "valueData": "134324346fe442f8b5c00714e1c37157"},
                       {"labelData": "副本数",
                        "paramType": "copy",
                        "type": "string",
                        "keyData": ".bp",
                        "valueData": 1},
                       {"labelData": "副本数",
                        "paramType": "copy",
                        "type": "string",
                        "keyData": ".bp1",
                        "valueData": 1}],
           "autoTestConfig": {},
           "configDesc": "",
           "scheduleDesc": "{\"replicasZeroBP\":[{\"bpId\":\"e8d29641-359d-11e9-9b2e-00505686c6ba\",\"label\":\"redis\",\"os\":\"Linux\",\"path\":\".bp\",\"api\":false,\"buildpackSupport\":false,\"ports\":[{\"domain\":null,\"port\":6379,\"protocol\":\"TCP\"}],\"replica_support\":true,\"sessionpersist_required\":false,\"replicas\":1},{\"bpId\":\"e8d97a83-359d-11e9-9b2e-00505686c6ba\",\"label\":\"Python\",\"os\":\"Linux\",\"path\":\".bp1\",\"api\":false,\"buildpackSupport\":true,\"ports\":[{\"domain\":null,\"port\":8080,\"protocol\":\"HTTP\"}],\"replica_support\":true,\"sessionpersist_required\":false,\"replicas\":1}],\"apiZeroBP\":[{\"bpId\":\"e8d97a83-359d-11e9-9b2e-00505686c6ba\",\"label\":\"Python\",\"os\":\"Linux\",\"path\":\".bp1\",\"api\":false,\"buildpackSupport\":true,\"ports\":[{\"domain\":null,\"port\":8080,\"protocol\":\"HTTP\"}],\"replica_support\":true,\"sessionpersist_required\":false}],\"autoTest\":{\"projectId\":\"\"},\"env\":\"134324346fe442f8b5c00714e1c37157\",\"applyConfigs\":[{\"type\":\"domain\",\"internal\":false,\"protocol\":\"HTTP\",\"port\":8080,\"required\":true,\"description\":\"8080端口服务的子域名\",\"initValue\":null,\"hidden\":false,\"keyData\":\"bp1_domain8080\",\"valueData\":\"84a31f9c46eb.play.cloudtogo.cn\",\"default\":null,\"labelData\":\"Python>8080端口访问域名\",\"domain\":\"84a31f9c46eb\",\"invalid\":false,\"domainSuffix\":\".play.cloudtogo.cn\"},{\"type\":\"string\",\"internal\":false,\"protocol\":null,\"port\":null,\"required\":false,\"description\":\"请填入镜像地址\",\"initValue\":null,\"hidden\":true,\"keyData\":\"bp1_image\",\"valueData\":null,\"default\":null,\"labelData\":\"Python>镜像地址\"},{\"type\":\"domain\",\"internal\":false,\"protocol\":\"TCP\",\"port\":6379,\"required\":true,\"description\":\"Redis port服务的子域名\",\"initValue\":null,\"hidden\":true,\"keyData\":\"bp_domain6379\",\"valueData\":\"undefined.play.cloudtogo.cn\",\"default\":\"$domain.ignore$\",\"labelData\":\"redis>Redis port访问域名\",\"domainSuffix\":\".play.cloudtogo.cn\"}],\"schedule\":{\"replicas\":1,\"scheduleType\":\"auto\",\"customFormConfigs\":[]},\"buildpack\":{\"buildpackType\":\"auto\",\"customFormConfigs\":[]}}",
           "deployDesc": "jenkins test",
           "flowId": "null"}

deploy_app(session, token, payload)
