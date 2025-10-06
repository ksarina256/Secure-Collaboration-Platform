import sodium from "libsodium-wrappers";

export async function encryptFor(message: string, recipientPublicKeyBase64: string){
  await sodium.ready;
  const pk = sodium.from_base64(recipientPublicKeyBase64);
  const ct = sodium.crypto_box_seal(sodium.from_string(message), pk);
  return sodium.to_base64(ct);
}

export async function decryptFrom(ciphertextBase64: string, myPublicKeyBase64: string, mySecretKeyBase64: string){
  await sodium.ready;
  const pk = sodium.from_base64(myPublicKeyBase64);
  const sk = sodium.from_base64(mySecretKeyBase64);
  const pt = sodium.crypto_box_seal_open(sodium.from_base64(ciphertextBase64), pk, sk);
  return sodium.to_string(pt);
}

export async function generateKeypair(){
  await sodium.ready;
  const kp = sodium.crypto_box_keypair();
  return {
    publicKey: sodium.to_base64(kp.publicKey),
    secretKey: sodium.to_base64(kp.privateKey)
  };
}
