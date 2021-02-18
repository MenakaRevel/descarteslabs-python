# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from descarteslabs.common.proto.discover import discover_pb2 as descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2


class AssetApiStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetAsset = channel.unary_unary(
        '/descarteslabs.discover.v0alpha.AssetApi/GetAsset',
        request_serializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.GetAssetRequest.SerializeToString,
        response_deserializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.GetAssetResponse.FromString,
        )
    self.ListAssets = channel.unary_unary(
        '/descarteslabs.discover.v0alpha.AssetApi/ListAssets',
        request_serializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.ListAssetsRequest.SerializeToString,
        response_deserializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.ListAssetsResponse.FromString,
        )
    self.UpdateAsset = channel.unary_unary(
        '/descarteslabs.discover.v0alpha.AssetApi/UpdateAsset',
        request_serializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.UpdateAssetRequest.SerializeToString,
        response_deserializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.UpdateAssetResponse.FromString,
        )


class AssetApiServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def GetAsset(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListAssets(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def UpdateAsset(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AssetApiServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetAsset': grpc.unary_unary_rpc_method_handler(
          servicer.GetAsset,
          request_deserializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.GetAssetRequest.FromString,
          response_serializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.GetAssetResponse.SerializeToString,
      ),
      'ListAssets': grpc.unary_unary_rpc_method_handler(
          servicer.ListAssets,
          request_deserializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.ListAssetsRequest.FromString,
          response_serializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.ListAssetsResponse.SerializeToString,
      ),
      'UpdateAsset': grpc.unary_unary_rpc_method_handler(
          servicer.UpdateAsset,
          request_deserializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.UpdateAssetRequest.FromString,
          response_serializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.UpdateAssetResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'descarteslabs.discover.v0alpha.AssetApi', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class AccessGrantApiStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.CreateAccessGrant = channel.unary_unary(
        '/descarteslabs.discover.v0alpha.AccessGrantApi/CreateAccessGrant',
        request_serializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.CreateAccessGrantRequest.SerializeToString,
        response_deserializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.CreateAccessGrantResponse.FromString,
        )
    self.GetAccessGrant = channel.unary_unary(
        '/descarteslabs.discover.v0alpha.AccessGrantApi/GetAccessGrant',
        request_serializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.GetAccessGrantRequest.SerializeToString,
        response_deserializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.GetAccessGrantResponse.FromString,
        )
    self.DeleteAccessGrant = channel.unary_unary(
        '/descarteslabs.discover.v0alpha.AccessGrantApi/DeleteAccessGrant',
        request_serializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.DeleteAccessGrantRequest.SerializeToString,
        response_deserializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.DeleteAccessGrantResponse.FromString,
        )
    self.ListAccessGrants = channel.unary_unary(
        '/descarteslabs.discover.v0alpha.AccessGrantApi/ListAccessGrants',
        request_serializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.ListAccessGrantsRequest.SerializeToString,
        response_deserializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.ListAccessGrantsResponse.FromString,
        )
    self.ListAccessGrantsStream = channel.unary_stream(
        '/descarteslabs.discover.v0alpha.AccessGrantApi/ListAccessGrantsStream',
        request_serializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.ListAccessGrantsStreamRequest.SerializeToString,
        response_deserializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.ListAccessGrantsStreamResponse.FromString,
        )
    self.ReplaceAccessGrant = channel.unary_unary(
        '/descarteslabs.discover.v0alpha.AccessGrantApi/ReplaceAccessGrant',
        request_serializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.ReplaceAccessGrantRequest.SerializeToString,
        response_deserializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.ReplaceAccessGrantResponse.FromString,
        )


class AccessGrantApiServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def CreateAccessGrant(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAccessGrant(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def DeleteAccessGrant(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListAccessGrants(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListAccessGrantsStream(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ReplaceAccessGrant(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_AccessGrantApiServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'CreateAccessGrant': grpc.unary_unary_rpc_method_handler(
          servicer.CreateAccessGrant,
          request_deserializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.CreateAccessGrantRequest.FromString,
          response_serializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.CreateAccessGrantResponse.SerializeToString,
      ),
      'GetAccessGrant': grpc.unary_unary_rpc_method_handler(
          servicer.GetAccessGrant,
          request_deserializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.GetAccessGrantRequest.FromString,
          response_serializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.GetAccessGrantResponse.SerializeToString,
      ),
      'DeleteAccessGrant': grpc.unary_unary_rpc_method_handler(
          servicer.DeleteAccessGrant,
          request_deserializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.DeleteAccessGrantRequest.FromString,
          response_serializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.DeleteAccessGrantResponse.SerializeToString,
      ),
      'ListAccessGrants': grpc.unary_unary_rpc_method_handler(
          servicer.ListAccessGrants,
          request_deserializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.ListAccessGrantsRequest.FromString,
          response_serializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.ListAccessGrantsResponse.SerializeToString,
      ),
      'ListAccessGrantsStream': grpc.unary_stream_rpc_method_handler(
          servicer.ListAccessGrantsStream,
          request_deserializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.ListAccessGrantsStreamRequest.FromString,
          response_serializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.ListAccessGrantsStreamResponse.SerializeToString,
      ),
      'ReplaceAccessGrant': grpc.unary_unary_rpc_method_handler(
          servicer.ReplaceAccessGrant,
          request_deserializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.ReplaceAccessGrantRequest.FromString,
          response_serializer=descarteslabs_dot_common_dot_proto_dot_discover_dot_discover__pb2.ReplaceAccessGrantResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'descarteslabs.discover.v0alpha.AccessGrantApi', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
