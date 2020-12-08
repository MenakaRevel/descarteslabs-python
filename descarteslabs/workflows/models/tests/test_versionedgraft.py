import json
import mock
import pytest

from descarteslabs.common.proto.workflow import workflow_pb2

from descarteslabs.client.version import __version__
from descarteslabs.workflows.types import Int, Function
from descarteslabs.workflows.client import Client
from descarteslabs.workflows.cereal import serialize_typespec
from descarteslabs.workflows.models.versionedgraft import VersionedGraft
from descarteslabs.workflows.models.tests import utils
from descarteslabs.workflows import _channel


@mock.patch(
    "descarteslabs.workflows.models.workflow.get_global_grpc_client",
    new=lambda: utils.MockedClient(),
)
@mock.patch("descarteslabs.common.proto.workflow.workflow_pb2_grpc.WorkflowAPIStub")
class TestVersionedGraft(object):
    def test_build(self, stub):
        obj = Int(42)
        version = "0.0.1"
        docstring = "int 42"
        labels = {
            "github_url": "http://github.com/someurl",
            "project": "some important project",
        }
        vg = VersionedGraft(version, obj, docstring=docstring, labels=labels)

        assert vg.version == version
        assert vg.object is obj
        assert vg.docstring == docstring
        assert vg.labels == labels
        assert vg._message.serialized_graft == json.dumps(obj.graft)
        assert vg._message.typespec == serialize_typespec(type(obj))
        assert vg.channel == _channel.__channel__
        assert vg._message.client_version == __version__
        assert vg.type == type(obj)

    def test_build_higher_order_function_fails(self, stub):
        @Function.from_callable
        def outer(x: Int):
            def inner(y: Int):
                return x + y

            return inner

        assert isinstance(outer, Function[Int, {}, Function[Int, {}, Int]])

        with pytest.raises(
            NotImplementedError,
            match="Cannot currently publish Functions that return Functions",
        ):
            VersionedGraft("0.0.1", outer)

    def test_from_proto(self, stub):
        obj = Int(40) + Int(42)
        version = "0.0.1"
        versionedGraft = VersionedGraft(version, obj)

        proto_msg = versionedGraft._message
        new_vg = VersionedGraft._from_proto(proto_msg)
        assert new_vg._message == proto_msg
        assert new_vg.type == type(obj)
        assert new_vg.version == version

    def test_get(self, stub):
        workflow_id = "foobar"
        version = "0.0.1"

        message = "foo"

        stub.return_value.GetVersion.return_value = message

        with mock.patch.object(VersionedGraft, "_from_proto") as _from_proto:
            VersionedGraft.get(workflow_id, version)
            _from_proto.assert_called_once()
            assert _from_proto.call_args[0][0] is message
            stub.return_value.GetVersion.assert_called_once_with(
                workflow_pb2.GetVersionRequest(id=workflow_id, version=version),
                timeout=Client.DEFAULT_TIMEOUT,
                metadata=mock.ANY,
            )

    def test_incompatible_channel(self, stub):
        obj = Int(42)
        version = "0.0.1"
        vg = VersionedGraft(version, obj)
        vg._message.channel = "foobar"

        with pytest.raises(ValueError, match="only defined for channel 'foobar'"):
            vg.object

    def test_url(self, stub):
        obj = utils.Foo(1)
        version = "1.0.1"
        vg = VersionedGraft(version, obj)

        with pytest.raises(ValueError, match="has not been persisted"):
            vg.url()

        url_template = vg._message.url_template = "http://base.net"

        assert vg.url() == url_template
